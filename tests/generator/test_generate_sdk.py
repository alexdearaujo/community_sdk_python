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
    _pb_stem,
    _proto_collisions,
    _qualify_colliding_imports,
    _rewrite_grpc_imports,
    clean_schema_names,
    hoist_inline_request_bodies,
    inline_request_body_refs,
    oneof_members_by_definition,
    patched_swagger,
    relax_oneof_required,
    relax_response_message_required,
)
from google.protobuf import descriptor_pb2  # noqa: E402

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
# patched_swagger: requestBody $ref inlining
#
# These drive patched_swagger rather than any in-place helper: it is the path
# `make generate` runs, so a break there fails these tests.
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
    original = json.dumps(_MINIMAL_SCHEMA_WITH_REF_BODY)
    swagger_path.write_text(original)

    with patched_swagger(swagger_path, version="v202411alpha1") as patched_path:
        result = json.loads(Path(patched_path).read_text())

    post_rb = result["paths"]["/things"]["post"]["requestBody"]
    put_rb = result["paths"]["/things/{id}"]["put"]["requestBody"]

    assert "$ref" not in post_rb, "POST requestBody $ref should be inlined"
    assert "content" in post_rb
    assert "application/json" in post_rb["content"]

    assert "$ref" not in put_rb, "PUT requestBody $ref should be inlined"
    assert "content" in put_rb

    assert swagger_path.read_text() == original, (
        "patched_swagger must not modify the schema checkout"
    )


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
    original = json.dumps(schema)
    swagger_path.write_text(original)

    with patched_swagger(swagger_path, version="v202411alpha1") as patched_path:
        result = json.loads(Path(patched_path).read_text())

    rb = result["paths"]["/things"]["post"]["requestBody"]
    assert "content" in rb
    assert "$ref" not in rb
    assert swagger_path.read_text() == original


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
    original = json.dumps(schema)
    swagger_path.write_text(original)

    with patched_swagger(swagger_path, version="v202411alpha1") as patched_path:
        result = json.loads(Path(patched_path).read_text())

    assert "requestBody" not in result["paths"]["/things/{id}"]["get"]
    assert "requestBody" not in result["paths"]["/things/{id}"]["delete"]
    assert swagger_path.read_text() == original


# ---------------------------------------------------------------------------
# Schema-to-generated-code parity: every requestBody in the schema must
# produce a `data:` parameter in the generated REST function.
# Skipped when the local api-schema-public sibling repo is absent.
# ---------------------------------------------------------------------------

_SCHEMA_ROOT = Path(__file__).resolve().parents[3] / "api-schema-public"
_GEN_ROOT = Path(__file__).resolve().parents[2] / "src" / "kentik_api" / "gen"


def _resolve_request_body(schema: dict, request_body: dict) -> Optional[dict]:
    """Dereferences a requestBody $ref from components.requestBodies, if present."""
    if "$ref" not in request_body:
        return request_body
    rb_name = request_body["$ref"].rsplit("/", 1)[-1]
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


def _inline_body_schema() -> dict:
    return {
        "paths": {
            "/capabilities/{capability.name}": {
                "patch": {
                    "operationId": "CapabilityAdminService_UpdateCapability",
                    "tags": ["CapabilityAdminService"],
                    "requestBody": {
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "object",
                                    "title": "capability",
                                    "properties": {"displayName": {"type": "string"}},
                                    "required": ["capability"],
                                }
                            }
                        }
                    },
                }
            }
        },
        "components": {"schemas": {}},
    }


def test_inline_request_body_is_hoisted_to_a_named_schema():
    # R16: an inline object body became Dict[str, Any] in the generated wrapper.
    schema = hoist_inline_request_bodies(_inline_body_schema())

    name = "CapabilityAdminServiceUpdateCapabilityBody"
    media = schema["paths"]["/capabilities/{capability.name}"]["patch"]["requestBody"]
    assert media["content"]["application/json"]["schema"] == {
        "$ref": f"#/components/schemas/{name}"
    }
    # `capability` wraps the body on the wire and is not one of its properties.
    assert schema["components"]["schemas"][name] == {
        "type": "object",
        "properties": {"displayName": {"type": "string"}},
    }


def test_hoisting_refuses_to_overwrite_an_existing_schema():
    schema = _inline_body_schema()
    schema["components"]["schemas"]["CapabilityAdminServiceUpdateCapabilityBody"] = {}

    with pytest.raises(ValueError, match="exists"):
        hoist_inline_request_bodies(schema)


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


# ---------------------------------------------------------------------------
# oneof members: protoc-gen-openapiv2 marks every REQUIRED oneof member as
# required, so the generated model rejects every valid message (B3).
# ---------------------------------------------------------------------------


def _descriptor_set() -> descriptor_pb2.FileDescriptorSet:
    message = descriptor_pb2.DescriptorProto(name="ExternalContext")
    message.oneof_decl.add(name="context")
    message.oneof_decl.add(name="_note")
    message.field.add(name="servicenow", json_name="servicenow", oneof_index=0)
    message.field.add(name="jira_cloud", json_name="jiraCloud", oneof_index=0)
    message.field.add(name="id", json_name="id")
    message.field.add(
        name="note", json_name="note", oneof_index=1, proto3_optional=True
    )
    nested = message.nested_type.add(name="Inner")
    nested.oneof_decl.add(name="kind")
    nested.field.add(name="a", json_name="a", oneof_index=0)
    file = descriptor_pb2.FileDescriptorProto(package="kentik.alerting.v202505")
    file.message_type.append(message)
    return descriptor_pb2.FileDescriptorSet(file=[file])


def test_oneof_members_by_definition_uses_swagger_names_and_skips_optional():
    assert oneof_members_by_definition(_descriptor_set()) == {
        "v202505ExternalContext": {"servicenow", "jiraCloud"},
        "v202505ExternalContextInner": {"a"},
    }


def test_patched_swagger_drops_oneof_members_from_required(tmp_path: Path):
    schema = {
        "components": {
            "schemas": {
                "v202505ExternalContext": {
                    "type": "object",
                    "required": ["servicenow", "jiraCloud", "id"],
                },
                "v202505ExternalContextInner": {"required": ["a"]},
            }
        }
    }
    swagger_path = tmp_path / "alert.swagger.json"
    swagger_path.write_text(json.dumps(schema), encoding="utf-8")
    members = oneof_members_by_definition(_descriptor_set())

    with patched_swagger(swagger_path, "v202505", members) as patched_path:
        schemas = json.loads(patched_path.read_text())["components"]["schemas"]

    assert schemas["ExternalContext"]["required"] == ["id"]
    assert "required" not in schemas["ExternalContextInner"]


def test_relax_oneof_required_does_not_mutate_input():
    schema = {"definitions": {"v1Thing": {"required": ["a", "b"]}}}
    result = relax_oneof_required(schema, {"v1Thing": {"a"}})
    assert result["definitions"]["v1Thing"]["required"] == ["b"]
    assert schema["definitions"]["v1Thing"]["required"] == ["a", "b"]


# ---------------------------------------------------------------------------
# Response models: proto REQUIRED binds requests only, and an unset message
# field is absent from a response, so FlowPolicySettings.baseline failed (R15).
# ---------------------------------------------------------------------------


def _policy_schema() -> dict:
    ref = "#/components/schemas/"
    return {
        "paths": {
            "/policies/{id}": {
                "get": {
                    "responses": {
                        "200": {
                            "content": {
                                "application/json": {
                                    "schema": {"$ref": f"{ref}GetPolicyResponse"}
                                }
                            }
                        }
                    }
                }
            },
            "/policies": {
                "post": {
                    "requestBody": {
                        "content": {
                            "application/json": {
                                "schema": {"$ref": f"{ref}CreatePolicyRequest"}
                            }
                        }
                    },
                    "responses": {},
                }
            },
        },
        "components": {
            "schemas": {
                "GetPolicyResponse": {
                    "properties": {"policy": {"$ref": f"{ref}Settings"}},
                    "required": ["policy"],
                },
                "Settings": {
                    "properties": {
                        "baseline": {"$ref": f"{ref}Baseline"},
                        "mode": {"$ref": f"{ref}Mode"},
                        "name": {"type": "string"},
                        "rules": {"type": "array", "items": {"$ref": f"{ref}Baseline"}},
                    },
                    "required": ["baseline", "mode", "name", "rules"],
                },
                "Baseline": {"properties": {"x": {"type": "string"}}},
                "Mode": {"type": "string", "enum": ["A", "B"]},
                "CreatePolicyRequest": {
                    "properties": {"settings": {"$ref": f"{ref}Baseline"}},
                    "required": ["settings"],
                },
            }
        },
    }


def test_response_models_drop_message_fields_from_required():
    schemas = relax_response_message_required(_policy_schema())["components"]["schemas"]
    assert "required" not in schemas["GetPolicyResponse"]
    # Enums, scalars and repeated fields always reach the response, so they stay.
    assert schemas["Settings"]["required"] == ["mode", "name", "rules"]


def test_request_only_models_keep_required_message_fields():
    original = _policy_schema()
    # A requestBodies entry's `required` is a bool, not a field list.
    original["components"]["requestBodies"] = {"Body": {"required": True}}
    schemas = relax_response_message_required(original)["components"]["schemas"]
    assert schemas["CreatePolicyRequest"]["required"] == ["settings"]
    assert original["components"]["schemas"]["Settings"]["required"] == [
        "baseline",
        "mode",
        "name",
        "rules",
    ]


# ---------------------------------------------------------------------------
# Proto file-name collisions: every folder of a Service compiles into one flat
# pb/ directory, so two `mitigation.proto` files overwrote each other (B4).
# ---------------------------------------------------------------------------


def test_proto_collisions_finds_stems_shared_across_compiled_folders(tmp_path):
    openapi_base, proto_base = tmp_path / "openapi", tmp_path / "proto"
    selected = {"alerting": [], "device": []}
    for service, folder, protos in [
        ("alerting", "alerting/public/v202505", ["mitigation", "alert"]),
        ("alerting", "alerting/types/v202506", ["mitigation", "sorting"]),
        ("device", "device/v202308beta1", ["device"]),
    ]:
        for proto in protos:
            path = proto_base / "kentik" / folder / f"{proto}.proto"
            path.parent.mkdir(parents=True, exist_ok=True)
            path.touch()
        selected[service].append({"path": str(openapi_base / folder / "x.json")})

    assert _proto_collisions(selected, openapi_base, proto_base) == {
        "alerting": {"mitigation"},
        "device": set(),
    }


def test_pb_stem_qualifies_only_colliding_kentik_modules():
    collisions = {"alerting": {"mitigation"}}
    assert (
        _pb_stem("kentik.alerting.types.v202506", "mitigation", collisions)
        == "mitigation_types_v202506"
    )
    assert _pb_stem("kentik.alerting.public.v202505", "alert", collisions) == "alert"
    assert _pb_stem("kentik.ktbgp.v202501", "mitigation", collisions) == "mitigation"


def test_qualify_colliding_imports_resolves_by_package_not_name():
    content = (
        "from kentik.alerting.types.v202506 import mitigation_pb2 as _types\n"
        "from kentik.alerting.public.v202505 import mitigation_pb2 as _public\n"
        "from kentik.alerting.public.v202505 import common_pb2 as _common\n"
    )
    result = _qualify_colliding_imports(content, {"alerting": {"mitigation"}})
    assert result == (
        "from kentik.alerting.types.v202506 import mitigation_types_v202506_pb2 as _types\n"
        "from kentik.alerting.public.v202505 import mitigation_public_v202505_pb2 as _public\n"
        "from kentik.alerting.public.v202505 import common_pb2 as _common\n"
    )
    assert "import mitigation_public_v202505_pb2 as _public" in _rewrite_grpc_imports(
        result
    )


# ---------------------------------------------------------------------------
# generate_modular_sdk: schema validation must run before any output is wiped
# ---------------------------------------------------------------------------


def test_generate_modular_sdk_validates_schema_before_cleaning_output_dir():
    """The corrupted-checkout gate must run before SDK_OUTPUT_DIR is touched.

    Regression test: an earlier version of this gate ran *after* the
    "Cleaning old modules" step, so a validation failure still left
    src/kentik_api/gen/ wiped out -- discovered by manually reproducing the
    2026-08-26 incident end-to-end rather than trusting fixture tests alone.
    Runs as a static/AST check (not a full generation) since
    generate_modular_sdk() shells out to git/protoc/uvx and isn't otherwise
    unit-tested in isolation.
    """
    source = (_scripts_dir / "generate_sdk.py").read_text(encoding="utf-8")
    func_node = _function_by_name(source, "generate_modular_sdk")
    assert func_node is not None, "generate_modular_sdk() not found"

    validate_lines: list[int] = []
    rmtree_lines: list[int] = []
    for node in ast.walk(func_node):
        if not isinstance(node, ast.Call):
            continue
        call_repr = ast.unparse(node.func)
        if call_repr.endswith("validate_schema_files_or_raise"):
            validate_lines.append(node.lineno)
        elif call_repr.endswith("rmtree"):
            rmtree_lines.append(node.lineno)

    assert validate_lines, "validate_schema_files_or_raise(...) call not found"
    assert rmtree_lines, "shutil.rmtree(...) call not found"
    assert max(validate_lines) < min(rmtree_lines), (
        "validate_schema_files_or_raise() must run before shutil.rmtree() "
        "cleans SDK_OUTPUT_DIR, so a validation failure never leaves "
        "generated output partially wiped"
    )


def test_clean_schema_names_keeps_the_prefix_when_stripping_would_overwrite_a_schema():
    schema = {
        "definitions": {
            "AlertAcknowledgement": {
                "type": "object",
                "properties": {"state": {"type": "string"}},
            },
            "v202505AlertAcknowledgement": {"type": "string", "enum": ["A", "B"]},
            "v202505Alert": {
                "type": "object",
                "properties": {
                    "acknowledgement": {"$ref": "#/definitions/AlertAcknowledgement"},
                    "legacy": {"$ref": "#/definitions/v202505AlertAcknowledgement"},
                },
            },
        }
    }

    result = clean_schema_names(schema, "v202505")["definitions"]

    assert result["AlertAcknowledgement"]["type"] == "object"
    assert result["v202505AlertAcknowledgement"]["enum"] == ["A", "B"]
    assert "Alert" in result
    props = result["Alert"]["properties"]
    assert props["acknowledgement"]["$ref"].endswith("/AlertAcknowledgement")
    assert props["legacy"]["$ref"].endswith("/v202505AlertAcknowledgement")


def test_the_real_alert_schema_keeps_acknowledgement_an_object():
    import json

    swagger = (
        Path(__file__).resolve().parents[3]
        / "api-schema-public"
        / "gen"
        / "openapiv3"
        / "kentik"
        / "alerting"
        / "public"
        / "v202505"
        / "alert.swagger.json"
    )
    if not swagger.exists():
        pytest.skip("local api-schema-public checkout not available")

    result = clean_schema_names(
        json.loads(swagger.read_text(encoding="utf-8")), "v202505"
    )
    definitions = result["components"]["schemas"]

    assert definitions["AlertAcknowledgement"].get("type") == "object"
    assert "v202505AlertAcknowledgement" in definitions
