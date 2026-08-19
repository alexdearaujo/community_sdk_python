# AUTO-GENERATED: scripts/generation/error_package.py, generate_service_error_package()
# Rebuilt on every `make generate`. Do not edit by hand.

from __future__ import annotations

from typing import Any

from kentik_api.errors import HTTPException

from ..models import rpcStatus


class CustomApplicationError(HTTPException):
    """Base service-local error for the custom_application API."""

    @classmethod
    def _build_error(
        cls, response: Any, *, operation_name: str, method: str, path: str
    ) -> "CustomApplicationError":
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
    ) -> "CustomApplicationError":
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


class CreateCustomApplicationUnexpectedError(CustomApplicationError):
    """Operation-local response error for CreateCustomApplication (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class CreateCustomApplicationError(CustomApplicationError):
    """Operation-local error for CreateCustomApplication."""

    response_error_map = {
        "default": CreateCustomApplicationUnexpectedError,
    }


class DeleteCustomApplicationUnexpectedError(CustomApplicationError):
    """Operation-local response error for DeleteCustomApplication (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class DeleteCustomApplicationError(CustomApplicationError):
    """Operation-local error for DeleteCustomApplication."""

    response_error_map = {
        "default": DeleteCustomApplicationUnexpectedError,
    }


class GetCustomApplicationUnexpectedError(CustomApplicationError):
    """Operation-local response error for GetCustomApplication (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class GetCustomApplicationError(CustomApplicationError):
    """Operation-local error for GetCustomApplication."""

    response_error_map = {
        "default": GetCustomApplicationUnexpectedError,
    }


class ListCustomApplicationsUnexpectedError(CustomApplicationError):
    """Operation-local response error for ListCustomApplications (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class ListCustomApplicationsError(CustomApplicationError):
    """Operation-local error for ListCustomApplications."""

    response_error_map = {
        "default": ListCustomApplicationsUnexpectedError,
    }


class UpdateCustomApplicationUnexpectedError(CustomApplicationError):
    """Operation-local response error for UpdateCustomApplication (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class UpdateCustomApplicationError(CustomApplicationError):
    """Operation-local error for UpdateCustomApplication."""

    response_error_map = {
        "default": UpdateCustomApplicationUnexpectedError,
    }


ERROR_BY_OPERATION: dict[str, type[CustomApplicationError]] = {
    "CreateCustomApplication": CreateCustomApplicationError,
    "DeleteCustomApplication": DeleteCustomApplicationError,
    "GetCustomApplication": GetCustomApplicationError,
    "ListCustomApplications": ListCustomApplicationsError,
    "UpdateCustomApplication": UpdateCustomApplicationError,
}

__all__ = [
    "CustomApplicationError",
    "CreateCustomApplicationUnexpectedError",
    "DeleteCustomApplicationUnexpectedError",
    "GetCustomApplicationUnexpectedError",
    "ListCustomApplicationsUnexpectedError",
    "UpdateCustomApplicationUnexpectedError",
    "CreateCustomApplicationError",
    "DeleteCustomApplicationError",
    "GetCustomApplicationError",
    "ListCustomApplicationsError",
    "UpdateCustomApplicationError",
    "ERROR_BY_OPERATION",
]
