from __future__ import annotations

from typing import Any

from kentik_api.errors import HTTPException

from ..models import rpcStatus


class CustomDimensionError(HTTPException):
    """Base service-local error for the custom_dimension API."""

    @classmethod
    def _build_error(
        cls, response: Any, *, operation_name: str, method: str, path: str
    ) -> "CustomDimensionError":
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
    ) -> "CustomDimensionError":
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


class CreateCustomDimensionUnexpectedError(CustomDimensionError):
    """Operation-local response error for CreateCustomDimension (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class CreateCustomDimensionError(CustomDimensionError):
    """Operation-local error for CreateCustomDimension."""

    response_error_map = {
        "default": CreateCustomDimensionUnexpectedError,
    }


class CreatePopulatorUnexpectedError(CustomDimensionError):
    """Operation-local response error for CreatePopulator (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class CreatePopulatorError(CustomDimensionError):
    """Operation-local error for CreatePopulator."""

    response_error_map = {
        "default": CreatePopulatorUnexpectedError,
    }


class DeleteCustomDimensionUnexpectedError(CustomDimensionError):
    """Operation-local response error for DeleteCustomDimension (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class DeleteCustomDimensionError(CustomDimensionError):
    """Operation-local error for DeleteCustomDimension."""

    response_error_map = {
        "default": DeleteCustomDimensionUnexpectedError,
    }


class DeletePopulatorUnexpectedError(CustomDimensionError):
    """Operation-local response error for DeletePopulator (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class DeletePopulatorError(CustomDimensionError):
    """Operation-local error for DeletePopulator."""

    response_error_map = {
        "default": DeletePopulatorUnexpectedError,
    }


class GetCustomDimensionInfoUnexpectedError(CustomDimensionError):
    """Operation-local response error for GetCustomDimensionInfo (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class GetCustomDimensionInfoError(CustomDimensionError):
    """Operation-local error for GetCustomDimensionInfo."""

    response_error_map = {
        "default": GetCustomDimensionInfoUnexpectedError,
    }


class GetPopulatorUnexpectedError(CustomDimensionError):
    """Operation-local response error for GetPopulator (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class GetPopulatorError(CustomDimensionError):
    """Operation-local error for GetPopulator."""

    response_error_map = {
        "default": GetPopulatorUnexpectedError,
    }


class GetPopulatorFieldUnexpectedError(CustomDimensionError):
    """Operation-local response error for GetPopulatorField (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class GetPopulatorFieldError(CustomDimensionError):
    """Operation-local error for GetPopulatorField."""

    response_error_map = {
        "default": GetPopulatorFieldUnexpectedError,
    }


class ListCustomDimensionsUnexpectedError(CustomDimensionError):
    """Operation-local response error for ListCustomDimensions (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class ListCustomDimensionsError(CustomDimensionError):
    """Operation-local error for ListCustomDimensions."""

    response_error_map = {
        "default": ListCustomDimensionsUnexpectedError,
    }


class UpdateCustomDimensionUnexpectedError(CustomDimensionError):
    """Operation-local response error for UpdateCustomDimension (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class UpdateCustomDimensionError(CustomDimensionError):
    """Operation-local error for UpdateCustomDimension."""

    response_error_map = {
        "default": UpdateCustomDimensionUnexpectedError,
    }


class UpdatePopulatorUnexpectedError(CustomDimensionError):
    """Operation-local response error for UpdatePopulator (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class UpdatePopulatorError(CustomDimensionError):
    """Operation-local error for UpdatePopulator."""

    response_error_map = {
        "default": UpdatePopulatorUnexpectedError,
    }


ERROR_BY_OPERATION: dict[str, type[CustomDimensionError]] = {
    "CreateCustomDimension": CreateCustomDimensionError,
    "CreatePopulator": CreatePopulatorError,
    "DeleteCustomDimension": DeleteCustomDimensionError,
    "DeletePopulator": DeletePopulatorError,
    "GetCustomDimensionInfo": GetCustomDimensionInfoError,
    "GetPopulator": GetPopulatorError,
    "GetPopulatorField": GetPopulatorFieldError,
    "ListCustomDimensions": ListCustomDimensionsError,
    "UpdateCustomDimension": UpdateCustomDimensionError,
    "UpdatePopulator": UpdatePopulatorError,
}

__all__ = [
    "CustomDimensionError",
    "CreateCustomDimensionUnexpectedError",
    "CreatePopulatorUnexpectedError",
    "DeleteCustomDimensionUnexpectedError",
    "DeletePopulatorUnexpectedError",
    "GetCustomDimensionInfoUnexpectedError",
    "GetPopulatorUnexpectedError",
    "GetPopulatorFieldUnexpectedError",
    "ListCustomDimensionsUnexpectedError",
    "UpdateCustomDimensionUnexpectedError",
    "UpdatePopulatorUnexpectedError",
    "CreateCustomDimensionError",
    "CreatePopulatorError",
    "DeleteCustomDimensionError",
    "DeletePopulatorError",
    "GetCustomDimensionInfoError",
    "GetPopulatorError",
    "GetPopulatorFieldError",
    "ListCustomDimensionsError",
    "UpdateCustomDimensionError",
    "UpdatePopulatorError",
    "ERROR_BY_OPERATION",
]
