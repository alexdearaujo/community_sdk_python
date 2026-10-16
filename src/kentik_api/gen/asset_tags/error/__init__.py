# AUTO-GENERATED: scripts/generation/error_package.py, generate_service_error_package()
# Rebuilt on every `make generate`. Do not edit by hand.

from __future__ import annotations

from typing import Any

from kentik_api.errors import HTTPException

from ..models import rpcStatus


class AssetTagsError(HTTPException):
    """Base service-local error for the asset_tags API."""

    @classmethod
    def _build_error(
        cls, response: Any, *, operation_name: str, method: str, path: str
    ) -> "AssetTagsError":
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
    ) -> "AssetTagsError":
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


class CreateTagKeyUnexpectedError(AssetTagsError):
    """Operation-local response error for CreateTagKey (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class CreateTagKeyError(AssetTagsError):
    """Operation-local error for CreateTagKey."""

    response_error_map = {
        "default": CreateTagKeyUnexpectedError,
    }


class DeleteTagKeyUnexpectedError(AssetTagsError):
    """Operation-local response error for DeleteTagKey (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class DeleteTagKeyError(AssetTagsError):
    """Operation-local error for DeleteTagKey."""

    response_error_map = {
        "default": DeleteTagKeyUnexpectedError,
    }


class DeleteTagValuesUnexpectedError(AssetTagsError):
    """Operation-local response error for DeleteTagValues (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class DeleteTagValuesError(AssetTagsError):
    """Operation-local error for DeleteTagValues."""

    response_error_map = {
        "default": DeleteTagValuesUnexpectedError,
    }


class GetTagKeyUnexpectedError(AssetTagsError):
    """Operation-local response error for GetTagKey (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class GetTagKeyError(AssetTagsError):
    """Operation-local error for GetTagKey."""

    response_error_map = {
        "default": GetTagKeyUnexpectedError,
    }


class GetTagValuesUnexpectedError(AssetTagsError):
    """Operation-local response error for GetTagValues (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class GetTagValuesError(AssetTagsError):
    """Operation-local error for GetTagValues."""

    response_error_map = {
        "default": GetTagValuesUnexpectedError,
    }


class ListTagKeysUnexpectedError(AssetTagsError):
    """Operation-local response error for ListTagKeys (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class ListTagKeysError(AssetTagsError):
    """Operation-local error for ListTagKeys."""

    response_error_map = {
        "default": ListTagKeysUnexpectedError,
    }


class ListTagValuesUnexpectedError(AssetTagsError):
    """Operation-local response error for ListTagValues (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class ListTagValuesError(AssetTagsError):
    """Operation-local error for ListTagValues."""

    response_error_map = {
        "default": ListTagValuesUnexpectedError,
    }


class SetTagValuesUnexpectedError(AssetTagsError):
    """Operation-local response error for SetTagValues (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class SetTagValuesError(AssetTagsError):
    """Operation-local error for SetTagValues."""

    response_error_map = {
        "default": SetTagValuesUnexpectedError,
    }


class UpdateTagKeyUnexpectedError(AssetTagsError):
    """Operation-local response error for UpdateTagKey (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class UpdateTagKeyError(AssetTagsError):
    """Operation-local error for UpdateTagKey."""

    response_error_map = {
        "default": UpdateTagKeyUnexpectedError,
    }


ERROR_BY_OPERATION: dict[str, type[AssetTagsError]] = {
    "CreateTagKey": CreateTagKeyError,
    "DeleteTagKey": DeleteTagKeyError,
    "DeleteTagValues": DeleteTagValuesError,
    "GetTagKey": GetTagKeyError,
    "GetTagValues": GetTagValuesError,
    "ListTagKeys": ListTagKeysError,
    "ListTagValues": ListTagValuesError,
    "SetTagValues": SetTagValuesError,
    "UpdateTagKey": UpdateTagKeyError,
}

__all__ = [
    "AssetTagsError",
    "CreateTagKeyUnexpectedError",
    "DeleteTagKeyUnexpectedError",
    "DeleteTagValuesUnexpectedError",
    "GetTagKeyUnexpectedError",
    "GetTagValuesUnexpectedError",
    "ListTagKeysUnexpectedError",
    "ListTagValuesUnexpectedError",
    "SetTagValuesUnexpectedError",
    "UpdateTagKeyUnexpectedError",
    "CreateTagKeyError",
    "DeleteTagKeyError",
    "DeleteTagValuesError",
    "GetTagKeyError",
    "GetTagValuesError",
    "ListTagKeysError",
    "ListTagValuesError",
    "SetTagValuesError",
    "UpdateTagKeyError",
    "ERROR_BY_OPERATION",
]
