"""Service-local error class generation and runtime error-dispatch injection."""

import json
import re
from pathlib import Path
from typing import TypedDict

from ._shared import discover_service_model_classes, service_to_pascal_case


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
