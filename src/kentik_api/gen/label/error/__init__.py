from __future__ import annotations

from typing import Any

from kentik_api.errors import HTTPException

from ..models import rpcStatus


class LabelError(HTTPException):
    """Base service-local error for the label API."""

    @classmethod
    def _build_error(
        cls, response: Any, *, operation_name: str, method: str, path: str
    ) -> "LabelError":
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
    ) -> "LabelError":
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


class CreateLabelUnexpectedError(LabelError):
    """Operation-local response error for CreateLabel (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class CreateLabelError(LabelError):
    """Operation-local error for CreateLabel."""

    response_error_map = {
        "default": CreateLabelUnexpectedError,
    }


class DeleteLabelUnexpectedError(LabelError):
    """Operation-local response error for DeleteLabel (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class DeleteLabelError(LabelError):
    """Operation-local error for DeleteLabel."""

    response_error_map = {
        "default": DeleteLabelUnexpectedError,
    }


class ListLabelsUnexpectedError(LabelError):
    """Operation-local response error for ListLabels (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class ListLabelsError(LabelError):
    """Operation-local error for ListLabels."""

    response_error_map = {
        "default": ListLabelsUnexpectedError,
    }


class UpdateLabelUnexpectedError(LabelError):
    """Operation-local response error for UpdateLabel (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class UpdateLabelError(LabelError):
    """Operation-local error for UpdateLabel."""

    response_error_map = {
        "default": UpdateLabelUnexpectedError,
    }


ERROR_BY_OPERATION: dict[str, type[LabelError]] = {
    "CreateLabel": CreateLabelError,
    "DeleteLabel": DeleteLabelError,
    "ListLabels": ListLabelsError,
    "UpdateLabel": UpdateLabelError,
}

__all__ = [
    "LabelError",
    "CreateLabelUnexpectedError",
    "DeleteLabelUnexpectedError",
    "ListLabelsUnexpectedError",
    "UpdateLabelUnexpectedError",
    "CreateLabelError",
    "DeleteLabelError",
    "ListLabelsError",
    "UpdateLabelError",
    "ERROR_BY_OPERATION",
]
