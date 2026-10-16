# AUTO-GENERATED: scripts/openapi_templates/service.jinja2 via openapi-python-generator
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Any, Dict, Optional

from kentik_api.core.api_config import APIConfig
from kentik_api.core.rest_runtime import (
    parse_response_model,
    path_segment,
    request_json,
)

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

    return parse_response_model(
        ListCredentialGroupResponse,
        body,
        operation_name="ListCredentialGroup",
        method="get",
        path="/credential/v202407alpha1/group",
    )


def GetCredentialGroup(
    api_config_override: Optional[APIConfig] = None, *, id: str
) -> GetCredentialGroupResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path=f"/credential/v202407alpha1/group/{path_segment(id)}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="GetCredentialGroup",
        error_cls=GetCredentialGroupError,
    )

    return parse_response_model(
        GetCredentialGroupResponse,
        body,
        operation_name="GetCredentialGroup",
        method="get",
        path="/credential/v202407alpha1/group/{id}",
    )
