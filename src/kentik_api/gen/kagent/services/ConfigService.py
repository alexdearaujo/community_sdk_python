# AUTO-GENERATED: scripts/openapi_templates/service.jinja2 via openapi-python-generator
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Any, Dict, Optional

from kentik_api.core.api_config import APIConfig
from kentik_api.core.rest_runtime import request_json

from ..error import (
    CreateConfigError,
    DeleteConfigError,
    GetConfigError,
    UpdateConfigError,
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


def CreateConfig(
    api_config_override: Optional[APIConfig] = None, *, data: Config
) -> CreateConfigResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="post",
        path="/kagent/v202401/config",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(),
        header_params=header_params,
        expected_status=200,
        operation_name="CreateConfig",
        error_cls=CreateConfigError,
    )

    return (
        CreateConfigResponse(**body)
        if body is not None
        else CreateConfigResponse.model_construct()
    )


def GetConfig(
    api_config_override: Optional[APIConfig] = None, *, configname: str
) -> GetConfigResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path=f"/kagent/v202401/config/{configname}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="GetConfig",
        error_cls=GetConfigError,
    )

    return (
        GetConfigResponse(**body)
        if body is not None
        else GetConfigResponse.model_construct()
    )


def DeleteConfig(
    api_config_override: Optional[APIConfig] = None, *, configname: str
) -> DeleteConfigResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="delete",
        path=f"/kagent/v202401/config/{configname}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="DeleteConfig",
        error_cls=DeleteConfigError,
    )

    return (
        DeleteConfigResponse(**body)
        if body is not None
        else DeleteConfigResponse.model_construct()
    )


def UpdateConfig(
    api_config_override: Optional[APIConfig] = None,
    *,
    configname: str,
    data: ConfigServiceUpdateConfigBody,
) -> UpdateConfigResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="patch",
        path=f"/kagent/v202401/config/{configname}",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(),
        header_params=header_params,
        expected_status=200,
        operation_name="UpdateConfig",
        error_cls=UpdateConfigError,
    )

    return (
        UpdateConfigResponse(**body)
        if body is not None
        else UpdateConfigResponse.model_construct()
    )
