from __future__ import annotations

from typing import Any

from kentik_api.errors import HTTPException

from ..models import rpcStatus


class NotificationChannelError(HTTPException):
    """Base service-local error for the notification_channel API."""

    @classmethod
    def _build_error(
        cls, response: Any, *, operation_name: str, method: str, path: str
    ) -> "NotificationChannelError":
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
    ) -> "NotificationChannelError":
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


class GetNotificationChannelUnexpectedError(NotificationChannelError):
    """Operation-local response error for GetNotificationChannel (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class GetNotificationChannelError(NotificationChannelError):
    """Operation-local error for GetNotificationChannel."""

    response_error_map = {
        "default": GetNotificationChannelUnexpectedError,
    }


class ListNotificationChannelsUnexpectedError(NotificationChannelError):
    """Operation-local response error for ListNotificationChannels (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class ListNotificationChannelsError(NotificationChannelError):
    """Operation-local error for ListNotificationChannels."""

    response_error_map = {
        "default": ListNotificationChannelsUnexpectedError,
    }


class SearchNotificationChannelsUnexpectedError(NotificationChannelError):
    """Operation-local response error for SearchNotificationChannels (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class SearchNotificationChannelsError(NotificationChannelError):
    """Operation-local error for SearchNotificationChannels."""

    response_error_map = {
        "default": SearchNotificationChannelsUnexpectedError,
    }


ERROR_BY_OPERATION: dict[str, type[NotificationChannelError]] = {
    "GetNotificationChannel": GetNotificationChannelError,
    "ListNotificationChannels": ListNotificationChannelsError,
    "SearchNotificationChannels": SearchNotificationChannelsError,
}

__all__ = [
    "NotificationChannelError",
    "GetNotificationChannelUnexpectedError",
    "ListNotificationChannelsUnexpectedError",
    "SearchNotificationChannelsUnexpectedError",
    "GetNotificationChannelError",
    "ListNotificationChannelsError",
    "SearchNotificationChannelsError",
    "ERROR_BY_OPERATION",
]
