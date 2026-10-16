# AUTO-GENERATED: scripts/generation/error_package.py, generate_service_error_package()
# Rebuilt on every `make generate`. Do not edit by hand.

from __future__ import annotations

from typing import Any

from kentik_api.errors import HTTPException

from ..models import rpcStatus


class KmetaError(HTTPException):
    """Base service-local error for the kmeta API."""

    @classmethod
    def _build_error(
        cls, response: Any, *, operation_name: str, method: str, path: str
    ) -> "KmetaError":
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
    ) -> "KmetaError":
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


class CreateServiceNowConfigUnexpectedError(KmetaError):
    """Operation-local response error for CreateServiceNowConfig (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class CreateServiceNowConfigError(KmetaError):
    """Operation-local error for CreateServiceNowConfig."""

    response_error_map = {
        "default": CreateServiceNowConfigUnexpectedError,
    }


class DeleteServiceNowConfigUnexpectedError(KmetaError):
    """Operation-local response error for DeleteServiceNowConfig (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class DeleteServiceNowConfigError(KmetaError):
    """Operation-local error for DeleteServiceNowConfig."""

    response_error_map = {
        "default": DeleteServiceNowConfigUnexpectedError,
    }


class GetServiceNowConfigUnexpectedError(KmetaError):
    """Operation-local response error for GetServiceNowConfig (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class GetServiceNowConfigError(KmetaError):
    """Operation-local error for GetServiceNowConfig."""

    response_error_map = {
        "default": GetServiceNowConfigUnexpectedError,
    }


class ListServiceNowConfigsUnexpectedError(KmetaError):
    """Operation-local response error for ListServiceNowConfigs (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class ListServiceNowConfigsError(KmetaError):
    """Operation-local error for ListServiceNowConfigs."""

    response_error_map = {
        "default": ListServiceNowConfigsUnexpectedError,
    }


class UpdateServiceNowConfigUnexpectedError(KmetaError):
    """Operation-local response error for UpdateServiceNowConfig (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class UpdateServiceNowConfigError(KmetaError):
    """Operation-local error for UpdateServiceNowConfig."""

    response_error_map = {
        "default": UpdateServiceNowConfigUnexpectedError,
    }


ERROR_BY_OPERATION: dict[str, type[KmetaError]] = {
    "CreateServiceNowConfig": CreateServiceNowConfigError,
    "DeleteServiceNowConfig": DeleteServiceNowConfigError,
    "GetServiceNowConfig": GetServiceNowConfigError,
    "ListServiceNowConfigs": ListServiceNowConfigsError,
    "UpdateServiceNowConfig": UpdateServiceNowConfigError,
}

__all__ = [
    "KmetaError",
    "CreateServiceNowConfigUnexpectedError",
    "DeleteServiceNowConfigUnexpectedError",
    "GetServiceNowConfigUnexpectedError",
    "ListServiceNowConfigsUnexpectedError",
    "UpdateServiceNowConfigUnexpectedError",
    "CreateServiceNowConfigError",
    "DeleteServiceNowConfigError",
    "GetServiceNowConfigError",
    "ListServiceNowConfigsError",
    "UpdateServiceNowConfigError",
    "ERROR_BY_OPERATION",
]
