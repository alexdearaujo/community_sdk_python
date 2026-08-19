# HAND-WRITTEN: not modified by `make generate`. Edit directly.
from __future__ import annotations

import json
from pathlib import Path

from scripts.generation.error_package import (
    collect_operation_error_responses,
    generate_service_error_package,
    inject_service_error_handling,
    merge_operation_error_responses,
    service_error_class_name,
    service_error_response_class_name,
)


def test_service_error_class_name():
    assert service_error_class_name("ListDevices") == "ListDevicesError"


def test_service_error_response_class_name_known_status():
    assert (
        service_error_response_class_name("ListDevices", "404")
        == "ListDevicesNotFoundError"
    )


def test_service_error_response_class_name_unknown_status_falls_back_to_http_prefix():
    assert (
        service_error_response_class_name("ListDevices", "418")
        == "ListDevicesHttp418Error"
    )


def _write_swagger(tmp_path: Path, name: str, paths: dict) -> Path:
    swagger_path = tmp_path / name
    swagger_path.write_text(json.dumps({"paths": paths}), encoding="utf-8")
    return swagger_path


def test_collect_operation_error_responses_ignores_2xx(tmp_path: Path):
    swagger_path = _write_swagger(
        tmp_path,
        "device.swagger.json",
        {
            "/devices": {
                "get": {
                    "operationId": "ListDevices",
                    "responses": {
                        "200": {"description": "ok"},
                        "404": {"description": "not found"},
                    },
                }
            }
        },
    )

    errors = collect_operation_error_responses(swagger_path)

    assert set(errors) == {"ListDevices"}
    assert set(errors["ListDevices"]["responses"]) == {"404"}
    assert errors["ListDevices"]["method"] == "GET"


def test_collect_operation_error_responses_skips_operations_without_errors(
    tmp_path: Path,
):
    swagger_path = _write_swagger(
        tmp_path,
        "device.swagger.json",
        {"/devices": {"get": {"operationId": "ListDevices", "responses": {"200": {}}}}},
    )

    errors = collect_operation_error_responses(swagger_path)

    assert errors == {}


def test_merge_operation_error_responses_combines_responses_across_files():
    first = {
        "ListDevices": {
            "path": "/devices",
            "method": "GET",
            "responses": {"404": {"description": "not found", "schema_ref": None}},
        }
    }
    second = {
        "ListDevices": {
            "path": "/devices",
            "method": "GET",
            "responses": {"500": {"description": "boom", "schema_ref": None}},
        }
    }

    merged = merge_operation_error_responses([first, second])

    assert set(merged["ListDevices"]["responses"]) == {"404", "500"}


def test_generate_service_error_package_writes_operation_and_leaf_classes(
    tmp_path: Path,
):
    swagger_path = _write_swagger(
        tmp_path,
        "device.swagger.json",
        {
            "/devices": {
                "get": {
                    "operationId": "ListDevices",
                    "responses": {"404": {"description": "not found"}},
                }
            }
        },
    )
    service_dir = tmp_path / "device"
    service_dir.mkdir()

    generate_service_error_package(service_dir, [swagger_path])

    content = (service_dir / "error" / "__init__.py").read_text(encoding="utf-8")
    assert "class DeviceError(HTTPException):" in content
    assert "class ListDevicesError(DeviceError):" in content
    assert "class ListDevicesNotFoundError(DeviceError):" in content
    assert '"ListDevices": ListDevicesError,' in content


def test_inject_service_error_handling_adds_import_and_error_cls():
    content = (
        "from kentik_api.core.rest_runtime import request_json\n"
        "\n"
        "def ListDevices(api_config_override=None):\n"
        "    return request_json(\n"
        "        method='get',\n"
        "        path='/devices',\n"
        "        operation_name='ListDevices',\n"
        "        expected_status=200,\n"
        "    )\n"
    )

    result = inject_service_error_handling(content)

    assert "from ..error import ListDevicesError" in result
    assert "error_cls=ListDevicesError," in result


def test_inject_service_error_handling_is_noop_without_operation_name():
    content = "def NotAnOperation():\n    return 1\n"

    assert inject_service_error_handling(content) == content
