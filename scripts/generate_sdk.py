# HAND-WRITTEN: orchestrates `make generate`. Not itself generated.
"""SDK generation entrypoint: downloads/validates the OpenAPI schema, runs every
phase module in scripts/generation/, and writes src/kentik_api/gen/ plus docs."""

import argparse
import contextlib
import json
import os
import re
import shutil
import subprocess
from pathlib import Path
from tempfile import TemporaryDirectory

from generation import docs_rendering, error_package, fixup, parity, wrapper_generation
from generation._shared import (
    PROJECT_ROOT,
    SDK_OUTPUT_DIR,
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


def _rewrite_grpc_imports(content: str) -> str:
    """Rewrites package-style pb2 imports to local relative imports.

    grpc_tools.protoc can emit any of three import styles depending on version
    and input layout. All three must become `from . import` so the compiled
    files are importable from within the flattened pb/ directory.
    """
    # bare: `import foo_pb2`
    content = re.sub(
        r"^import (\w+_pb2)", r"from . import \1", content, flags=re.MULTILINE
    )
    # parenthesised from-import: `from pkg import (foo_pb2 as alias,)`
    content = re.sub(
        r"^from [\w\.]+ import \(\s*(\w+_pb2) as ([\w_]+),\s*\)$",
        r"from . import \1 as \2",
        content,
        flags=re.MULTILINE,
    )
    # unparenthesised from-import: `from pkg import foo_pb2 as alias`
    content = re.sub(
        r"^from [\w\.]+ import (\w+_pb2) as ([\w_]+)$",
        r"from . import \1 as \2",
        content,
        flags=re.MULTILINE,
    )
    return content


def clean_schema_names(schema: dict, version: str) -> dict:
    import copy

    schema = copy.deepcopy(schema)

    def _clean_refs(node: object) -> None:
        if isinstance(node, dict):
            if "$ref" in node and isinstance(node["$ref"], str):
                if f"/{version}" in node["$ref"]:
                    node["$ref"] = node["$ref"].replace(f"/{version}", "/")
            for child_value in node.values():
                _clean_refs(child_value)
        elif isinstance(node, list):
            for item in node:
                _clean_refs(item)

    _clean_refs(schema)

    for section in _definition_sections(schema):
        for old_key in [key for key in section if key.startswith(version)]:
            new_key = old_key[len(version) :]
            if new_key:
                section[new_key] = section.pop(old_key)

    return schema


def inline_request_body_refs(schema: dict) -> dict:
    """Returns a copy of schema with requestBody $refs inlined from components/requestBodies.

    openapi-python-generator silently ignores requestBody entries that are bare
    $refs; inlining them ensures the generator emits a `data` parameter.
    """
    import copy

    schema = copy.deepcopy(schema)
    request_bodies = schema.get("components", {}).get("requestBodies", {})
    if not request_bodies:
        return schema
    for path_item in schema.get("paths", {}).values():
        for op in path_item.values():
            if not isinstance(op, dict):
                continue
            request_body = op.get("requestBody", {})
            if isinstance(request_body, dict) and "$ref" in request_body:
                rb_name = request_body["$ref"].rsplit("/", 1)[-1]
                if rb_name in request_bodies:
                    op["requestBody"] = copy.deepcopy(request_bodies[rb_name])
    return schema


def _definition_sections(schema: dict) -> list[dict]:
    sections: list[dict] = []
    if "definitions" in schema:
        sections.append(schema["definitions"])
    if "components" in schema:
        for c in ["schemas", "parameters", "responses", "requestBodies"]:
            if c in schema["components"]:
                sections.append(schema["components"][c])
    return sections


@contextlib.contextmanager
def patched_swagger(swagger_path: Path, version: str):
    """Yields a temp-file path containing the schema with clean names and inlined request bodies.

    The original swagger_path is never modified, so local schema checkouts stay clean.
    """
    from tempfile import NamedTemporaryFile

    schema = json.loads(swagger_path.read_text(encoding="utf-8"))
    schema = clean_schema_names(schema, version)
    schema = inline_request_body_refs(schema)
    with NamedTemporaryFile(
        mode="w",
        suffix=".json",
        delete=False,
        encoding="utf-8",
        dir=swagger_path.parent,
    ) as tmp:
        json.dump(schema, tmp)
        tmp_path = Path(tmp.name)
    try:
        yield tmp_path
    finally:
        tmp_path.unlink(missing_ok=True)


def patch_schema_for_clean_names(swagger_path: Path, version: str) -> None:
    """Scrubs version prefixes from models and inlines requestBody $refs.

    Modifies swagger_path in place. Prefer patched_swagger() for new call sites
    to avoid mutating the schema checkout.
    """
    schema = json.loads(swagger_path.read_text(encoding="utf-8"))
    schema = clean_schema_names(schema, version)
    schema = inline_request_body_refs(schema)
    swagger_path.write_text(json.dumps(schema), encoding="utf-8")


_PB_COMPANIONS_INIT = """\
# isort: skip_file
\"\"\"Proto companion registry: loads all shared vendor descriptors into the pool.

The load order is critical for proto descriptor registration and must not be
changed. The isort: skip_file directive prevents ruff from resorting these imports.
\"\"\"

# foundation: google/protobuf/descriptor.proto
from google.protobuf import descriptor_pb2 as _descriptor_pb2  # noqa: F401

# google/api/*.proto from googleapis-common-protos
from google.api import annotations_pb2 as _ga_annotations  # noqa: F401
from google.api import client_pb2 as _ga_client  # noqa: F401
from google.api import field_behavior_pb2 as _ga_field_behavior  # noqa: F401
from google.protobuf import duration_pb2 as _duration  # noqa: F401
from google.protobuf import struct_pb2 as _struct  # noqa: F401
from google.protobuf import timestamp_pb2 as _timestamp  # noqa: F401

# protoc-gen-openapiv2/options/*.proto from grpc-gateway (must be before kentik/core)
# openapiv2_pb2 must be before annotations_pb2 (annotations imports openapiv2)
from .protoc_gen_openapiv2.options import openapiv2_pb2 as _oa_openapiv2  # noqa: F401
from .protoc_gen_openapiv2.options import annotations_pb2 as _oa_annotations  # noqa: F401

# kentik/core/v202303/*.proto (must be after protoc-gen-openapiv2 companions)
import kentik_api.gen.core.pb.annotations_pb2 as _core_annotations  # noqa: F401, E402
import kentik_api.gen.core.pb.user_info_pb2 as _core_user_info  # noqa: F401, E402
"""


def _compile_proto_companions(schema_root: Path) -> None:
    """Compiles the protoc-gen-openapiv2 vendor protos into pb_companions/.

    These are third-party proto definitions that Kentik's service protos depend
    on via openapiv2 annotations. Compiling them here registers their
    descriptors so the service pb2 imports succeed at runtime.
    """
    companions_dir = SDK_OUTPUT_DIR / "pb_companions"
    vendor_path = (
        schema_root / "protovendor" / "github.com" / "grpc-ecosystem" / "grpc-gateway"
    )
    if not vendor_path.exists():
        print("    ⚠️  proto vendor path not found, skipping companion compilation.")
        return

    print("Compiling protoc-gen-openapiv2 proto companions...")

    options_out = companions_dir / "protoc_gen_openapiv2" / "options"
    options_out.mkdir(parents=True, exist_ok=True)
    (companions_dir / "__init__.py").write_text(_PB_COMPANIONS_INIT, encoding="utf-8")
    (companions_dir / "protoc_gen_openapiv2" / "__init__.py").write_text(
        "", encoding="utf-8"
    )
    (options_out / "__init__.py").write_text("", encoding="utf-8")

    proto_files = [
        "protoc-gen-openapiv2/options/annotations.proto",
        "protoc-gen-openapiv2/options/openapiv2.proto",
    ]
    cmd = [
        "uv",
        "run",
        "--with",
        "grpcio-tools",
        "python",
        "-m",
        "grpc_tools.protoc",
        f"-I{vendor_path}",
        f"--python_out={companions_dir}",
        *proto_files,
    ]
    try:
        subprocess.run(cmd, check=True, capture_output=True, text=True)
        # Patch bare 'protoc_gen_openapiv2' imports to the full package path so
        # the compiled pb2 files are importable from within this package.
        for pb_file in options_out.glob("*_pb2.py"):
            content = pb_file.read_text(encoding="utf-8")
            content = content.replace(
                "from protoc_gen_openapiv2.",
                "from kentik_api.gen.pb_companions.protoc_gen_openapiv2.",
            )
            pb_file.write_text(content, encoding="utf-8")
        print("    ✅ Proto companions compiled successfully.")
    except subprocess.CalledProcessError as e:
        print(f"    ❌ Proto companion compilation failed: {e.stderr or e.stdout}")


def generate_modular_sdk(repo_source=DEFAULT_REPO):
    # Setup directories
    SDK_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    (SDK_OUTPUT_DIR / "__init__.py").touch(exist_ok=True)

    print("Cleaning old modules...")
    for item in SDK_OUTPUT_DIR.iterdir():
        if item.is_dir() and item.name != "__pycache__":
            shutil.rmtree(item)

    with get_schema_root(repo_source) as schema_root:
        _compile_proto_companions(schema_root)
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
                with patched_swagger(swagger_path, version) as tmp_swagger:
                    run_cmd(openapi_generator_cmd(tmp_swagger, out_dir))

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
                                    content = _rewrite_grpc_imports(content)
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
        if service_dir.is_dir() and service_dir.name != "__pycache__":
            fixup.fix_generated_service(service_dir)

    print("\nFormatting...")
    run_cmd(
        ["uv", "run", "ruff", "check", "--select", "F,I", "--fix", str(SDK_OUTPUT_DIR)]
    )
    run_cmd(["uv", "run", "ruff", "format", str(SDK_OUTPUT_DIR)])

    print("\nGenerating Wrappers & Documentation...")
    wrapper_generation.generate()
    docs_rendering.generate()
    endpoint_docs_collector.render()

    print("\nFinal formatting pass for generated code...")
    run_cmd(
        ["uv", "run", "ruff", "check", "--select", "F,I", "--fix", str(SDK_OUTPUT_DIR)]
    )
    run_cmd(["uv", "run", "ruff", "format", str(SDK_OUTPUT_DIR)])
    # client_mixin.py lives outside gen/ but is also fully generated.
    run_cmd(
        [
            "uv",
            "run",
            "ruff",
            "format",
            str(PROJECT_ROOT / "src" / "kentik_api" / "client_mixin.py"),
        ]
    )

    # Run after ruff so it cannot reorder the header comments.
    _inject_generated_headers(SDK_OUTPUT_DIR)

    print("\n✅ SDK and Documentation Generation Complete!")


def _inject_generated_headers(output_dir: Path) -> None:
    """Prepends AUTO-GENERATED file headers to every .py file in gen/."""
    # Map a path segment to (source_file, function_name) for the annotation.
    _SRC: dict[str, tuple[str, str]] = {
        "models": ("openapi-python-generator", "model generation"),
        "error": (
            "scripts/generation/error_package.py",
            "generate_service_error_package()",
        ),
        "pb": ("grpc_tools.protoc", "proto compilation"),
    }

    count = 0
    for py_file in sorted(output_dir.rglob("*.py")):
        content = py_file.read_text(encoding="utf-8")

        # Skip files that already carry a file-level annotation.
        if content.startswith("# AUTO-GENERATED") or content.startswith(
            "# HAND-WRITTEN"
        ):
            continue
        # Skip wrapper files annotated via the class docstring.
        if '"""AUTO-GENERATED:' in content:
            continue

        rel_parts = py_file.relative_to(output_dir).parts

        # pb_companions: compiled by _compile_proto_companions() with isort:skip_file.
        if rel_parts[0] == "pb_companions":
            source, generator_func_name = (
                "scripts/generate_sdk.py",
                "_compile_proto_companions()",
            )
        elif len(rel_parts) >= 2 and rel_parts[-2] in _SRC:
            source, generator_func_name = _SRC[rel_parts[-2]]
        else:
            source, generator_func_name = (
                "scripts/generate_sdk.py",
                "generate_modular_sdk()",
            )

        header = (
            f"# AUTO-GENERATED: {source}, {generator_func_name}\n"
            "# Rebuilt on every `make generate`. Do not edit by hand.\n"
            "\n"
        )
        py_file.write_text(header + content, encoding="utf-8")
        count += 1

    print(f"    ✅ AUTO-GENERATED headers injected into {count} gen/ files.")


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
