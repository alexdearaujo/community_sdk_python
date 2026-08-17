from typing import Any, Dict, Optional

from kentik_api.core.api_config import APIConfig
from kentik_api.core.rest_runtime import request_json

from ..error import CreatePathfinderReportError
from ..models import (  # noqa: F401
    CloudProvider,
    CreatePathfinderReportRequest,
    CreatePathfinderReportResponse,
    EntityType,
    PathElement,
    protobufAny,
    rpcStatus,
)


def CreatePathfinderReport(
    api_config_override: Optional[APIConfig] = None,
    *,
    data: CreatePathfinderReportRequest,
) -> CreatePathfinderReportResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="post",
        path="/pathfinder/v202505beta1/create",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(),
        header_params=header_params,
        expected_status=200,
        operation_name="CreatePathfinderReport",
        error_cls=CreatePathfinderReportError,
    )

    return (
        CreatePathfinderReportResponse(**body)
        if body is not None
        else CreatePathfinderReportResponse.model_construct()
    )
