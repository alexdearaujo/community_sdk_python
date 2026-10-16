# AUTO-GENERATED: scripts/openapi_templates/service.jinja2 via openapi-python-generator
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Any, Dict, Optional

from kentik_api.core.api_config import APIConfig
from kentik_api.core.rest_runtime import request_json

from ..error import (
    DeleteAgentCapabilityError,
    GetAgentCapabilityError,
    ListAgentCapabilitiesError,
    UpsertAgentCapabilityError,
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


def ListAgentCapabilities(
    api_config_override: Optional[APIConfig] = None, *, agentId: str
) -> ListAgentCapabilitiesResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path=f"/kagent/v202401/agents/{agentId}/capabilities",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="ListAgentCapabilities",
        error_cls=ListAgentCapabilitiesError,
    )

    return (
        ListAgentCapabilitiesResponse(**body)
        if body is not None
        else ListAgentCapabilitiesResponse.model_construct()
    )


def GetAgentCapability(
    api_config_override: Optional[APIConfig] = None,
    *,
    agentId: str,
    capabilityname: str,
) -> GetAgentCapabilityResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path=f"/kagent/v202401/agents/{agentId}/capabilities/{capabilityname}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="GetAgentCapability",
        error_cls=GetAgentCapabilityError,
    )

    return (
        GetAgentCapabilityResponse(**body)
        if body is not None
        else GetAgentCapabilityResponse.model_construct()
    )


def DeleteAgentCapability(
    api_config_override: Optional[APIConfig] = None,
    *,
    agentId: str,
    capabilityname: str,
) -> DeleteAgentCapabilityResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="delete",
        path=f"/kagent/v202401/agents/{agentId}/capabilities/{capabilityname}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="DeleteAgentCapability",
        error_cls=DeleteAgentCapabilityError,
    )

    return (
        DeleteAgentCapabilityResponse(**body)
        if body is not None
        else DeleteAgentCapabilityResponse.model_construct()
    )


def UpsertAgentCapability(
    api_config_override: Optional[APIConfig] = None,
    *,
    agentId: str,
    capabilityname: str,
    data: Dict[str, Any],
    mask: Optional[str] = None,
) -> UpsertAgentCapabilityResponse:
    query_params: Dict[str, Any] = {"mask": mask}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="patch",
        path=f"/kagent/v202401/agents/{agentId}/capabilities/{capabilityname}",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data,
        header_params=header_params,
        expected_status=200,
        operation_name="UpsertAgentCapability",
        error_cls=UpsertAgentCapabilityError,
    )

    return (
        UpsertAgentCapabilityResponse(**body)
        if body is not None
        else UpsertAgentCapabilityResponse.model_construct()
    )
