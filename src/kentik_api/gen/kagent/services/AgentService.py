# AUTO-GENERATED: scripts/openapi_templates/service.jinja2 via openapi-python-generator
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Any, Dict, List, Optional

from kentik_api.core.api_config import APIConfig
from kentik_api.core.rest_runtime import request_json

from ..error import (
    AuthorizeError,
    CreateAgentError,
    DeleteAgentError,
    GenerateInstallCommandsError,
    GetAgentError,
    ListAgentsError,
    UpdateAgentError,
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


def ListAgents(
    api_config_override: Optional[APIConfig] = None,
    *,
    unregistered: Optional[bool] = None,
    ids: Optional[List[str]] = None,
    capabilities: Optional[List[str]] = None,
    includeDesiredState: Optional[bool] = None,
) -> ListAgentsResponse:
    query_params: Dict[str, Any] = {
        "unregistered": unregistered,
        "ids": ids,
        "capabilities": capabilities,
        "includeDesiredState": includeDesiredState,
    }

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path="/kagent/v202401/agents",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="ListAgents",
        error_cls=ListAgentsError,
    )

    return (
        ListAgentsResponse(**body)
        if body is not None
        else ListAgentsResponse.model_construct()
    )


def CreateAgent(
    api_config_override: Optional[APIConfig] = None, *, data: CreateAgentRequest
) -> CreateAgentResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="post",
        path="/kagent/v202401/agents",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(),
        header_params=header_params,
        expected_status=200,
        operation_name="CreateAgent",
        error_cls=CreateAgentError,
    )

    return (
        CreateAgentResponse(**body)
        if body is not None
        else CreateAgentResponse.model_construct()
    )


def Authorize(
    api_config_override: Optional[APIConfig] = None, *, installId: str
) -> AuthorizeResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="put",
        path=f"/kagent/v202401/agents/authorize/{installId}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="Authorize",
        error_cls=AuthorizeError,
    )

    return (
        AuthorizeResponse(**body)
        if body is not None
        else AuthorizeResponse.model_construct()
    )


def GenerateInstallCommands(
    api_config_override: Optional[APIConfig] = None,
    *,
    data: GenerateInstallCommandsRequest,
) -> GenerateInstallCommandsResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="post",
        path="/kagent/v202401/agents/install-commands",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(),
        header_params=header_params,
        expected_status=200,
        operation_name="GenerateInstallCommands",
        error_cls=GenerateInstallCommandsError,
    )

    return (
        GenerateInstallCommandsResponse(**body)
        if body is not None
        else GenerateInstallCommandsResponse.model_construct()
    )


def GetAgent(
    api_config_override: Optional[APIConfig] = None,
    *,
    agentid: str,
    unregistered: Optional[bool] = None,
) -> GetAgentResponse:
    query_params: Dict[str, Any] = {"unregistered": unregistered}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path=f"/kagent/v202401/agents/{agentid}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="GetAgent",
        error_cls=GetAgentError,
    )

    return (
        GetAgentResponse(**body)
        if body is not None
        else GetAgentResponse.model_construct()
    )


def DeleteAgent(
    api_config_override: Optional[APIConfig] = None,
    *,
    agentid: str,
    unregistered: Optional[bool] = None,
) -> DeleteAgentResponse:
    query_params: Dict[str, Any] = {"unregistered": unregistered}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="delete",
        path=f"/kagent/v202401/agents/{agentid}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="DeleteAgent",
        error_cls=DeleteAgentError,
    )

    return (
        DeleteAgentResponse(**body)
        if body is not None
        else DeleteAgentResponse.model_construct()
    )


def UpdateAgent(
    api_config_override: Optional[APIConfig] = None,
    *,
    agentid: str,
    data: Dict[str, Any],
    mask: Optional[str] = None,
) -> UpdateAgentResponse:
    query_params: Dict[str, Any] = {"mask": mask}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="patch",
        path=f"/kagent/v202401/agents/{agentid}",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data,
        header_params=header_params,
        expected_status=200,
        operation_name="UpdateAgent",
        error_cls=UpdateAgentError,
    )

    return (
        UpdateAgentResponse(**body)
        if body is not None
        else UpdateAgentResponse.model_construct()
    )
