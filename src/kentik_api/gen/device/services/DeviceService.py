# AUTO-GENERATED: scripts/openapi_templates/service.jinja2 via openapi-python-generator
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Any, Dict, Optional

from kentik_api.core.api_config import APIConfig
from kentik_api.core.rest_runtime import (
    parse_response_model,
    path_segment,
    request_json,
)

from ..error import (
    CreateDeviceError,
    CreateDevicesError,
    DeleteDeviceError,
    DeleteDevicesError,
    GetDeviceByNameError,
    GetDeviceError,
    ListDevicesError,
    UpdateDeviceError,
    UpdateDeviceLabelsError,
    UpdateDevicesError,
)
from ..models import (  # noqa: F401
    CreateDeviceRequest,
    CreateDeviceResponse,
    CreateDevicesRequest,
    CreateDevicesResponse,
    CustomColumnData,
    DeleteDeviceResponse,
    DeleteDevicesRequest,
    DeleteDevicesResponse,
    DeviceConcise,
    DeviceDetailed,
    DeviceNmsConfig,
    DeviceNmsSnmpConfig,
    DeviceNmsStConfig,
    DeviceQuery,
    DeviceServiceUpdateDeviceBody,
    DeviceServiceUpdateDeviceLabelsBody,
    DeviceSnmpV3Conf,
    DeviceView,
    GetDeviceByNameResponse,
    GetDeviceResponse,
    GnmiV1Conf,
    Interface,
    LabelConcise,
    ListDevicesResponse,
    Plan,
    Site,
    UpdateDeviceLabelsResponse,
    UpdateDeviceResponse,
    UpdateDevicesRequest,
    UpdateDevicesResponse,
    devicev202504beta2Label,
    protobufAny,
    rpcStatus,
)


def ListDevices(
    api_config_override: Optional[APIConfig] = None,
    *,
    querynoCustomColumns: Optional[bool] = None,
    view: Optional[str] = None,
) -> ListDevicesResponse:
    query_params: Dict[str, Any] = {
        "query.noCustomColumns": querynoCustomColumns,
        "view": view,
    }

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path="/device/v202504beta2/device",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="ListDevices",
        error_cls=ListDevicesError,
    )

    return parse_response_model(
        ListDevicesResponse,
        body,
        operation_name="ListDevices",
        method="get",
        path="/device/v202504beta2/device",
    )


def CreateDevice(
    api_config_override: Optional[APIConfig] = None, *, data: CreateDeviceRequest
) -> CreateDeviceResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="post",
        path="/device/v202504beta2/device",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(by_alias=True),
        header_params=header_params,
        expected_status=200,
        operation_name="CreateDevice",
        error_cls=CreateDeviceError,
    )

    return parse_response_model(
        CreateDeviceResponse,
        body,
        operation_name="CreateDevice",
        method="post",
        path="/device/v202504beta2/device",
    )


def CreateDevices(
    api_config_override: Optional[APIConfig] = None, *, data: CreateDevicesRequest
) -> CreateDevicesResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="post",
        path="/device/v202504beta2/device/batch_create",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(by_alias=True),
        header_params=header_params,
        expected_status=200,
        operation_name="CreateDevices",
        error_cls=CreateDevicesError,
    )

    return parse_response_model(
        CreateDevicesResponse,
        body,
        operation_name="CreateDevices",
        method="post",
        path="/device/v202504beta2/device/batch_create",
    )


def DeleteDevices(
    api_config_override: Optional[APIConfig] = None, *, data: DeleteDevicesRequest
) -> DeleteDevicesResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="post",
        path="/device/v202504beta2/device/batch_delete",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(by_alias=True),
        header_params=header_params,
        expected_status=200,
        operation_name="DeleteDevices",
        error_cls=DeleteDevicesError,
    )

    return parse_response_model(
        DeleteDevicesResponse,
        body,
        operation_name="DeleteDevices",
        method="post",
        path="/device/v202504beta2/device/batch_delete",
    )


def UpdateDevices(
    api_config_override: Optional[APIConfig] = None, *, data: UpdateDevicesRequest
) -> UpdateDevicesResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="put",
        path="/device/v202504beta2/device/batch_update",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(by_alias=True),
        header_params=header_params,
        expected_status=200,
        operation_name="UpdateDevices",
        error_cls=UpdateDevicesError,
    )

    return parse_response_model(
        UpdateDevicesResponse,
        body,
        operation_name="UpdateDevices",
        method="put",
        path="/device/v202504beta2/device/batch_update",
    )


def GetDeviceByName(
    api_config_override: Optional[APIConfig] = None,
    *,
    deviceName: str,
    querynoCustomColumns: Optional[bool] = None,
) -> GetDeviceByNameResponse:
    query_params: Dict[str, Any] = {"query.noCustomColumns": querynoCustomColumns}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path=f"/device/v202504beta2/device/name/{path_segment(deviceName)}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="GetDeviceByName",
        error_cls=GetDeviceByNameError,
    )

    return parse_response_model(
        GetDeviceByNameResponse,
        body,
        operation_name="GetDeviceByName",
        method="get",
        path="/device/v202504beta2/device/name/{deviceName}",
    )


def GetDevice(
    api_config_override: Optional[APIConfig] = None,
    *,
    deviceid: str,
    querynoCustomColumns: Optional[bool] = None,
) -> GetDeviceResponse:
    query_params: Dict[str, Any] = {"query.noCustomColumns": querynoCustomColumns}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path=f"/device/v202504beta2/device/{path_segment(deviceid)}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="GetDevice",
        error_cls=GetDeviceError,
    )

    return parse_response_model(
        GetDeviceResponse,
        body,
        operation_name="GetDevice",
        method="get",
        path="/device/v202504beta2/device/{device.id}",
    )


def UpdateDevice(
    api_config_override: Optional[APIConfig] = None,
    *,
    deviceid: str,
    data: DeviceServiceUpdateDeviceBody,
) -> UpdateDeviceResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="put",
        path=f"/device/v202504beta2/device/{path_segment(deviceid)}",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(by_alias=True),
        header_params=header_params,
        expected_status=200,
        operation_name="UpdateDevice",
        error_cls=UpdateDeviceError,
    )

    return parse_response_model(
        UpdateDeviceResponse,
        body,
        operation_name="UpdateDevice",
        method="put",
        path="/device/v202504beta2/device/{device.id}",
    )


def DeleteDevice(
    api_config_override: Optional[APIConfig] = None, *, deviceid: str
) -> DeleteDeviceResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="delete",
        path=f"/device/v202504beta2/device/{path_segment(deviceid)}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="DeleteDevice",
        error_cls=DeleteDeviceError,
    )

    return parse_response_model(
        DeleteDeviceResponse,
        body,
        operation_name="DeleteDevice",
        method="delete",
        path="/device/v202504beta2/device/{device.id}",
    )


def UpdateDeviceLabels(
    api_config_override: Optional[APIConfig] = None,
    *,
    id: str,
    data: DeviceServiceUpdateDeviceLabelsBody,
) -> UpdateDeviceLabelsResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="put",
        path=f"/device/v202504beta2/device/{path_segment(id)}/labels",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(by_alias=True),
        header_params=header_params,
        expected_status=200,
        operation_name="UpdateDeviceLabels",
        error_cls=UpdateDeviceLabelsError,
    )

    return parse_response_model(
        UpdateDeviceLabelsResponse,
        body,
        operation_name="UpdateDeviceLabels",
        method="put",
        path="/device/v202504beta2/device/{id}/labels",
    )
