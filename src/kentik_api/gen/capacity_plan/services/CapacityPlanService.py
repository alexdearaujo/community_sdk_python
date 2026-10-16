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
    GetCapacityPlanError,
    GetCapacitySummaryError,
    ListCapacityPlansError,
    ListCapacitySummariesError,
)
from ..models import (  # noqa: F401
    CapacityPlan,
    CapacityPlanInterfaceDetail,
    CapacitySummary,
    CapacitySummaryInterfacesDetail,
    Config,
    ConfigRunoutConfig,
    ConfigUtilConfig,
    GetCapacityPlanResponse,
    GetCapacitySummaryResponse,
    InterfacesDetailStatusDetail,
    ListCapacityPlansResponse,
    ListCapacitySummariesResponse,
    SummaryStatus,
    SummaryStatusRunoutStatus,
    SummaryStatusUtilStatus,
    protobufAny,
    rpcStatus,
)


def ListCapacityPlans(
    api_config_override: Optional[APIConfig] = None,
) -> ListCapacityPlansResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path="/capacity_plan/v202212/capacity_plan",
        path_template="/capacity_plan/v202212/capacity_plan",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="ListCapacityPlans",
        error_cls=ListCapacityPlansError,
    )

    return parse_response_model(
        ListCapacityPlansResponse,
        body,
        operation_name="ListCapacityPlans",
        method="get",
        path="/capacity_plan/v202212/capacity_plan",
    )


def ListCapacitySummaries(
    api_config_override: Optional[APIConfig] = None,
) -> ListCapacitySummariesResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path="/capacity_plan/v202212/capacity_plan/summary",
        path_template="/capacity_plan/v202212/capacity_plan/summary",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="ListCapacitySummaries",
        error_cls=ListCapacitySummariesError,
    )

    return parse_response_model(
        ListCapacitySummariesResponse,
        body,
        operation_name="ListCapacitySummaries",
        method="get",
        path="/capacity_plan/v202212/capacity_plan/summary",
    )


def GetCapacityPlan(
    api_config_override: Optional[APIConfig] = None, *, id: str
) -> GetCapacityPlanResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path=f"/capacity_plan/v202212/capacity_plan/{path_segment(id)}",
        path_template="/capacity_plan/v202212/capacity_plan/{id}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="GetCapacityPlan",
        error_cls=GetCapacityPlanError,
    )

    return parse_response_model(
        GetCapacityPlanResponse,
        body,
        operation_name="GetCapacityPlan",
        method="get",
        path="/capacity_plan/v202212/capacity_plan/{id}",
    )


def GetCapacitySummary(
    api_config_override: Optional[APIConfig] = None, *, id: str
) -> GetCapacitySummaryResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path=f"/capacity_plan/v202212/capacity_plan/{path_segment(id)}/summary",
        path_template="/capacity_plan/v202212/capacity_plan/{id}/summary",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="GetCapacitySummary",
        error_cls=GetCapacitySummaryError,
    )

    return parse_response_model(
        GetCapacitySummaryResponse,
        body,
        operation_name="GetCapacitySummary",
        method="get",
        path="/capacity_plan/v202212/capacity_plan/{id}/summary",
    )
