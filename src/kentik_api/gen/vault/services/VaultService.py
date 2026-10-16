# AUTO-GENERATED: scripts/openapi_templates/service.jinja2 via openapi-python-generator
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Any, Dict, List, Optional

from kentik_api.core.api_config import APIConfig
from kentik_api.core.rest_runtime import request_json

from ..error import GetSecretError, ListSecretError
from ..models import (  # noqa: F401
    GetSecretResponse,
    ListSecretResponse,
    Secret,
    SecretType,
    protobufAny,
    rpcStatus,
)


def ListSecret(
    api_config_override: Optional[APIConfig] = None, *, names: List[str]
) -> ListSecretResponse:
    query_params: Dict[str, Any] = {"names": names}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path="/vault/v202312alpha1/secrets",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="ListSecret",
        error_cls=ListSecretError,
    )

    return (
        ListSecretResponse(**body)
        if body is not None
        else ListSecretResponse.model_construct()
    )


def GetSecret(
    api_config_override: Optional[APIConfig] = None, *, name: str
) -> GetSecretResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path=f"/vault/v202312alpha1/secrets/{name}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="GetSecret",
        error_cls=GetSecretError,
    )

    return (
        GetSecretResponse(**body)
        if body is not None
        else GetSecretResponse.model_construct()
    )
