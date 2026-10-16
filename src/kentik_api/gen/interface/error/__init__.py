# AUTO-GENERATED: scripts/generation/error_package.py, generate_service_error_package()
# Rebuilt on every `make generate`. Do not edit by hand.

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


class InterfaceCreateError(InterfaceError):
    """Operation-local error for client.interface.interface_create()."""

    response_error_map: dict[str, type[InterfaceError]] = {}


class InterfaceCreateUnexpectedError(InterfaceCreateError):
    """Operation-local response error for interface_create (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


InterfaceCreateError.response_error_map = {
    "default": InterfaceCreateUnexpectedError,
}


class InterfaceDeleteError(InterfaceError):
    """Operation-local error for client.interface.interface_delete()."""

    response_error_map: dict[str, type[InterfaceError]] = {}


class InterfaceDeleteUnexpectedError(InterfaceDeleteError):
    """Operation-local response error for interface_delete (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


InterfaceDeleteError.response_error_map = {
    "default": InterfaceDeleteUnexpectedError,
}


class InterfaceGetError(InterfaceError):
    """Operation-local error for client.interface.interface_get()."""

    response_error_map: dict[str, type[InterfaceError]] = {}


class InterfaceGetUnexpectedError(InterfaceGetError):
    """Operation-local response error for interface_get (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


InterfaceGetError.response_error_map = {
    "default": InterfaceGetUnexpectedError,
}


class InterfaceUpdateError(InterfaceError):
    """Operation-local error for client.interface.interface_update()."""

    response_error_map: dict[str, type[InterfaceError]] = {}


class InterfaceUpdateUnexpectedError(InterfaceUpdateError):
    """Operation-local response error for interface_update (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


InterfaceUpdateError.response_error_map = {
    "default": InterfaceUpdateUnexpectedError,
}


class ListInterfaceError(InterfaceError):
    """Operation-local error for client.interface.list_interface()."""

    response_error_map: dict[str, type[InterfaceError]] = {}


class ListInterfaceUnexpectedError(ListInterfaceError):
    """Operation-local response error for list_interface (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


ListInterfaceError.response_error_map = {
    "default": ListInterfaceUnexpectedError,
}


class ManualClassifyError(InterfaceError):
    """Operation-local error for client.interface.manual_classify()."""

    response_error_map: dict[str, type[InterfaceError]] = {}


class ManualClassifyUnexpectedError(ManualClassifyError):
    """Operation-local response error for manual_classify (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


ManualClassifyError.response_error_map = {
    "default": ManualClassifyUnexpectedError,
}

ERROR_BY_METHOD: dict[str, type[InterfaceError]] = {
    "interface_create": InterfaceCreateError,
    "interface_delete": InterfaceDeleteError,
    "interface_get": InterfaceGetError,
    "interface_update": InterfaceUpdateError,
    "list_interface": ListInterfaceError,
    "manual_classify": ManualClassifyError,
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
    "ERROR_BY_METHOD",
]
