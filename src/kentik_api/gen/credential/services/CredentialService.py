# AUTO-GENERATED: scripts/openapi_templates/service.jinja2 via openapi-python-generator
# Rebuilt on every `uv run poe generate`. Do not edit by hand.

from typing import Any, Dict, Optional

from kentik_api.core.api_config import APIConfig
from kentik_api.core.rest_runtime import (
    parse_response_model,
    path_segment,
    request_json,
)

from ..error import GetGroupError, ListGroupError
from ..models import (  # noqa: F401
    CredentialGroup,
    GetCredentialGroupResponse,
    LandingType,
    ListCredentialGroupResponse,
    PermissionEntry,
    Role,
    Secret,
    SecretType,
    User,
    protobufAny,
    rpcStatus,
)


def ListCredentialGroup(
    api_config_override: Optional[APIConfig] = None,
) -> ListCredentialGroupResponse:
    """
    List credential groups.

    Returns list of credential group information in Kentik vault.
    """
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path="/credential/v202407alpha1/group",
        path_template="/credential/v202407alpha1/group",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="ListCredentialGroup",
        error_cls=ListGroupError,
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
    """
    Get a credential group by id.

    Returns specific credential group information in Kentik vault.
    """
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path=f"/credential/v202407alpha1/group/{path_segment(id)}",
        path_template="/credential/v202407alpha1/group/{id}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="GetCredentialGroup",
        error_cls=GetGroupError,
    )

    return parse_response_model(
        GetCredentialGroupResponse,
        body,
        operation_name="GetCredentialGroup",
        method="get",
        path="/credential/v202407alpha1/group/{id}",
    )
