from __future__ import annotations

from typing import Any

from kentik_api.errors import HTTPException

from ..models import rpcStatus


class MkpError(HTTPException):
    """Base service-local error for the mkp API."""

    @classmethod
    def _build_error(
        cls, response: Any, *, operation_name: str, method: str, path: str
    ) -> "MkpError":
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
    ) -> "MkpError":
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


class PackageCreateUnexpectedError(MkpError):
    """Operation-local response error for PackageCreate (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class PackageCreateError(MkpError):
    """Operation-local error for PackageCreate."""

    response_error_map = {
        "default": PackageCreateUnexpectedError,
    }


class PackageDeleteUnexpectedError(MkpError):
    """Operation-local response error for PackageDelete (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class PackageDeleteError(MkpError):
    """Operation-local error for PackageDelete."""

    response_error_map = {
        "default": PackageDeleteUnexpectedError,
    }


class PackageGetUnexpectedError(MkpError):
    """Operation-local response error for PackageGet (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class PackageGetError(MkpError):
    """Operation-local error for PackageGet."""

    response_error_map = {
        "default": PackageGetUnexpectedError,
    }


class PackageListUnexpectedError(MkpError):
    """Operation-local response error for PackageList (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class PackageListError(MkpError):
    """Operation-local error for PackageList."""

    response_error_map = {
        "default": PackageListUnexpectedError,
    }


class PackageUpdateUnexpectedError(MkpError):
    """Operation-local response error for PackageUpdate (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class PackageUpdateError(MkpError):
    """Operation-local error for PackageUpdate."""

    response_error_map = {
        "default": PackageUpdateUnexpectedError,
    }


class TenantCreateUnexpectedError(MkpError):
    """Operation-local response error for TenantCreate (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class TenantCreateError(MkpError):
    """Operation-local error for TenantCreate."""

    response_error_map = {
        "default": TenantCreateUnexpectedError,
    }


class TenantDeleteUnexpectedError(MkpError):
    """Operation-local response error for TenantDelete (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class TenantDeleteError(MkpError):
    """Operation-local error for TenantDelete."""

    response_error_map = {
        "default": TenantDeleteUnexpectedError,
    }


class TenantGetUnexpectedError(MkpError):
    """Operation-local response error for TenantGet (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class TenantGetError(MkpError):
    """Operation-local error for TenantGet."""

    response_error_map = {
        "default": TenantGetUnexpectedError,
    }


class TenantListUnexpectedError(MkpError):
    """Operation-local response error for TenantList (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class TenantListError(MkpError):
    """Operation-local error for TenantList."""

    response_error_map = {
        "default": TenantListUnexpectedError,
    }


class TenantUpdateUnexpectedError(MkpError):
    """Operation-local response error for TenantUpdate (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class TenantUpdateError(MkpError):
    """Operation-local error for TenantUpdate."""

    response_error_map = {
        "default": TenantUpdateUnexpectedError,
    }


class TenantUserCreateUnexpectedError(MkpError):
    """Operation-local response error for TenantUserCreate (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class TenantUserCreateError(MkpError):
    """Operation-local error for TenantUserCreate."""

    response_error_map = {
        "default": TenantUserCreateUnexpectedError,
    }


class TenantUserDeleteUnexpectedError(MkpError):
    """Operation-local response error for TenantUserDelete (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class TenantUserDeleteError(MkpError):
    """Operation-local error for TenantUserDelete."""

    response_error_map = {
        "default": TenantUserDeleteUnexpectedError,
    }


class TenantUserListUnexpectedError(MkpError):
    """Operation-local response error for TenantUserList (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class TenantUserListError(MkpError):
    """Operation-local error for TenantUserList."""

    response_error_map = {
        "default": TenantUserListUnexpectedError,
    }


class TenantUserUpdateUnexpectedError(MkpError):
    """Operation-local response error for TenantUserUpdate (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class TenantUserUpdateError(MkpError):
    """Operation-local error for TenantUserUpdate."""

    response_error_map = {
        "default": TenantUserUpdateUnexpectedError,
    }


ERROR_BY_OPERATION: dict[str, type[MkpError]] = {
    "PackageCreate": PackageCreateError,
    "PackageDelete": PackageDeleteError,
    "PackageGet": PackageGetError,
    "PackageList": PackageListError,
    "PackageUpdate": PackageUpdateError,
    "TenantCreate": TenantCreateError,
    "TenantDelete": TenantDeleteError,
    "TenantGet": TenantGetError,
    "TenantList": TenantListError,
    "TenantUpdate": TenantUpdateError,
    "TenantUserCreate": TenantUserCreateError,
    "TenantUserDelete": TenantUserDeleteError,
    "TenantUserList": TenantUserListError,
    "TenantUserUpdate": TenantUserUpdateError,
}

__all__ = [
    "MkpError",
    "PackageCreateUnexpectedError",
    "PackageDeleteUnexpectedError",
    "PackageGetUnexpectedError",
    "PackageListUnexpectedError",
    "PackageUpdateUnexpectedError",
    "TenantCreateUnexpectedError",
    "TenantDeleteUnexpectedError",
    "TenantGetUnexpectedError",
    "TenantListUnexpectedError",
    "TenantUpdateUnexpectedError",
    "TenantUserCreateUnexpectedError",
    "TenantUserDeleteUnexpectedError",
    "TenantUserListUnexpectedError",
    "TenantUserUpdateUnexpectedError",
    "PackageCreateError",
    "PackageDeleteError",
    "PackageGetError",
    "PackageListError",
    "PackageUpdateError",
    "TenantCreateError",
    "TenantDeleteError",
    "TenantGetError",
    "TenantListError",
    "TenantUpdateError",
    "TenantUserCreateError",
    "TenantUserDeleteError",
    "TenantUserListError",
    "TenantUserUpdateError",
    "ERROR_BY_OPERATION",
]
