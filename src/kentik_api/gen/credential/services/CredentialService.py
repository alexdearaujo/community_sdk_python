from typing import Any, Dict, Optional

from kentik_api.core.api_config import APIConfig
from kentik_api.core.rest_runtime import request_json

from ..error import GetCredentialGroupError, ListCredentialGroupError
from ..models import (  # noqa: F401
    CredentialGroup,
    GetCredentialGroupResponse,
    ListCredentialGroupResponse,
    protobufAny,
    rpcStatus,
    v202211LandingType,
    v202211PermissionEntry,
    v202211Role,
    v202211User,
    v202312alpha1Secret,
    v202312alpha1SecretType,
)


def ListCredentialGroup(
    api_config_override: Optional[APIConfig] = None,
) -> ListCredentialGroupResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path="/credential/v202407alpha1/group",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="ListCredentialGroup",
        error_cls=ListCredentialGroupError,
    )

    return (
        ListCredentialGroupResponse(**body)
        if body is not None
        else ListCredentialGroupResponse.model_construct()
    )


def GetCredentialGroup(
    api_config_override: Optional[APIConfig] = None, *, id: str
) -> GetCredentialGroupResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path=f"/credential/v202407alpha1/group/{id}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="GetCredentialGroup",
        error_cls=GetCredentialGroupError,
    )

    return (
        GetCredentialGroupResponse(**body)
        if body is not None
        else GetCredentialGroupResponse.model_construct()
    )
