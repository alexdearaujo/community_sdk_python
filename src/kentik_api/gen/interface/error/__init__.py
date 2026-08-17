from __future__ import annotations

from typing import Any

from kentik_api.errors import HTTPException

from ..models import rpcStatus


class InterfaceError(HTTPException):
    """Base service-local error for the interface API."""

    @classmethod
    def _build_error(
        cls, response: Any, *, operation_name: str, method: str, path: str
    ) -> "InterfaceError":
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
    ) -> "InterfaceError":
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


class InterfaceCreateUnexpectedError(InterfaceError):
    """Operation-local response error for InterfaceCreate (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class InterfaceCreateError(InterfaceError):
    """Operation-local error for InterfaceCreate."""

    response_error_map = {
        "default": InterfaceCreateUnexpectedError,
    }


class InterfaceDeleteUnexpectedError(InterfaceError):
    """Operation-local response error for InterfaceDelete (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class InterfaceDeleteError(InterfaceError):
    """Operation-local error for InterfaceDelete."""

    response_error_map = {
        "default": InterfaceDeleteUnexpectedError,
    }


class InterfaceGetUnexpectedError(InterfaceError):
    """Operation-local response error for InterfaceGet (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class InterfaceGetError(InterfaceError):
    """Operation-local error for InterfaceGet."""

    response_error_map = {
        "default": InterfaceGetUnexpectedError,
    }


class InterfaceUpdateUnexpectedError(InterfaceError):
    """Operation-local response error for InterfaceUpdate (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class InterfaceUpdateError(InterfaceError):
    """Operation-local error for InterfaceUpdate."""

    response_error_map = {
        "default": InterfaceUpdateUnexpectedError,
    }


class ListInterfaceUnexpectedError(InterfaceError):
    """Operation-local response error for ListInterface (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class ListInterfaceError(InterfaceError):
    """Operation-local error for ListInterface."""

    response_error_map = {
        "default": ListInterfaceUnexpectedError,
    }


class ManualClassifyUnexpectedError(InterfaceError):
    """Operation-local response error for ManualClassify (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class ManualClassifyError(InterfaceError):
    """Operation-local error for ManualClassify."""

    response_error_map = {
        "default": ManualClassifyUnexpectedError,
    }


ERROR_BY_OPERATION: dict[str, type[InterfaceError]] = {
    "InterfaceCreate": InterfaceCreateError,
    "InterfaceDelete": InterfaceDeleteError,
    "InterfaceGet": InterfaceGetError,
    "InterfaceUpdate": InterfaceUpdateError,
    "ListInterface": ListInterfaceError,
    "ManualClassify": ManualClassifyError,
}

__all__ = [
    "InterfaceError",
    "InterfaceCreateUnexpectedError",
    "InterfaceDeleteUnexpectedError",
    "InterfaceGetUnexpectedError",
    "InterfaceUpdateUnexpectedError",
    "ListInterfaceUnexpectedError",
    "ManualClassifyUnexpectedError",
    "InterfaceCreateError",
    "InterfaceDeleteError",
    "InterfaceGetError",
    "InterfaceUpdateError",
    "ListInterfaceError",
    "ManualClassifyError",
    "ERROR_BY_OPERATION",
]
