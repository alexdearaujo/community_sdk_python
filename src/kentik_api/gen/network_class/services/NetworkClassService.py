# AUTO-GENERATED: scripts/openapi_templates/service.jinja2 via openapi-python-generator
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Any, Dict, Optional

from kentik_api.core.api_config import APIConfig
from kentik_api.core.rest_runtime import request_json

from ..error import NetworkClassGetError, NetworkClassUpdateError
from ..models import (  # noqa: F401
    CloudSubnet,
    CloudType,
    GetNetworkClassResponse,
    NetworkClass,
    UpdateNetworkClassRequest,
    UpdateNetworkClassResponse,
    protobufAny,
    rpcStatus,
)


def NetworkClassGet(
    api_config_override: Optional[APIConfig] = None,
) -> GetNetworkClassResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path="/network_class/v202109alpha1/network_class",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="NetworkClassGet",
        error_cls=NetworkClassGetError,
    )

    return (
        GetNetworkClassResponse(**body)
        if body is not None
        else GetNetworkClassResponse.model_construct()
    )


def NetworkClassUpdate(
    api_config_override: Optional[APIConfig] = None, *, data: UpdateNetworkClassRequest
) -> UpdateNetworkClassResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="post",
        path="/network_class/v202109alpha1/network_class",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(),
        header_params=header_params,
        expected_status=200,
        operation_name="NetworkClassUpdate",
        error_cls=NetworkClassUpdateError,
    )

    return (
        UpdateNetworkClassResponse(**body)
        if body is not None
        else UpdateNetworkClassResponse.model_construct()
    )
