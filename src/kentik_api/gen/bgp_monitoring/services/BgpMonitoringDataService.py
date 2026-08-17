from typing import Any, Dict, Optional

from kentik_api.core.api_config import APIConfig
from kentik_api.core.rest_runtime import request_json

from ..error import GetMetricsForTargetError, GetRoutesForTargetError
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


def GetMetricsForTarget(
    api_config_override: Optional[APIConfig] = None, *, data: GetMetricsForTargetRequest
) -> GetMetricsForTargetResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="post",
        path="/bgp_monitoring/v202210/metrics",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(),
        header_params=header_params,
        expected_status=200,
        operation_name="GetMetricsForTarget",
        error_cls=GetMetricsForTargetError,
    )

    return (
        GetMetricsForTargetResponse(**body)
        if body is not None
        else GetMetricsForTargetResponse.model_construct()
    )


def GetRoutesForTarget(
    api_config_override: Optional[APIConfig] = None, *, data: GetRoutesForTargetRequest
) -> GetRoutesForTargetResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="post",
        path="/bgp_monitoring/v202210/routes",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(),
        header_params=header_params,
        expected_status=200,
        operation_name="GetRoutesForTarget",
        error_cls=GetRoutesForTargetError,
    )

    return (
        GetRoutesForTargetResponse(**body)
        if body is not None
        else GetRoutesForTargetResponse.model_construct()
    )
