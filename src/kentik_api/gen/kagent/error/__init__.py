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
                details["rpc_status"] = status.model_dump()
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


class AuthorizeUnexpectedError(KagentError):
    """Operation-local response error for Authorize (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class AuthorizeError(KagentError):
    """Operation-local error for Authorize."""

    response_error_map = {
        "default": AuthorizeUnexpectedError,
    }


class CapabilityAdminService_CreateCapabilityUnexpectedError(KagentError):
    """Operation-local response error for CapabilityAdminService_CreateCapability (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class CapabilityAdminService_CreateCapabilityError(KagentError):
    """Operation-local error for CapabilityAdminService_CreateCapability."""

    response_error_map = {
        "default": CapabilityAdminService_CreateCapabilityUnexpectedError,
    }


class CapabilityAdminService_DeleteCapabilityUnexpectedError(KagentError):
    """Operation-local response error for CapabilityAdminService_DeleteCapability (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class CapabilityAdminService_DeleteCapabilityError(KagentError):
    """Operation-local error for CapabilityAdminService_DeleteCapability."""

    response_error_map = {
        "default": CapabilityAdminService_DeleteCapabilityUnexpectedError,
    }


class CapabilityAdminService_GetCapabilityUnexpectedError(KagentError):
    """Operation-local response error for CapabilityAdminService_GetCapability (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class CapabilityAdminService_GetCapabilityError(KagentError):
    """Operation-local error for CapabilityAdminService_GetCapability."""

    response_error_map = {
        "default": CapabilityAdminService_GetCapabilityUnexpectedError,
    }


class CapabilityAdminService_ListCapabilitiesUnexpectedError(KagentError):
    """Operation-local response error for CapabilityAdminService_ListCapabilities (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class CapabilityAdminService_ListCapabilitiesError(KagentError):
    """Operation-local error for CapabilityAdminService_ListCapabilities."""

    response_error_map = {
        "default": CapabilityAdminService_ListCapabilitiesUnexpectedError,
    }


class CapabilityAdminService_UpdateCapabilityUnexpectedError(KagentError):
    """Operation-local response error for CapabilityAdminService_UpdateCapability (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class CapabilityAdminService_UpdateCapabilityError(KagentError):
    """Operation-local error for CapabilityAdminService_UpdateCapability."""

    response_error_map = {
        "default": CapabilityAdminService_UpdateCapabilityUnexpectedError,
    }


class CapabilityReleaseService_GetCapabilityLatestReleasesUnexpectedError(KagentError):
    """Operation-local response error for CapabilityReleaseService_GetCapabilityLatestReleases (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class CapabilityReleaseService_GetCapabilityLatestReleasesError(KagentError):
    """Operation-local error for CapabilityReleaseService_GetCapabilityLatestReleases."""

    response_error_map = {
        "default": CapabilityReleaseService_GetCapabilityLatestReleasesUnexpectedError,
    }


class CapabilityReleaseService_GetCapabilityReleaseUnexpectedError(KagentError):
    """Operation-local response error for CapabilityReleaseService_GetCapabilityRelease (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class CapabilityReleaseService_GetCapabilityReleaseError(KagentError):
    """Operation-local error for CapabilityReleaseService_GetCapabilityRelease."""

    response_error_map = {
        "default": CapabilityReleaseService_GetCapabilityReleaseUnexpectedError,
    }


class CapabilityReleaseService_GetCapabilitySupportedDistrosUnexpectedError(
    KagentError
):
    """Operation-local response error for CapabilityReleaseService_GetCapabilitySupportedDistros (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class CapabilityReleaseService_GetCapabilitySupportedDistrosError(KagentError):
    """Operation-local error for CapabilityReleaseService_GetCapabilitySupportedDistros."""

    response_error_map = {
        "default": CapabilityReleaseService_GetCapabilitySupportedDistrosUnexpectedError,
    }


class CreateAgentUnexpectedError(KagentError):
    """Operation-local response error for CreateAgent (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class CreateAgentError(KagentError):
    """Operation-local error for CreateAgent."""

    response_error_map = {
        "default": CreateAgentUnexpectedError,
    }


class CreateConfigUnexpectedError(KagentError):
    """Operation-local response error for CreateConfig (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class CreateConfigError(KagentError):
    """Operation-local error for CreateConfig."""

    response_error_map = {
        "default": CreateConfigUnexpectedError,
    }


class CreateProvisioningTokenUnexpectedError(KagentError):
    """Operation-local response error for CreateProvisioningToken (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class CreateProvisioningTokenError(KagentError):
    """Operation-local error for CreateProvisioningToken."""

    response_error_map = {
        "default": CreateProvisioningTokenUnexpectedError,
    }


class DeleteAgentUnexpectedError(KagentError):
    """Operation-local response error for DeleteAgent (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class DeleteAgentError(KagentError):
    """Operation-local error for DeleteAgent."""

    response_error_map = {
        "default": DeleteAgentUnexpectedError,
    }


class DeleteAgentCapabilityUnexpectedError(KagentError):
    """Operation-local response error for DeleteAgentCapability (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class DeleteAgentCapabilityError(KagentError):
    """Operation-local error for DeleteAgentCapability."""

    response_error_map = {
        "default": DeleteAgentCapabilityUnexpectedError,
    }


class DeleteConfigUnexpectedError(KagentError):
    """Operation-local response error for DeleteConfig (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class DeleteConfigError(KagentError):
    """Operation-local error for DeleteConfig."""

    response_error_map = {
        "default": DeleteConfigUnexpectedError,
    }


class GenerateInstallCommandsUnexpectedError(KagentError):
    """Operation-local response error for GenerateInstallCommands (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class GenerateInstallCommandsError(KagentError):
    """Operation-local error for GenerateInstallCommands."""

    response_error_map = {
        "default": GenerateInstallCommandsUnexpectedError,
    }


class GetAgentUnexpectedError(KagentError):
    """Operation-local response error for GetAgent (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class GetAgentError(KagentError):
    """Operation-local error for GetAgent."""

    response_error_map = {
        "default": GetAgentUnexpectedError,
    }


class GetAgentCapabilityUnexpectedError(KagentError):
    """Operation-local response error for GetAgentCapability (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class GetAgentCapabilityError(KagentError):
    """Operation-local error for GetAgentCapability."""

    response_error_map = {
        "default": GetAgentCapabilityUnexpectedError,
    }


class GetConfigUnexpectedError(KagentError):
    """Operation-local response error for GetConfig (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class GetConfigError(KagentError):
    """Operation-local error for GetConfig."""

    response_error_map = {
        "default": GetConfigUnexpectedError,
    }


class GetProvisioningTokenUnexpectedError(KagentError):
    """Operation-local response error for GetProvisioningToken (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class GetProvisioningTokenError(KagentError):
    """Operation-local error for GetProvisioningToken."""

    response_error_map = {
        "default": GetProvisioningTokenUnexpectedError,
    }


class ListAgentCapabilitiesUnexpectedError(KagentError):
    """Operation-local response error for ListAgentCapabilities (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class ListAgentCapabilitiesError(KagentError):
    """Operation-local error for ListAgentCapabilities."""

    response_error_map = {
        "default": ListAgentCapabilitiesUnexpectedError,
    }


class ListAgentsUnexpectedError(KagentError):
    """Operation-local response error for ListAgents (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class ListAgentsError(KagentError):
    """Operation-local error for ListAgents."""

    response_error_map = {
        "default": ListAgentsUnexpectedError,
    }


class ListAgentsByProvisioningTokenUnexpectedError(KagentError):
    """Operation-local response error for ListAgentsByProvisioningToken (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class ListAgentsByProvisioningTokenError(KagentError):
    """Operation-local error for ListAgentsByProvisioningToken."""

    response_error_map = {
        "default": ListAgentsByProvisioningTokenUnexpectedError,
    }


class ListProvisioningTokensUnexpectedError(KagentError):
    """Operation-local response error for ListProvisioningTokens (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class ListProvisioningTokensError(KagentError):
    """Operation-local error for ListProvisioningTokens."""

    response_error_map = {
        "default": ListProvisioningTokensUnexpectedError,
    }


class RevokeProvisioningTokenUnexpectedError(KagentError):
    """Operation-local response error for RevokeProvisioningToken (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class RevokeProvisioningTokenError(KagentError):
    """Operation-local error for RevokeProvisioningToken."""

    response_error_map = {
        "default": RevokeProvisioningTokenUnexpectedError,
    }


class UpdateAgentUnexpectedError(KagentError):
    """Operation-local response error for UpdateAgent (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class UpdateAgentError(KagentError):
    """Operation-local error for UpdateAgent."""

    response_error_map = {
        "default": UpdateAgentUnexpectedError,
    }


class UpdateConfigUnexpectedError(KagentError):
    """Operation-local response error for UpdateConfig (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class UpdateConfigError(KagentError):
    """Operation-local error for UpdateConfig."""

    response_error_map = {
        "default": UpdateConfigUnexpectedError,
    }


class UpsertAgentCapabilityUnexpectedError(KagentError):
    """Operation-local response error for UpsertAgentCapability (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class UpsertAgentCapabilityError(KagentError):
    """Operation-local error for UpsertAgentCapability."""

    response_error_map = {
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
