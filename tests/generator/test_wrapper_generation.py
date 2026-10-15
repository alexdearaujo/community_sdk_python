# HAND-WRITTEN: not modified by `make generate`. Edit directly.
from __future__ import annotations

from pathlib import Path

import pytest

from scripts.generation import wrapper_generation
from scripts.generation._shared import RestOperation
from scripts.generation.parity import select_latest_swagger_files_by_service
from scripts.generation.wrapper_generation import (
    _drop_service_word,
    _to_snake_case,
    _wrapper_method_names,
    qualify_wrapper_annotation_types,
)


@pytest.mark.parametrize(
    ("pascal_name", "expected_snake_name"),
    [
        ("ListDevices", "list_devices"),
        ("ListASGroups", "list_as_groups"),
        ("CreateASGroup", "create_as_group"),
        ("GetASNInsights", "get_asn_insights"),
        ("GetASNDetails", "get_asn_details"),
        ("ASGroup", "as_group"),
    ],
)
def test_to_snake_case_keeps_acronyms_as_one_word(pascal_name, expected_snake_name):
    assert _to_snake_case(pascal_name) == expected_snake_name


def _op(name: str, path: str) -> RestOperation:
    return RestOperation(name, "get", path, 200, "Err", name, (), 0, "None", ())


def _names(
    ops_by_file: dict[str, list[RestOperation]], service: str = "demo"
) -> dict[str, str]:
    files = {Path(f"{stem}.py"): ops for stem, ops in ops_by_file.items()}
    return {
        f"{path.stem}.{op}": name
        for (path, op), name in _wrapper_method_names(service, files).items()
    }


def test_shared_operation_names_are_prefixed_in_every_module():
    # B11: the first module in file order used to keep the bare `list`, so a new
    # module that sorts earlier would silently take it over.
    names = _names(
        {
            "AlertAutoAckService": [_op("List", "/auto-acks")],
            "AlertService": [_op("List", "/alerts"), _op("Ack", "/alerts/{id}")],
        },
        service="alerting",
    )
    assert names == {
        "AlertAutoAckService.List": "auto_ack_list",
        "AlertService.List": "alert_list",
        "AlertService.Ack": "ack",
    }


def test_a_new_module_does_not_change_existing_prefixed_names():
    before = _names({"BService": [_op("List", "/b")], "CService": [_op("List", "/c")]})
    after = _names(
        {
            "AService": [_op("List", "/a")],
            "BService": [_op("List", "/b")],
            "CService": [_op("List", "/c")],
        }
    )
    assert before.items() <= after.items()


def test_second_http_route_is_named_by_its_extra_path_parameters():
    names = _names(
        {
            "AuditService": [
                _op("GetAuditEvent", "/events/{id}"),
                _op("GetAuditEvent_2", "/events/{id}/{ctime}"),
            ]
        },
        service="audit",
    )
    assert names == {
        "AuditService.GetAuditEvent": "get_event",
        "AuditService.GetAuditEvent_2": "get_event_by_ctime",
    }


@pytest.mark.parametrize(
    ("service", "name", "expected"),
    [
        ("audit", "list_audit_events", "list_events"),
        ("alerting", "alert_silence_notifications_get", "silence_notifications_get"),
        ("site", "update_site_market", "update_market"),
        ("custom_dimension", "get_custom_dimension_info", "get_info"),
        # The Service word is the object of the call: keep it.
        ("device", "get_device", "get_device"),
        # Dropping it would leave one word.
        ("alerting", "alert_list", "alert_list"),
        ("interface", "interface_get", "interface_get"),
        # A route suffix is never shortened.
        ("device", "get_device_by_device_name", "get_device_by_device_name"),
    ],
)
def test_drop_service_word(service, name, expected):
    assert _drop_service_word(service, name) == expected


def test_routes_that_cannot_be_told_apart_fail_generation():
    with pytest.raises(ValueError, match="same number of path parameters"):
        _names({"XService": [_op("Get", "/a/{id}"), _op("Get_2", "/b/{id}")]})


def test_keyword_operation_names_get_a_trailing_underscore():
    names = _names({"XService": [_op("Import", "/import"), _op("Return", "/return")]})
    assert names == {"XService.Import": "import_", "XService.Return": "return_"}


def test_qualify_wrapper_annotation_types_qualifies_known_model_names():
    result = qualify_wrapper_annotation_types(
        "data: CreateDeviceRequest", {"CreateDeviceRequest"}
    )
    assert result == "data: rest_models.CreateDeviceRequest"


def test_qualify_wrapper_annotation_types_ignores_unrelated_text():
    result = qualify_wrapper_annotation_types("data: str", {"CreateDeviceRequest"})
    assert result == "data: str"


def test_qualify_wrapper_annotation_types_does_not_double_qualify():
    result = qualify_wrapper_annotation_types(
        "rest_models.CreateDeviceRequest", {"CreateDeviceRequest"}
    )
    assert result == "rest_models.CreateDeviceRequest"


def test_qualify_wrapper_annotation_types_returns_text_unchanged_without_model_classes():
    assert qualify_wrapper_annotation_types("data: str", set()) == "data: str"


def test_generate_writes_wrapper_and_mounts_it_in_client_mixin(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
):
    sdk_output_dir = tmp_path / "gen"
    project_root = tmp_path
    monkeypatch.setattr(wrapper_generation, "SDK_OUTPUT_DIR", sdk_output_dir)
    monkeypatch.setattr(wrapper_generation, "PROJECT_ROOT", project_root)

    services_dir = sdk_output_dir / "device" / "services"
    services_dir.mkdir(parents=True)
    (services_dir / "DeviceService.py").write_text(
        "from typing import Optional\n"
        "from kentik_api.core.api_config import APIConfig\n"
        "from kentik_api.core.rest_runtime import request_json\n"
        "from ..error import ListDevicesError\n\n"
        "def ListDevices(api_config_override=None) -> str:\n"
        "    return request_json(\n"
        "        method='get', path='/device/v1/device',\n"
        "        expected_status=200, operation_name='ListDevices',\n"
        "        error_cls=ListDevicesError,\n"
        "    )\n",
        encoding="utf-8",
    )
    (project_root / "src" / "kentik_api").mkdir(parents=True)

    wrapper_generation.generate()

    wrapper_content = (services_dir / "device.py").read_text(encoding="utf-8")
    assert "class DeviceServiceWrapper:" in wrapper_content
    assert "def list_devices(self," in wrapper_content
    assert "RestDeviceModule1.ListDevices(" in wrapper_content

    mixin_content = (project_root / "src" / "kentik_api" / "client_mixin.py").read_text(
        encoding="utf-8"
    )
    assert "DeviceServiceWrapper" in mixin_content
    assert "self.device = DeviceServiceWrapper(self._transport)" in mixin_content


def test_wrapper_method_keeps_the_rest_function_docstring_exactly(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
):
    monkeypatch.setattr(wrapper_generation, "SDK_OUTPUT_DIR", tmp_path / "gen")
    monkeypatch.setattr(wrapper_generation, "PROJECT_ROOT", tmp_path)
    services_dir = tmp_path / "gen" / "device" / "services"
    services_dir.mkdir(parents=True)
    (tmp_path / "src" / "kentik_api").mkdir(parents=True)
    # Escaped and indented as the REST template writes it.
    doc = '    List "all" devices.\n\n' + r"    Matches \\d+ and \"\"\" quotes."
    (services_dir / "DeviceService.py").write_text(
        "from kentik_api.core.rest_runtime import request_json\n\n"
        "def ListDevices(api_config_override=None) -> str:\n"
        f'    """\n{doc}\n    """\n'
        "    return request_json(method='get', path='/device/v1/device',\n"
        "        expected_status=200, operation_name='ListDevices', error_cls=E)\n",
        encoding="utf-8",
    )

    wrapper_generation.generate()

    tree = ast.parse((services_dir / "device.py").read_text(encoding="utf-8"))
    method = next(
        n
        for n in ast.walk(tree)
        if isinstance(n, ast.FunctionDef) and n.name == "list_devices"
    )
    assert (
        ast.get_docstring(method)
        == 'List "all" devices.\n\nMatches \\d+ and """ quotes.'
    )


def test_rpc_taking_and_returning_empty_gets_a_working_grpc_branch(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
):
    from google.api import annotations_pb2
    from google.protobuf import descriptor_pb2

    from scripts.generation._shared import grpc_call, grpc_stub_services

    monkeypatch.setattr(wrapper_generation, "SDK_OUTPUT_DIR", tmp_path / "gen")
    monkeypatch.setattr(wrapper_generation, "PROJECT_ROOT", tmp_path)
    (tmp_path / "src" / "kentik_api").mkdir(parents=True)
    services_dir = tmp_path / "gen" / "ping" / "services"
    services_dir.mkdir(parents=True)
    (services_dir / "PingService.py").write_text(
        "from typing import Any, Dict\n"
        "from kentik_api.core.rest_runtime import request_json\n\n"
        "def Ping(api_config_override=None, *, data: Dict[str, Any]) -> Dict[str, Any]:\n"
        "    return request_json(method='post', path='/ping/v1/ping',\n"
        "        expected_status=200, operation_name='Ping', error_cls=PingError)\n",
        encoding="utf-8",
    )
    fd = descriptor_pb2.FileDescriptorProto(name="kentik/ping/v1/ping.proto")
    fd.package = "kentik.ping.v1"
    method = fd.service.add(name="PingService").method.add(
        name="Ping",
        input_type=".google.protobuf.Empty",
        output_type=".google.protobuf.Empty",
    )
    rule = method.options.Extensions[annotations_pb2.http]  # pyright: ignore[reportArgumentType]  # ty: ignore[invalid-argument-type]
    rule.post, rule.body = "/ping/v1/ping", "*"
    pb_dir = tmp_path / "gen" / "ping" / "pb"
    pb_dir.mkdir()
    (pb_dir / "ping_pb2.py").write_text(
        f"DESCRIPTOR = _pool.AddSerializedFile({fd.SerializeToString()!r})\n"
    )
    (pb_dir / "ping_pb2_grpc.py").write_text("")

    wrapper_generation.generate()

    source = (services_dir / "ping.py").read_text(encoding="utf-8")
    tree = ast.parse(source)
    assert "from google.protobuf import empty_pb2" in source
    assert "return grpc_response_body(_resp)" in source
    init, ping = (
        next(
            n
            for n in ast.walk(tree)
            if isinstance(n, ast.FunctionDef) and n.name == name
        )
        for name in ("__init__", "ping")
    )
    call = grpc_call(ping, grpc_stub_services(init))
    assert call is not None
    assert (call.rpc, call.request) == ("PingService/Ping", "Empty")


@pytest.mark.parametrize(
    ("versions", "expected"),
    [
        (["v202504beta2", "v202504"], "v202504"),
        (["v202501beta9", "v202501beta10"], "v202501beta10"),
        (["v202501alpha9", "v202501alpha10"], "v202501alpha10"),
        (["v20260515beta1", "v202605"], "v202605"),
        (["v202509", "v202605alpha1"], "v202605alpha1"),
    ],
)
def test_version_selection_uses_release_order_not_plain_string_order(
    tmp_path: Path, versions: list[str], expected: str
):
    for version in versions:
        swagger_dir = tmp_path / "svc" / version
        swagger_dir.mkdir(parents=True, exist_ok=True)
        (swagger_dir / "svc.swagger.json").write_text("{}", encoding="utf-8")

    by_service, selected_count, _ = select_latest_swagger_files_by_service(tmp_path)

    assert selected_count == 1
    assert by_service["svc"][0]["version"] == expected


# --- end to end, against a sandbox copy of the committed tree -----------------

import ast  # noqa: E402
import subprocess  # noqa: E402
import sys  # noqa: E402

# generate_sdk.py imports `generation` script-style, so scripts/ must be on sys.path.
_SCRIPTS_DIR = Path(__file__).resolve().parents[2] / "scripts"
if str(_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR))

from generate_sdk import (  # noqa: E402
    _inject_generated_headers,  # type: ignore[import-not-found]
)

REAL_GEN = Path(__file__).resolve().parents[2] / "src" / "kentik_api" / "gen"


def _post_process_like_generate_sdk(sandbox) -> None:
    """The same ruff pass and header injection generate_modular_sdk() applies."""
    for cmd in (
        ["ruff", "check", "--select", "F,I", "--fix", str(sandbox.gen)],
        ["ruff", "format", "--quiet", str(sandbox.gen)],
    ):
        result = subprocess.run(
            [sys.executable, "-m", *cmd],
            cwd=sandbox.root,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0, result.stdout + result.stderr
    _inject_generated_headers(sandbox.gen)


@pytest.mark.parametrize("service", ["device", "alerting"])
def test_regenerated_wrapper_matches_the_committed_one_byte_for_byte(sandbox, service):
    sandbox.wrapper_file(service).unlink()

    wrapper_generation.generate()
    _post_process_like_generate_sdk(sandbox)

    committed = (REAL_GEN / service / "services" / f"{service}.py").read_text()
    assert sandbox.wrapper_file(service).read_text() == committed


def test_wrapper_generation_is_deterministic_across_repeated_runs(sandbox):
    wrapper_generation.generate()

    first = {
        "device": sandbox.wrapper_file("device").read_text(),
        "alerting": sandbox.wrapper_file("alerting").read_text(),
        "mixin": (sandbox.package / "client_mixin.py").read_text(),
    }

    wrapper_generation.generate()

    assert sandbox.wrapper_file("device").read_text() == first["device"]
    assert sandbox.wrapper_file("alerting").read_text() == first["alerting"]
    assert (sandbox.package / "client_mixin.py").read_text() == first["mixin"]


def test_service_without_rest_paths_gets_no_wrapper(sandbox):
    wrapper_generation.generate()

    assert not sandbox.wrapper_file("core").exists()


def test_mixin_mounts_exactly_the_services_that_have_a_wrapper(sandbox):
    wrapper_generation.generate()

    mixin = (sandbox.package / "client_mixin.py").read_text()
    ast.parse(mixin)
    assert "self.device = DeviceServiceWrapper(self._transport)" in mixin
    assert "self.alerting = AlertingServiceWrapper(self._transport)" in mixin
    assert (
        "from kentik_api.gen.device.services.device import DeviceServiceWrapper"
        in mixin
    )
    assert "core" not in {
        line.split("self.")[1].split(" ")[0]
        for line in mixin.splitlines()
        if "= " in line and "self." in line
    }


def test_wrapper_for_a_service_without_proto_stubs_is_rest_only(sandbox):
    import shutil

    shutil.rmtree(sandbox.gen / "device" / "pb")
    sandbox.wrapper_file("device").unlink()

    wrapper_generation.generate()

    wrapper = sandbox.wrapper_file("device").read_text()
    ast.parse(wrapper)
    assert "call_grpc" not in wrapper
    assert "gRPC translation for" in wrapper
    assert "RestDeviceModule1.ListDevices(" in wrapper


def test_discover_grpc_methods_keys_each_rpc_by_service_and_http_rule():
    stubs, methods = wrapper_generation._discover_grpc_methods(REAL_GEN / "device")

    assert any(stub_class == "DeviceServiceStub" for _, _, stub_class, _ in stubs)
    get = methods[("DeviceService", "get", "/device/v202504beta2/device/{}")]
    assert (get.name, get.request_class, get.path_fields, get.body) == (
        "GetDevice",
        "GetDeviceRequest",
        ("id",),
        "",
    )
    update = methods[("DeviceService", "put", "/device/v202504beta2/device/{}")]
    assert (update.path_fields, update.body) == (("device.id",), "*")


def test_discover_grpc_methods_without_pb_dir_is_empty(tmp_path):
    assert wrapper_generation._discover_grpc_methods(tmp_path) == ([], {})


def test_discover_grpc_methods_skips_unparseable_files(tmp_path):
    (tmp_path / "pb").mkdir()
    (tmp_path / "pb" / "broken_pb2.py").write_text("def (:\n")

    assert wrapper_generation._discover_grpc_methods(tmp_path) == ([], {})


def _grpc_calls_by_rest_module(wrapper_file: Path) -> dict[str, list[str | None]]:
    """Maps each REST module a wrapper calls to the stub class its gRPC branch uses."""
    tree = ast.parse(wrapper_file.read_text())
    module_of_alias = {
        alias.asname: alias.name.rsplit(".", 1)[1]
        for node in tree.body
        if isinstance(node, ast.Import)
        for alias in node.names
        if alias.asname
    }
    init = next(
        n
        for n in ast.walk(tree)
        if isinstance(n, ast.FunctionDef) and n.name == "__init__"
    )
    stub_class_of_attr = {
        stmt.targets[0].attr: stmt.value.func.attr
        for stmt in ast.walk(init)
        if isinstance(stmt, ast.Assign)
        and isinstance(stmt.targets[0], ast.Attribute)
        and stmt.targets[0].attr.startswith("_grpc_stub_")
        and isinstance(stmt.value, ast.Call)
        and isinstance(stmt.value.func, ast.Attribute)
    }

    calls: dict[str, list[str | None]] = {}
    for method in ast.walk(tree):
        if not isinstance(method, ast.FunctionDef) or method.name == "__init__":
            continue
        attrs = [n for n in ast.walk(method) if isinstance(n, ast.Attribute)]
        rest_module = next(
            module_of_alias[a.value.id]
            for a in attrs
            if isinstance(a.value, ast.Name) and a.value.id in module_of_alias
        )
        stub = next(
            (
                stub_class_of_attr[a.value.attr]
                for a in attrs
                if isinstance(a.value, ast.Attribute)
                and a.value.attr in stub_class_of_attr
            ),
            None,
        )
        calls.setdefault(rest_module, []).append(stub)
    return calls


def test_each_grpc_call_uses_the_stub_of_its_own_rest_service(sandbox):
    # alerting's services all declare generic RPC names such as Delete. Keyed by
    # name alone, every Delete went to whichever stub was discovered last.
    sandbox.wrapper_file("alerting").unlink()

    wrapper_generation.generate()

    calls = _grpc_calls_by_rest_module(sandbox.wrapper_file("alerting"))
    assert len(calls) > 2
    for rest_module, stubs in calls.items():
        assert stubs == [f"{rest_module}Stub"] * len(stubs), rest_module


def test_grpc_request_maps_arguments_to_the_rpc_request_fields(sandbox):
    sandbox.wrapper_file("device").unlink()

    wrapper_generation.generate()

    wrapper = sandbox.wrapper_file("device").read_text()
    # The REST path says {device.id}, but GetDeviceRequest's field is `id`.
    assert '{"id": deviceid, "query.noCustomColumns": querynoCustomColumns}' in wrapper
    assert '{"device.id": deviceid}' in wrapper
