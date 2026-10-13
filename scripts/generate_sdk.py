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

from generation import (
    api_surface,
    docs_rendering,
    error_package,
    fixup,
    parity,
    wrapper_generation,
)
from generation._shared import (
    PROJECT_ROOT,
    SDK_OUTPUT_DIR,
)
from generation.endpoint_docs import EndpointDocsCollector
from google.protobuf import descriptor_pb2

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
            # Logged so a CI determinism failure can be traced to the schema
            # commit it generated from, separating upstream drift from a
            # generator regression.
            commit = subprocess.run(
                ["git", "-C", str(tmp_path), "rev-parse", "HEAD"],
                capture_output=True,
                text=True,
                check=True,
            ).stdout.strip()
            print(f"Schema commit: {commit}")
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


def _relink_pb2_dependency_imports(output_dir: Path) -> int:
    """Repoints protoc's dependency imports at the flattened gen/<service>/pb/ layout.

    protoc writes these against the original proto package tree (`from
    kentik.core.v202303 import annotations_pb2`), which does not exist here. In a
    _pb2 module they look unused, but importing them is what registers each
    dependency in the descriptor pool, so an unresolved one makes
    AddSerializedFile raise TypeError at import and silently disables the whole
    service's gRPC transport. In a .pyi stub the same imports carry the types.
    """
    pattern = re.compile(
        r"^from ([\w\.]+) import (\w+_pb2) as ([\w_]+)$", flags=re.MULTILINE
    )
    rewritten = 0

    for pb_dir in sorted(output_dir.glob("*/pb")):
        siblings = {path.stem for path in pb_dir.glob("*_pb2.py")}

        def _replace(match: re.Match, siblings=siblings) -> str:
            package, module, alias = match.groups()
            if package.startswith("google."):
                return match.group(0)  # resolved by googleapis-common-protos
            if package.split(".")[0] == "protoc_gen_openapiv2":
                return (
                    f"from kentik_api.gen.pb_companions.{package} "
                    f"import {module} as {alias}"
                )
            if module in siblings:
                return f"from . import {module} as {alias}"
            parts = package.split(".")
            if parts[0] == "kentik" and len(parts) > 1:
                target = output_dir / parts[1] / "pb" / f"{module}.py"
                if target.exists():
                    return (
                        f"from kentik_api.gen.{parts[1]}.pb import {module} as {alias}"
                    )
            return match.group(0)

        for pb_file in sorted([*pb_dir.glob("*_pb2.py"), *pb_dir.glob("*.pyi")]):
            content = pb_file.read_text(encoding="utf-8")
            patched = pattern.sub(_replace, content)
            if patched != content:
                pb_file.write_text(patched, encoding="utf-8")
                rewritten += 1

    return rewritten


def _proto_collisions(
    selected_swagger_files: dict, openapi_base: Path, proto_base: Path
) -> dict[str, set[str]]:
    """Per service, the proto file stems that more than one compiled folder declares.

    Every folder of a service compiles into one flat pb/ directory, so without a
    rename the last `mitigation_pb2.py` written wins and the other is lost.
    """
    collisions: dict[str, set[str]] = {}
    for service, files in selected_swagger_files.items():
        folders: dict[str, set[Path]] = {}
        for metadata in files:
            folder = Path(metadata["path"]).relative_to(openapi_base).parent
            for proto in (proto_base / "kentik" / folder).glob("*.proto"):
                folders.setdefault(proto.stem, set()).add(folder)
        collisions[service] = {s for s, dirs in folders.items() if len(dirs) > 1}
    return collisions


def _pb_stem(package: str, stem: str, collisions: dict[str, set[str]]) -> str:
    """The pb/ module stem for proto `stem` in `package`, qualified when it collides.

    `kentik.alerting.types.v202506` + `mitigation` -> `mitigation_types_v202506`.
    """
    parts = package.split(".")
    if parts[0] != "kentik" or len(parts) < 3:
        return stem
    if stem not in collisions.get(parts[1], set()):
        return stem
    return "_".join([stem, *parts[2:]])


def _qualify_colliding_imports(content: str, collisions: dict[str, set[str]]) -> str:
    """Points protoc's `from kentik.<pkg> import <stem>_pb2` lines at renamed modules."""
    return re.sub(
        r"^(from (kentik(?:\.\w+)+) import )(\w+)_pb2\b",
        lambda m: f"{m[1]}{_pb_stem(m[2], m[3], collisions)}_pb2",
        content,
        flags=re.MULTILINE,
    )


def clean_schema_names(schema: dict, version: str) -> dict:
    import copy

    schema = copy.deepcopy(schema)

    # A versioned name whose stripped form already exists is a different schema,
    # for example an enum `v202505AlertAcknowledgement` next to the object
    # `AlertAcknowledgement`. Stripping it would overwrite the object, so it
    # keeps its prefix, and so do the references that point at it.
    keep_prefixed = {
        old_key
        for section in _definition_sections(schema)
        for old_key in section
        if old_key.startswith(version)
        and old_key[len(version) :] in section
        and len(old_key) > len(version)
    }
    for old_key in sorted(keep_prefixed):
        print(
            f"    ⚠️ Schema name collision: keeping `{old_key}` because "
            f"`{old_key[len(version) :]}` already exists."
        )

    def _clean_refs(node: object) -> None:
        if isinstance(node, dict):
            ref = node.get("$ref")
            if isinstance(ref, str) and f"/{version}" in ref:
                if ref.rsplit("/", 1)[-1] not in keep_prefixed:
                    node["$ref"] = ref.replace(f"/{version}", "/")
            for child_value in node.values():
                _clean_refs(child_value)
        elif isinstance(node, list):
            for item in node:
                _clean_refs(item)

    _clean_refs(schema)

    for section in _definition_sections(schema):
        for old_key in [
            key
            for key in section
            if key.startswith(version) and key not in keep_prefixed
        ]:
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


def oneof_members_by_definition(
    descriptors: descriptor_pb2.FileDescriptorSet,
) -> dict[str, set[str]]:
    """Maps each swagger definition name to the JSON names of its oneof members.

    Keys follow protoc-gen-openapiv2's naming: the last package component, then
    the message name chain (`v202505ExternalContext`). Proto3 `optional` fields
    sit in synthetic oneofs and are left out.
    """
    members: dict[str, set[str]] = {}

    def walk(prefix: str, messages) -> None:
        for message in messages:
            name = prefix + message.name
            in_oneof = {
                field.json_name
                for field in message.field
                if field.HasField("oneof_index") and not field.proto3_optional
            }
            if in_oneof:
                members[name] = in_oneof
            walk(name, message.nested_type)

    for file in descriptors.file:
        walk(file.package.rsplit(".", 1)[-1], file.message_type)
    return members


def relax_oneof_required(schema: dict, oneof_members: dict[str, set[str]]) -> dict:
    """Returns a copy of schema with oneof members removed from `required`.

    protoc-gen-openapiv2 drops the oneof grouping, so members marked REQUIRED
    all land in `required` and no valid message can satisfy the model.
    """
    import copy

    schema = copy.deepcopy(schema)
    for section in _definition_sections(schema):
        for name, definition in section.items():
            members = oneof_members.get(name)
            if not members or not isinstance(definition, dict):
                continue
            required = definition.get("required")
            if not required:
                continue
            kept = [field for field in required if field not in members]
            if kept:
                definition["required"] = kept
            else:
                del definition["required"]
    return schema


def relax_response_message_required(schema: dict) -> dict:
    """Returns a copy of schema where response models never require a message field.

    Proto REQUIRED binds the request, not the response (AIP-203), and an unset
    message field is absent from the response on both transports. Models only
    requests reach keep `required`, so a missing field still fails before a send.
    """
    import copy

    schema = copy.deepcopy(schema)
    definitions = {
        name: definition
        for section in _definition_sections(schema)
        for name, definition in section.items()
        if isinstance(definition, dict)
    }

    def refs(node: object) -> list[str]:
        if isinstance(node, dict):
            ref = node.get("$ref")
            found = [ref.rsplit("/", 1)[-1]] if isinstance(ref, str) else []
            return found + [r for value in node.values() for r in refs(value)]
        if isinstance(node, list):
            return [r for item in node for r in refs(item)]
        return []

    def is_message(name: str) -> bool:
        return "properties" in definitions.get(name, {})

    reachable: set[str] = set()
    pending = [
        name
        for path_item in schema.get("paths", {}).values()
        for op in path_item.values()
        if isinstance(op, dict)
        for name in refs(op.get("responses", {}))
    ]
    while pending:
        name = pending.pop()
        if name in reachable or name not in definitions:
            continue
        reachable.add(name)
        pending.extend(refs(definitions[name]))

    for name in reachable:
        definition = definitions[name]
        properties = definition.get("properties", {})
        required = definition.get("required")
        if not isinstance(required, list) or not required:
            continue
        kept = [
            field
            for field in required
            if not any(is_message(r) for r in refs(properties.get(field, {})))
            or properties.get(field, {}).get("type") == "array"
        ]
        if kept:
            definition["required"] = kept
        else:
            del definition["required"]
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
def patched_swagger(
    swagger_path: Path,
    version: str,
    oneof_members: dict[str, set[str]] | None = None,
):
    """Yields a temp-file path containing the schema with clean names and inlined request bodies.

    The original swagger_path is never modified, so local schema checkouts stay clean.
    """
    from tempfile import NamedTemporaryFile

    schema = json.loads(swagger_path.read_text(encoding="utf-8"))
    # Before clean_schema_names: oneof_members is keyed by the prefixed names.
    schema = relax_oneof_required(schema, oneof_members or {})
    schema = relax_response_message_required(schema)
    schema = clean_schema_names(schema, version)
    schema = inline_request_body_refs(schema)
    with NamedTemporaryFile(
        mode="w",
        suffix=".json",
        delete=False,
        encoding="utf-8",
    ) as tmp:
        json.dump(schema, tmp)
        tmp_path = Path(tmp.name)
    try:
        yield tmp_path
    finally:
        tmp_path.unlink(missing_ok=True)


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

        # Fail loudly on a corrupted/truncated schema checkout instead of
        # silently generating an incomplete SDK from it (2026-08-26 incident).
        # This MUST run before anything below touches SDK_OUTPUT_DIR: an
        # earlier version of this check ran after the "clean old modules"
        # step, so a validation failure still left src/kentik_api/gen/
        # wiped out -- discovered by manually reproducing the incident
        # end-to-end rather than trusting fixture tests alone.
        parity.validate_schema_files_or_raise(
            [
                Path(metadata["path"])
                for service_files in selected_swagger_files.values()
                for metadata in service_files
            ]
        )

        # Setup directories (only now, once the schema checkout is known-good)
        SDK_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        (SDK_OUTPUT_DIR / "__init__.py").touch(exist_ok=True)

        print("Cleaning old modules...")
        # Deliberately broader than iter_service_dirs(): pb_companions must be
        # wiped too, since _compile_proto_companions() regenerates it below.
        for item in SDK_OUTPUT_DIR.iterdir():
            if item.is_dir() and item.name != "__pycache__":
                shutil.rmtree(item)

        _compile_proto_companions(schema_root)

        proto_collisions = _proto_collisions(
            selected_swagger_files, openapi_base, proto_base
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
                # 1. GENERATE PROTOBUF (gRPC), first: REST models need its oneofs
                # -----------------------------------------------------------------
                oneof_members: dict[str, set[str]] = {}
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
                                f"--pyi_out={tmp_pb_path}",
                                f"--descriptor_set_out={tmp_pb_path / 'descriptors.pb'}",
                                "--include_imports",
                            ]
                            cmd.extend(rel_proto_files)

                            try:
                                subprocess.run(
                                    cmd, check=True, capture_output=True, text=True
                                )

                                generated_files = [
                                    path
                                    for suffix in ("*.py", "*.pyi")
                                    for path in tmp_pb_path.rglob(suffix)
                                ]
                                print(
                                    f"    ✅ Protoc successfully generated {len(generated_files)} files."
                                )

                                for gen_py in generated_files:
                                    package = ".".join(
                                        gen_py.relative_to(tmp_pb_path).parent.parts
                                    )
                                    stem, _, suffix = gen_py.name.partition("_pb2")
                                    target = pb_dir / (
                                        _pb_stem(package, stem, proto_collisions)
                                        + "_pb2"
                                        + suffix
                                    )
                                    target.write_text(
                                        _qualify_colliding_imports(
                                            gen_py.read_text(encoding="utf-8"),
                                            proto_collisions,
                                        ),
                                        encoding="utf-8",
                                    )

                                for pb_file in pb_dir.rglob("*_grpc.py"):
                                    content = pb_file.read_text(encoding="utf-8")
                                    content = _rewrite_grpc_imports(content)
                                    pb_file.write_text(content, encoding="utf-8")

                                oneof_members = oneof_members_by_definition(
                                    descriptor_pb2.FileDescriptorSet.FromString(
                                        (tmp_pb_path / "descriptors.pb").read_bytes()
                                    )
                                )

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
                                raise
                    else:
                        print(
                            "    ⚠️ Directory exists, but no .proto files found inside."
                        )
                else:
                    print("    ⚠️ No proto directory found, skipping gRPC.")

                # -----------------------------------------------------------------
                # 2. GENERATE OPENAPI (REST)
                # -----------------------------------------------------------------
                with patched_swagger(
                    swagger_path, version, oneof_members
                ) as tmp_swagger:
                    run_cmd(openapi_generator_cmd(tmp_swagger, out_dir))

                # Extract per-operation documentation now, while the swagger
                # file is still available -- rendered as real Sphinx text
                # later (endpoint_docs_collector.render()), once wrapper
                # methods exist.
                endpoint_docs_collector.extract(service, swagger_path)

        for service, swagger_paths in service_swagger_paths.items():
            service_dir = SDK_OUTPUT_DIR / service
            if service_dir.exists():
                error_package.generate_service_error_package(service_dir, swagger_paths)

    parity.validate_generated_service_parity(source_services, SDK_OUTPUT_DIR)

    # -----------------------------------------------------------------
    # 3. POST-PROCESSING (Rest & Models Cleanup)
    # -----------------------------------------------------------------
    print("\nPatching generated code...")
    # Deliberately broader than iter_service_dirs(), like the cleanup loop
    # above: fixup normalises every generated file, pb_companions included.
    for service_dir in SDK_OUTPUT_DIR.iterdir():
        if service_dir.is_dir() and service_dir.name != "__pycache__":
            fixup.fix_generated_service(service_dir)

    # Runs once every pb/ directory exists, so cross-service targets resolve.
    relinked = _relink_pb2_dependency_imports(SDK_OUTPUT_DIR)
    print(f"    ✅ Relinked descriptor dependency imports in {relinked} pb2 modules.")

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

    # Last: the surface record must reflect the final formatted output.
    surface_path = api_surface.generate()
    print(f"\nRecorded API surface in {surface_path.name}")
    print(
        api_surface.render_regeneration_alert(
            api_surface.recorded_at("HEAD"), api_surface.read(surface_path)
        )
    )

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
