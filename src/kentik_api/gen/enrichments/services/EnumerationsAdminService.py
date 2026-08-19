# AUTO-GENERATED: scripts/openapi_templates/service.jinja2 via openapi-python-generator
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Any, Dict, Optional

from kentik_api.core.api_config import APIConfig
from kentik_api.core.rest_runtime import request_json

from ..error import FetchValuesByIdsError
from ..models import (  # noqa: F401
    FetchValuesByIdsRequest,
    FetchValuesByIdsResponse,
    protobufAny,
    rpcStatus,
)


def FetchValuesByIds(
    api_config_override: Optional[APIConfig] = None, *, data: FetchValuesByIdsRequest
) -> FetchValuesByIdsResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="post",
        path="/enrichments/enumerations/v202601alpha1/values:fetch_by_ids",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(),
        header_params=header_params,
        expected_status=200,
        operation_name="FetchValuesByIds",
        error_cls=FetchValuesByIdsError,
    )

    return (
        FetchValuesByIdsResponse(**body)
        if body is not None
        else FetchValuesByIdsResponse.model_construct()
    )
