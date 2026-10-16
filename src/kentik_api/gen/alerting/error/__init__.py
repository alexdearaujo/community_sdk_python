# AUTO-GENERATED: scripts/generation/error_package.py, generate_service_error_package()
# Rebuilt on every `make generate`. Do not edit by hand.

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


class AckError(AlertingError):
    """Operation-local error for Ack."""

    response_error_map: dict[str, type[AlertingError]] = {}


class AckUnexpectedError(AckError):
    """Operation-local response error for Ack (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


AckError.response_error_map = {
    "default": AckUnexpectedError,
}


class ActError(AlertingError):
    """Operation-local error for Act."""

    response_error_map: dict[str, type[AlertingError]] = {}


class ActUnexpectedError(ActError):
    """Operation-local response error for Act (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


ActError.response_error_map = {
    "default": ActUnexpectedError,
}


class AddCommentError(AlertingError):
    """Operation-local error for AddComment."""

    response_error_map: dict[str, type[AlertingError]] = {}


class AddCommentUnexpectedError(AddCommentError):
    """Operation-local response error for AddComment (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


AddCommentError.response_error_map = {
    "default": AddCommentUnexpectedError,
}


class AvailableActionsError(AlertingError):
    """Operation-local error for AvailableActions."""

    response_error_map: dict[str, type[AlertingError]] = {}


class AvailableActionsUnexpectedError(AvailableActionsError):
    """Operation-local response error for AvailableActions (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


AvailableActionsError.response_error_map = {
    "default": AvailableActionsUnexpectedError,
}


class AvailableActionsForMitigationError(AlertingError):
    """Operation-local error for AvailableActionsForMitigation."""

    response_error_map: dict[str, type[AlertingError]] = {}


class AvailableActionsForMitigationUnexpectedError(AvailableActionsForMitigationError):
    """Operation-local response error for AvailableActionsForMitigation (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


AvailableActionsForMitigationError.response_error_map = {
    "default": AvailableActionsForMitigationUnexpectedError,
}


class ClearError(AlertingError):
    """Operation-local error for Clear."""

    response_error_map: dict[str, type[AlertingError]] = {}


class ClearUnexpectedError(ClearError):
    """Operation-local response error for Clear (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


ClearError.response_error_map = {
    "default": ClearUnexpectedError,
}


class CreateError(AlertingError):
    """Operation-local error for Create."""

    response_error_map: dict[str, type[AlertingError]] = {}


class CreateUnexpectedError(CreateError):
    """Operation-local response error for Create (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


CreateError.response_error_map = {
    "default": CreateUnexpectedError,
}


class DeleteError(AlertingError):
    """Operation-local error for Delete."""

    response_error_map: dict[str, type[AlertingError]] = {}


class DeleteUnexpectedError(DeleteError):
    """Operation-local response error for Delete (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


DeleteError.response_error_map = {
    "default": DeleteUnexpectedError,
}


class DisableError(AlertingError):
    """Operation-local error for Disable."""

    response_error_map: dict[str, type[AlertingError]] = {}


class DisableUnexpectedError(DisableError):
    """Operation-local response error for Disable (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


DisableError.response_error_map = {
    "default": DisableUnexpectedError,
}


class EnableError(AlertingError):
    """Operation-local error for Enable."""

    response_error_map: dict[str, type[AlertingError]] = {}


class EnableUnexpectedError(EnableError):
    """Operation-local response error for Enable (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


EnableError.response_error_map = {
    "default": EnableUnexpectedError,
}


class GetError(AlertingError):
    """Operation-local error for Get."""

    response_error_map: dict[str, type[AlertingError]] = {}


class GetUnexpectedError(GetError):
    """Operation-local response error for Get (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


GetError.response_error_map = {
    "default": GetUnexpectedError,
}


class ListError(AlertingError):
    """Operation-local error for List."""

    response_error_map: dict[str, type[AlertingError]] = {}


class ListUnexpectedError(ListError):
    """Operation-local response error for List (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


ListError.response_error_map = {
    "default": ListUnexpectedError,
}


class ListCommentsError(AlertingError):
    """Operation-local error for ListComments."""

    response_error_map: dict[str, type[AlertingError]] = {}


class ListCommentsUnexpectedError(ListCommentsError):
    """Operation-local response error for ListComments (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


ListCommentsError.response_error_map = {
    "default": ListCommentsUnexpectedError,
}


class ReplaceError(AlertingError):
    """Operation-local error for Replace."""

    response_error_map: dict[str, type[AlertingError]] = {}


class ReplaceUnexpectedError(ReplaceError):
    """Operation-local response error for Replace (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


ReplaceError.response_error_map = {
    "default": ReplaceUnexpectedError,
}


class SetExternalContextError(AlertingError):
    """Operation-local error for SetExternalContext."""

    response_error_map: dict[str, type[AlertingError]] = {}


class SetExternalContextUnexpectedError(SetExternalContextError):
    """Operation-local response error for SetExternalContext (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


SetExternalContextError.response_error_map = {
    "default": SetExternalContextUnexpectedError,
}


class UnAckError(AlertingError):
    """Operation-local error for UnAck."""

    response_error_map: dict[str, type[AlertingError]] = {}


class UnAckUnexpectedError(UnAckError):
    """Operation-local response error for UnAck (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


UnAckError.response_error_map = {
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
