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
        path_template="/bgp_monitoring/v202210/monitors",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="ListMonitors",
        error_cls=ListMonitorsError,
    )

    return parse_response_model(
        ListMonitorsResponse,
        body,
        operation_name="ListMonitors",
        method="get",
        path="/bgp_monitoring/v202210/monitors",
    )


def CreateMonitor(
    api_config_override: Optional[APIConfig] = None, *, data: CreateMonitorRequest
) -> CreateMonitorResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="post",
        path="/bgp_monitoring/v202210/monitors",
        path_template="/bgp_monitoring/v202210/monitors",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(by_alias=True, exclude_unset=True),
        header_params=header_params,
        expected_status=200,
        operation_name="CreateMonitor",
        error_cls=CreateMonitorError,
    )

    return parse_response_model(
        CreateMonitorResponse,
        body,
        operation_name="CreateMonitor",
        method="post",
        path="/bgp_monitoring/v202210/monitors",
    )


def GetMonitor(
    api_config_override: Optional[APIConfig] = None, *, id: str
) -> GetMonitorResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path=f"/bgp_monitoring/v202210/monitors/{path_segment(id)}",
        path_template="/bgp_monitoring/v202210/monitors/{id}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="GetMonitor",
        error_cls=GetMonitorError,
    )

    return parse_response_model(
        GetMonitorResponse,
        body,
        operation_name="GetMonitor",
        method="get",
        path="/bgp_monitoring/v202210/monitors/{id}",
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
        path=f"/bgp_monitoring/v202210/monitors/{path_segment(id)}",
        path_template="/bgp_monitoring/v202210/monitors/{id}",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(by_alias=True, exclude_unset=True),
        header_params=header_params,
        expected_status=200,
        operation_name="UpdateMonitor",
        error_cls=UpdateMonitorError,
    )

    return parse_response_model(
        UpdateMonitorResponse,
        body,
        operation_name="UpdateMonitor",
        method="put",
        path="/bgp_monitoring/v202210/monitors/{id}",
    )


def DeleteMonitor(
    api_config_override: Optional[APIConfig] = None, *, id: str
) -> DeleteMonitorResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="delete",
        path=f"/bgp_monitoring/v202210/monitors/{path_segment(id)}",
        path_template="/bgp_monitoring/v202210/monitors/{id}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="DeleteMonitor",
        error_cls=DeleteMonitorError,
    )

    return parse_response_model(
        DeleteMonitorResponse,
        body,
        operation_name="DeleteMonitor",
        method="delete",
        path="/bgp_monitoring/v202210/monitors/{id}",
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
        path=f"/bgp_monitoring/v202210/monitors/{path_segment(id)}/status",
        path_template="/bgp_monitoring/v202210/monitors/{id}/status",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(by_alias=True, exclude_unset=True),
        header_params=header_params,
        expected_status=200,
        operation_name="SetMonitorStatus",
        error_cls=SetMonitorStatusError,
    )

    return parse_response_model(
        SetMonitorStatusResponse,
        body,
        operation_name="SetMonitorStatus",
        method="put",
        path="/bgp_monitoring/v202210/monitors/{id}/status",
    )
