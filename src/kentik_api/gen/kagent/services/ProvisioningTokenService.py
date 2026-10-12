# AUTO-GENERATED: scripts/openapi_templates/service.jinja2 via openapi-python-generator
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Any, Dict, Optional

from kentik_api.core.api_config import APIConfig
from kentik_api.core.rest_runtime import (
    parse_response_model,
    path_segment,
    request_json,
)

from ..error import (
    CreateProvisioningTokenError,
    GetProvisioningTokenError,
    ListAgentsByProvisioningTokenError,
    ListProvisioningTokensError,
    RevokeProvisioningTokenError,
)
from ..models import (  # noqa: F401
    Agent,
    AgentCapability,
    AgentRegistration,
    AuthorizeResponse,
    BootstrapInfo,
    Capability,
    CapabilityDistro,
    CapabilityRelease,
    CapabilitySupportedDistro,
    CompatibilityInfo,
    Config,
    ConfigLayer,
    ConfigLayerLayerType,
    ConfigServiceUpdateConfigBody,
    CreateAgentRequest,
    CreateAgentResponse,
    CreateCapabilityResponse,
    CreateConfigResponse,
    CreateProvisioningTokenResponse,
    DeleteAgentCapabilityResponse,
    DeleteAgentResponse,
    DeleteCapabilityResponse,
    DeleteConfigResponse,
    GenerateInstallCommandsRequest,
    GenerateInstallCommandsResponse,
    GetAgentCapabilityResponse,
    GetAgentResponse,
    GetCapabilityLatestReleasesResponse,
    GetCapabilityReleaseResponse,
    GetCapabilityResponse,
    GetCapabilitySupportedDistrosResponse,
    GetConfigResponse,
    GetProvisioningTokenResponse,
    HostMetadata,
    InstallConfig,
    InstallerType,
    ListAgentCapabilitiesResponse,
    ListAgentsByProvisioningTokenResponse,
    ListAgentsResponse,
    ListCapabilitiesResponse,
    ListProvisioningTokensResponse,
    ProvisioningToken,
    ProvisioningTokenAgentConfig,
    ProvisioningTokenServiceRevokeProvisioningTokenBody,
    RegistrationConfig,
    RevokeProvisioningTokenResponse,
    RuntimeConfig,
    RuntimeConfigEnvVar,
    TelemetryConfig,
    TokenRevoked,
    UpdateAgentResponse,
    UpdateCapabilityResponse,
    UpdateConfigResponse,
    UpsertAgentCapabilityResponse,
    kagentv202401AgentConfig,
    protobufAny,
    rpcStatus,
)


def ListProvisioningTokens(
    api_config_override: Optional[APIConfig] = None,
) -> ListProvisioningTokensResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path="/kagent/v202401/provisioning-tokens",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="ListProvisioningTokens",
        error_cls=ListProvisioningTokensError,
    )

    return parse_response_model(
        ListProvisioningTokensResponse,
        body,
        operation_name="ListProvisioningTokens",
        method="get",
        path="/kagent/v202401/provisioning-tokens",
    )


def CreateProvisioningToken(
    api_config_override: Optional[APIConfig] = None, *, data: ProvisioningToken
) -> CreateProvisioningTokenResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="post",
        path="/kagent/v202401/provisioning-tokens",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(by_alias=True),
        header_params=header_params,
        expected_status=200,
        operation_name="CreateProvisioningToken",
        error_cls=CreateProvisioningTokenError,
    )

    return parse_response_model(
        CreateProvisioningTokenResponse,
        body,
        operation_name="CreateProvisioningToken",
        method="post",
        path="/kagent/v202401/provisioning-tokens",
    )


def GetProvisioningToken(
    api_config_override: Optional[APIConfig] = None, *, token: str
) -> GetProvisioningTokenResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path=f"/kagent/v202401/provisioning-tokens/{path_segment(token)}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="GetProvisioningToken",
        error_cls=GetProvisioningTokenError,
    )

    return parse_response_model(
        GetProvisioningTokenResponse,
        body,
        operation_name="GetProvisioningToken",
        method="get",
        path="/kagent/v202401/provisioning-tokens/{token}",
    )


def ListAgentsByProvisioningToken(
    api_config_override: Optional[APIConfig] = None, *, token: str
) -> ListAgentsByProvisioningTokenResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path=f"/kagent/v202401/provisioning-tokens/{path_segment(token)}/agents",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="ListAgentsByProvisioningToken",
        error_cls=ListAgentsByProvisioningTokenError,
    )

    return parse_response_model(
        ListAgentsByProvisioningTokenResponse,
        body,
        operation_name="ListAgentsByProvisioningToken",
        method="get",
        path="/kagent/v202401/provisioning-tokens/{token}/agents",
    )


def RevokeProvisioningToken(
    api_config_override: Optional[APIConfig] = None,
    *,
    token: str,
    data: ProvisioningTokenServiceRevokeProvisioningTokenBody,
) -> RevokeProvisioningTokenResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="post",
        path=f"/kagent/v202401/provisioning-tokens/{path_segment(token)}/revoke",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(by_alias=True),
        header_params=header_params,
        expected_status=200,
        operation_name="RevokeProvisioningToken",
        error_cls=RevokeProvisioningTokenError,
    )

    return parse_response_model(
        RevokeProvisioningTokenResponse,
        body,
        operation_name="RevokeProvisioningToken",
        method="post",
        path="/kagent/v202401/provisioning-tokens/{token}/revoke",
    )
