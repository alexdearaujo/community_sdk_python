# AUTO-GENERATED: scripts/generation/error_package.py, generate_service_error_package()
# Rebuilt on every `make generate`. Do not edit by hand.

from __future__ import annotations

from typing import Any

from kentik_api.errors import HTTPException

from ..models import rpcStatus


class CredentialError(HTTPException):
    """Base service-local error for the credential API."""

    @classmethod
    def _build_error(
        cls, response: Any, *, operation_name: str, method: str, path: str
    ) -> "CredentialError":
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
    ) -> "CredentialError":
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


class GetGroupError(CredentialError):
    """Operation-local error for client.credential.get_group()."""

    response_error_map: dict[str, type[CredentialError]] = {}


class GetGroupUnexpectedError(GetGroupError):
    """Operation-local response error for get_group (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


GetGroupError.response_error_map = {
    "default": GetGroupUnexpectedError,
}


class ListGroupError(CredentialError):
    """Operation-local error for client.credential.list_group()."""

    response_error_map: dict[str, type[CredentialError]] = {}


class ListGroupUnexpectedError(ListGroupError):
    """Operation-local response error for list_group (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


ListGroupError.response_error_map = {
    "default": ListGroupUnexpectedError,
}

ERROR_BY_METHOD: dict[str, type[CredentialError]] = {
    "get_group": GetGroupError,
    "list_group": ListGroupError,
}

__all__ = [
    "CredentialError",
    "GetGroupUnexpectedError",
    "ListGroupUnexpectedError",
    "GetGroupError",
    "ListGroupError",
    "ERROR_BY_METHOD",
]
