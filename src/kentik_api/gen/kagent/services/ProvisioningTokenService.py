# AUTO-GENERATED: scripts/openapi_templates/service.jinja2 via openapi-python-generator
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Any, Dict, Optional

from kentik_api.core.api_config import APIConfig
from kentik_api.core.rest_runtime import request_json

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

    return (
        ListProvisioningTokensResponse(**body)
        if body is not None
        else ListProvisioningTokensResponse.model_construct()
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
        json_body=data.model_dump(),
        header_params=header_params,
        expected_status=200,
        operation_name="CreateProvisioningToken",
        error_cls=CreateProvisioningTokenError,
    )

    return (
        CreateProvisioningTokenResponse(**body)
        if body is not None
        else CreateProvisioningTokenResponse.model_construct()
    )


def GetProvisioningToken(
    api_config_override: Optional[APIConfig] = None, *, token: str
) -> GetProvisioningTokenResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path=f"/kagent/v202401/provisioning-tokens/{token}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="GetProvisioningToken",
        error_cls=GetProvisioningTokenError,
    )

    return (
        GetProvisioningTokenResponse(**body)
        if body is not None
        else GetProvisioningTokenResponse.model_construct()
    )


def ListAgentsByProvisioningToken(
    api_config_override: Optional[APIConfig] = None, *, token: str
) -> ListAgentsByProvisioningTokenResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path=f"/kagent/v202401/provisioning-tokens/{token}/agents",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="ListAgentsByProvisioningToken",
        error_cls=ListAgentsByProvisioningTokenError,
    )

    return (
        ListAgentsByProvisioningTokenResponse(**body)
        if body is not None
        else ListAgentsByProvisioningTokenResponse.model_construct()
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
        path=f"/kagent/v202401/provisioning-tokens/{token}/revoke",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(),
        header_params=header_params,
        expected_status=200,
        operation_name="RevokeProvisioningToken",
        error_cls=RevokeProvisioningTokenError,
    )

    return (
        RevokeProvisioningTokenResponse(**body)
        if body is not None
        else RevokeProvisioningTokenResponse.model_construct()
    )
