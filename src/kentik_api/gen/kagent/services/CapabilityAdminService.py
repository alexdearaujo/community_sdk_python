# AUTO-GENERATED: scripts/openapi_templates/service.jinja2 via openapi-python-generator
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Any, Dict, Optional

from kentik_api.core.api_config import APIConfig
from kentik_api.core.rest_runtime import request_json

from ..error import (
    CapabilityAdminService_CreateCapabilityError,
    CapabilityAdminService_DeleteCapabilityError,
    CapabilityAdminService_GetCapabilityError,
    CapabilityAdminService_ListCapabilitiesError,
    CapabilityAdminService_UpdateCapabilityError,
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


def CapabilityAdminService_ListCapabilities(
    api_config_override: Optional[APIConfig] = None,
) -> ListCapabilitiesResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path="/kagent/v202401/capabilities",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="CapabilityAdminService_ListCapabilities",
        error_cls=CapabilityAdminService_ListCapabilitiesError,
    )

    return (
        ListCapabilitiesResponse(**body)
        if body is not None
        else ListCapabilitiesResponse.model_construct()
    )


def CapabilityAdminService_CreateCapability(
    api_config_override: Optional[APIConfig] = None, *, data: Capability
) -> CreateCapabilityResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="post",
        path="/kagent/v202401/capabilities",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(),
        header_params=header_params,
        expected_status=200,
        operation_name="CapabilityAdminService_CreateCapability",
        error_cls=CapabilityAdminService_CreateCapabilityError,
    )

    return (
        CreateCapabilityResponse(**body)
        if body is not None
        else CreateCapabilityResponse.model_construct()
    )


def CapabilityAdminService_GetCapability(
    api_config_override: Optional[APIConfig] = None, *, capabilityname: str
) -> GetCapabilityResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path=f"/kagent/v202401/capabilities/{capabilityname}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="CapabilityAdminService_GetCapability",
        error_cls=CapabilityAdminService_GetCapabilityError,
    )

    return (
        GetCapabilityResponse(**body)
        if body is not None
        else GetCapabilityResponse.model_construct()
    )


def CapabilityAdminService_DeleteCapability(
    api_config_override: Optional[APIConfig] = None, *, capabilityname: str
) -> DeleteCapabilityResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="delete",
        path=f"/kagent/v202401/capabilities/{capabilityname}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="CapabilityAdminService_DeleteCapability",
        error_cls=CapabilityAdminService_DeleteCapabilityError,
    )

    return (
        DeleteCapabilityResponse(**body)
        if body is not None
        else DeleteCapabilityResponse.model_construct()
    )


def CapabilityAdminService_UpdateCapability(
    api_config_override: Optional[APIConfig] = None,
    *,
    capabilityname: str,
    data: Dict[str, Any],
) -> UpdateCapabilityResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="patch",
        path=f"/kagent/v202401/capabilities/{capabilityname}",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data,
        header_params=header_params,
        expected_status=200,
        operation_name="CapabilityAdminService_UpdateCapability",
        error_cls=CapabilityAdminService_UpdateCapabilityError,
    )

    return (
        UpdateCapabilityResponse(**body)
        if body is not None
        else UpdateCapabilityResponse.model_construct()
    )
