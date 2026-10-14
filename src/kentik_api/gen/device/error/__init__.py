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


class CreateDeviceError(DeviceError):
    """Operation-local error for CreateDevice."""

    response_error_map: dict[str, type[DeviceError]] = {}


class CreateDeviceUnexpectedError(CreateDeviceError):
    """Operation-local response error for CreateDevice (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


CreateDeviceError.response_error_map = {
    "default": CreateDeviceUnexpectedError,
}


class CreateDevicesError(DeviceError):
    """Operation-local error for CreateDevices."""

    response_error_map: dict[str, type[DeviceError]] = {}


class CreateDevicesUnexpectedError(CreateDevicesError):
    """Operation-local response error for CreateDevices (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


CreateDevicesError.response_error_map = {
    "default": CreateDevicesUnexpectedError,
}


class DeleteDeviceError(DeviceError):
    """Operation-local error for DeleteDevice."""

    response_error_map: dict[str, type[DeviceError]] = {}


class DeleteDeviceUnexpectedError(DeleteDeviceError):
    """Operation-local response error for DeleteDevice (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


DeleteDeviceError.response_error_map = {
    "default": DeleteDeviceUnexpectedError,
}


class DeleteDevicesError(DeviceError):
    """Operation-local error for DeleteDevices."""

    response_error_map: dict[str, type[DeviceError]] = {}


class DeleteDevicesUnexpectedError(DeleteDevicesError):
    """Operation-local response error for DeleteDevices (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


DeleteDevicesError.response_error_map = {
    "default": DeleteDevicesUnexpectedError,
}


class GetDeviceError(DeviceError):
    """Operation-local error for GetDevice."""

    response_error_map: dict[str, type[DeviceError]] = {}


class GetDeviceUnexpectedError(GetDeviceError):
    """Operation-local response error for GetDevice (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


GetDeviceError.response_error_map = {
    "default": GetDeviceUnexpectedError,
}


class GetDeviceByNameError(DeviceError):
    """Operation-local error for GetDeviceByName."""

    response_error_map: dict[str, type[DeviceError]] = {}


class GetDeviceByNameUnexpectedError(GetDeviceByNameError):
    """Operation-local response error for GetDeviceByName (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


GetDeviceByNameError.response_error_map = {
    "default": GetDeviceByNameUnexpectedError,
}


class ListDevicesError(DeviceError):
    """Operation-local error for ListDevices."""

    response_error_map: dict[str, type[DeviceError]] = {}


class ListDevicesUnexpectedError(ListDevicesError):
    """Operation-local response error for ListDevices (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


ListDevicesError.response_error_map = {
    "default": ListDevicesUnexpectedError,
}


class UpdateDeviceError(DeviceError):
    """Operation-local error for UpdateDevice."""

    response_error_map: dict[str, type[DeviceError]] = {}


class UpdateDeviceUnexpectedError(UpdateDeviceError):
    """Operation-local response error for UpdateDevice (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


UpdateDeviceError.response_error_map = {
    "default": UpdateDeviceUnexpectedError,
}


class UpdateDeviceLabelsError(DeviceError):
    """Operation-local error for UpdateDeviceLabels."""

    response_error_map: dict[str, type[DeviceError]] = {}


class UpdateDeviceLabelsUnexpectedError(UpdateDeviceLabelsError):
    """Operation-local response error for UpdateDeviceLabels (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


UpdateDeviceLabelsError.response_error_map = {
    "default": UpdateDeviceLabelsUnexpectedError,
}


class UpdateDevicesError(DeviceError):
    """Operation-local error for UpdateDevices."""

    response_error_map: dict[str, type[DeviceError]] = {}


class UpdateDevicesUnexpectedError(UpdateDevicesError):
    """Operation-local response error for UpdateDevices (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


UpdateDevicesError.response_error_map = {
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
