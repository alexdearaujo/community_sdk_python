# AUTO-GENERATED: scripts/openapi_templates/service.jinja2 via openapi-python-generator
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Any, Dict, Optional

from kentik_api.core.api_config import APIConfig
from kentik_api.core.rest_runtime import request_json

from ..error import (
    CreateMonitorError,
    DeleteMonitorError,
    GetMonitorError,
    ListMonitorsError,
    SetMonitorStatusError,
    UpdateMonitorError,
)
from ..models import (  # noqa: F401
    BgpHealthSettings,
    BgpMetric,
    BgpMetricType,
    BgpMonitor,
    BgpMonitoringAdminServiceSetMonitorStatusBody,
    BgpMonitoringAdminServiceUpdateMonitorBody,
    BgpMonitorSettings,
    BgpMonitorStatus,
    CreateMonitorRequest,
    CreateMonitorResponse,
    DeleteMonitorResponse,
    GetMetricsForTargetRequest,
    GetMetricsForTargetResponse,
    GetMonitorResponse,
    GetRoutesForTargetRequest,
    GetRoutesForTargetResponse,
    ListMonitorsResponse,
    Nlri,
    RouteInfo,
    SetMonitorStatusResponse,
    UpdateMonitorResponse,
    protobufAny,
    rpcStatus,
    v202303Afi,
    v202303RpkiStatus,
    v202303Safi,
    v202303UserInfo,
    v202303VantagePoint,
)


def ListMonitors(
    api_config_override: Optional[APIConfig] = None,
) -> ListMonitorsResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path="/bgp_monitoring/v202210/monitors",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="ListMonitors",
        error_cls=ListMonitorsError,
    )

    return (
        ListMonitorsResponse(**body)
        if body is not None
        else ListMonitorsResponse.model_construct()
    )


def CreateMonitor(
    api_config_override: Optional[APIConfig] = None, *, data: CreateMonitorRequest
) -> CreateMonitorResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="post",
        path="/bgp_monitoring/v202210/monitors",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(),
        header_params=header_params,
        expected_status=200,
        operation_name="CreateMonitor",
        error_cls=CreateMonitorError,
    )

    return (
        CreateMonitorResponse(**body)
        if body is not None
        else CreateMonitorResponse.model_construct()
    )


def GetMonitor(
    api_config_override: Optional[APIConfig] = None, *, id: str
) -> GetMonitorResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path=f"/bgp_monitoring/v202210/monitors/{id}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="GetMonitor",
        error_cls=GetMonitorError,
    )

    return (
        GetMonitorResponse(**body)
        if body is not None
        else GetMonitorResponse.model_construct()
    )


def UpdateMonitor(
    api_config_override: Optional[APIConfig] = None,
    *,
    id: str,
    data: BgpMonitoringAdminServiceUpdateMonitorBody,
) -> UpdateMonitorResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="put",
        path=f"/bgp_monitoring/v202210/monitors/{id}",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(),
        header_params=header_params,
        expected_status=200,
        operation_name="UpdateMonitor",
        error_cls=UpdateMonitorError,
    )

    return (
        UpdateMonitorResponse(**body)
        if body is not None
        else UpdateMonitorResponse.model_construct()
    )


def DeleteMonitor(
    api_config_override: Optional[APIConfig] = None, *, id: str
) -> DeleteMonitorResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="delete",
        path=f"/bgp_monitoring/v202210/monitors/{id}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="DeleteMonitor",
        error_cls=DeleteMonitorError,
    )

    return (
        DeleteMonitorResponse(**body)
        if body is not None
        else DeleteMonitorResponse.model_construct()
    )


def SetMonitorStatus(
    api_config_override: Optional[APIConfig] = None,
    *,
    id: str,
    data: BgpMonitoringAdminServiceSetMonitorStatusBody,
) -> SetMonitorStatusResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="put",
        path=f"/bgp_monitoring/v202210/monitors/{id}/status",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(),
        header_params=header_params,
        expected_status=200,
        operation_name="SetMonitorStatus",
        error_cls=SetMonitorStatusError,
    )

    return (
        SetMonitorStatusResponse(**body)
        if body is not None
        else SetMonitorStatusResponse.model_construct()
    )
