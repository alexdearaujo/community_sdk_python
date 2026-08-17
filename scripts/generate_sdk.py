import argparse
import ast
import contextlib
import json
import os
import re
import shutil
import subprocess
import textwrap
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import TypedDict

# Configuration
PROJECT_ROOT = Path(__file__).parent.parent
SDK_OUTPUT_DIR = PROJECT_ROOT / "src" / "kentik_api" / "gen"
DEFAULT_REPO = "https://github.com/kentik/api-schema-public.git"
DEFAULT_OPENAPI_GENERATOR = "openapi-python-generator"
CUSTOM_OPENAPI_TEMPLATE_PATH = PROJECT_ROOT / "scripts" / "openapi_templates"
MD_FENCE = "`" * 3


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


def service_to_pascal_case(service: str) -> str:
    """Converts a snake_case service name to PascalCase."""
    return "".join(part.capitalize() for part in service.split("_") if part)


def discover_service_model_classes(service_dir: Path) -> set[str]:
    """Collects model class names generated for a service."""
    model_classes: set[str] = set()

    files_to_scan = (
        list((service_dir / "models").rglob("*.py"))
        if (service_dir / "models").exists()
        else []
    )
    if (service_dir / "models.py").exists():
        files_to_scan.append(service_dir / "models.py")

    for f in files_to_scan:
        model_classes.update(
            re.findall(r"^class ([A-Za-z0-9_]+)[\(:]", f.read_text(), re.MULTILINE)
        )

    return model_classes


def qualify_wrapper_annotation_types(text: str, model_classes: set[str]) -> str:
    """Qualifies model type names with rest_models in wrapper annotations."""
    if not model_classes:
        return text

    qualified = text
    for model_name in sorted(model_classes, key=len, reverse=True):
        qualified = re.sub(
            rf"(?<!\.)\b{re.escape(model_name)}\b",
            f"rest_models.{model_name}",
            qualified,
        )
    return qualified


def service_error_class_name(operation_id: str) -> str:
    """Builds a service-local exception name for an OpenAPI operation."""
    return f"{operation_id}Error"


def service_error_response_class_name(operation_id: str, status_code: str) -> str:
    """Builds a leaf error class name for a specific swagger response code."""
    status_name_map = {
        "default": "Unexpected",
        "400": "BadRequest",
        "401": "Unauthorized",
        "402": "PaymentRequired",
        "403": "Forbidden",
        "404": "NotFound",
        "405": "MethodNotAllowed",
        "409": "Conflict",
        "410": "Gone",
        "415": "UnsupportedMediaType",
        "422": "UnprocessableEntity",
        "429": "TooManyRequests",
        "500": "InternalServerError",
        "501": "NotImplemented",
        "502": "BadGateway",
        "503": "ServiceUnavailable",
        "504": "GatewayTimeout",
    }
    suffix = status_name_map.get(status_code, f"Http{status_code}")
    return f"{operation_id}{suffix}Error"


class ErrorResponseMetadata(TypedDict):
    description: str | None
    schema_ref: str | None


class OperationErrorMetadata(TypedDict):
    path: str
    method: str
    responses: dict[str, ErrorResponseMetadata]


def collect_operation_error_responses(
    swagger_path: Path,
) -> dict[str, OperationErrorMetadata]:
    """Extracts non-2xx response metadata for each operation from a swagger file."""
    with open(swagger_path, "r", encoding="utf-8") as f:
        schema = json.load(f)

    operation_errors: dict[str, OperationErrorMetadata] = {}

    for path, methods in schema.get("paths", {}).items():
        if not isinstance(methods, dict):
            continue

        for method, operation in methods.items():
            if not isinstance(operation, dict):
                continue

            operation_id = operation.get("operationId")
            if not isinstance(operation_id, str) or not operation_id:
                continue

            responses_obj = operation.get("responses", {})
            error_responses: dict[str, ErrorResponseMetadata] = {}

            if isinstance(responses_obj, dict):
                responses: dict[str, object] = responses_obj
                for status_code, response in responses.items():
                    status_code_text = str(status_code)
                    if status_code_text.startswith("2"):
                        continue

                    schema_ref: str | None = None
                    description: str | None = None
                    if isinstance(response, dict):
                        description_raw = response.get("description")
                        if isinstance(description_raw, str):
                            description = description_raw
                        content = response.get("content", {})
                        if isinstance(content, dict):
                            json_content = content.get("application/json", {})
                            if isinstance(json_content, dict):
                                schema = json_content.get("schema", {})
                                if isinstance(schema, dict):
                                    schema_ref_raw = schema.get("$ref")
                                    if isinstance(schema_ref_raw, str):
                                        schema_ref = schema_ref_raw

                    error_responses[status_code_text] = {
                        "description": description,
                        "schema_ref": schema_ref,
                    }

            if error_responses:
                operation_errors[operation_id] = {
                    "path": path,
                    "method": str(method).upper(),
                    "responses": error_responses,
                }

    return operation_errors


def merge_operation_error_responses(
    operation_error_sets: list[dict[str, OperationErrorMetadata]],
) -> dict[str, OperationErrorMetadata]:
    """Merges operation error maps from multiple swagger files for one service."""
    merged: dict[str, OperationErrorMetadata] = {}

    for operation_errors in operation_error_sets:
        for operation_id, metadata in operation_errors.items():
            existing = merged.get(operation_id)
            if existing is None:
                merged[operation_id] = {
                    "path": metadata["path"],
                    "method": metadata["method"],
                    "responses": dict(metadata["responses"]),
                }
                continue

            existing["responses"].update(metadata["responses"])

    return merged


def generate_service_error_package(
    service_dir: Path, swagger_paths: list[Path]
) -> None:
    """Generates a service-local error package from one or more swagger files."""
    service = service_dir.name
    title = service_to_pascal_case(service)
    model_classes = discover_service_model_classes(service_dir)
    operation_errors = merge_operation_error_responses(
        [
            collect_operation_error_responses(swagger_path)
            for swagger_path in swagger_paths
        ]
    )

    error_dir = service_dir / "error"
    error_dir.mkdir(exist_ok=True)

    base_imports = [
        "from __future__ import annotations",
        "",
        "from typing import Any",
        "",
        "from kentik_api.errors import HTTPException",
    ]

    model_import_line = None
    if "rpcStatus" in model_classes:
        model_import_line = "from ..models import rpcStatus"
        base_imports.extend(["", model_import_line])

    lines = [
        *base_imports,
        "",
        f"class {title}Error(HTTPException):",
        f'    """Base service-local error for the {service} API."""',
        "",
        "    @classmethod",
        f'    def _build_error(cls, response: Any, *, operation_name: str, method: str, path: str) -> "{title}Error":',
        '        preview = getattr(response, "text", "")[:200].replace("\\n", " ")',
        '        headers = getattr(response, "headers", {})',
        '        content_type = headers.get("content-type", "unknown") if hasattr(headers, "get") else "unknown"',
        "        details: dict[str, Any] = {",
        '            "content_type": content_type,',
        '            "preview": preview,',
        "        }",
        "        message = f\"{operation_name} failed with status code: {getattr(response, 'status_code', 'unknown')}\"",
        "        try:",
        "            payload = response.json()",
        "        except Exception:",
        "            payload = None",
        "        if isinstance(payload, dict):",
        '            details["response_json"] = payload',
    ]

    if "rpcStatus" in model_classes:
        lines.extend(
            [
                "            try:",
                "                status = rpcStatus.model_validate(payload)",
                "            except Exception:",
                "                status = None",
                "            if status is not None:",
                '                details["rpc_status"] = status.model_dump()',
                "                if status.code is not None:",
                '                    details["rpc_status_code"] = status.code',
                "                if status.message:",
                "                    message = status.message",
                "                else:",
                '                    message = payload.get("message") or message',
                "            else:",
                '                message = payload.get("message") or message',
            ]
        )
    else:
        lines.extend(
            [
                '            message = payload.get("message") or message',
            ]
        )

    lines.extend(
        [
            "        elif payload is not None:",
            '            details["response_json"] = payload',
            "        return cls(",
            '            getattr(response, "status_code", 500),',
            "            message,",
            "            method=method,",
            "            path=path,",
            "            details=details,",
            "        )",
            "",
            "    @classmethod",
            f'    def from_response(cls, response: Any, *, operation_name: str, method: str, path: str) -> "{title}Error":',
            '        status_key = str(getattr(response, "status_code", ""))',
            '        response_error_map = getattr(cls, "response_error_map", {})',
            '        target_cls = response_error_map.get(status_key) or response_error_map.get("default") or cls',
            "        return target_cls._build_error(",
            "            response,",
            "            operation_name=operation_name,",
            "            method=method,",
            "            path=path,",
            "        )",
            "",
        ]
    )

    leaf_class_names: list[str] = []
    operation_class_names: list[str] = []
    for operation_id, metadata in sorted(operation_errors.items()):
        operation_class = service_error_class_name(operation_id)
        operation_class_names.append(operation_class)
        response_mapping_entries: list[str] = []
        for status_code, response in sorted(
            metadata["responses"].items(), key=lambda item: item[0]
        ):
            description = response["description"] or ""
            schema_ref = response["schema_ref"] or ""
            leaf_class = service_error_response_class_name(operation_id, status_code)
            leaf_class_names.append(leaf_class)
            response_bits = f"{status_code}: {description} {schema_ref}".strip()
            leaf_doc = (
                f"Operation-local response error for {operation_id} ({response_bits})."
                if response_bits
                else f"Operation-local response error for {operation_id}."
            )
            lines.extend(
                [
                    "",
                    f"class {leaf_class}({title}Error):",
                    f'    """{leaf_doc}"""',
                    "    pass",
                ]
            )
            response_mapping_entries.append(f'        "{status_code}": {leaf_class},')

        lines.extend(
            [
                "",
                f"class {operation_class}({title}Error):",
                f'    """Operation-local error for {operation_id}."""',
                "    response_error_map = {",
                *response_mapping_entries,
                "    }",
            ]
        )

    lines.extend(
        [
            "",
            f"ERROR_BY_OPERATION: dict[str, type[{title}Error]] = {{",
        ]
    )

    for operation_id in sorted(operation_errors):
        lines.append(f'    "{operation_id}": {service_error_class_name(operation_id)},')

    lines.extend(
        [
            "}",
            "",
            f'__all__ = ["{title}Error",',
        ]
    )
    for leaf_class in leaf_class_names:
        lines.append(f'    "{leaf_class}",')
    for operation_class in operation_class_names:
        lines.append(f'    "{operation_class}",')
    lines.extend(
        [
            '    "ERROR_BY_OPERATION",',
            "]",
            "",
        ]
    )

    (error_dir / "__init__.py").write_text("\n".join(lines), encoding="utf-8")


def inject_service_error_handling(content: str) -> str:
    """Adds per-operation service error classes to generated REST modules."""
    operation_ids = sorted(
        set(re.findall(r"operation_name=['\"]([A-Za-z0-9_]+)['\"]", content))
    )
    if not operation_ids:
        return content

    error_class_names = [
        service_error_class_name(operation_id) for operation_id in operation_ids
    ]

    if "from ..error import" not in content:
        runtime_import = "from kentik_api.core.rest_runtime import request_json\n"
        if runtime_import in content:
            content = content.replace(
                runtime_import,
                runtime_import
                + "\nfrom ..error import "
                + ", ".join(error_class_names)
                + "\n",
                1,
            )

    def _inject_into_block(match: re.Match[str]) -> str:
        block = match.group(0)
        if "request_json(" not in block or "error_cls=" in block:
            return block

        operation_match = re.search(
            r"operation_name\s*=\s*['\"]([A-Za-z0-9_]+)['\"]", block
        )
        if not operation_match:
            return block

        error_class_name = service_error_class_name(operation_match.group(1))

        def _replace_operation_line(op_match: re.Match[str]) -> str:
            line = op_match.group(0)
            indent_match = re.match(r"^(\s*)", line)
            indent = indent_match.group(1) if indent_match else ""
            if "error_cls=" in block:
                return line
            return line + f"\n{indent}error_cls={error_class_name},"

        return re.sub(
            r"operation_name\s*=\s*['\"][^'\"]+['\"],",
            _replace_operation_line,
            block,
            count=1,
        )

    content = re.sub(
        r"^def\s+[A-Za-z_][A-Za-z0-9_]*\s*\(.*?(?=^def\s+[A-Za-z_]|\Z)",
        _inject_into_block,
        content,
        flags=re.MULTILINE | re.DOTALL,
    )
    return content


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


@dataclass(frozen=True)
class EndpointParam:
    name: str
    location: str
    type_label: str
    required: bool


@dataclass(frozen=True)
class EndpointResponse:
    status: str
    description: str
    type_label: str


@dataclass(frozen=True)
class EndpointDoc:
    tag: str
    method: str
    path: str
    operation_id: str
    summary: str
    description: str
    parameters: list[EndpointParam]
    request_body: EndpointParam | None
    responses: list[EndpointResponse]


def _schema_type_label(schema: object) -> str:
    """Renders a short, human-readable type label for an OpenAPI schema object."""
    if not isinstance(schema, dict):
        return "-"
    ref = schema.get("$ref")
    if isinstance(ref, str) and ref:
        return ref.rsplit("/", 1)[-1]
    if schema.get("type") == "array":
        return f"{_schema_type_label(schema.get('items'))}[]"
    schema_type = schema.get("type")
    if isinstance(schema_type, str) and schema_type:
        fmt = schema.get("format")
        return f"{schema_type} ({fmt})" if isinstance(fmt, str) and fmt else schema_type
    return "object"


def extract_endpoint_docs(swagger_path: Path) -> list[EndpointDoc]:
    """Extracts per-operation documentation (params, every response) from a swagger file.

    Unlike collect_operation_error_responses (which only looks at non-2xx
    responses, for error-class generation), this captures every declared
    response so it can be rendered as real Sphinx text -- tables and a
    generated usage example -- instead of a PlantUML table image.
    """
    with open(swagger_path, "r", encoding="utf-8") as f:
        schema = json.load(f)

    tags_raw = schema.get("tags") if isinstance(schema.get("tags"), list) else []
    default_tag = None
    for tag in tags_raw:
        if isinstance(tag, dict) and tag.get("name"):
            default_tag = str(tag["name"]).strip()
            break

    paths_obj = schema.get("paths") if isinstance(schema.get("paths"), dict) else {}
    method_order = ["get", "post", "put", "patch", "delete", "options", "head", "trace"]

    docs: list[EndpointDoc] = []
    for endpoint, methods in sorted(paths_obj.items(), key=lambda item: item[0]):
        if not isinstance(methods, dict):
            continue
        for method in method_order:
            op = methods.get(method)
            if not isinstance(op, dict):
                continue

            op_tags_raw = op.get("tags")
            op_tags = op_tags_raw if isinstance(op_tags_raw, list) else []
            tag = next(
                (
                    str(item).strip()
                    for item in op_tags
                    if isinstance(item, str) and str(item).strip()
                ),
                default_tag or "default",
            )

            parameters: list[EndpointParam] = []
            for param in op.get("parameters") or []:
                if not isinstance(param, dict):
                    continue
                parameters.append(
                    EndpointParam(
                        name=str(param.get("name") or "-"),
                        location=str(param.get("in") or "-"),
                        type_label=_schema_type_label(param.get("schema")),
                        required=bool(param.get("required", False)),
                    )
                )

            request_body: EndpointParam | None = None
            body = op.get("requestBody")
            if isinstance(body, dict):
                content = body.get("content", {})
                json_content = (
                    content.get("application/json", {})
                    if isinstance(content, dict)
                    else {}
                )
                request_body = EndpointParam(
                    name="data",
                    location="body",
                    type_label=_schema_type_label(
                        json_content.get("schema")
                        if isinstance(json_content, dict)
                        else None
                    ),
                    required=bool(body.get("required", False)),
                )

            responses: list[EndpointResponse] = []
            responses_obj = op.get("responses")
            if isinstance(responses_obj, dict):
                for status, resp in sorted(responses_obj.items()):
                    if not isinstance(resp, dict):
                        continue
                    content = resp.get("content", {})
                    json_content = (
                        content.get("application/json", {})
                        if isinstance(content, dict)
                        else {}
                    )
                    responses.append(
                        EndpointResponse(
                            status=str(status),
                            description=str(resp.get("description") or "-"),
                            type_label=_schema_type_label(
                                json_content.get("schema")
                                if isinstance(json_content, dict)
                                else None
                            ),
                        )
                    )

            docs.append(
                EndpointDoc(
                    tag=tag,
                    method=method.upper(),
                    path=str(endpoint),
                    operation_id=str(op.get("operationId") or "-"),
                    summary=str(op.get("summary") or ""),
                    description=str(op.get("description") or ""),
                    parameters=parameters,
                    request_body=request_body,
                    responses=responses,
                )
            )

    return docs


def render_diagrams():
    """Downloads PlantUML JAR (if missing) and renders the runtime architecture diagram to .svg."""
    PLANTUML_JAR_URL = "https://github.com/plantuml/plantuml/releases/download/v1.2026.6/plantuml-1.2026.6.jar"
    bin_dir = PROJECT_ROOT / "bin"
    bin_dir.mkdir(exist_ok=True)
    jar_path = bin_dir / "plantuml.jar"

    # 1. Ensure the JAR exists locally
    if not jar_path.exists():
        print("Downloading PlantUML JAR...")
        urllib.request.urlretrieve(PLANTUML_JAR_URL, jar_path)

    print("Patching local PUML titles and rendering to SVG...")

    # 2. Find all .puml files
    puml_paths = sorted(
        (PROJECT_ROOT / "docs" / "source" / "architecture").glob("*.puml")
    )

    if not puml_paths:
        print("⚠️ No .puml files found to render.")
        return

    # 3. Patch the files (removes duplicate @startuml tags or artifacts)
    for puml_path in puml_paths:
        content = puml_path.read_text(encoding="utf-8")
        patched = re.sub(r"^@startuml.*$", "@startuml", content, flags=re.MULTILINE)
        if patched != content:
            puml_path.write_text(patched, encoding="utf-8")

    # 4. Execute the JAR against all found files at once
    print(f"Rendering {len(puml_paths)} diagrams using local JAR...")
    cmd = ["java", "-jar", str(jar_path), "-tsvg"] + [str(p) for p in puml_paths]

    try:
        # We use check=True to catch if Java fails to execute
        subprocess.run(cmd, check=True)
        print("✅ Diagram generation complete!")
    except subprocess.CalledProcessError as e:
        print(f"❌ PlantUML rendering failed: {e}")


def generate_service_readmes():
    """Generates README.md files inside each service directory."""
    print("Generating module READMEs...")
    for service_dir in sorted(SDK_OUTPUT_DIR.iterdir(), key=lambda p: p.name):
        if not service_dir.is_dir() or service_dir.name == "__pycache__":
            continue

        service_name = service_dir.name

        lines = [
            f"# {service_name.replace('_', ' ').title()} Service",
            "",
            "This module was automatically generated from the Kentik OpenAPIv3 schema.",
            "",
            "For the full endpoint reference (parameters, responses, usage "
            "examples) and data model documentation, see the Sphinx docs: "
            f"`docs/source/services/{service_name}.md`.",
            "",
        ]

        doc_content = "\n".join(lines) + "\n"

        # Keep generated README self-contained and deterministic.
        (service_dir / "README.md").write_text(doc_content, encoding="utf-8")


def _module_name_from_path(py_path: Path, package_root: Path) -> str:
    rel = py_path.relative_to(package_root).with_suffix("")
    return "kentik_api." + ".".join(rel.parts)


def _resolve_import_from(current_module: str, level: int, module: str | None) -> str:
    if level == 0:
        return module or ""

    parts = current_module.split(".")[:-1]
    if level > 0:
        # Relative import semantics: one dot is current package.
        ups = max(level - 1, 0)
        parts = parts[: len(parts) - ups] if ups <= len(parts) else []
    suffix = module.split(".") if module else []
    return ".".join(parts + suffix)


def _module_group(module_name: str, source_file: Path | None = None) -> str | None:
    if module_name == "kentik_api.client":
        return "Client API"
    if module_name == "kentik_api.client_mixin":
        return "Client Mixin"
    if module_name.startswith("kentik_api.auth"):
        return "Auth Credentials"
    if module_name.startswith("kentik_api.core.api_config"):
        return "API Config"
    if module_name.startswith("kentik_api.core.rest_runtime"):
        return "REST Runtime"
    if module_name.startswith("kentik_api.errors"):
        return "Error Types"
    if module_name.startswith("kentik_api.transports.base"):
        return "Transport Base"
    if module_name.startswith("kentik_api.transports.rest_client"):
        return "REST Transport"
    if module_name.startswith("kentik_api.transports.grpc_client"):
        return "gRPC Transport"

    if module_name.startswith("kentik_api.gen."):
        if ".error" in module_name:
            return "Generated Error Classes"
        if ".services." in module_name:
            if source_file is not None and source_file.name[:1].islower():
                return "Generated Service Wrappers"
            tail = module_name.split(".")[-1]
            if tail and tail[0].islower():
                return "Generated Service Wrappers"
            return "Generated REST Services"
        if ".models" in module_name:
            return "Generated Models"

    return None


def generate_runtime_architecture_docs() -> None:
    """Generates a high-level runtime architecture page and dependency graph."""
    package_root = PROJECT_ROOT / "src" / "kentik_api"
    docs_root = PROJECT_ROOT / "docs" / "source"
    architecture_dir = docs_root / "architecture"
    architecture_dir.mkdir(parents=True, exist_ok=True)

    scan_paths: list[Path] = []
    scan_paths.extend([package_root / "client.py", package_root / "client_mixin.py"])
    for rel in ("auth", "core", "errors", "transports"):
        root = package_root / rel
        if root.exists():
            scan_paths.extend(sorted(root.rglob("*.py")))

    gen_root = package_root / "gen"
    if gen_root.exists():
        for service_dir in sorted([p for p in gen_root.iterdir() if p.is_dir()]):
            for folder in ("services", "service"):
                sf = service_dir / folder
                if sf.exists():
                    scan_paths.extend(sorted(sf.glob("*.py")))
            err_file = service_dir / "error" / "__init__.py"
            if err_file.exists():
                scan_paths.append(err_file)

    edge_counts: dict[tuple[str, str], int] = {}
    nodes: set[str] = set()

    for py_file in scan_paths:
        if not py_file.exists() or py_file.name == "__init__.py":
            continue
        try:
            tree = ast.parse(py_file.read_text(encoding="utf-8"))
        except Exception:
            continue

        current_module = _module_name_from_path(py_file, package_root)
        src_group = _module_group(current_module, source_file=py_file)
        if src_group is None:
            continue
        nodes.add(src_group)

        for node in ast.walk(tree):
            target_modules: list[str] = []
            if isinstance(node, ast.Import):
                target_modules.extend(alias.name for alias in node.names)
            elif isinstance(node, ast.ImportFrom):
                target_modules.append(
                    _resolve_import_from(current_module, node.level, node.module)
                )

            for target_module in target_modules:
                if not target_module.startswith("kentik_api"):
                    continue
                dst_group = _module_group(target_module)
                if dst_group is None or dst_group == src_group:
                    continue
                nodes.add(dst_group)
                key = (src_group, dst_group)
                edge_counts[key] = edge_counts.get(key, 0) + 1

    puml_lines = [
        "@startuml",
        "title Kentik SDK Runtime Dependency Map",
        "left to right direction",
        "skinparam componentStyle rectangle",
        "skinparam shadowing false",
        "",
    ]

    for node_name in sorted(nodes):
        puml_lines.append(
            f'component "{node_name}" as {re.sub(r"[^A-Za-z0-9_]", "_", node_name)}'
        )

    puml_lines.append("")
    for (src, dst), count in sorted(edge_counts.items()):
        src_id = re.sub(r"[^A-Za-z0-9_]", "_", src)
        dst_id = re.sub(r"[^A-Za-z0-9_]", "_", dst)
        label = f" : x{count}" if count > 1 else ""
        puml_lines.append(f"{src_id} --> {dst_id}{label}")

    puml_lines.append("@enduml")
    (architecture_dir / "sdk_runtime_dependencies.puml").write_text(
        "\n".join(puml_lines) + "\n", encoding="utf-8"
    )

    architecture_md = [
        "# SDK Runtime Architecture",
        "",
        "This page explains how core runtime modules and generated services connect at runtime.",
        "",
        "## Runtime Flow",
        "",
        "1. `kentik_api.client.KentikAPI` reads credentials and selects transport.",
        "2. `kentik_api.client_mixin.KentikClientMixin` mounts generated service wrappers.",
        "3. Wrapper classes in `kentik_api.gen.<service>.services.<service>` delegate to generated REST functions.",
        "4. Generated REST services use `kentik_api.core.api_config` and `kentik_api.core.rest_runtime`.",
        "5. Runtime failures are normalized into `kentik_api.errors` and generated service-local error classes.",
        "",
        "## Module Dependency Graph",
        "",
        "![Runtime Dependency Graph](architecture/sdk_runtime_dependencies.svg)",
        "",
        "## Reading The Graph",
        "",
        "- `Client API` and `Client Mixin` are the orchestration entrypoints.",
        "- `Generated Service Wrappers` are transport-aware facades exposed as `client.<service>`.",
        "- `Generated REST Services` host operation functions generated from OpenAPI schemas.",
        "- `API Config`, `REST Runtime`, and `Error Types` form the shared runtime foundation.",
        "",
    ]
    (docs_root / "sdk_runtime_architecture.md").write_text(
        "\n".join(architecture_md), encoding="utf-8"
    )

    index_path = docs_root / "index.md"
    if index_path.exists():
        index_text = index_path.read_text(encoding="utf-8")
        if "sdk_runtime_architecture" not in index_text:
            marker = "local_generation_workflow\n"
            if marker in index_text:
                index_text = index_text.replace(
                    marker, marker + "sdk_runtime_architecture\n", 1
                )
            else:
                index_text += "\nsdk_runtime_architecture\n"
            index_path.write_text(index_text, encoding="utf-8")


def generate_client_mixin():
    """Generates an IDE-friendly Mixin class that mounts all service wrappers."""
    print("Generating IDE-Friendly Client Mixin...")

    imports = []
    type_hints = []
    mounts = []

    for service_dir in sorted(SDK_OUTPUT_DIR.iterdir()):
        if not service_dir.is_dir() or service_dir.name in (
            "__pycache__",
            "docs",
            "core",
            "pb",
        ):
            continue

        service = service_dir.name
        services_folder = service_dir / "services"
        if not services_folder.exists():
            services_folder = service_dir / "service"
            if not services_folder.exists():
                continue

        wrapper_file = services_folder / f"{service}.py"
        if not wrapper_file.exists():
            continue

        title = service_to_pascal_case(service)
        wrapper_class = f"{title}ServiceWrapper"

        # 1. Setup the import from the encapsulated gen directory
        imports.append(
            f"from kentik_api.gen.{service}.{services_folder.name}.{service} import {wrapper_class}"
        )

        # 2. Setup the IDE type hint
        type_hints.append(f"        {service}: '{wrapper_class}'")

        # 3. Setup the runtime mounting logic
        mounts.append(f"        self.{service} = {wrapper_class}(self._transport)")

    mixin_code = [
        "from typing import TYPE_CHECKING",
        "",
        *imports,
        "",
        "if TYPE_CHECKING:",
        "    from kentik_api.transports.grpc_client import GrpcTransport",
        "    from kentik_api.transports.rest_client import RestTransport",
        "",
        "class KentikClientMixin:",
        '    """Auto-generated Mixin to wire up all service wrappers to the main client."""',
        "",
        "    if TYPE_CHECKING:",
        "        _transport: 'GrpcTransport | RestTransport'",
        *type_hints,
        "",
        "    def _mount_generated_services(self) -> None:",
        '        """Mounts all generated service wrappers using the active transport."""',
        *mounts,
        "",
    ]

    mixin_file = PROJECT_ROOT / "src" / "kentik_api" / "client_mixin.py"
    mixin_file.write_text("\n".join(mixin_code), encoding="utf-8")


def generate_service_wrappers():
    """Auto-generates the dual-transport wrapper classes for every service."""
    print("Generating unified service wrappers...")

    def _to_snake_case(name: str) -> str:
        return re.sub(r"(?<!^)(?=[A-Z])", "_", name).lower()

    for service_dir in SDK_OUTPUT_DIR.iterdir():
        if not service_dir.is_dir() or service_dir.name in (
            "__pycache__",
            "docs",
            "core",
            "pb",
        ):
            continue

        service = service_dir.name
        title = service_to_pascal_case(service)
        model_classes = discover_service_model_classes(service_dir)

        # 1. Dynamically find the services directory
        services_folder = service_dir / "services"
        if not services_folder.exists():
            services_folder = service_dir / "service"
            if not services_folder.exists():
                continue

        # 2. Collect generated REST service modules (e.g. DeviceService.py, SyntheticsAdminService.py)
        rest_files = [
            f
            for f in sorted(services_folder.glob("*.py"))
            if f.name != "__init__.py"
            and f.name != f"{service}.py"
            and not f.name.startswith("async_")
            and f.stem.endswith("Service")
        ]

        if not rest_files:
            print(
                f"    ⚠️ Could not find REST functions for {service}, skipping wrapper."
            )
            continue

        required_typing_symbols = {"Union", "cast"}

        wrapper_code = [
            "from typing import Union, cast",
            f"from kentik_api.gen.{service} import models as rest_models",
            "from kentik_api.transports.grpc_client import GrpcTransport",
            "from kentik_api.transports.rest_client import RestTransport",
            "",
            f"class {title}ServiceWrapper:",
            '    """Unified Service routing to either gRPC or REST."""',
            "    def __init__(self, transport: Union[GrpcTransport, RestTransport]):",
            "        self._transport = transport",
            "        if isinstance(self._transport, GrpcTransport):",
            "            pass # TODO: Initialize gRPC stub here",
            "",
        ]

        emitted_method_names: set[str] = set()

        for idx, service_py in enumerate(rest_files, start=1):
            rest_module_name = service_py.stem  # e.g., 'DeviceService'
            module_alias = f"Rest{title}Module{idx}"
            wrapper_code.insert(
                2 + (idx - 1),
                f"import kentik_api.gen.{service}.{services_folder.name}.{rest_module_name} as {module_alias}",
            )

            content = service_py.read_text(encoding="utf-8")

            # Regex to find all generated functions
            func_pattern = re.compile(
                r"^def\s+([A-Z][a-zA-Z0-9_]*)\s*\((.*?)\)\s*->\s*([a-zA-Z0-9_\[\]\.]+):",
                re.MULTILINE | re.DOTALL,
            )

            for match in func_pattern.finditer(content):
                func_name_pascal = match.group(1)
                func_args_raw = match.group(2)
                return_type = match.group(3)

                # Convert PascalCase to snake_case (ListDevices -> list_devices)
                func_name_snake = _to_snake_case(func_name_pascal)

                # Keep wrapper method names unique across the full class.
                # If a collision occurs (e.g., many sub-services each define `List`),
                # prefix with module name and then add numeric suffixes if needed.
                unique_method_name = func_name_snake
                if unique_method_name in emitted_method_names:
                    module_prefix = _to_snake_case(
                        re.sub(r"Service$", "", rest_module_name)
                    )
                    unique_method_name = f"{module_prefix}_{func_name_snake}"
                    suffix = 2
                    while unique_method_name in emitted_method_names:
                        unique_method_name = (
                            f"{module_prefix}_{func_name_snake}_{suffix}"
                        )
                        suffix += 1

                emitted_method_names.add(func_name_snake)
                emitted_method_names.add(unique_method_name)

                # Clean up the signature for the wrapper (remove the api_config_override)
                sig_args = re.sub(
                    r"api_config_override:\s*Optional\[APIConfig\]\s*=\s*None,?\s*",
                    "",
                    func_args_raw,
                )
                sig_args = qualify_wrapper_annotation_types(sig_args, model_classes)
                return_type = qualify_wrapper_annotation_types(
                    return_type, model_classes
                )

                # Service modules may alias typing.List to TypingList to avoid
                # collisions with functions named `List`; wrappers should expose
                # standard List annotations.
                sig_args = re.sub(r"\bTypingList\b", "List", sig_args)
                return_type = re.sub(r"\bTypingList\b", "List", return_type)

                for typing_symbol in (
                    "Any",
                    "Optional",
                    "Dict",
                    "List",
                    "Tuple",
                    "Set",
                    "Literal",
                    "Callable",
                ):
                    if re.search(rf"\b{typing_symbol}\b", sig_args) or re.search(
                        rf"\b{typing_symbol}\b", return_type
                    ):
                        required_typing_symbols.add(typing_symbol)

                # Extract variable names to pass into the REST function call
                arg_names = re.findall(r"([a-zA-Z0-9_]+)\s*:", func_args_raw)
                call_args = [
                    f"{arg}={arg}" for arg in arg_names if arg != "api_config_override"
                ]

                call_args_str = ", ".join(call_args)
                if call_args_str:
                    call_args_str = ", " + call_args_str

                wrapper_code.extend(
                    [
                        f"    def {unique_method_name}(self, {sig_args}) -> {return_type}:",
                        "        if isinstance(self._transport, GrpcTransport):",
                        f'            raise NotImplementedError("gRPC translation for {func_name_pascal} is not yet implemented.")',
                        "        elif isinstance(self._transport, RestTransport):",
                        "            rest_transport = cast(RestTransport, self._transport)",
                        f"            return {module_alias}.{func_name_pascal}(",
                        f"                api_config_override=rest_transport.api_config{call_args_str}",
                        "            )",
                        "        else:",
                        '            raise TypeError(f"Unsupported transport type: {self._transport.__class__.__name__}")',
                        "",
                    ]
                )

        preferred_order = [
            "Union",
            "cast",
            "Any",
            "Optional",
            "Dict",
            "List",
            "Tuple",
            "Set",
            "Literal",
            "Callable",
        ]
        ordered_symbols = [
            symbol for symbol in preferred_order if symbol in required_typing_symbols
        ]
        wrapper_code[0] = f"from typing import {', '.join(ordered_symbols)}"

        # Write to gen/<service>/services/<service>.py
        wrapper_file = services_folder / f"{service}.py"
        wrapper_file.write_text("\n".join(wrapper_code), encoding="utf-8")


def _md_cell(value: str) -> str:
    """Escapes text for safe use inside a single Markdown table cell."""
    text = re.sub(r"\s+", " ", str(value)).strip()
    return text.replace("|", "\\|") or "-"


def _normalize_path_for_matching(path: str) -> str:
    """Strips dots from path-parameter placeholders (`{device.id}` -> `{deviceid}`)
    so a raw-schema path and its generated-code path template compare equal."""
    return re.sub(r"\{([a-zA-Z0-9_]+)\.([a-zA-Z0-9_]+)\}", r"{\1\2}", path)


def _rest_function_path_and_method(
    rest_file: Path, function_name: str
) -> tuple[str, str] | None:
    """Extracts method/path literals from a generated REST function's
    request_json(...) call, via AST (no import/execution)."""
    try:
        tree = ast.parse(rest_file.read_text(encoding="utf-8"))
    except Exception:
        return None

    for node in tree.body:
        if not (isinstance(node, ast.FunctionDef) and node.name == function_name):
            continue
        for call_node in ast.walk(node):
            if not (
                isinstance(call_node, ast.Call)
                and isinstance(call_node.func, ast.Name)
                and call_node.func.id == "request_json"
            ):
                continue
            http_method = None
            path_parts: list[str] = []
            for kw in call_node.keywords:
                if kw.arg == "method" and isinstance(kw.value, ast.Constant):
                    http_method = str(kw.value.value).upper()
                if kw.arg == "path":
                    if isinstance(kw.value, ast.Constant):
                        path_parts = [str(kw.value.value)]
                    elif isinstance(kw.value, ast.JoinedStr):
                        for part in kw.value.values:
                            if isinstance(part, ast.Constant):
                                path_parts.append(str(part.value))
                            elif isinstance(part, ast.FormattedValue):
                                path_parts.append(f"{{{ast.unparse(part.value)}}}")
            if http_method and path_parts:
                return http_method, "".join(path_parts)
    return None


def _parse_wrapper_method_signatures(
    wrapper_file: Path,
) -> dict[tuple[str, str], tuple[str, list[tuple[str, str, bool]]]]:
    """Maps (http_method, normalized_path) -> (wrapper_method_name, params).

    Keyed by method+path rather than operationId: multi-swagger-file
    services legitimately reuse generic operationIds like "List"/"Get"
    across different underlying REST modules (e.g. alerting's AlertService
    and SuppressionService both declare an operationId of exactly "List"),
    so operationId alone can't disambiguate which wrapper method an
    EndpointDoc (extracted straight from one swagger file) corresponds to.
    Method+path is guaranteed unique -- OpenAPI forbids two operations
    sharing both within one merged service.

    Reads the actual generated ServiceWrapper class and its underlying REST
    module (via AST, no import/execution) so example snippets always match
    the real, callable signature -- including flattened nested-object
    parameter names like `pagination.limit` -> `paginationlimit` that only
    exist post-generation.
    """
    tree = ast.parse(wrapper_file.read_text(encoding="utf-8"))
    services_folder = wrapper_file.parent

    module_alias_to_file: dict[str, Path] = {}
    for node in tree.body:
        if isinstance(node, ast.Import):
            for alias in node.names:
                if not alias.asname or "." not in alias.name:
                    continue
                candidate = services_folder / f"{alias.name.rsplit('.', 1)[-1]}.py"
                if candidate.exists():
                    module_alias_to_file[alias.asname] = candidate

    wrapper_class = None
    for node in tree.body:
        if isinstance(node, ast.ClassDef) and node.name.endswith("ServiceWrapper"):
            wrapper_class = node
            break
    if wrapper_class is None:
        return {}

    mapping: dict[tuple[str, str], tuple[str, list[tuple[str, str, bool]]]] = {}
    for node in wrapper_class.body:
        if not isinstance(node, ast.FunctionDef) or node.name == "__init__":
            continue

        alias = None
        operation_id = None
        for sub in ast.walk(node):
            if (
                isinstance(sub, ast.Return)
                and isinstance(sub.value, ast.Call)
                and isinstance(sub.value.func, ast.Attribute)
                and isinstance(sub.value.func.value, ast.Name)
                and sub.value.func.value.id.startswith("Rest")
            ):
                alias = sub.value.func.value.id
                operation_id = sub.value.func.attr
                break
        if alias is None or operation_id is None:
            continue

        rest_file = module_alias_to_file.get(alias)
        if rest_file is None:
            continue
        metadata = _rest_function_path_and_method(rest_file, operation_id)
        if metadata is None:
            continue
        http_method, path_template = metadata

        params: list[tuple[str, str, bool]] = []
        args = node.args
        defaults_start = len(args.args) - len(args.defaults)
        for idx, arg in enumerate(args.args):
            if arg.arg == "self":
                continue
            annotation_text = ast.unparse(arg.annotation) if arg.annotation else "Any"
            params.append((arg.arg, annotation_text, idx < defaults_start))
        for arg, default in zip(args.kwonlyargs, args.kw_defaults):
            annotation_text = ast.unparse(arg.annotation) if arg.annotation else "Any"
            params.append((arg.arg, annotation_text, default is None))

        mapping[(http_method, _normalize_path_for_matching(path_template))] = (
            node.name,
            params,
        )

    return mapping


def _example_value_for_annotation(annotation_text: str, name: str) -> str:
    """Builds a plausible Python source snippet for a parameter's example value."""
    text = annotation_text.strip()
    if text.startswith("Optional[") and text.endswith("]"):
        text = text[len("Optional[") : -1].strip()
    for list_prefix in ("List[", "list["):
        if text.startswith(list_prefix) and text.endswith("]"):
            inner = text[len(list_prefix) : -1].strip()
            return f"[{_example_value_for_annotation(inner, name)}]"

    if text == "str":
        return f'"{name}-example"'
    if text == "int":
        return "1"
    if text == "float":
        return "1.0"
    if text == "bool":
        return "True"
    if text == "bytes":
        return 'b"example"'
    if text in ("Any", ""):
        return "..."

    # Anything else is a model reference (e.g. rest_models.CreateASGroupRequest).
    class_name = text.rsplit(".", 1)[-1]
    return f"{class_name}(...)"


def _render_example_snippet(
    service: str, method_name: str, params: list[tuple[str, str, bool]]
) -> str:
    """Renders a runnable-looking usage example from a real wrapper method signature."""
    required_params = [p for p in params if p[2]]
    lines = [
        "from kentik_api.client import KentikAPI",
        "",
        "client = KentikAPI()  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env",
    ]
    if required_params:
        lines.append(f"response = client.{service}.{method_name}(")
        for param_name, annotation_text, _ in required_params:
            lines.append(
                f"    {param_name}={_example_value_for_annotation(annotation_text, param_name)},"
            )
        lines.append(")")
    else:
        lines.append(f"response = client.{service}.{method_name}()")
    return "\n".join(lines)


def _render_endpoint_section(
    service: str,
    doc: EndpointDoc,
    wrapper_signatures: dict[tuple[str, str], tuple[str, list[tuple[str, str, bool]]]],
    heading_level: int = 4,
) -> list[str]:
    heading = "#" * heading_level
    lines = [f"{heading} `{doc.method}` `{doc.path}`", ""]
    if doc.summary:
        lines.extend([doc.summary, ""])
    if doc.description and doc.description != doc.summary:
        lines.extend([doc.description, ""])

    all_params = list(doc.parameters)
    if doc.request_body:
        all_params.append(doc.request_body)

    if all_params:
        lines.extend(
            [
                "**Parameters**",
                "",
                "| Name | In | Type | Required |",
                "|------|----|------|----------|",
            ]
        )
        for param in all_params:
            # Generated wrapper methods flatten dotted nested-object params
            # (e.g. schema `asGroup.id` -> kwarg `asGroupid`); show the name
            # callers actually type, matching the example below.
            display_name = param.name.replace(".", "")
            lines.append(
                f"| `{_md_cell(display_name)}` | {_md_cell(param.location)} | "
                f"`{_md_cell(param.type_label)}` | {'Yes' if param.required else 'No'} |"
            )
        lines.append("")

    if doc.responses:
        lines.extend(
            [
                "**Responses**",
                "",
                "| Status | Description | Model |",
                "|--------|--------------|-------|",
            ]
        )
        for resp in doc.responses:
            lines.append(
                f"| {_md_cell(resp.status)} | {_md_cell(resp.description)} | "
                f"`{_md_cell(resp.type_label)}` |"
            )
        lines.append("")

    signature = wrapper_signatures.get(
        (doc.method, _normalize_path_for_matching(doc.path))
    )
    if signature:
        method_name, params = signature
        lines.extend(
            [
                "**Example**",
                "",
                f"{MD_FENCE}python",
                _render_example_snippet(service, method_name, params),
                MD_FENCE,
                "",
            ]
        )

    return lines


def _autodoc_directive_for_model(models_dir: Path, class_name: str) -> str:
    """Picks the right autodoc directive for a generated model class.

    Most generated classes are Pydantic BaseModel subclasses, which
    sphinxcontrib.autodoc_pydantic renders beautifully via
    `autopydantic_model`. But OpenAPI enum schemas generate plain
    `class X(str, Enum)` classes -- feeding those into autopydantic_model
    crashes the Sphinx build (it assumes `__pydantic_decorators__` exists),
    so they need the standard `autoclass` directive instead.
    """
    model_file = models_dir / f"{class_name}.py"
    try:
        tree = ast.parse(model_file.read_text(encoding="utf-8"))
    except Exception:
        return "autopydantic_model"

    for node in tree.body:
        if not (isinstance(node, ast.ClassDef) and node.name == class_name):
            continue
        for base in node.bases:
            base_name = ast.unparse(base)
            if base_name.rsplit(".", 1)[-1] == "BaseModel":
                return "autopydantic_model"
        return "autoclass"

    return "autopydantic_model"


def generate_sphinx_stubs(service_endpoint_docs: dict[str, list[EndpointDoc]]):
    """Generates Sphinx MyST stubs with real per-endpoint text and model docs.

    Replaces the old PlantUML "API table" image (unreadable once summaries/
    descriptions got long, and rendered even for swagger files with zero
    operations) with real MyST tables plus an auto-generated usage example
    per endpoint, and replaces the PlantUML model class diagrams (illegible
    once a service has more than a couple dozen models, e.g. alerting's 185)
    with sphinxcontrib.autodoc_pydantic's per-model field/JSON-schema docs.
    """
    print("Generating Sphinx documentation stubs...")

    DOCS_SERVICES_DIR = PROJECT_ROOT / "docs" / "source" / "services"
    DOCS_SERVICES_DIR.mkdir(parents=True, exist_ok=True)

    index_entries: list[str] = []

    for service_dir in sorted(SDK_OUTPUT_DIR.iterdir(), key=lambda p: p.name):
        if not service_dir.is_dir() or service_dir.name in (
            "__pycache__",
            "docs",
            "core",
        ):
            continue

        service = service_dir.name
        title = service.replace("_", " ").title()

        services_folder = service_dir / "services"
        if not services_folder.exists():
            services_folder = service_dir / "service"
        wrapper_file = (
            services_folder / f"{service}.py" if services_folder.exists() else None
        )
        wrapper_signatures = (
            _parse_wrapper_method_signatures(wrapper_file)
            if wrapper_file and wrapper_file.exists()
            else {}
        )

        lines = [f"# {title} Service", "", "## Endpoints", ""]

        endpoint_docs = service_endpoint_docs.get(service, [])
        if not endpoint_docs:
            lines.extend(
                [
                    "This service's schema defines shared types only -- no REST endpoints.",
                    "",
                ]
            )
        else:
            grouped: dict[str, list[EndpointDoc]] = {}
            group_order: list[str] = []
            for doc in endpoint_docs:
                if doc.tag not in grouped:
                    grouped[doc.tag] = []
                    group_order.append(doc.tag)
                grouped[doc.tag].append(doc)

            show_group_headers = len(group_order) > 1
            endpoint_heading_level = 4 if show_group_headers else 3
            for group_name in group_order:
                if show_group_headers:
                    lines.extend([f"### {group_name}", ""])
                # A thematic break between consecutive endpoints within a
                # group makes long pages (e.g. alerting's 37 operations)
                # scannable -- without it, sections with the same shape
                # (heading, prose, two tables, a code block) visually
                # bleed into each other. Not needed before the first
                # endpoint in a group: the group/service heading above it
                # is already a strong enough break.
                for idx, doc in enumerate(grouped[group_name]):
                    if idx > 0:
                        lines.extend(["---", ""])
                    lines.extend(
                        _render_endpoint_section(
                            service, doc, wrapper_signatures, endpoint_heading_level
                        )
                    )

        lines.extend(["## Data Models", ""])
        models_dir = service_dir / "models"
        model_classes = sorted(discover_service_model_classes(service_dir))
        if not model_classes:
            lines.extend(["No data models for this service.", ""])
        else:
            for class_name in model_classes:
                directive = _autodoc_directive_for_model(models_dir, class_name)
                lines.extend(
                    [
                        f"{MD_FENCE}{{eval-rst}}",
                        f".. {directive}:: kentik_api.gen.{service}.models.{class_name}",
                        *(["   :members:"] if directive == "autoclass" else []),
                        f"{MD_FENCE}",
                        "",
                    ]
                )

        stub_content = "\n".join(lines)

        (DOCS_SERVICES_DIR / f"{service}.md").write_text(stub_content, encoding="utf-8")
        index_entries.append(service)

    index_content = (
        "# API Services\n\n"
        "For a runtime-level map of how the SDK client, mixin, auth/core/errors, "
        "and generated services connect, see "
        "[SDK Runtime Architecture](../sdk_runtime_architecture.md).\n\n"
        f"{MD_FENCE}{{toctree}}\n:maxdepth: 1\n\n"
    )
    index_content += "\n".join(sorted(index_entries)) + "\n"
    index_content += f"{MD_FENCE}\n"
    (DOCS_SERVICES_DIR / "index.md").write_text(index_content, encoding="utf-8")


class SwaggerFileMetadata(TypedDict):
    path: Path
    service: str
    namespace: tuple[str, ...]
    version: str
    filename: str


def _swagger_file_metadata(
    swagger_path: Path, openapi_base: Path
) -> SwaggerFileMetadata:
    """Extracts normalized metadata for a swagger file path."""
    rel = swagger_path.relative_to(openapi_base)
    if len(rel.parts) < 3:
        raise ValueError(f"Unexpected swagger path shape: {rel}")

    return {
        "path": swagger_path,
        "service": rel.parts[0],
        "namespace": tuple(rel.parts[1:-2]),
        "version": rel.parts[-2],
        "filename": rel.parts[-1],
    }


def _select_latest_swagger_files_by_service(
    openapi_base: Path,
) -> tuple[dict[str, list[SwaggerFileMetadata]], int, int]:
    """Selects latest swagger per (service, namespace, filename) and groups by service."""
    all_swaggers = sorted(openapi_base.rglob("*.swagger.json"))
    latest_by_family: dict[tuple[str, tuple[str, ...], str], SwaggerFileMetadata] = {}

    for swagger_path in all_swaggers:
        metadata = _swagger_file_metadata(swagger_path, openapi_base)
        family_key = (
            metadata["service"],
            metadata["namespace"],
            metadata["filename"],
        )
        existing = latest_by_family.get(family_key)
        if existing is None or metadata["version"] > existing["version"]:
            latest_by_family[family_key] = metadata

    by_service: dict[str, list[SwaggerFileMetadata]] = {}
    for metadata in latest_by_family.values():
        service = metadata["service"]
        by_service.setdefault(service, []).append(metadata)

    for service in by_service:
        by_service[service].sort(
            key=lambda item: (
                item["namespace"],
                item["filename"],
                item["version"],
            )
        )

    selected_count = len(latest_by_family)
    ignored_count = len(all_swaggers) - selected_count
    return by_service, selected_count, ignored_count


def _validate_generated_service_parity(
    source_services: set[str], generated_root: Path
) -> None:
    """Fails generation if top-level generated service dirs drift from schema dirs."""
    generated_services = {
        p.name
        for p in generated_root.iterdir()
        if p.is_dir() and p.name != "__pycache__"
    }

    missing = sorted(source_services - generated_services)
    extra = sorted(generated_services - source_services)
    if not missing and not extra:
        return

    print("\n❌ Service directory parity check failed.")
    if missing:
        print("  Missing in generated output:", ", ".join(missing))
    if extra:
        print("  Extra generated directories:", ", ".join(extra))
    raise RuntimeError(
        "Generated service directories do not match source schema top-level directories."
    )


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
            _select_latest_swagger_files_by_service(openapi_base)
        )
        print(
            f"Discovered {selected_count} latest swagger files across "
            f"{len(selected_swagger_files)} services (ignored {ignored_count} older file versions)."
        )

        service_swagger_paths: dict[str, list[Path]] = {}
        service_endpoint_docs: dict[str, list[EndpointDoc]] = {}

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
                # later (generate_sphinx_stubs), once wrapper methods exist.
                try:
                    service_endpoint_docs.setdefault(service, []).extend(
                        extract_endpoint_docs(swagger_path)
                    )
                except Exception as e:
                    print(f"⚠️ Endpoint doc extraction failed for {service}: {e}")

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
                generate_service_error_package(service_dir, swagger_paths)

    _validate_generated_service_parity(source_services, SDK_OUTPUT_DIR)

    # -----------------------------------------------------------------
    # 3. POST-PROCESSING (Rest & Models Cleanup)
    # -----------------------------------------------------------------
    print("\nPatching generated code...")
    for service_dir in SDK_OUTPUT_DIR.iterdir():
        if not service_dir.is_dir() or service_dir.name == "__pycache__":
            continue

        # Discover models for explicit mapping
        model_classes = set()
        files_to_scan = (
            list((service_dir / "models").rglob("*.py"))
            if (service_dir / "models").exists()
            else []
        )
        if (service_dir / "models.py").exists():
            files_to_scan.append(service_dir / "models.py")

        for f in files_to_scan:
            model_classes.update(
                re.findall(r"^class ([a-zA-Z0-9_]+)[\(:]", f.read_text(), re.MULTILINE)
            )

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
                content = inject_service_error_handling(content)

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
    generate_service_wrappers()
    generate_client_mixin()
    generate_runtime_architecture_docs()
    render_diagrams()
    generate_service_readmes()
    generate_sphinx_stubs(service_endpoint_docs)

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
