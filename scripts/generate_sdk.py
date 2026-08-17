import argparse
import contextlib
import json
import os
import re
import shutil
import subprocess
import textwrap
from pathlib import Path
from tempfile import TemporaryDirectory

from generation import docs_rendering, error_package, parity, wrapper_generation
from generation._shared import (
    PROJECT_ROOT,
    SDK_OUTPUT_DIR,
    discover_service_model_classes,
)
from generation.endpoint_docs import EndpointDocsCollector

# Configuration
DEFAULT_REPO = "https://github.com/kentik/api-schema-public.git"
DEFAULT_OPENAPI_GENERATOR = "openapi-python-generator"
CUSTOM_OPENAPI_TEMPLATE_PATH = PROJECT_ROOT / "scripts" / "openapi_templates"


def run_cmd(cmd: list[str]):
    print(f" Running: {' '.join(cmd)}")
    subprocess.check_call(cmd)


def openapi_generator_cmd(swagger_path: Path, out_dir: Path) -> list[str]:
    """Builds the openapi generator command with optional fork and template overrides.

    Environment variables:
    - OPENAPI_GENERATOR_FROM: uvx --from source, e.g. git+https://github.com/<org>/<repo>.git
    - OPENAPI_GENERATOR_CMD: executable name, defaults to openapi-python-generator
    """
    generator_from = os.getenv("OPENAPI_GENERATOR_FROM", "").strip()
    generator_cmd = os.getenv(
        "OPENAPI_GENERATOR_CMD", DEFAULT_OPENAPI_GENERATOR
    ).strip()

    cmd = ["uvx"]
    if generator_from:
        cmd.extend(["--from", generator_from])

    cmd.extend(
        [
            generator_cmd,
            str(swagger_path),
            str(out_dir),
            "--library",
            "httpx",
            "--formatter",
            "none",
        ]
    )

    if CUSTOM_OPENAPI_TEMPLATE_PATH.exists():
        cmd.extend(["--custom-template-path", str(CUSTOM_OPENAPI_TEMPLATE_PATH)])

    return cmd


def dedupe_top_level_function_names(content: str) -> str:
    """Renames duplicate top-level def names to avoid collisions (F811).

    Example: GetAuditEvent, GetAuditEvent -> GetAuditEvent, GetAuditEvent_2
    """
    func_name_pattern = re.compile(
        r"^def\s+([A-Za-z_][A-Za-z0-9_]*)\s*\(", re.MULTILINE
    )

    seen: dict[str, int] = {}
    out: list[str] = []
    cursor = 0

    for match in func_name_pattern.finditer(content):
        func_name = match.group(1)
        seen[func_name] = seen.get(func_name, 0) + 1

        if seen[func_name] == 1:
            continue

        new_name = f"{func_name}_{seen[func_name]}"
        out.append(content[cursor : match.start(1)])
        out.append(new_name)
        cursor = match.end(1)

    if not out:
        return content

    out.append(content[cursor:])
    return "".join(out)


@contextlib.contextmanager
def get_schema_root(repo_source: str):
    """Handles local paths or remote Git repos for schema source."""
    if repo_source.startswith("http") or repo_source.startswith("git@"):
        with TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            print(f"Cloning schema repository from {repo_source}...")
            run_cmd(["git", "clone", "--depth", "1", repo_source, str(tmp_path)])
            yield tmp_path
    else:
        local_path = Path(repo_source.replace("file://", "")).resolve()
        print(f"Using local schema repository at {local_path}...")
        yield local_path


def patch_schema_for_clean_names(swagger_path: Path, version: str):
    """Scrubs version prefixes from models to ensure clean class names."""
    with open(swagger_path, "r", encoding="utf-8") as f:
        schema = json.load(f)

    def clean_refs(node):
        if isinstance(node, dict):
            if "$ref" in node and isinstance(node["$ref"], str):
                if f"/{version}" in node["$ref"]:
                    node["$ref"] = node["$ref"].replace(f"/{version}", "/")
            for v in node.values():
                clean_refs(v)
        elif isinstance(node, list):
            for item in node:
                clean_refs(item)

    clean_refs(schema)

    sections = []
    if "definitions" in schema:
        sections.append(schema["definitions"])
    if "components" in schema:
        for c in ["schemas", "parameters", "responses", "requestBodies"]:
            if c in schema["components"]:
                sections.append(schema["components"][c])

    for section in sections:
        keys_to_rename = [k for k in section.keys() if k.startswith(version)]
        for old_key in keys_to_rename:
            new_key = old_key[len(version) :]
            if new_key:
                section[new_key] = section.pop(old_key)

    with open(swagger_path, "w", encoding="utf-8") as f:
        json.dump(schema, f)


def normalize_triple_quoted_docstrings(content: str) -> str:
    """Normalizes indentation/spacing of triple-quoted docstrings.

    Generated model docstrings can contain inconsistent indentation that docutils
    interprets as malformed block quotes during Sphinx autodoc rendering.
    """

    pattern = re.compile(r"(^[ \t]*)(\"\"\"|''')([\s\S]*?)(\2)", re.MULTILINE)

    def _rewrite(match: re.Match[str]) -> str:
        indent = match.group(1)
        quote = match.group(2)
        body = match.group(3)

        if "\n" not in body:
            return match.group(0)

        dedented = textwrap.dedent(body).replace("\r\n", "\n").strip("\n")
        if not dedented:
            return f"{indent}{quote}{quote}"

        lines = dedented.split("\n")
        inner_indent = indent + ("    " if indent else "")
        formatted_lines = [
            (f"{inner_indent}{line.rstrip()}" if line.strip() else "") for line in lines
        ]
        return f"{indent}{quote}\n" + "\n".join(formatted_lines) + f"\n{indent}{quote}"

    return pattern.sub(_rewrite, content)


def generate_modular_sdk(repo_source=DEFAULT_REPO):
    # Setup directories
    SDK_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    (SDK_OUTPUT_DIR / "__init__.py").touch(exist_ok=True)

    print("Cleaning old modules...")
    for item in SDK_OUTPUT_DIR.iterdir():
        if item.is_dir() and item.name != "__pycache__":
            shutil.rmtree(item)

    with get_schema_root(repo_source) as schema_root:
        # Define base paths using the yielded root
        openapi_base = schema_root / "gen" / "openapiv3" / "kentik"
        proto_base = schema_root / "proto"
        source_services = {
            p.name
            for p in openapi_base.iterdir()
            if p.is_dir() and p.name != "__pycache__"
        }

        selected_swagger_files, selected_count, ignored_count = (
            parity.select_latest_swagger_files_by_service(openapi_base)
        )
        print(
            f"Discovered {selected_count} latest swagger files across "
            f"{len(selected_swagger_files)} services (ignored {ignored_count} older file versions)."
        )

        service_swagger_paths: dict[str, list[Path]] = {}
        endpoint_docs_collector = EndpointDocsCollector()

        for service in sorted(selected_swagger_files):
            out_dir = SDK_OUTPUT_DIR / service
            out_dir.mkdir(parents=True, exist_ok=True)
            (out_dir / "__init__.py").touch(exist_ok=True)

            # Setup specific directories
            pb_dir = out_dir / "pb"
            pb_dir.mkdir(exist_ok=True)
            (pb_dir / "__init__.py").touch(exist_ok=True)

            service_swagger_paths[service] = []

            for metadata in selected_swagger_files[service]:
                swagger_path = Path(metadata["path"])
                version = str(metadata["version"])
                namespace = "/".join(metadata["namespace"])
                namespace_label = namespace if namespace else "root"
                service_swagger_paths[service].append(swagger_path)

                print(
                    f"\nGenerating {service} [{namespace_label}] "
                    f"{metadata['filename']} ({version})..."
                )

                # -----------------------------------------------------------------
                # 1. GENERATE OPENAPI (REST)
                # -----------------------------------------------------------------
                patch_schema_for_clean_names(swagger_path, version)

                run_cmd(openapi_generator_cmd(swagger_path, out_dir))

                # Extract per-operation documentation now, while the swagger
                # file is still available -- rendered as real Sphinx text
                # later (endpoint_docs_collector.render()), once wrapper
                # methods exist.
                endpoint_docs_collector.extract(service, swagger_path)

                # -----------------------------------------------------------------
                # 2. GENERATE PROTOBUF (gRPC)
                # -----------------------------------------------------------------
                swagger_rel_parent = swagger_path.relative_to(openapi_base).parent
                proto_dir = proto_base / "kentik" / swagger_rel_parent
                print(f"    Hunting for protos in: {proto_dir}")

                if proto_dir.exists():
                    proto_files = list(proto_dir.glob("*.proto"))
                    if proto_files:
                        print(
                            f"    Compiling {len(proto_files)} .proto file(s) into pb/..."
                        )

                        with TemporaryDirectory() as tmp_pb:
                            tmp_pb_path = Path(tmp_pb)

                            rel_proto_files = [
                                str(p.relative_to(proto_base)) for p in proto_files
                            ]

                            # Set up the paths to the vendored dependencies
                            vendor_base = schema_root / "protovendor" / "github.com"
                            googleapis_path = vendor_base / "googleapis" / "googleapis"
                            grpc_gateway_path = (
                                vendor_base / "grpc-ecosystem" / "grpc-gateway"
                            )

                            # Add the vendored paths to the protoc Include (-I) arguments
                            cmd = [
                                "uv",
                                "run",
                                "--with",
                                "grpcio-tools",
                                "python",
                                "-m",
                                "grpc_tools.protoc",
                                f"-I{proto_base}",
                                f"-I{googleapis_path}",
                                f"-I{grpc_gateway_path}",
                                f"--python_out={tmp_pb_path}",
                                f"--grpc_python_out={tmp_pb_path}",
                            ]
                            cmd.extend(rel_proto_files)

                            try:
                                subprocess.run(
                                    cmd, check=True, capture_output=True, text=True
                                )

                                generated_files = list(tmp_pb_path.rglob("*.py"))
                                print(
                                    f"    ✅ Protoc successfully generated {len(generated_files)} files."
                                )

                                for gen_py in generated_files:
                                    shutil.copy(gen_py, pb_dir / gen_py.name)

                                for pb_file in pb_dir.rglob("*_grpc.py"):
                                    content = pb_file.read_text(encoding="utf-8")
                                    # grpc_tools can emit either local-style imports:
                                    #   import foo_pb2
                                    # or package-style imports:
                                    #   from kentik.service.version import (foo_pb2 as alias,)
                                    # We flatten generated files into pb/, so both must become local imports.
                                    content = re.sub(
                                        r"^import (\w+_pb2)",
                                        r"from . import \1",
                                        content,
                                        flags=re.MULTILINE,
                                    )
                                    content = re.sub(
                                        r"^from [\w\.]+ import \(\s*(\w+_pb2) as ([\w_]+),\s*\)$",
                                        r"from . import \1 as \2",
                                        content,
                                        flags=re.MULTILINE,
                                    )
                                    content = re.sub(
                                        r"^from [\w\.]+ import (\w+_pb2) as ([\w_]+)$",
                                        r"from . import \1 as \2",
                                        content,
                                        flags=re.MULTILINE,
                                    )
                                    pb_file.write_text(content, encoding="utf-8")

                            except subprocess.CalledProcessError as e:
                                print(
                                    f"    ❌ Protobuf generation failed for {service}!"
                                )
                                print("    --- PROTOC ERROR LOG ---")
                                if e.stderr:
                                    print("    [stderr]")
                                    print(e.stderr)
                                if e.stdout:
                                    print("    [stdout]")
                                    print(e.stdout)
                                print("    ------------------------")
                    else:
                        print(
                            "    ⚠️ Directory exists, but no .proto files found inside."
                        )
                else:
                    print("    ⚠️ No proto directory found, skipping gRPC.")

        for service, swagger_paths in service_swagger_paths.items():
            service_dir = SDK_OUTPUT_DIR / service
            if service_dir.exists():
                error_package.generate_service_error_package(service_dir, swagger_paths)

    parity.validate_generated_service_parity(source_services, SDK_OUTPUT_DIR)

    # -----------------------------------------------------------------
    # 3. POST-PROCESSING (Rest & Models Cleanup)
    # -----------------------------------------------------------------
    print("\nPatching generated code...")
    for service_dir in SDK_OUTPUT_DIR.iterdir():
        if not service_dir.is_dir() or service_dir.name == "__pycache__":
            continue

        # Discover models for explicit mapping
        model_classes = discover_service_model_classes(service_dir)

        explicit_models_import = (
            f"from ..models import {', '.join(sorted(model_classes))}"
            if model_classes
            else ""
        )
        explicit_models_local = (
            f"from .models import {', '.join(sorted(model_classes))}"
            if model_classes
            else ""
        )

        # Rebuild models/__init__.py from every model file on disk.
        #
        # openapi-python-generator is invoked once per swagger file for
        # multi-schema services (e.g. alerting, saved_filter, plan), and each
        # invocation overwrites models/__init__.py with only *its own*
        # models. Left alone, only the last-processed swagger file's models
        # stay exported; `from ..models import X` for anything else silently
        # resolves to the `models/X.py` submodule instead of raising
        # ImportError, since Python falls back to submodule lookup for names
        # a package's __init__.py doesn't bind. That surfaces later as
        # `TypeError: 'module' object is not callable` wherever X(...) is
        # instantiated. Rebuilding from a full directory scan keeps every
        # class explicitly bound in the package namespace regardless of how
        # many swagger files contributed to this service.
        models_dir = service_dir / "models"
        if models_dir.exists():
            init_lines = []
            for model_file in sorted(models_dir.glob("*.py")):
                if model_file.name == "__init__.py":
                    continue
                classes = re.findall(
                    r"^class\s+([A-Za-z0-9_]+)",
                    model_file.read_text(encoding="utf-8"),
                    re.MULTILINE,
                )
                if not classes:
                    continue
                exports = ", ".join(f"{c} as {c}" for c in classes)
                init_lines.append(f"from .{model_file.stem} import {exports}")
            (models_dir / "__init__.py").write_text(
                "\n".join(init_lines) + ("\n" if init_lines else ""),
                encoding="utf-8",
            )

        # Fix explicit imports in __init__.py files by reading the referenced modules
        for init_file in service_dir.rglob("__init__.py"):
            if "error" in init_file.parts:
                continue
            content = init_file.read_text(encoding="utf-8")
            new_lines = []
            for line in content.splitlines():
                # Look for: from .filename import *
                match = re.match(r"^from \.([a-zA-Z0-9_]+) import \*$", line)
                if match:
                    module_name = match.group(1)
                    target_py = init_file.parent / f"{module_name}.py"

                    if target_py.exists():
                        target_content = target_py.read_text(encoding="utf-8")
                        classes = re.findall(
                            r"^class\s+([A-Za-z0-9_]+)",
                            target_content,
                            flags=re.MULTILINE,
                        )
                        if classes:
                            # Use explicit re-export style to satisfy the most pedantic linters
                            explicit_imports = ", ".join(
                                [f"{c} as {c}" for c in classes]
                            )
                            new_lines.append(
                                f"from .{module_name} import {explicit_imports}"
                            )
                            continue
                new_lines.append(line)
            init_file.write_text("\n".join(new_lines) + "\n", encoding="utf-8")

        # General content patches for all .py files in the service directory
        for py_file in service_dir.rglob("*.py"):
            # CRITICAL: Skip the 'pb' directory entirely so we don't corrupt the gRPC stubs!
            if "pb" in py_file.parts or "error" in py_file.parts:
                continue

            if py_file.name.startswith("async_") or py_file.name == "api_config.py":
                py_file.unlink()
                continue

            # De-duplicate filenames (DeviceService_service.py -> DeviceService.py)
            if "Service_service" in py_file.name or "_service" in py_file.name.lower():
                clean_name = (
                    py_file.name.replace("Service_service", "Service")
                    .replace("_service_service", "Service")
                    .replace("_service", "Service")
                )
                # Ensure it starts with a capital letter (deviceService -> DeviceService)
                clean_name = clean_name[:1].upper() + clean_name[1:]

                new_path = py_file.with_name(clean_name)
                py_file.rename(new_path)
                py_file = new_path

            content = py_file.read_text(encoding="utf-8")

            content = re.sub(
                r"from \.*api_config import APIConfig, HTTPException",
                "from kentik_api.core.api_config import APIConfig\nfrom kentik_api.errors import HTTPException",
                content,
            )

            content = re.sub(
                r"from \.*api_config import APIConfig as APIConfig",
                "from kentik_api.core.api_config import APIConfig",
                content,
            )
            content = re.sub(
                r"from \.*api_config import HTTPException as HTTPException",
                "from kentik_api.errors import HTTPException",
                content,
            )

            content = re.sub(
                r"return ([A-Za-z0-9_]+)\(\*\*body\) if body.*? else \1\(\)",
                r"return \1(**body) if body is not None else \1.model_construct()",
                content,
            )

            # Path parameter sanitization ({device.id} -> {id})
            content = re.sub(
                r"path\s*=\s*f[\"'].*?[\"']",
                lambda m: re.sub(
                    r"\{([a-zA-Z0-9_]+)\.([a-zA-Z0-9_]+)\}", r"{\1\2}", m.group(0)
                ),
                content,
            )

            content = re.sub(
                r'["\']Authorization["\']:\s*f["\']Bearer\s*\{[^}]+\}["\'],?',
                r'"X-CH-Auth-Email": api_config.auth_email,\n        "X-CH-Auth-API-Token": api_config.auth_token,',
                content,
            )

            if py_file.name == "api_config.py":
                content = content.replace(
                    "access_token: Optional[str] = None",
                    "auth_email: Optional[str] = None\n    auth_token: Optional[str] = None",
                )
                content = content.replace("def get_access_token", "def get_auth_token")
                content = content.replace("self.access_token", "self.auth_token")

            functions = re.split(r"^(?=async def |def )", content, flags=re.MULTILINE)
            fixed_funcs = []

            for func in functions:
                if not func.strip():
                    fixed_funcs.append(func)
                    continue

                sig_part = func.split("->")[0] if "->" in func else func.split(":\n")[0]
                has_data_param = "data:" in sig_part or "data :" in sig_part
                has_json_kwarg = "json=" in func
                has_json_body_kwarg = "json_body=" in func

                if has_data_param and not (has_json_kwarg or has_json_body_kwarg):
                    if "request_json(" in func:
                        func = re.sub(
                            r"(query_params=query_params)(,?)(\s*)",
                            r"\1,\n                json_body=data.model_dump()\3",
                            func,
                            count=1,
                        )
                    else:
                        func = re.sub(
                            r"(params=query_params)(,?)(\s*\))",
                            r"\1, json=data.model_dump()\3",
                            func,
                        )

                # Pydantic v2 compatibility: normalize any legacy `.dict()` payloads.
                func = re.sub(r"\bdata\.dict\(\)", "data.model_dump()", func)

                if not has_data_param and has_json_kwarg:
                    func = re.sub(r",\s*json=data\.model_dump\(\)", "", func)
                    func = re.sub(r"json=data\.model_dump\(\)", "", func)

                if not has_data_param and has_json_body_kwarg:
                    func = re.sub(r",\s*json_body\s*=\s*data\.model_dump\(\)", "", func)
                    func = re.sub(
                        r"json_body\s*=\s*data\.model_dump\(\)\s*,?", "", func
                    )

                fixed_funcs.append(func)

            content = "".join(fixed_funcs)

            if py_file.parent.name in ("services", "service") and py_file.name not in (
                "__init__.py",
            ):
                content = error_package.inject_service_error_handling(content)

            # Keep generated docstrings parseable by docutils/Sphinx autodoc.
            content = normalize_triple_quoted_docstrings(content)

            # Wildcard Imports (Typing & Models)
            if "from typing import *" in content:
                content = content.replace(
                    "from typing import *",
                    "from typing import Any, Callable, Dict, Generic, List, Optional, Set, Tuple, Type, TypeVar, Union",
                )

            # Some generated services expose an operation literally named `List`.
            # That clashes with `from typing import List` (F811), so alias typing List.
            if re.search(r"^def\s+List\s*\(", content, flags=re.MULTILINE):
                content = re.sub(
                    r"from typing import ([^\n]*)\bList\b([^\n]*)",
                    lambda m: f"from typing import {m.group(1)}List as TypingList{m.group(2)}",
                    content,
                    count=1,
                )
                content = re.sub(r"\bList\[", "TypingList[", content)

            if explicit_models_import:
                content = content.replace(
                    "from ..models import *", explicit_models_import + "  # noqa: F401"
                )
                content = content.replace(
                    "from .models import *", explicit_models_local + "  # noqa: F401"
                )

            content = dedupe_top_level_function_names(content)

            py_file.write_text(content, encoding="utf-8")

    print("\nFormatting...")
    run_cmd(["uvx", "ruff", "check", "--select", "F,I", "--fix", str(SDK_OUTPUT_DIR)])
    run_cmd(["uvx", "ruff", "format", str(SDK_OUTPUT_DIR)])

    print("\nGenerating Wrappers & Documentation...")
    wrapper_generation.generate()
    docs_rendering.generate()
    endpoint_docs_collector.render()

    print("\nFinal formatting pass for generated code...")
    run_cmd(["uvx", "ruff", "check", "--select", "F,I", "--fix", str(SDK_OUTPUT_DIR)])
    run_cmd(["uvx", "ruff", "format", str(SDK_OUTPUT_DIR)])

    print("\n✅ SDK and Documentation Generation Complete!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate Kentik SDK from a schema repository."
    )
    parser.add_argument(
        "--local-repo",
        dest="local_repo",
        default=DEFAULT_REPO,
        help="Local schema repository path (or file:// path). Defaults to the public repo URL.",
    )
    args = parser.parse_args()

    generate_modular_sdk(args.local_repo)
