# HAND-WRITTEN: not modified by `make generate`. Edit directly.
"""Tests for scripts/generate_sdk.py top-level helpers.

All tests use tmp_path so no schema download or full generation run is needed
for the unit tests. The integration test (test_schema_request_body_coverage)
also skips gracefully when the local schema repo is absent.
"""

from __future__ import annotations

import ast
import json
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

# generate_sdk.py uses `from generation import ...` (script-style absolute
# import that requires scripts/ on sys.path). Add scripts/ so the import
# resolves the same way it does when the script runs directly.
_scripts_dir = Path(__file__).resolve().parents[2] / "scripts"
if str(_scripts_dir) not in sys.path:
    sys.path.insert(0, str(_scripts_dir))

from generate_sdk import (  # noqa: E402  # type: ignore[import-not-found]
    _fix_module_level_classvar,
    _pb_stem,
    _proto_collisions,
    _qualify_colliding_imports,
    _relink_pb2_dependency_imports,
    _rewrite_grpc_imports,
    _silence_grpc_experimental,
    check_model_names,
    clean_schema_names,
    fetch_schema,
    get_schema_root,
    hoist_inline_request_bodies,
    inline_request_body_refs,
    local_schema_commit,
    oneof_members_by_definition,
    openapi_generator_cmd,
    patched_swagger,
    read_schema_pin,
    relax_oneof_required,
    relax_response_message_required,
    restored_on_failure,
)
from google.protobuf import descriptor_pb2  # noqa: E402


def test_generator_runs_from_the_locked_environment_by_default(monkeypatch):
    monkeypatch.delenv("OPENAPI_GENERATOR_FROM", raising=False)
    monkeypatch.delenv("OPENAPI_GENERATOR_CMD", raising=False)

    cmd = openapi_generator_cmd(Path("in.json"), Path("out"))

    assert cmd[:4] == [sys.executable, "-m", "openapi_python_generator", "in.json"]


def test_a_fork_source_runs_through_uvx(monkeypatch):
    monkeypatch.setenv("OPENAPI_GENERATOR_FROM", "git+https://example.invalid/fork.git")
    monkeypatch.delenv("OPENAPI_GENERATOR_CMD", raising=False)

    cmd = openapi_generator_cmd(Path("in.json"), Path("out"))

    assert cmd[:5] == [
        "uvx",
        "--from",
        "git+https://example.invalid/fork.git",
        "openapi-python-generator",
        "in.json",
    ]


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


def test_grpc_directive_is_added_once():
    once = _silence_grpc_experimental("import grpc\n")

    assert once.startswith("# pyright: reportAttributeAccessIssue=false\n")
    assert _silence_grpc_experimental(once) == once


def test_module_level_classvar_becomes_int_and_class_body_keeps_it():
    stub = (
        "VISIBILITY_FIELD_NUMBER: _ClassVar[int]\n"
        "class Device(_message.Message):\n"
        "    ID_FIELD_NUMBER: _ClassVar[int]\n"
    )

    assert _fix_module_level_classvar(stub) == (
        "VISIBILITY_FIELD_NUMBER: int\n"
        "class Device(_message.Message):\n"
        "    ID_FIELD_NUMBER: _ClassVar[int]\n"
    )


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


def _schemas(*names: str, **definitions: dict) -> dict:
    return {
        "components": {"schemas": {name: definitions.get(name, {}) for name in names}}
    }


def test_models_differing_only_by_case_fail_across_files_of_a_service():
    seen: dict = {}
    check_model_names(_schemas("DeviceLabel", "Device"), seen, "a.json")

    with pytest.raises(
        RuntimeError, match="`deviceLabel` differs from model `DeviceLabel`"
    ):
        check_model_names(_schemas("deviceLabel"), seen, "b.json")


def test_same_model_with_the_same_definition_in_two_files_passes():
    seen: dict = {}
    status = {"type": "object", "properties": {"code": {"type": "integer"}}}
    check_model_names(_schemas("rpcStatus", "Device", rpcStatus=status), seen, "a.json")
    check_model_names(_schemas("rpcStatus", rpcStatus=dict(status)), seen, "b.json")


def test_same_model_with_a_different_definition_fails():
    seen: dict = {}
    check_model_names(
        _schemas("Mitigation", Mitigation={"properties": {"id": {}}}), seen, "a.json"
    )

    with pytest.raises(RuntimeError, match="defined differently in a.json"):
        check_model_names(
            _schemas("Mitigation", Mitigation={"properties": {"name": {}}}),
            seen,
            "b.json",
        )


def test_rewrite_grpc_imports_keeps_google_imports_absolute():
    line = (
        "from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2\n"
    )
    assert _rewrite_grpc_imports(line) == line


def _pb_module(root: Path, service: str, name: str, *imports: str) -> Path:
    path = root / service / "pb" / f"{name}.py"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(f"{line}\n" for line in imports), encoding="utf-8")
    return path


def test_relink_points_each_import_at_the_service_that_compiled_it(tmp_path: Path):
    owners = {
        ("kentik.user.v202405", "user_pb2"): "user",
        ("kentik.device.v202308", "device_pb2"): "device",
        ("kentik.device.v202308", "common_pb2"): "device",
    }
    _pb_module(tmp_path, "user", "user_pb2")
    module = _pb_module(
        tmp_path,
        "device",
        "device_pb2",
        "from kentik.user.v202405 import user_pb2 as _user",
        "from kentik.device.v202308 import common_pb2 as _common",
        "from google.api import annotations_pb2 as _ann",
    )

    _relink_pb2_dependency_imports(tmp_path, owners)

    assert module.read_text(encoding="utf-8").splitlines() == [
        "from kentik_api.gen.user.pb import user_pb2 as _user",
        "from . import common_pb2 as _common",
        "from google.api import annotations_pb2 as _ann",
    ]


def test_relink_fails_on_a_proto_version_nobody_compiled(tmp_path: Path):
    """Linking by module name alone would pick the user service's newer user_pb2."""
    owners = {("kentik.user.v202405", "user_pb2"): "user"}
    _pb_module(tmp_path, "user", "user_pb2")
    _pb_module(
        tmp_path,
        "device",
        "device_pb2",
        "from kentik.user.v202211 import user_pb2 as _user",
    )

    with pytest.raises(RuntimeError, match=r"kentik\.user\.v202211\.user_pb2"):
        _relink_pb2_dependency_imports(tmp_path, owners)


# ---------------------------------------------------------------------------
# generate_modular_sdk: schema validation must run before any output is wiped
# ---------------------------------------------------------------------------


def _function_by_name(source: str, name: str) -> ast.FunctionDef | None:
    return next(
        (
            node
            for node in ast.walk(ast.parse(source))
            if isinstance(node, ast.FunctionDef) and node.name == name
        ),
        None,
    )


@pytest.mark.parametrize(
    "check", ["validate_schema_files_or_raise", "validate_selected_services_or_raise"]
)
def test_generate_modular_sdk_validates_schema_before_cleaning_output_dir(check):
    """The corrupted-checkout gates must run before SDK_OUTPUT_DIR is touched.

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
        if call_repr.endswith(check):
            validate_lines.append(node.lineno)
        elif call_repr.endswith("rmtree"):
            rmtree_lines.append(node.lineno)

    assert validate_lines, f"{check}(...) call not found"
    assert rmtree_lines, "shutil.rmtree(...) call not found"
    assert max(validate_lines) < min(rmtree_lines), (
        f"{check}() must run before shutil.rmtree() "
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


# ---------------------------------------------------------------------------
# Schema pin: schema.lock names the commit the committed tree came from
# ---------------------------------------------------------------------------


def _git(repo: Path, *args: str) -> str:
    return subprocess.run(
        ["git", "-C", str(repo), *args], capture_output=True, text=True, check=True
    ).stdout.strip()


def _schema_repo(path: Path, commits: int = 1) -> list[str]:
    """A git repo with `commits` commits, oldest first."""
    path.mkdir()
    _git(path, "init", "-q")
    _git(path, "config", "user.email", "t@example.invalid")
    _git(path, "config", "user.name", "t")
    shas = []
    for n in range(commits):
        (path / "schema.json").write_text(str(n), encoding="utf-8")
        _git(path, "add", "schema.json")
        _git(path, "commit", "-q", "-m", str(n))
        shas.append(_git(path, "rev-parse", "HEAD"))
    return shas


def test_the_committed_pin_is_one_commit_sha():
    assert len(read_schema_pin()) == 40


@pytest.mark.parametrize("content", ["", "HEAD", "9de9a68", "x" * 40])
def test_a_malformed_pin_is_rejected(tmp_path, content):
    pin = tmp_path / "schema.lock"
    pin.write_text(content, encoding="utf-8")

    with pytest.raises(ValueError, match="40-character commit SHA"):
        read_schema_pin(pin)


def test_a_missing_pin_names_the_command_that_writes_it(tmp_path):
    with pytest.raises(ValueError, match="make sync-schema"):
        read_schema_pin(tmp_path / "schema.lock")


def test_fetch_checks_out_the_pinned_commit_not_the_tip(tmp_path):
    upstream = tmp_path / "upstream"
    first, _ = _schema_repo(upstream, commits=2)
    # GitHub serves any reachable commit; a local repo needs this to match it.
    _git(upstream, "config", "uploadpack.allowAnySHA1InWant", "true")

    commit = fetch_schema(str(upstream), first, tmp_path / "checkout")

    assert commit == first
    assert (tmp_path / "checkout" / "schema.json").read_text() == "0"


def test_fetch_rejects_a_ref_git_would_read_as_an_option(tmp_path):
    with pytest.raises(ValueError, match="must not start with"):
        fetch_schema("https://example.invalid/r.git", "--upload-pack=x", tmp_path)


def test_a_clean_local_checkout_reports_its_commit(tmp_path):
    repo = tmp_path / "schema"
    (sha,) = _schema_repo(repo)
    (repo / "uv.lock").write_text("untracked", encoding="utf-8")

    assert local_schema_commit(repo) == sha


def test_a_modified_local_checkout_reports_no_commit(tmp_path):
    repo = tmp_path / "schema"
    _schema_repo(repo)
    (repo / "schema.json").write_text("edited", encoding="utf-8")

    assert local_schema_commit(repo) is None


def test_a_local_folder_outside_git_reports_no_commit(tmp_path):
    assert local_schema_commit(tmp_path) is None


def test_a_ref_with_a_local_schema_is_rejected(tmp_path):
    with pytest.raises(ValueError, match="remote repository only"):
        with get_schema_root(str(tmp_path), "HEAD"):
            pass


# ---------------------------------------------------------------------------
# restored_on_failure: a failed run leaves the previous output in place
# ---------------------------------------------------------------------------


def _outputs(tmp_path: Path) -> tuple[Path, Path, Path]:
    gen = tmp_path / "gen"
    (gen / "device").mkdir(parents=True)
    (gen / "device" / "wrapper.py").write_text("old", encoding="utf-8")
    mixin = tmp_path / "client_mixin.py"
    mixin.write_text("old", encoding="utf-8")
    return gen, mixin, tmp_path / "schema.lock"


def _half_build(gen: Path, mixin: Path, pin: Path) -> None:
    shutil.rmtree(gen)
    (gen / "user").mkdir(parents=True)
    mixin.write_text("new", encoding="utf-8")
    pin.write_text("new", encoding="utf-8")


@pytest.mark.parametrize("error", [RuntimeError, KeyboardInterrupt])
def test_a_failed_run_restores_every_output(tmp_path, error):
    gen, mixin, pin = _outputs(tmp_path)

    with pytest.raises(error):
        with restored_on_failure((gen, mixin, pin)):
            _half_build(gen, mixin, pin)
            raise error

    assert sorted(p.name for p in gen.iterdir()) == ["device"]
    assert (gen / "device" / "wrapper.py").read_text() == "old"
    assert mixin.read_text() == "old"
    assert not pin.exists()


def test_a_completed_run_keeps_the_new_output(tmp_path):
    gen, mixin, pin = _outputs(tmp_path)

    with restored_on_failure((gen, mixin, pin)):
        _half_build(gen, mixin, pin)

    assert sorted(p.name for p in gen.iterdir()) == ["user"]
    assert mixin.read_text() == "new"
    assert pin.read_text() == "new"
