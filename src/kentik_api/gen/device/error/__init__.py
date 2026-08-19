# AUTO-GENERATED: scripts/generation/error_package.py, generate_service_error_package()
# Rebuilt on every `make generate`. Do not edit by hand.

from __future__ import annotations

from typing import Any

from kentik_api.errors import HTTPException

from ..models import rpcStatus


class DeviceError(HTTPException):
    """Base service-local error for the device API."""

    @classmethod
    def _build_error(
        cls, response: Any, *, operation_name: str, method: str, path: str
    ) -> "DeviceError":
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
    ) -> "DeviceError":
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


class CreateDeviceUnexpectedError(DeviceError):
    """Operation-local response error for CreateDevice (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class CreateDeviceError(DeviceError):
    """Operation-local error for CreateDevice."""

    response_error_map = {
        "default": CreateDeviceUnexpectedError,
    }


class CreateDevicesUnexpectedError(DeviceError):
    """Operation-local response error for CreateDevices (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class CreateDevicesError(DeviceError):
    """Operation-local error for CreateDevices."""

    response_error_map = {
        "default": CreateDevicesUnexpectedError,
    }


class DeleteDeviceUnexpectedError(DeviceError):
    """Operation-local response error for DeleteDevice (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class DeleteDeviceError(DeviceError):
    """Operation-local error for DeleteDevice."""

    response_error_map = {
        "default": DeleteDeviceUnexpectedError,
    }


class DeleteDevicesUnexpectedError(DeviceError):
    """Operation-local response error for DeleteDevices (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class DeleteDevicesError(DeviceError):
    """Operation-local error for DeleteDevices."""

    response_error_map = {
        "default": DeleteDevicesUnexpectedError,
    }


class GetDeviceUnexpectedError(DeviceError):
    """Operation-local response error for GetDevice (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class GetDeviceError(DeviceError):
    """Operation-local error for GetDevice."""

    response_error_map = {
        "default": GetDeviceUnexpectedError,
    }


class GetDeviceByNameUnexpectedError(DeviceError):
    """Operation-local response error for GetDeviceByName (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class GetDeviceByNameError(DeviceError):
    """Operation-local error for GetDeviceByName."""

    response_error_map = {
        "default": GetDeviceByNameUnexpectedError,
    }


class ListDevicesUnexpectedError(DeviceError):
    """Operation-local response error for ListDevices (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class ListDevicesError(DeviceError):
    """Operation-local error for ListDevices."""

    response_error_map = {
        "default": ListDevicesUnexpectedError,
    }


class UpdateDeviceUnexpectedError(DeviceError):
    """Operation-local response error for UpdateDevice (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class UpdateDeviceError(DeviceError):
    """Operation-local error for UpdateDevice."""

    response_error_map = {
        "default": UpdateDeviceUnexpectedError,
    }


class UpdateDeviceLabelsUnexpectedError(DeviceError):
    """Operation-local response error for UpdateDeviceLabels (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class UpdateDeviceLabelsError(DeviceError):
    """Operation-local error for UpdateDeviceLabels."""

    response_error_map = {
        "default": UpdateDeviceLabelsUnexpectedError,
    }


class UpdateDevicesUnexpectedError(DeviceError):
    """Operation-local response error for UpdateDevices (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class UpdateDevicesError(DeviceError):
    """Operation-local error for UpdateDevices."""

    response_error_map = {
        "default": UpdateDevicesUnexpectedError,
    }


ERROR_BY_OPERATION: dict[str, type[DeviceError]] = {
    "CreateDevice": CreateDeviceError,
    "CreateDevices": CreateDevicesError,
    "DeleteDevice": DeleteDeviceError,
    "DeleteDevices": DeleteDevicesError,
    "GetDevice": GetDeviceError,
    "GetDeviceByName": GetDeviceByNameError,
    "ListDevices": ListDevicesError,
    "UpdateDevice": UpdateDeviceError,
    "UpdateDeviceLabels": UpdateDeviceLabelsError,
    "UpdateDevices": UpdateDevicesError,
}

__all__ = [
    "DeviceError",
    "CreateDeviceUnexpectedError",
    "CreateDevicesUnexpectedError",
    "DeleteDeviceUnexpectedError",
    "DeleteDevicesUnexpectedError",
    "GetDeviceUnexpectedError",
    "GetDeviceByNameUnexpectedError",
    "ListDevicesUnexpectedError",
    "UpdateDeviceUnexpectedError",
    "UpdateDeviceLabelsUnexpectedError",
    "UpdateDevicesUnexpectedError",
    "CreateDeviceError",
    "CreateDevicesError",
    "DeleteDeviceError",
    "DeleteDevicesError",
    "GetDeviceError",
    "GetDeviceByNameError",
    "ListDevicesError",
    "UpdateDeviceError",
    "UpdateDeviceLabelsError",
    "UpdateDevicesError",
    "ERROR_BY_OPERATION",
]
