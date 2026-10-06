# HAND-WRITTEN: not modified by `make generate`. Edit directly.
from __future__ import annotations

from pathlib import Path

import pytest

from scripts.generation import wrapper_generation
from scripts.generation.wrapper_generation import (
    _to_snake_case,
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


# --- end to end, against a sandbox copy of the committed tree -----------------

import ast  # noqa: E402
import subprocess  # noqa: E402
import sys  # noqa: E402

# generate_sdk.py imports `generation` script-style, so scripts/ must be on sys.path.
_SCRIPTS_DIR = Path(__file__).resolve().parents[2] / "scripts"
if str(_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR))

from generate_sdk import _inject_generated_headers  # noqa: E402  # type: ignore[import-not-found]

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
        if rest_module == "MitigationsService":
            # No proto declares this service, so it has no gRPC translation.
            assert stubs == [None] * len(stubs)
        else:
            assert stubs == [f"{rest_module}Stub"] * len(stubs), rest_module


def test_grpc_request_maps_arguments_to_the_rpc_request_fields(sandbox):
    sandbox.wrapper_file("device").unlink()

    wrapper_generation.generate()

    wrapper = sandbox.wrapper_file("device").read_text()
    # The REST path says {device.id}, but GetDeviceRequest's field is `id`.
    assert '{"id": deviceid, "query.noCustomColumns": querynoCustomColumns}' in wrapper
    assert '{"device.id": deviceid}' in wrapper
