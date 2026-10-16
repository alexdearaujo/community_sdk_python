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
    GetCostProviderSummaryError,
    ListCostProvidersError,
    ListCostProviderSummariesError,
)
from ..models import (  # noqa: F401
    CostProviderConcise,
    CostProviderSummary,
    GetCostProviderSummaryResponse,
    ListCostProvidersResponse,
    ListCostProviderSummariesResponse,
    costv202308Status,
    googlerpcStatus,
    protobufAny,
)


def ListCostProviders(
    api_config_override: Optional[APIConfig] = None,
) -> ListCostProvidersResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path="/cost/v202308/cost/providers",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="ListCostProviders",
        error_cls=ListCostProvidersError,
    )

    return parse_response_model(
        ListCostProvidersResponse,
        body,
        operation_name="ListCostProviders",
        method="get",
        path="/cost/v202308/cost/providers",
    )


def ListCostProviderSummaries(
    api_config_override: Optional[APIConfig] = None, *, date: Optional[str] = None
) -> ListCostProviderSummariesResponse:
    query_params: Dict[str, Any] = {"date": date}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path="/cost/v202308/cost/summary",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="ListCostProviderSummaries",
        error_cls=ListCostProviderSummariesError,
    )

    return parse_response_model(
        ListCostProviderSummariesResponse,
        body,
        operation_name="ListCostProviderSummaries",
        method="get",
        path="/cost/v202308/cost/summary",
    )


def GetCostProviderSummary(
    api_config_override: Optional[APIConfig] = None,
    *,
    id: str,
    date: Optional[str] = None,
) -> GetCostProviderSummaryResponse:
    query_params: Dict[str, Any] = {"date": date}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path=f"/cost/v202308/cost/summary/{path_segment(id)}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="GetCostProviderSummary",
        error_cls=GetCostProviderSummaryError,
    )

    return parse_response_model(
        GetCostProviderSummaryResponse,
        body,
        operation_name="GetCostProviderSummary",
        method="get",
        path="/cost/v202308/cost/summary/{id}",
    )
