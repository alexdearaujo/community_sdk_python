from __future__ import annotations

from typing import Any

from kentik_api.errors import HTTPException

from ..models import rpcStatus


class AlertingError(HTTPException):
    """Base service-local error for the alerting API."""

    @classmethod
    def _build_error(
        cls, response: Any, *, operation_name: str, method: str, path: str
    ) -> "AlertingError":
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
    ) -> "AlertingError":
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


class AckUnexpectedError(AlertingError):
    """Operation-local response error for Ack (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class AckError(AlertingError):
    """Operation-local error for Ack."""

    response_error_map = {
        "default": AckUnexpectedError,
    }


class ActUnexpectedError(AlertingError):
    """Operation-local response error for Act (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class ActError(AlertingError):
    """Operation-local error for Act."""

    response_error_map = {
        "default": ActUnexpectedError,
    }


class AddCommentUnexpectedError(AlertingError):
    """Operation-local response error for AddComment (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class AddCommentError(AlertingError):
    """Operation-local error for AddComment."""

    response_error_map = {
        "default": AddCommentUnexpectedError,
    }


class AvailableActionsUnexpectedError(AlertingError):
    """Operation-local response error for AvailableActions (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class AvailableActionsError(AlertingError):
    """Operation-local error for AvailableActions."""

    response_error_map = {
        "default": AvailableActionsUnexpectedError,
    }


class AvailableActionsForMitigationUnexpectedError(AlertingError):
    """Operation-local response error for AvailableActionsForMitigation (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class AvailableActionsForMitigationError(AlertingError):
    """Operation-local error for AvailableActionsForMitigation."""

    response_error_map = {
        "default": AvailableActionsForMitigationUnexpectedError,
    }


class ClearUnexpectedError(AlertingError):
    """Operation-local response error for Clear (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class ClearError(AlertingError):
    """Operation-local error for Clear."""

    response_error_map = {
        "default": ClearUnexpectedError,
    }


class CreateUnexpectedError(AlertingError):
    """Operation-local response error for Create (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class CreateError(AlertingError):
    """Operation-local error for Create."""

    response_error_map = {
        "default": CreateUnexpectedError,
    }


class DeleteUnexpectedError(AlertingError):
    """Operation-local response error for Delete (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class DeleteError(AlertingError):
    """Operation-local error for Delete."""

    response_error_map = {
        "default": DeleteUnexpectedError,
    }


class DisableUnexpectedError(AlertingError):
    """Operation-local response error for Disable (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class DisableError(AlertingError):
    """Operation-local error for Disable."""

    response_error_map = {
        "default": DisableUnexpectedError,
    }


class EnableUnexpectedError(AlertingError):
    """Operation-local response error for Enable (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class EnableError(AlertingError):
    """Operation-local error for Enable."""

    response_error_map = {
        "default": EnableUnexpectedError,
    }


class GetUnexpectedError(AlertingError):
    """Operation-local response error for Get (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class GetError(AlertingError):
    """Operation-local error for Get."""

    response_error_map = {
        "default": GetUnexpectedError,
    }


class ListUnexpectedError(AlertingError):
    """Operation-local response error for List (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class ListError(AlertingError):
    """Operation-local error for List."""

    response_error_map = {
        "default": ListUnexpectedError,
    }


class ListCommentsUnexpectedError(AlertingError):
    """Operation-local response error for ListComments (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class ListCommentsError(AlertingError):
    """Operation-local error for ListComments."""

    response_error_map = {
        "default": ListCommentsUnexpectedError,
    }


class ReplaceUnexpectedError(AlertingError):
    """Operation-local response error for Replace (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class ReplaceError(AlertingError):
    """Operation-local error for Replace."""

    response_error_map = {
        "default": ReplaceUnexpectedError,
    }


class SetExternalContextUnexpectedError(AlertingError):
    """Operation-local response error for SetExternalContext (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class SetExternalContextError(AlertingError):
    """Operation-local error for SetExternalContext."""

    response_error_map = {
        "default": SetExternalContextUnexpectedError,
    }


class UnAckUnexpectedError(AlertingError):
    """Operation-local response error for UnAck (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class UnAckError(AlertingError):
    """Operation-local error for UnAck."""

    response_error_map = {
        "default": UnAckUnexpectedError,
    }


ERROR_BY_OPERATION: dict[str, type[AlertingError]] = {
    "Ack": AckError,
    "Act": ActError,
    "AddComment": AddCommentError,
    "AvailableActions": AvailableActionsError,
    "AvailableActionsForMitigation": AvailableActionsForMitigationError,
    "Clear": ClearError,
    "Create": CreateError,
    "Delete": DeleteError,
    "Disable": DisableError,
    "Enable": EnableError,
    "Get": GetError,
    "List": ListError,
    "ListComments": ListCommentsError,
    "Replace": ReplaceError,
    "SetExternalContext": SetExternalContextError,
    "UnAck": UnAckError,
}

__all__ = [
    "AlertingError",
    "AckUnexpectedError",
    "ActUnexpectedError",
    "AddCommentUnexpectedError",
    "AvailableActionsUnexpectedError",
    "AvailableActionsForMitigationUnexpectedError",
    "ClearUnexpectedError",
    "CreateUnexpectedError",
    "DeleteUnexpectedError",
    "DisableUnexpectedError",
    "EnableUnexpectedError",
    "GetUnexpectedError",
    "ListUnexpectedError",
    "ListCommentsUnexpectedError",
    "ReplaceUnexpectedError",
    "SetExternalContextUnexpectedError",
    "UnAckUnexpectedError",
    "AckError",
    "ActError",
    "AddCommentError",
    "AvailableActionsError",
    "AvailableActionsForMitigationError",
    "ClearError",
    "CreateError",
    "DeleteError",
    "DisableError",
    "EnableError",
    "GetError",
    "ListError",
    "ListCommentsError",
    "ReplaceError",
    "SetExternalContextError",
    "UnAckError",
    "ERROR_BY_OPERATION",
]
