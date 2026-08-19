# AUTO-GENERATED: scripts/openapi_templates/service.jinja2 via openapi-python-generator
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Any, Dict, Optional

from kentik_api.core.api_config import APIConfig
from kentik_api.core.rest_runtime import request_json

from ..error import CreateConnectivityReportError
from ..models import (  # noqa: F401
    CloudProvider,
    CreateConnectivityReportRequest,
    CreateConnectivityReportResponse,
    EntityType,
    protobufAny,
    rpcStatus,
)


def CreateConnectivityReport(
    api_config_override: Optional[APIConfig] = None,
    *,
    data: CreateConnectivityReportRequest,
) -> CreateConnectivityReportResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="post",
        path="/connectivity_checker/v202410beta1/create",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(),
        header_params=header_params,
        expected_status=200,
        operation_name="CreateConnectivityReport",
        error_cls=CreateConnectivityReportError,
    )

    return (
        CreateConnectivityReportResponse(**body)
        if body is not None
        else CreateConnectivityReportResponse.model_construct()
    )
