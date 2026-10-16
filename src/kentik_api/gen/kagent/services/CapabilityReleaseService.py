# AUTO-GENERATED: scripts/openapi_templates/service.jinja2 via openapi-python-generator
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Any, Dict, List, Optional

from kentik_api.core.api_config import APIConfig
from kentik_api.core.rest_runtime import request_json

from ..error import (
    CapabilityReleaseService_GetCapabilityLatestReleasesError,
    CapabilityReleaseService_GetCapabilityReleaseError,
    CapabilityReleaseService_GetCapabilitySupportedDistrosError,
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


def CapabilityReleaseService_GetCapabilityRelease(
    api_config_override: Optional[APIConfig] = None,
    *,
    os: Optional[str] = None,
    arch: Optional[str] = None,
    channel: Optional[str] = None,
    capability: Optional[str] = None,
    semver: Optional[str] = None,
    distro: Optional[str] = None,
) -> GetCapabilityReleaseResponse:
    query_params: Dict[str, Any] = {
        "os": os,
        "arch": arch,
        "channel": channel,
        "capability": capability,
        "semver": semver,
        "distro": distro,
    }

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path="/kagent/v202401/releases",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="CapabilityReleaseService_GetCapabilityRelease",
        error_cls=CapabilityReleaseService_GetCapabilityReleaseError,
    )

    return (
        GetCapabilityReleaseResponse(**body)
        if body is not None
        else GetCapabilityReleaseResponse.model_construct()
    )


def CapabilityReleaseService_GetCapabilityLatestReleases(
    api_config_override: Optional[APIConfig] = None,
    *,
    os: Optional[str] = None,
    arch: Optional[str] = None,
    channel: Optional[str] = None,
    installId: Optional[str] = None,
    capabilities: Optional[List[str]] = None,
    distro: Optional[str] = None,
) -> GetCapabilityLatestReleasesResponse:
    query_params: Dict[str, Any] = {
        "os": os,
        "arch": arch,
        "channel": channel,
        "installId": installId,
        "capabilities": capabilities,
        "distro": distro,
    }

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path="/kagent/v202401/releases/latest",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="CapabilityReleaseService_GetCapabilityLatestReleases",
        error_cls=CapabilityReleaseService_GetCapabilityLatestReleasesError,
    )

    return (
        GetCapabilityLatestReleasesResponse(**body)
        if body is not None
        else GetCapabilityLatestReleasesResponse.model_construct()
    )


def CapabilityReleaseService_GetCapabilitySupportedDistros(
    api_config_override: Optional[APIConfig] = None,
    *,
    capabilities: Optional[List[str]] = None,
) -> GetCapabilitySupportedDistrosResponse:
    query_params: Dict[str, Any] = {"capabilities": capabilities}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path="/kagent/v202401/releases/supported_distros",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="CapabilityReleaseService_GetCapabilitySupportedDistros",
        error_cls=CapabilityReleaseService_GetCapabilitySupportedDistrosError,
    )

    return (
        GetCapabilitySupportedDistrosResponse(**body)
        if body is not None
        else GetCapabilitySupportedDistrosResponse.model_construct()
    )
