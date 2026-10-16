# AUTO-GENERATED: scripts/generation/error_package.py, generate_service_error_package()
# Rebuilt on every `make generate`. Do not edit by hand.

from __future__ import annotations

from typing import Any

from kentik_api.errors import HTTPException

from ..models import rpcStatus


class KagentError(HTTPException):
    """Base service-local error for the kagent API."""

    @classmethod
    def _build_error(
        cls, response: Any, *, operation_name: str, method: str, path: str
    ) -> "KagentError":
        preview = getattr(response, "text", "")[:200].replace("\n", " ")
        headers = getattr(response, "headers", {})
        content_type = (
            headers.get("content-type", "unknown")
            if hasattr(headers, "get")
            else "unknown"
        )
        details: dict[str, Any] = {
            "content_type": content_type,
            "preview": preview,
        }
        message = f"{operation_name} failed with status code: {getattr(response, 'status_code', 'unknown')}"
        try:
            payload = response.json()
        except Exception:
            payload = None
        if isinstance(payload, dict):
            details["response_json"] = payload
            try:
                status = rpcStatus.model_validate(payload)
            except Exception:
                status = None
            if status is not None:
                details["rpc_status"] = payload
                if status.code is not None:
                    details["rpc_status_code"] = status.code
                if status.message:
                    message = status.message
                else:
                    message = payload.get("message") or message
            else:
                message = payload.get("message") or message
        elif payload is not None:
            details["response_json"] = payload
        return cls(
            getattr(response, "status_code", 500),
            message,
            method=method,
            path=path,
            details=details,
        )

    @classmethod
    def from_response(
        cls, response: Any, *, operation_name: str, method: str, path: str
    ) -> "KagentError":
        status_key = str(getattr(response, "status_code", ""))
        response_error_map = getattr(cls, "response_error_map", {})
        target_cls = (
            response_error_map.get(status_key)
            or response_error_map.get("default")
            or cls
        )
        return target_cls._build_error(
            response,
            operation_name=operation_name,
            method=method,
            path=path,
        )


class AuthorizeError(KagentError):
    """Operation-local error for Authorize."""

    response_error_map: dict[str, type[KagentError]] = {}


class AuthorizeUnexpectedError(AuthorizeError):
    """Operation-local response error for Authorize (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


AuthorizeError.response_error_map = {
    "default": AuthorizeUnexpectedError,
}


class CapabilityAdminService_CreateCapabilityError(KagentError):
    """Operation-local error for CapabilityAdminService_CreateCapability."""

    response_error_map: dict[str, type[KagentError]] = {}


class CapabilityAdminService_CreateCapabilityUnexpectedError(
    CapabilityAdminService_CreateCapabilityError
):
    """Operation-local response error for CapabilityAdminService_CreateCapability (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


CapabilityAdminService_CreateCapabilityError.response_error_map = {
    "default": CapabilityAdminService_CreateCapabilityUnexpectedError,
}


class CapabilityAdminService_DeleteCapabilityError(KagentError):
    """Operation-local error for CapabilityAdminService_DeleteCapability."""

    response_error_map: dict[str, type[KagentError]] = {}


class CapabilityAdminService_DeleteCapabilityUnexpectedError(
    CapabilityAdminService_DeleteCapabilityError
):
    """Operation-local response error for CapabilityAdminService_DeleteCapability (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


CapabilityAdminService_DeleteCapabilityError.response_error_map = {
    "default": CapabilityAdminService_DeleteCapabilityUnexpectedError,
}


class CapabilityAdminService_GetCapabilityError(KagentError):
    """Operation-local error for CapabilityAdminService_GetCapability."""

    response_error_map: dict[str, type[KagentError]] = {}


class CapabilityAdminService_GetCapabilityUnexpectedError(
    CapabilityAdminService_GetCapabilityError
):
    """Operation-local response error for CapabilityAdminService_GetCapability (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


CapabilityAdminService_GetCapabilityError.response_error_map = {
    "default": CapabilityAdminService_GetCapabilityUnexpectedError,
}


class CapabilityAdminService_ListCapabilitiesError(KagentError):
    """Operation-local error for CapabilityAdminService_ListCapabilities."""

    response_error_map: dict[str, type[KagentError]] = {}


class CapabilityAdminService_ListCapabilitiesUnexpectedError(
    CapabilityAdminService_ListCapabilitiesError
):
    """Operation-local response error for CapabilityAdminService_ListCapabilities (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


CapabilityAdminService_ListCapabilitiesError.response_error_map = {
    "default": CapabilityAdminService_ListCapabilitiesUnexpectedError,
}


class CapabilityAdminService_UpdateCapabilityError(KagentError):
    """Operation-local error for CapabilityAdminService_UpdateCapability."""

    response_error_map: dict[str, type[KagentError]] = {}


class CapabilityAdminService_UpdateCapabilityUnexpectedError(
    CapabilityAdminService_UpdateCapabilityError
):
    """Operation-local response error for CapabilityAdminService_UpdateCapability (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


CapabilityAdminService_UpdateCapabilityError.response_error_map = {
    "default": CapabilityAdminService_UpdateCapabilityUnexpectedError,
}


class CapabilityReleaseService_GetCapabilityLatestReleasesError(KagentError):
    """Operation-local error for CapabilityReleaseService_GetCapabilityLatestReleases."""

    response_error_map: dict[str, type[KagentError]] = {}


class CapabilityReleaseService_GetCapabilityLatestReleasesUnexpectedError(
    CapabilityReleaseService_GetCapabilityLatestReleasesError
):
    """Operation-local response error for CapabilityReleaseService_GetCapabilityLatestReleases (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


CapabilityReleaseService_GetCapabilityLatestReleasesError.response_error_map = {
    "default": CapabilityReleaseService_GetCapabilityLatestReleasesUnexpectedError,
}


class CapabilityReleaseService_GetCapabilityReleaseError(KagentError):
    """Operation-local error for CapabilityReleaseService_GetCapabilityRelease."""

    response_error_map: dict[str, type[KagentError]] = {}


class CapabilityReleaseService_GetCapabilityReleaseUnexpectedError(
    CapabilityReleaseService_GetCapabilityReleaseError
):
    """Operation-local response error for CapabilityReleaseService_GetCapabilityRelease (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


CapabilityReleaseService_GetCapabilityReleaseError.response_error_map = {
    "default": CapabilityReleaseService_GetCapabilityReleaseUnexpectedError,
}


class CapabilityReleaseService_GetCapabilitySupportedDistrosError(KagentError):
    """Operation-local error for CapabilityReleaseService_GetCapabilitySupportedDistros."""

    response_error_map: dict[str, type[KagentError]] = {}


class CapabilityReleaseService_GetCapabilitySupportedDistrosUnexpectedError(
    CapabilityReleaseService_GetCapabilitySupportedDistrosError
):
    """Operation-local response error for CapabilityReleaseService_GetCapabilitySupportedDistros (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


CapabilityReleaseService_GetCapabilitySupportedDistrosError.response_error_map = {
    "default": CapabilityReleaseService_GetCapabilitySupportedDistrosUnexpectedError,
}


class CreateAgentError(KagentError):
    """Operation-local error for CreateAgent."""

    response_error_map: dict[str, type[KagentError]] = {}


class CreateAgentUnexpectedError(CreateAgentError):
    """Operation-local response error for CreateAgent (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


CreateAgentError.response_error_map = {
    "default": CreateAgentUnexpectedError,
}


class CreateConfigError(KagentError):
    """Operation-local error for CreateConfig."""

    response_error_map: dict[str, type[KagentError]] = {}


class CreateConfigUnexpectedError(CreateConfigError):
    """Operation-local response error for CreateConfig (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


CreateConfigError.response_error_map = {
    "default": CreateConfigUnexpectedError,
}


class CreateProvisioningTokenError(KagentError):
    """Operation-local error for CreateProvisioningToken."""

    response_error_map: dict[str, type[KagentError]] = {}


class CreateProvisioningTokenUnexpectedError(CreateProvisioningTokenError):
    """Operation-local response error for CreateProvisioningToken (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


CreateProvisioningTokenError.response_error_map = {
    "default": CreateProvisioningTokenUnexpectedError,
}


class DeleteAgentError(KagentError):
    """Operation-local error for DeleteAgent."""

    response_error_map: dict[str, type[KagentError]] = {}


class DeleteAgentUnexpectedError(DeleteAgentError):
    """Operation-local response error for DeleteAgent (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


DeleteAgentError.response_error_map = {
    "default": DeleteAgentUnexpectedError,
}


class DeleteAgentCapabilityError(KagentError):
    """Operation-local error for DeleteAgentCapability."""

    response_error_map: dict[str, type[KagentError]] = {}


class DeleteAgentCapabilityUnexpectedError(DeleteAgentCapabilityError):
    """Operation-local response error for DeleteAgentCapability (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


DeleteAgentCapabilityError.response_error_map = {
    "default": DeleteAgentCapabilityUnexpectedError,
}


class DeleteConfigError(KagentError):
    """Operation-local error for DeleteConfig."""

    response_error_map: dict[str, type[KagentError]] = {}


class DeleteConfigUnexpectedError(DeleteConfigError):
    """Operation-local response error for DeleteConfig (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


DeleteConfigError.response_error_map = {
    "default": DeleteConfigUnexpectedError,
}


class GenerateInstallCommandsError(KagentError):
    """Operation-local error for GenerateInstallCommands."""

    response_error_map: dict[str, type[KagentError]] = {}


class GenerateInstallCommandsUnexpectedError(GenerateInstallCommandsError):
    """Operation-local response error for GenerateInstallCommands (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


GenerateInstallCommandsError.response_error_map = {
    "default": GenerateInstallCommandsUnexpectedError,
}


class GetAgentError(KagentError):
    """Operation-local error for GetAgent."""

    response_error_map: dict[str, type[KagentError]] = {}


class GetAgentUnexpectedError(GetAgentError):
    """Operation-local response error for GetAgent (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


GetAgentError.response_error_map = {
    "default": GetAgentUnexpectedError,
}


class GetAgentCapabilityError(KagentError):
    """Operation-local error for GetAgentCapability."""

    response_error_map: dict[str, type[KagentError]] = {}


class GetAgentCapabilityUnexpectedError(GetAgentCapabilityError):
    """Operation-local response error for GetAgentCapability (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


GetAgentCapabilityError.response_error_map = {
    "default": GetAgentCapabilityUnexpectedError,
}


class GetConfigError(KagentError):
    """Operation-local error for GetConfig."""

    response_error_map: dict[str, type[KagentError]] = {}


class GetConfigUnexpectedError(GetConfigError):
    """Operation-local response error for GetConfig (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


GetConfigError.response_error_map = {
    "default": GetConfigUnexpectedError,
}


class GetProvisioningTokenError(KagentError):
    """Operation-local error for GetProvisioningToken."""

    response_error_map: dict[str, type[KagentError]] = {}


class GetProvisioningTokenUnexpectedError(GetProvisioningTokenError):
    """Operation-local response error for GetProvisioningToken (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


GetProvisioningTokenError.response_error_map = {
    "default": GetProvisioningTokenUnexpectedError,
}


class ListAgentCapabilitiesError(KagentError):
    """Operation-local error for ListAgentCapabilities."""

    response_error_map: dict[str, type[KagentError]] = {}


class ListAgentCapabilitiesUnexpectedError(ListAgentCapabilitiesError):
    """Operation-local response error for ListAgentCapabilities (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


ListAgentCapabilitiesError.response_error_map = {
    "default": ListAgentCapabilitiesUnexpectedError,
}


class ListAgentsError(KagentError):
    """Operation-local error for ListAgents."""

    response_error_map: dict[str, type[KagentError]] = {}


class ListAgentsUnexpectedError(ListAgentsError):
    """Operation-local response error for ListAgents (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


ListAgentsError.response_error_map = {
    "default": ListAgentsUnexpectedError,
}


class ListAgentsByProvisioningTokenError(KagentError):
    """Operation-local error for ListAgentsByProvisioningToken."""

    response_error_map: dict[str, type[KagentError]] = {}


class ListAgentsByProvisioningTokenUnexpectedError(ListAgentsByProvisioningTokenError):
    """Operation-local response error for ListAgentsByProvisioningToken (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


ListAgentsByProvisioningTokenError.response_error_map = {
    "default": ListAgentsByProvisioningTokenUnexpectedError,
}


class ListProvisioningTokensError(KagentError):
    """Operation-local error for ListProvisioningTokens."""

    response_error_map: dict[str, type[KagentError]] = {}


class ListProvisioningTokensUnexpectedError(ListProvisioningTokensError):
    """Operation-local response error for ListProvisioningTokens (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


ListProvisioningTokensError.response_error_map = {
    "default": ListProvisioningTokensUnexpectedError,
}


class RevokeProvisioningTokenError(KagentError):
    """Operation-local error for RevokeProvisioningToken."""

    response_error_map: dict[str, type[KagentError]] = {}


class RevokeProvisioningTokenUnexpectedError(RevokeProvisioningTokenError):
    """Operation-local response error for RevokeProvisioningToken (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


RevokeProvisioningTokenError.response_error_map = {
    "default": RevokeProvisioningTokenUnexpectedError,
}


class UpdateAgentError(KagentError):
    """Operation-local error for UpdateAgent."""

    response_error_map: dict[str, type[KagentError]] = {}


class UpdateAgentUnexpectedError(UpdateAgentError):
    """Operation-local response error for UpdateAgent (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


UpdateAgentError.response_error_map = {
    "default": UpdateAgentUnexpectedError,
}


class UpdateConfigError(KagentError):
    """Operation-local error for UpdateConfig."""

    response_error_map: dict[str, type[KagentError]] = {}


class UpdateConfigUnexpectedError(UpdateConfigError):
    """Operation-local response error for UpdateConfig (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


UpdateConfigError.response_error_map = {
    "default": UpdateConfigUnexpectedError,
}


class UpsertAgentCapabilityError(KagentError):
    """Operation-local error for UpsertAgentCapability."""

    response_error_map: dict[str, type[KagentError]] = {}


class UpsertAgentCapabilityUnexpectedError(UpsertAgentCapabilityError):
    """Operation-local response error for UpsertAgentCapability (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


UpsertAgentCapabilityError.response_error_map = {
    "default": UpsertAgentCapabilityUnexpectedError,
}

ERROR_BY_OPERATION: dict[str, type[KagentError]] = {
    "Authorize": AuthorizeError,
    "CapabilityAdminService_CreateCapability": CapabilityAdminService_CreateCapabilityError,
    "CapabilityAdminService_DeleteCapability": CapabilityAdminService_DeleteCapabilityError,
    "CapabilityAdminService_GetCapability": CapabilityAdminService_GetCapabilityError,
    "CapabilityAdminService_ListCapabilities": CapabilityAdminService_ListCapabilitiesError,
    "CapabilityAdminService_UpdateCapability": CapabilityAdminService_UpdateCapabilityError,
    "CapabilityReleaseService_GetCapabilityLatestReleases": CapabilityReleaseService_GetCapabilityLatestReleasesError,
    "CapabilityReleaseService_GetCapabilityRelease": CapabilityReleaseService_GetCapabilityReleaseError,
    "CapabilityReleaseService_GetCapabilitySupportedDistros": CapabilityReleaseService_GetCapabilitySupportedDistrosError,
    "CreateAgent": CreateAgentError,
    "CreateConfig": CreateConfigError,
    "CreateProvisioningToken": CreateProvisioningTokenError,
    "DeleteAgent": DeleteAgentError,
    "DeleteAgentCapability": DeleteAgentCapabilityError,
    "DeleteConfig": DeleteConfigError,
    "GenerateInstallCommands": GenerateInstallCommandsError,
    "GetAgent": GetAgentError,
    "GetAgentCapability": GetAgentCapabilityError,
    "GetConfig": GetConfigError,
    "GetProvisioningToken": GetProvisioningTokenError,
    "ListAgentCapabilities": ListAgentCapabilitiesError,
    "ListAgents": ListAgentsError,
    "ListAgentsByProvisioningToken": ListAgentsByProvisioningTokenError,
    "ListProvisioningTokens": ListProvisioningTokensError,
    "RevokeProvisioningToken": RevokeProvisioningTokenError,
    "UpdateAgent": UpdateAgentError,
    "UpdateConfig": UpdateConfigError,
    "UpsertAgentCapability": UpsertAgentCapabilityError,
}

__all__ = [
    "KagentError",
    "AuthorizeUnexpectedError",
    "CapabilityAdminService_CreateCapabilityUnexpectedError",
    "CapabilityAdminService_DeleteCapabilityUnexpectedError",
    "CapabilityAdminService_GetCapabilityUnexpectedError",
    "CapabilityAdminService_ListCapabilitiesUnexpectedError",
    "CapabilityAdminService_UpdateCapabilityUnexpectedError",
    "CapabilityReleaseService_GetCapabilityLatestReleasesUnexpectedError",
    "CapabilityReleaseService_GetCapabilityReleaseUnexpectedError",
    "CapabilityReleaseService_GetCapabilitySupportedDistrosUnexpectedError",
    "CreateAgentUnexpectedError",
    "CreateConfigUnexpectedError",
    "CreateProvisioningTokenUnexpectedError",
    "DeleteAgentUnexpectedError",
    "DeleteAgentCapabilityUnexpectedError",
    "DeleteConfigUnexpectedError",
    "GenerateInstallCommandsUnexpectedError",
    "GetAgentUnexpectedError",
    "GetAgentCapabilityUnexpectedError",
    "GetConfigUnexpectedError",
    "GetProvisioningTokenUnexpectedError",
    "ListAgentCapabilitiesUnexpectedError",
    "ListAgentsUnexpectedError",
    "ListAgentsByProvisioningTokenUnexpectedError",
    "ListProvisioningTokensUnexpectedError",
    "RevokeProvisioningTokenUnexpectedError",
    "UpdateAgentUnexpectedError",
    "UpdateConfigUnexpectedError",
    "UpsertAgentCapabilityUnexpectedError",
    "AuthorizeError",
    "CapabilityAdminService_CreateCapabilityError",
    "CapabilityAdminService_DeleteCapabilityError",
    "CapabilityAdminService_GetCapabilityError",
    "CapabilityAdminService_ListCapabilitiesError",
    "CapabilityAdminService_UpdateCapabilityError",
    "CapabilityReleaseService_GetCapabilityLatestReleasesError",
    "CapabilityReleaseService_GetCapabilityReleaseError",
    "CapabilityReleaseService_GetCapabilitySupportedDistrosError",
    "CreateAgentError",
    "CreateConfigError",
    "CreateProvisioningTokenError",
    "DeleteAgentError",
    "DeleteAgentCapabilityError",
    "DeleteConfigError",
    "GenerateInstallCommandsError",
    "GetAgentError",
    "GetAgentCapabilityError",
    "GetConfigError",
    "GetProvisioningTokenError",
    "ListAgentCapabilitiesError",
    "ListAgentsError",
    "ListAgentsByProvisioningTokenError",
    "ListProvisioningTokensError",
    "RevokeProvisioningTokenError",
    "UpdateAgentError",
    "UpdateConfigError",
    "UpsertAgentCapabilityError",
    "ERROR_BY_OPERATION",
]
