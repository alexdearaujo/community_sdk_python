# AUTO-GENERATED: scripts/generation/error_package.py, generate_service_error_package()
# Rebuilt on every `make generate`. Do not edit by hand.

from __future__ import annotations

from typing import Any

from kentik_api.errors import HTTPException

from ..models import rpcStatus


class RbuxError(HTTPException):
    """Base service-local error for the rbux API."""

    @classmethod
    def _build_error(
        cls, response: Any, *, operation_name: str, method: str, path: str
    ) -> "RbuxError":
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
    ) -> "RbuxError":
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


class CreateScopeUnexpectedError(RbuxError):
    """Operation-local response error for CreateScope (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class CreateScopeError(RbuxError):
    """Operation-local error for CreateScope."""

    response_error_map = {
        "default": CreateScopeUnexpectedError,
    }


class DeleteScopeUnexpectedError(RbuxError):
    """Operation-local response error for DeleteScope (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class DeleteScopeError(RbuxError):
    """Operation-local error for DeleteScope."""

    response_error_map = {
        "default": DeleteScopeUnexpectedError,
    }


class GetScopeUnexpectedError(RbuxError):
    """Operation-local response error for GetScope (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class GetScopeError(RbuxError):
    """Operation-local error for GetScope."""

    response_error_map = {
        "default": GetScopeUnexpectedError,
    }


class ListScopesUnexpectedError(RbuxError):
    """Operation-local response error for ListScopes (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class ListScopesError(RbuxError):
    """Operation-local error for ListScopes."""

    response_error_map = {
        "default": ListScopesUnexpectedError,
    }


class UpdateScopeUnexpectedError(RbuxError):
    """Operation-local response error for UpdateScope (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class UpdateScopeError(RbuxError):
    """Operation-local error for UpdateScope."""

    response_error_map = {
        "default": UpdateScopeUnexpectedError,
    }


ERROR_BY_OPERATION: dict[str, type[RbuxError]] = {
    "CreateScope": CreateScopeError,
    "DeleteScope": DeleteScopeError,
    "GetScope": GetScopeError,
    "ListScopes": ListScopesError,
    "UpdateScope": UpdateScopeError,
}

__all__ = [
    "RbuxError",
    "CreateScopeUnexpectedError",
    "DeleteScopeUnexpectedError",
    "GetScopeUnexpectedError",
    "ListScopesUnexpectedError",
    "UpdateScopeUnexpectedError",
    "CreateScopeError",
    "DeleteScopeError",
    "GetScopeError",
    "ListScopesError",
    "UpdateScopeError",
    "ERROR_BY_OPERATION",
]
