# AUTO-GENERATED: scripts/generation/error_package.py, generate_service_error_package()
# Rebuilt on every `make generate`. Do not edit by hand.

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


class GetNotificationChannelError(NotificationChannelError):
    """Operation-local error for client.notification_channel.get_notification_channel()."""

    response_error_map: dict[str, type[NotificationChannelError]] = {}


class GetNotificationChannelUnexpectedError(GetNotificationChannelError):
    """Operation-local response error for get_notification_channel (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


GetNotificationChannelError.response_error_map = {
    "default": GetNotificationChannelUnexpectedError,
}


class ListNotificationChannelsError(NotificationChannelError):
    """Operation-local error for client.notification_channel.list_notification_channels()."""

    response_error_map: dict[str, type[NotificationChannelError]] = {}


class ListNotificationChannelsUnexpectedError(ListNotificationChannelsError):
    """Operation-local response error for list_notification_channels (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


ListNotificationChannelsError.response_error_map = {
    "default": ListNotificationChannelsUnexpectedError,
}


class SearchNotificationChannelsError(NotificationChannelError):
    """Operation-local error for client.notification_channel.search_notification_channels()."""

    response_error_map: dict[str, type[NotificationChannelError]] = {}


class SearchNotificationChannelsUnexpectedError(SearchNotificationChannelsError):
    """Operation-local response error for search_notification_channels (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


SearchNotificationChannelsError.response_error_map = {
    "default": SearchNotificationChannelsUnexpectedError,
}

ERROR_BY_METHOD: dict[str, type[NotificationChannelError]] = {
    "get_notification_channel": GetNotificationChannelError,
    "list_notification_channels": ListNotificationChannelsError,
    "search_notification_channels": SearchNotificationChannelsError,
}

__all__ = [
    "NotificationChannelError",
    "GetNotificationChannelUnexpectedError",
    "ListNotificationChannelsUnexpectedError",
    "SearchNotificationChannelsUnexpectedError",
    "GetNotificationChannelError",
    "ListNotificationChannelsError",
    "SearchNotificationChannelsError",
    "ERROR_BY_METHOD",
]
