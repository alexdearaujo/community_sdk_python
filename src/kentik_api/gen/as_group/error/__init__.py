# AUTO-GENERATED: scripts/generation/error_package.py, generate_service_error_package()
# Rebuilt on every `make generate`. Do not edit by hand.

from __future__ import annotations

from typing import Any

from kentik_api.errors import HTTPException

from ..models import rpcStatus


class AsGroupError(HTTPException):
    """Base service-local error for the as_group API."""

    @classmethod
    def _build_error(
        cls, response: Any, *, operation_name: str, method: str, path: str
    ) -> "AsGroupError":
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
    ) -> "AsGroupError":
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


class CreateASGroupUnexpectedError(AsGroupError):
    """Operation-local response error for CreateASGroup (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class CreateASGroupError(AsGroupError):
    """Operation-local error for CreateASGroup."""

    response_error_map = {
        "default": CreateASGroupUnexpectedError,
    }


class DeleteASGroupUnexpectedError(AsGroupError):
    """Operation-local response error for DeleteASGroup (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class DeleteASGroupError(AsGroupError):
    """Operation-local error for DeleteASGroup."""

    response_error_map = {
        "default": DeleteASGroupUnexpectedError,
    }


class GetASGroupUnexpectedError(AsGroupError):
    """Operation-local response error for GetASGroup (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class GetASGroupError(AsGroupError):
    """Operation-local error for GetASGroup."""

    response_error_map = {
        "default": GetASGroupUnexpectedError,
    }


class ListASGroupsUnexpectedError(AsGroupError):
    """Operation-local response error for ListASGroups (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class ListASGroupsError(AsGroupError):
    """Operation-local error for ListASGroups."""

    response_error_map = {
        "default": ListASGroupsUnexpectedError,
    }


class UpdateASGroupUnexpectedError(AsGroupError):
    """Operation-local response error for UpdateASGroup (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class UpdateASGroupError(AsGroupError):
    """Operation-local error for UpdateASGroup."""

    response_error_map = {
        "default": UpdateASGroupUnexpectedError,
    }


ERROR_BY_OPERATION: dict[str, type[AsGroupError]] = {
    "CreateASGroup": CreateASGroupError,
    "DeleteASGroup": DeleteASGroupError,
    "GetASGroup": GetASGroupError,
    "ListASGroups": ListASGroupsError,
    "UpdateASGroup": UpdateASGroupError,
}

__all__ = [
    "AsGroupError",
    "CreateASGroupUnexpectedError",
    "DeleteASGroupUnexpectedError",
    "GetASGroupUnexpectedError",
    "ListASGroupsUnexpectedError",
    "UpdateASGroupUnexpectedError",
    "CreateASGroupError",
    "DeleteASGroupError",
    "GetASGroupError",
    "ListASGroupsError",
    "UpdateASGroupError",
    "ERROR_BY_OPERATION",
]
