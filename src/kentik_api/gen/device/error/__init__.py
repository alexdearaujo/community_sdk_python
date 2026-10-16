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
    """Operation-local error for client.device.create_device()."""

    response_error_map: dict[str, type[DeviceError]] = {}


class CreateDeviceUnexpectedError(CreateDeviceError):
    """Operation-local response error for create_device (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


CreateDeviceError.response_error_map = {
    "default": CreateDeviceUnexpectedError,
}


class CreateDevicesError(DeviceError):
    """Operation-local error for client.device.create_devices()."""

    response_error_map: dict[str, type[DeviceError]] = {}


class CreateDevicesUnexpectedError(CreateDevicesError):
    """Operation-local response error for create_devices (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


CreateDevicesError.response_error_map = {
    "default": CreateDevicesUnexpectedError,
}


class DeleteDeviceError(DeviceError):
    """Operation-local error for client.device.delete_device()."""

    response_error_map: dict[str, type[DeviceError]] = {}


class DeleteDeviceUnexpectedError(DeleteDeviceError):
    """Operation-local response error for delete_device (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


DeleteDeviceError.response_error_map = {
    "default": DeleteDeviceUnexpectedError,
}


class DeleteDevicesError(DeviceError):
    """Operation-local error for client.device.delete_devices()."""

    response_error_map: dict[str, type[DeviceError]] = {}


class DeleteDevicesUnexpectedError(DeleteDevicesError):
    """Operation-local response error for delete_devices (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


DeleteDevicesError.response_error_map = {
    "default": DeleteDevicesUnexpectedError,
}


class GetDeviceError(DeviceError):
    """Operation-local error for client.device.get_device()."""

    response_error_map: dict[str, type[DeviceError]] = {}


class GetDeviceUnexpectedError(GetDeviceError):
    """Operation-local response error for get_device (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


GetDeviceError.response_error_map = {
    "default": GetDeviceUnexpectedError,
}


class GetDeviceByNameError(DeviceError):
    """Operation-local error for client.device.get_device_by_name()."""

    response_error_map: dict[str, type[DeviceError]] = {}


class GetDeviceByNameUnexpectedError(GetDeviceByNameError):
    """Operation-local response error for get_device_by_name (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


GetDeviceByNameError.response_error_map = {
    "default": GetDeviceByNameUnexpectedError,
}


class ListDevicesError(DeviceError):
    """Operation-local error for client.device.list_devices()."""

    response_error_map: dict[str, type[DeviceError]] = {}


class ListDevicesUnexpectedError(ListDevicesError):
    """Operation-local response error for list_devices (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


ListDevicesError.response_error_map = {
    "default": ListDevicesUnexpectedError,
}


class UpdateDeviceError(DeviceError):
    """Operation-local error for client.device.update_device()."""

    response_error_map: dict[str, type[DeviceError]] = {}


class UpdateDeviceUnexpectedError(UpdateDeviceError):
    """Operation-local response error for update_device (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


UpdateDeviceError.response_error_map = {
    "default": UpdateDeviceUnexpectedError,
}


class UpdateDevicesError(DeviceError):
    """Operation-local error for client.device.update_devices()."""

    response_error_map: dict[str, type[DeviceError]] = {}


class UpdateDevicesUnexpectedError(UpdateDevicesError):
    """Operation-local response error for update_devices (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


UpdateDevicesError.response_error_map = {
    "default": UpdateDevicesUnexpectedError,
}


class UpdateLabelsError(DeviceError):
    """Operation-local error for client.device.update_labels()."""

    response_error_map: dict[str, type[DeviceError]] = {}


class UpdateLabelsUnexpectedError(UpdateLabelsError):
    """Operation-local response error for update_labels (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


UpdateLabelsError.response_error_map = {
    "default": UpdateLabelsUnexpectedError,
}

ERROR_BY_METHOD: dict[str, type[DeviceError]] = {
    "create_device": CreateDeviceError,
    "create_devices": CreateDevicesError,
    "delete_device": DeleteDeviceError,
    "delete_devices": DeleteDevicesError,
    "get_device": GetDeviceError,
    "get_device_by_name": GetDeviceByNameError,
    "list_devices": ListDevicesError,
    "update_device": UpdateDeviceError,
    "update_devices": UpdateDevicesError,
    "update_labels": UpdateLabelsError,
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
    "UpdateDevicesUnexpectedError",
    "UpdateLabelsUnexpectedError",
    "CreateDeviceError",
    "CreateDevicesError",
    "DeleteDeviceError",
    "DeleteDevicesError",
    "GetDeviceError",
    "GetDeviceByNameError",
    "ListDevicesError",
    "UpdateDeviceError",
    "UpdateDevicesError",
    "UpdateLabelsError",
    "ERROR_BY_METHOD",
]
