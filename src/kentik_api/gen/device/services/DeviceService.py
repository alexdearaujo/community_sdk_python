from typing import Any, Dict, Optional

from kentik_api.core.api_config import APIConfig
from kentik_api.core.rest_runtime import request_json

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

    return (
        ListDevicesResponse(**body)
        if body is not None
        else ListDevicesResponse.model_construct()
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
        json_body=data.model_dump(),
        header_params=header_params,
        expected_status=200,
        operation_name="CreateDevice",
        error_cls=CreateDeviceError,
    )

    return (
        CreateDeviceResponse(**body)
        if body is not None
        else CreateDeviceResponse.model_construct()
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
        json_body=data.model_dump(),
        header_params=header_params,
        expected_status=200,
        operation_name="CreateDevices",
        error_cls=CreateDevicesError,
    )

    return (
        CreateDevicesResponse(**body)
        if body is not None
        else CreateDevicesResponse.model_construct()
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
        json_body=data.model_dump(),
        header_params=header_params,
        expected_status=200,
        operation_name="DeleteDevices",
        error_cls=DeleteDevicesError,
    )

    return (
        DeleteDevicesResponse(**body)
        if body is not None
        else DeleteDevicesResponse.model_construct()
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
        json_body=data.model_dump(),
        header_params=header_params,
        expected_status=200,
        operation_name="UpdateDevices",
        error_cls=UpdateDevicesError,
    )

    return (
        UpdateDevicesResponse(**body)
        if body is not None
        else UpdateDevicesResponse.model_construct()
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
        path=f"/device/v202504beta2/device/name/{deviceName}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="GetDeviceByName",
        error_cls=GetDeviceByNameError,
    )

    return (
        GetDeviceByNameResponse(**body)
        if body is not None
        else GetDeviceByNameResponse.model_construct()
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
        path=f"/device/v202504beta2/device/{deviceid}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="GetDevice",
        error_cls=GetDeviceError,
    )

    return (
        GetDeviceResponse(**body)
        if body is not None
        else GetDeviceResponse.model_construct()
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
        path=f"/device/v202504beta2/device/{deviceid}",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(),
        header_params=header_params,
        expected_status=200,
        operation_name="UpdateDevice",
        error_cls=UpdateDeviceError,
    )

    return (
        UpdateDeviceResponse(**body)
        if body is not None
        else UpdateDeviceResponse.model_construct()
    )


def DeleteDevice(
    api_config_override: Optional[APIConfig] = None, *, deviceid: str
) -> DeleteDeviceResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="delete",
        path=f"/device/v202504beta2/device/{deviceid}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="DeleteDevice",
        error_cls=DeleteDeviceError,
    )

    return (
        DeleteDeviceResponse(**body)
        if body is not None
        else DeleteDeviceResponse.model_construct()
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
        path=f"/device/v202504beta2/device/{id}/labels",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(),
        header_params=header_params,
        expected_status=200,
        operation_name="UpdateDeviceLabels",
        error_cls=UpdateDeviceLabelsError,
    )

    return (
        UpdateDeviceLabelsResponse(**body)
        if body is not None
        else UpdateDeviceLabelsResponse.model_construct()
    )
