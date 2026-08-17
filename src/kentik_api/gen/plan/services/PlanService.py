from typing import Any, Dict, Optional

from kentik_api.core.api_config import APIConfig
from kentik_api.core.rest_runtime import request_json

from ..error import ListPlansError
from ..models import (  # noqa: F401
    DeviceSubtype,
    ListPlansResponse,
    Plan,
    PlanDevice,
    protobufAny,
    rpcStatus,
)


def ListPlans(api_config_override: Optional[APIConfig] = None) -> ListPlansResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path="/plans/v202501alpha1",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="ListPlans",
        error_cls=ListPlansError,
    )

    return (
        ListPlansResponse(**body)
        if body is not None
        else ListPlansResponse.model_construct()
    )
