# AUTO-GENERATED: scripts/generation/error_package.py, generate_service_error_package()
# Rebuilt on every `make generate`. Do not edit by hand.

from __future__ import annotations

from typing import Any

from kentik_api.errors import HTTPException

from ..models import rpcStatus


class UserError(HTTPException):
    """Base service-local error for the user API."""

    @classmethod
    def _build_error(
        cls, response: Any, *, operation_name: str, method: str, path: str
    ) -> "UserError":
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
    ) -> "UserError":
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


class CreateUserUnexpectedError(UserError):
    """Operation-local response error for CreateUser (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class CreateUserError(UserError):
    """Operation-local error for CreateUser."""

    response_error_map = {
        "default": CreateUserUnexpectedError,
    }


class DeleteUserUnexpectedError(UserError):
    """Operation-local response error for DeleteUser (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class DeleteUserError(UserError):
    """Operation-local error for DeleteUser."""

    response_error_map = {
        "default": DeleteUserUnexpectedError,
    }


class GetUserUnexpectedError(UserError):
    """Operation-local response error for GetUser (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class GetUserError(UserError):
    """Operation-local error for GetUser."""

    response_error_map = {
        "default": GetUserUnexpectedError,
    }


class ListUsersUnexpectedError(UserError):
    """Operation-local response error for ListUsers (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class ListUsersError(UserError):
    """Operation-local error for ListUsers."""

    response_error_map = {
        "default": ListUsersUnexpectedError,
    }


class ResetActiveSessionsUnexpectedError(UserError):
    """Operation-local response error for ResetActiveSessions (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class ResetActiveSessionsError(UserError):
    """Operation-local error for ResetActiveSessions."""

    response_error_map = {
        "default": ResetActiveSessionsUnexpectedError,
    }


class ResetApiTokenUnexpectedError(UserError):
    """Operation-local response error for ResetApiToken (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class ResetApiTokenError(UserError):
    """Operation-local error for ResetApiToken."""

    response_error_map = {
        "default": ResetApiTokenUnexpectedError,
    }


class UpdateUserUnexpectedError(UserError):
    """Operation-local response error for UpdateUser (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class UpdateUserError(UserError):
    """Operation-local error for UpdateUser."""

    response_error_map = {
        "default": UpdateUserUnexpectedError,
    }


ERROR_BY_OPERATION: dict[str, type[UserError]] = {
    "CreateUser": CreateUserError,
    "DeleteUser": DeleteUserError,
    "GetUser": GetUserError,
    "ListUsers": ListUsersError,
    "ResetActiveSessions": ResetActiveSessionsError,
    "ResetApiToken": ResetApiTokenError,
    "UpdateUser": UpdateUserError,
}

__all__ = [
    "UserError",
    "CreateUserUnexpectedError",
    "DeleteUserUnexpectedError",
    "GetUserUnexpectedError",
    "ListUsersUnexpectedError",
    "ResetActiveSessionsUnexpectedError",
    "ResetApiTokenUnexpectedError",
    "UpdateUserUnexpectedError",
    "CreateUserError",
    "DeleteUserError",
    "GetUserError",
    "ListUsersError",
    "ResetActiveSessionsError",
    "ResetApiTokenError",
    "UpdateUserError",
    "ERROR_BY_OPERATION",
]
