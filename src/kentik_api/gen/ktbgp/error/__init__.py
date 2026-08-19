# AUTO-GENERATED: scripts/generation/error_package.py, generate_service_error_package()
# Rebuilt on every `make generate`. Do not edit by hand.

from __future__ import annotations

from typing import Any

from kentik_api.errors import HTTPException

from ..models import rpcStatus


class KtbgpError(HTTPException):
    """Base service-local error for the ktbgp API."""

    @classmethod
    def _build_error(
        cls, response: Any, *, operation_name: str, method: str, path: str
    ) -> "KtbgpError":
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
    ) -> "KtbgpError":
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


class RouteService_AnnounceUnexpectedError(KtbgpError):
    """Operation-local response error for RouteService_Announce (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class RouteService_AnnounceError(KtbgpError):
    """Operation-local error for RouteService_Announce."""

    response_error_map = {
        "default": RouteService_AnnounceUnexpectedError,
    }


class RouteService_ListUnexpectedError(KtbgpError):
    """Operation-local response error for RouteService_List (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class RouteService_ListError(KtbgpError):
    """Operation-local error for RouteService_List."""

    response_error_map = {
        "default": RouteService_ListUnexpectedError,
    }


class RouteService_WithdrawUnexpectedError(KtbgpError):
    """Operation-local response error for RouteService_Withdraw (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class RouteService_WithdrawError(KtbgpError):
    """Operation-local error for RouteService_Withdraw."""

    response_error_map = {
        "default": RouteService_WithdrawUnexpectedError,
    }


ERROR_BY_OPERATION: dict[str, type[KtbgpError]] = {
    "RouteService_Announce": RouteService_AnnounceError,
    "RouteService_List": RouteService_ListError,
    "RouteService_Withdraw": RouteService_WithdrawError,
}

__all__ = [
    "KtbgpError",
    "RouteService_AnnounceUnexpectedError",
    "RouteService_ListUnexpectedError",
    "RouteService_WithdrawUnexpectedError",
    "RouteService_AnnounceError",
    "RouteService_ListError",
    "RouteService_WithdrawError",
    "ERROR_BY_OPERATION",
]
