from __future__ import annotations

from typing import Any

from kentik_api.errors import HTTPException

from ..models import rpcStatus


class SavedFilterError(HTTPException):
    """Base service-local error for the saved_filter API."""

    @classmethod
    def _build_error(
        cls, response: Any, *, operation_name: str, method: str, path: str
    ) -> "SavedFilterError":
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
    ) -> "SavedFilterError":
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


class CreateSavedFilterUnexpectedError(SavedFilterError):
    """Operation-local response error for CreateSavedFilter (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class CreateSavedFilterError(SavedFilterError):
    """Operation-local error for CreateSavedFilter."""

    response_error_map = {
        "default": CreateSavedFilterUnexpectedError,
    }


class DeleteSavedFilterUnexpectedError(SavedFilterError):
    """Operation-local response error for DeleteSavedFilter (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class DeleteSavedFilterError(SavedFilterError):
    """Operation-local error for DeleteSavedFilter."""

    response_error_map = {
        "default": DeleteSavedFilterUnexpectedError,
    }


class GetSavedFilterUnexpectedError(SavedFilterError):
    """Operation-local response error for GetSavedFilter (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class GetSavedFilterError(SavedFilterError):
    """Operation-local error for GetSavedFilter."""

    response_error_map = {
        "default": GetSavedFilterUnexpectedError,
    }


class ListSavedFiltersUnexpectedError(SavedFilterError):
    """Operation-local response error for ListSavedFilters (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class ListSavedFiltersError(SavedFilterError):
    """Operation-local error for ListSavedFilters."""

    response_error_map = {
        "default": ListSavedFiltersUnexpectedError,
    }


class ListSavedFiltersAllUnexpectedError(SavedFilterError):
    """Operation-local response error for ListSavedFiltersAll (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class ListSavedFiltersAllError(SavedFilterError):
    """Operation-local error for ListSavedFiltersAll."""

    response_error_map = {
        "default": ListSavedFiltersAllUnexpectedError,
    }


class UpdateSavedFilterUnexpectedError(SavedFilterError):
    """Operation-local response error for UpdateSavedFilter (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class UpdateSavedFilterError(SavedFilterError):
    """Operation-local error for UpdateSavedFilter."""

    response_error_map = {
        "default": UpdateSavedFilterUnexpectedError,
    }


ERROR_BY_OPERATION: dict[str, type[SavedFilterError]] = {
    "CreateSavedFilter": CreateSavedFilterError,
    "DeleteSavedFilter": DeleteSavedFilterError,
    "GetSavedFilter": GetSavedFilterError,
    "ListSavedFilters": ListSavedFiltersError,
    "ListSavedFiltersAll": ListSavedFiltersAllError,
    "UpdateSavedFilter": UpdateSavedFilterError,
}

__all__ = [
    "SavedFilterError",
    "CreateSavedFilterUnexpectedError",
    "DeleteSavedFilterUnexpectedError",
    "GetSavedFilterUnexpectedError",
    "ListSavedFiltersUnexpectedError",
    "ListSavedFiltersAllUnexpectedError",
    "UpdateSavedFilterUnexpectedError",
    "CreateSavedFilterError",
    "DeleteSavedFilterError",
    "GetSavedFilterError",
    "ListSavedFiltersError",
    "ListSavedFiltersAllError",
    "UpdateSavedFilterError",
    "ERROR_BY_OPERATION",
]
