# AUTO-GENERATED: scripts/generation/error_package.py, generate_service_error_package()
# Rebuilt on every `make generate`. Do not edit by hand.

from __future__ import annotations

from typing import Any

from kentik_api.errors import HTTPException

from ..models import rpcStatus


class BgpMonitoringError(HTTPException):
    """Base service-local error for the bgp_monitoring API."""

    @classmethod
    def _build_error(
        cls, response: Any, *, operation_name: str, method: str, path: str
    ) -> "BgpMonitoringError":
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
    ) -> "BgpMonitoringError":
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


class CreateMonitorUnexpectedError(BgpMonitoringError):
    """Operation-local response error for CreateMonitor (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class CreateMonitorError(BgpMonitoringError):
    """Operation-local error for CreateMonitor."""

    response_error_map = {
        "default": CreateMonitorUnexpectedError,
    }


class DeleteMonitorUnexpectedError(BgpMonitoringError):
    """Operation-local response error for DeleteMonitor (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class DeleteMonitorError(BgpMonitoringError):
    """Operation-local error for DeleteMonitor."""

    response_error_map = {
        "default": DeleteMonitorUnexpectedError,
    }


class GetMetricsForTargetUnexpectedError(BgpMonitoringError):
    """Operation-local response error for GetMetricsForTarget (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class GetMetricsForTargetError(BgpMonitoringError):
    """Operation-local error for GetMetricsForTarget."""

    response_error_map = {
        "default": GetMetricsForTargetUnexpectedError,
    }


class GetMonitorUnexpectedError(BgpMonitoringError):
    """Operation-local response error for GetMonitor (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class GetMonitorError(BgpMonitoringError):
    """Operation-local error for GetMonitor."""

    response_error_map = {
        "default": GetMonitorUnexpectedError,
    }


class GetRoutesForTargetUnexpectedError(BgpMonitoringError):
    """Operation-local response error for GetRoutesForTarget (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class GetRoutesForTargetError(BgpMonitoringError):
    """Operation-local error for GetRoutesForTarget."""

    response_error_map = {
        "default": GetRoutesForTargetUnexpectedError,
    }


class ListMonitorsUnexpectedError(BgpMonitoringError):
    """Operation-local response error for ListMonitors (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class ListMonitorsError(BgpMonitoringError):
    """Operation-local error for ListMonitors."""

    response_error_map = {
        "default": ListMonitorsUnexpectedError,
    }


class SetMonitorStatusUnexpectedError(BgpMonitoringError):
    """Operation-local response error for SetMonitorStatus (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class SetMonitorStatusError(BgpMonitoringError):
    """Operation-local error for SetMonitorStatus."""

    response_error_map = {
        "default": SetMonitorStatusUnexpectedError,
    }


class UpdateMonitorUnexpectedError(BgpMonitoringError):
    """Operation-local response error for UpdateMonitor (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class UpdateMonitorError(BgpMonitoringError):
    """Operation-local error for UpdateMonitor."""

    response_error_map = {
        "default": UpdateMonitorUnexpectedError,
    }


ERROR_BY_OPERATION: dict[str, type[BgpMonitoringError]] = {
    "CreateMonitor": CreateMonitorError,
    "DeleteMonitor": DeleteMonitorError,
    "GetMetricsForTarget": GetMetricsForTargetError,
    "GetMonitor": GetMonitorError,
    "GetRoutesForTarget": GetRoutesForTargetError,
    "ListMonitors": ListMonitorsError,
    "SetMonitorStatus": SetMonitorStatusError,
    "UpdateMonitor": UpdateMonitorError,
}

__all__ = [
    "BgpMonitoringError",
    "CreateMonitorUnexpectedError",
    "DeleteMonitorUnexpectedError",
    "GetMetricsForTargetUnexpectedError",
    "GetMonitorUnexpectedError",
    "GetRoutesForTargetUnexpectedError",
    "ListMonitorsUnexpectedError",
    "SetMonitorStatusUnexpectedError",
    "UpdateMonitorUnexpectedError",
    "CreateMonitorError",
    "DeleteMonitorError",
    "GetMetricsForTargetError",
    "GetMonitorError",
    "GetRoutesForTargetError",
    "ListMonitorsError",
    "SetMonitorStatusError",
    "UpdateMonitorError",
    "ERROR_BY_OPERATION",
]
