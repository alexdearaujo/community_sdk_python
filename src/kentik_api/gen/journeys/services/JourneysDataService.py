from typing import Any, Dict, Optional

from kentik_api.core.api_config import APIConfig
from kentik_api.core.rest_runtime import request_json

from ..error import GetJourneysNlqError
from ..models import (  # noqa: F401
    GetJourneysNlqResponse,
    ResultFormat,
    ResultType,
    protobufAny,
    rpcStatus,
)


def GetJourneysNlq(
    api_config_override: Optional[APIConfig] = None, *, prompt: str
) -> GetJourneysNlqResponse:
    query_params: Dict[str, Any] = {"prompt": prompt}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path="/journeys/v202406/GetJourneysNlq",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="GetJourneysNlq",
        error_cls=GetJourneysNlqError,
    )

    return (
        GetJourneysNlqResponse(**body)
        if body is not None
        else GetJourneysNlqResponse.model_construct()
    )
