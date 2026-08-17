from typing import Any, Dict, Optional

from kentik_api.core.api_config import APIConfig
from kentik_api.core.rest_runtime import request_json

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

    return (
        ListCostProvidersResponse(**body)
        if body is not None
        else ListCostProvidersResponse.model_construct()
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

    return (
        ListCostProviderSummariesResponse(**body)
        if body is not None
        else ListCostProviderSummariesResponse.model_construct()
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
        path=f"/cost/v202308/cost/summary/{id}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="GetCostProviderSummary",
        error_cls=GetCostProviderSummaryError,
    )

    return (
        GetCostProviderSummaryResponse(**body)
        if body is not None
        else GetCostProviderSummaryResponse.model_construct()
    )
