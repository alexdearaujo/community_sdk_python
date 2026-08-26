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
