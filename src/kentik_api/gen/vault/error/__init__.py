# AUTO-GENERATED: scripts/generation/error_package.py, generate_service_error_package()
# Rebuilt on every `make generate`. Do not edit by hand.

from __future__ import annotations

from typing import Any

from kentik_api.errors import HTTPException

from ..models import rpcStatus


class VaultError(HTTPException):
    """Base service-local error for the vault API."""

    @classmethod
    def _build_error(
        cls, response: Any, *, operation_name: str, method: str, path: str
    ) -> "VaultError":
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
    ) -> "VaultError":
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


class GetSecretUnexpectedError(VaultError):
    """Operation-local response error for GetSecret (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class GetSecretError(VaultError):
    """Operation-local error for GetSecret."""

    response_error_map = {
        "default": GetSecretUnexpectedError,
    }


class ListSecretUnexpectedError(VaultError):
    """Operation-local response error for ListSecret (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class ListSecretError(VaultError):
    """Operation-local error for ListSecret."""

    response_error_map = {
        "default": ListSecretUnexpectedError,
    }


ERROR_BY_OPERATION: dict[str, type[VaultError]] = {
    "GetSecret": GetSecretError,
    "ListSecret": ListSecretError,
}

__all__ = [
    "VaultError",
    "GetSecretUnexpectedError",
    "ListSecretUnexpectedError",
    "GetSecretError",
    "ListSecretError",
    "ERROR_BY_OPERATION",
]
