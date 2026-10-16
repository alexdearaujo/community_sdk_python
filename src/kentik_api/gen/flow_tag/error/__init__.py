# AUTO-GENERATED: scripts/generation/error_package.py, generate_service_error_package()
# Rebuilt on every `make generate`. Do not edit by hand.

from __future__ import annotations

from typing import Any

from kentik_api.errors import HTTPException

from ..models import rpcStatus


class FlowTagError(HTTPException):
    """Base service-local error for the flow_tag API."""

    @classmethod
    def _build_error(
        cls, response: Any, *, operation_name: str, method: str, path: str
    ) -> "FlowTagError":
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
    ) -> "FlowTagError":
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


class CreateFlowTagUnexpectedError(FlowTagError):
    """Operation-local response error for CreateFlowTag (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class CreateFlowTagError(FlowTagError):
    """Operation-local error for CreateFlowTag."""

    response_error_map = {
        "default": CreateFlowTagUnexpectedError,
    }


class DeleteFlowTagUnexpectedError(FlowTagError):
    """Operation-local response error for DeleteFlowTag (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class DeleteFlowTagError(FlowTagError):
    """Operation-local error for DeleteFlowTag."""

    response_error_map = {
        "default": DeleteFlowTagUnexpectedError,
    }


class GetFlowTagUnexpectedError(FlowTagError):
    """Operation-local response error for GetFlowTag (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class GetFlowTagError(FlowTagError):
    """Operation-local error for GetFlowTag."""

    response_error_map = {
        "default": GetFlowTagUnexpectedError,
    }


class SearchFlowTagUnexpectedError(FlowTagError):
    """Operation-local response error for SearchFlowTag (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class SearchFlowTagError(FlowTagError):
    """Operation-local error for SearchFlowTag."""

    response_error_map = {
        "default": SearchFlowTagUnexpectedError,
    }


class UpdateFlowTagUnexpectedError(FlowTagError):
    """Operation-local response error for UpdateFlowTag (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class UpdateFlowTagError(FlowTagError):
    """Operation-local error for UpdateFlowTag."""

    response_error_map = {
        "default": UpdateFlowTagUnexpectedError,
    }


ERROR_BY_OPERATION: dict[str, type[FlowTagError]] = {
    "CreateFlowTag": CreateFlowTagError,
    "DeleteFlowTag": DeleteFlowTagError,
    "GetFlowTag": GetFlowTagError,
    "SearchFlowTag": SearchFlowTagError,
    "UpdateFlowTag": UpdateFlowTagError,
}

__all__ = [
    "FlowTagError",
    "CreateFlowTagUnexpectedError",
    "DeleteFlowTagUnexpectedError",
    "GetFlowTagUnexpectedError",
    "SearchFlowTagUnexpectedError",
    "UpdateFlowTagUnexpectedError",
    "CreateFlowTagError",
    "DeleteFlowTagError",
    "GetFlowTagError",
    "SearchFlowTagError",
    "UpdateFlowTagError",
    "ERROR_BY_OPERATION",
]
