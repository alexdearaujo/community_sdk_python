# HAND-WRITTEN: not modified by `make generate`. Edit directly.
"""Tests for scripts/generate_sdk.py top-level helpers.

All tests use tmp_path so no schema download or full generation run is needed
for the unit tests. The integration test (test_schema_request_body_coverage)
also skips gracefully when the local schema repo is absent.
"""

from __future__ import annotations

import ast
import json
import sys
from pathlib import Path
from typing import Optional

import pytest

# generate_sdk.py uses `from generation import ...` (script-style absolute
# import that requires scripts/ on sys.path). Add scripts/ so the import
# resolves the same way it does when the script runs directly.
_scripts_dir = Path(__file__).resolve().parents[2] / "scripts"
if str(_scripts_dir) not in sys.path:
    sys.path.insert(0, str(_scripts_dir))

from generate_sdk import (  # noqa: E402  # type: ignore[import-not-found]
    _rewrite_grpc_imports,
    clean_schema_names,
    inline_request_body_refs,
    patch_schema_for_clean_names,
    patched_swagger,
)

# ---------------------------------------------------------------------------
# _rewrite_grpc_imports: three protoc output styles
# ---------------------------------------------------------------------------


def test_rewrite_bare_import():
    result = _rewrite_grpc_imports("import device_pb2\n")
    assert result == "from . import device_pb2\n"


def test_rewrite_parenthesised_from_import():
    result = _rewrite_grpc_imports(
        "from kentik.device.v202308 import (\n    device_pb2 as _device,\n)\n"
    )
    assert "from . import device_pb2 as _device" in result


def test_rewrite_unparenthesised_from_import():
    result = _rewrite_grpc_imports(
        "from kentik.device.v202308 import device_pb2 as _device\n"
    )
    assert result == "from . import device_pb2 as _device\n"


def test_rewrite_leaves_non_pb2_imports_unchanged():
    content = "from kentik_api.core.api_config import APIConfig\n"
    assert _rewrite_grpc_imports(content) == content


# ---------------------------------------------------------------------------
# patch_schema_for_clean_names: requestBody $ref inlining
# ---------------------------------------------------------------------------

_MINIMAL_SCHEMA_WITH_REF_BODY = {
    "paths": {
        "/things": {
            "post": {
                "operationId": "CreateThing",
                "requestBody": {"$ref": "#/components/requestBodies/Thing"},
                "responses": {"200": {}},
            }
        },
        "/things/{id}": {
            "put": {
                "operationId": "UpdateThing",
                "requestBody": {"$ref": "#/components/requestBodies/Thing"},
                "responses": {"200": {}},
            },
            "get": {
                "operationId": "GetThing",
                "responses": {"200": {}},
            },
        },
    },
    "components": {
        "requestBodies": {
            "Thing": {
                "content": {
                    "application/json": {
                        "schema": {"$ref": "#/components/schemas/Thing"}
                    }
                },
                "required": True,
            }
        },
        "schemas": {
            "Thing": {
                "type": "object",
                "properties": {"name": {"type": "string"}},
            }
        },
    },
}


def test_patch_schema_inlines_request_body_ref(tmp_path: Path):
    swagger_path = tmp_path / "things.swagger.json"
    swagger_path.write_text(json.dumps(_MINIMAL_SCHEMA_WITH_REF_BODY))

    patch_schema_for_clean_names(swagger_path, version="v202411alpha1")

    result = json.loads(swagger_path.read_text())
    post_rb = result["paths"]["/things"]["post"]["requestBody"]
    put_rb = result["paths"]["/things/{id}"]["put"]["requestBody"]

    assert "$ref" not in post_rb, "POST requestBody $ref should be inlined"
    assert "content" in post_rb
    assert "application/json" in post_rb["content"]

    assert "$ref" not in put_rb, "PUT requestBody $ref should be inlined"
    assert "content" in put_rb


def test_patch_schema_leaves_inline_request_body_unchanged(tmp_path: Path):
    inline_rb = {
        "content": {
            "application/json": {"schema": {"$ref": "#/components/schemas/Thing"}}
        },
        "required": True,
    }
    schema = {
        "paths": {
            "/things": {
                "post": {
                    "operationId": "CreateThing",
                    "requestBody": inline_rb,
                    "responses": {"200": {}},
                }
            }
        },
        "components": {"schemas": {"Thing": {"type": "object"}}},
    }
    swagger_path = tmp_path / "things.swagger.json"
    swagger_path.write_text(json.dumps(schema))

    patch_schema_for_clean_names(swagger_path, version="v202411alpha1")

    result = json.loads(swagger_path.read_text())
    rb = result["paths"]["/things"]["post"]["requestBody"]
    assert "content" in rb
    assert "$ref" not in rb


def test_patch_schema_leaves_operations_without_request_body_unchanged(tmp_path: Path):
    schema = {
        "paths": {
            "/things/{id}": {
                "get": {"operationId": "GetThing", "responses": {"200": {}}},
                "delete": {
                    "operationId": "DeleteThing",
                    "responses": {"200": {}},
                },
            }
        },
        "components": {},
    }
    swagger_path = tmp_path / "things.swagger.json"
    swagger_path.write_text(json.dumps(schema))

    patch_schema_for_clean_names(swagger_path, version="v202411alpha1")

    result = json.loads(swagger_path.read_text())
    assert "requestBody" not in result["paths"]["/things/{id}"]["get"]
    assert "requestBody" not in result["paths"]["/things/{id}"]["delete"]


# ---------------------------------------------------------------------------
# Schema-to-generated-code parity: every requestBody in the schema must
# produce a `data:` parameter in the generated REST function.
# Skipped when the local api-schema-public sibling repo is absent.
# ---------------------------------------------------------------------------

_SCHEMA_ROOT = Path(__file__).resolve().parents[3] / "api-schema-public"
_GEN_ROOT = Path(__file__).resolve().parents[2] / "src" / "kentik_api" / "gen"


def _resolve_request_body(schema: dict, rb: dict) -> Optional[dict]:
    """Dereferences a requestBody $ref from components.requestBodies, if present."""
    if "$ref" not in rb:
        return rb
    rb_name = rb["$ref"].rsplit("/", 1)[-1]
    return schema.get("components", {}).get("requestBodies", {}).get(rb_name)


def _has_data_param(func_node: ast.FunctionDef) -> bool:
    for arg in func_node.args.kwonlyargs:
        if arg.arg == "data":
            return True
    for arg in func_node.args.args:
        if arg.arg == "data":
            return True
    return False


def _function_by_name(source: str, name: str) -> Optional[ast.FunctionDef]:
    tree = ast.parse(source)
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == name:
            return node
    return None


def _collect_write_ops_with_body(swagger_files: list[Path]) -> list[tuple[str, str]]:
    """Returns (operationId, swagger_file_stem) pairs for ops with a requestBody."""
    ops = []
    for path in swagger_files:
        schema = json.loads(path.read_text())
        for _path_item in schema.get("paths", {}).values():
            for _, op in _path_item.items():
                if not isinstance(op, dict):
                    continue
                rb = op.get("requestBody")
                if rb is None:
                    continue
                resolved = _resolve_request_body(schema, rb)
                if resolved is None:
                    continue
                content = resolved.get("content", {})
                if not content.get("application/json"):
                    continue
                op_id = op.get("operationId")
                if op_id:
                    ops.append((op_id, path.stem))
    return ops


@pytest.mark.skipif(
    not _SCHEMA_ROOT.exists(),
    reason="Local api-schema-public repo not found; run `make generate local` first.",
)
def test_schema_request_body_coverage():
    """Every operation whose schema declares a requestBody must have data: in the
    generated REST function. This catches the class of generator bug where
    requestBody entries are silently dropped, leaving write operations with no
    body parameter.
    """
    openapi_base = _SCHEMA_ROOT / "gen" / "openapiv3" / "kentik"
    assert openapi_base.exists(), f"Schema openapiv3 path not found: {openapi_base}"

    failures: list[str] = []

    for service_dir in sorted(_GEN_ROOT.iterdir()):
        if not service_dir.is_dir() or service_dir.name.startswith("_"):
            continue

        service = service_dir.name
        schema_service_dir = openapi_base / service
        if not schema_service_dir.exists():
            continue

        swagger_files = list(schema_service_dir.rglob("*.swagger.json"))
        if not swagger_files:
            continue

        ops_with_body = _collect_write_ops_with_body(swagger_files)
        if not ops_with_body:
            continue

        services_dir = service_dir / "services"
        if not services_dir.exists():
            services_dir = service_dir / "service"
        if not services_dir.exists():
            continue

        all_service_sources: list[tuple[Path, str]] = [
            (p, p.read_text())
            for p in sorted(services_dir.glob("*.py"))
            if p.name != "__init__.py" and p.stem.endswith("Service")
        ]

        for op_id, swagger_stem in ops_with_body:
            found = False
            for gen_path, source in all_service_sources:
                func_node = _function_by_name(source, op_id)
                if func_node is None:
                    continue
                found = True
                if not _has_data_param(func_node):
                    failures.append(
                        f"{service}/{gen_path.name}::{op_id} "
                        f"(from {swagger_stem}): schema declares requestBody "
                        f"but generated function has no `data:` parameter"
                    )
                break

            if not found:
                # operationId may have been renamed by deduplication; not a failure
                pass

    if failures:
        pytest.fail(
            f"{len(failures)} operation(s) missing body parameter:\n"
            + "\n".join(f"  {f}" for f in failures)
        )


# ---------------------------------------------------------------------------
# clean_schema_names and inline_request_body_refs: pure in-memory transforms
# ---------------------------------------------------------------------------


def test_clean_schema_names_strips_version_prefix_from_definitions():
    schema = {
        "definitions": {
            "v202404beta1Thing": {"type": "object"},
        }
    }
    result = clean_schema_names(schema, "v202404beta1")
    assert "Thing" in result["definitions"]
    assert "v202404beta1Thing" not in result["definitions"]


def test_clean_schema_names_rewrites_refs():
    schema = {
        "paths": {
            "/thing": {
                "get": {
                    "responses": {
                        "200": {"schema": {"$ref": "#/definitions/v202404beta1Thing"}}
                    }
                }
            }
        },
        "definitions": {},
    }
    result = clean_schema_names(schema, "v202404beta1")
    ref = result["paths"]["/thing"]["get"]["responses"]["200"]["schema"]["$ref"]
    assert "v202404beta1" not in ref


def test_clean_schema_names_does_not_mutate_input():
    schema = {"definitions": {"v202404beta1Thing": {"type": "object"}}}
    original_keys = set(schema["definitions"].keys())
    clean_schema_names(schema, "v202404beta1")
    assert set(schema["definitions"].keys()) == original_keys


def test_inline_request_body_refs_resolves_ref():
    schema = {
        "paths": {
            "/things": {
                "post": {"requestBody": {"$ref": "#/components/requestBodies/Thing"}}
            }
        },
        "components": {
            "requestBodies": {
                "Thing": {"content": {"application/json": {}}, "required": True}
            }
        },
    }
    result = inline_request_body_refs(schema)
    rb = result["paths"]["/things"]["post"]["requestBody"]
    assert "content" in rb
    assert "$ref" not in rb


def test_inline_request_body_refs_does_not_mutate_input():
    schema = {
        "paths": {
            "/things": {
                "post": {"requestBody": {"$ref": "#/components/requestBodies/Thing"}}
            }
        },
        "components": {"requestBodies": {"Thing": {"content": {}}}},
    }
    post = schema["paths"]["/things"]["post"]
    inline_request_body_refs(schema)
    assert "$ref" in post["requestBody"]


def test_patched_swagger_does_not_modify_original(tmp_path: Path):
    schema = {
        "paths": {},
        "components": {"schemas": {"v202404beta1Thing": {"type": "object"}}},
    }
    swagger_path = tmp_path / "things.swagger.json"
    swagger_path.write_text(json.dumps(schema), encoding="utf-8")
    original_text = swagger_path.read_text()

    with patched_swagger(swagger_path, "v202404beta1") as tmp_path_arg:
        # The temp file should contain the patched schema
        patched = json.loads(Path(tmp_path_arg).read_text())
        assert "Thing" in patched["components"]["schemas"]

    # The original file must be unchanged
    assert swagger_path.read_text() == original_text
    # The temp file must be cleaned up
    assert not tmp_path_arg.exists()
