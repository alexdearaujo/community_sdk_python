from __future__ import annotations

from typing import Any

from kentik_api.errors import HTTPException

from ..models import rpcStatus


class KmiError(HTTPException):
    """Base service-local error for the kmi API."""

    @classmethod
    def _build_error(
        cls, response: Any, *, operation_name: str, method: str, path: str
    ) -> "KmiError":
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
    ) -> "KmiError":
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


class GetASNDetailsUnexpectedError(KmiError):
    """Operation-local response error for GetASNDetails (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class GetASNDetailsError(KmiError):
    """Operation-local error for GetASNDetails."""

    response_error_map = {
        "default": GetASNDetailsUnexpectedError,
    }


class GetASNInsightsUnexpectedError(KmiError):
    """Operation-local response error for GetASNInsights (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class GetASNInsightsError(KmiError):
    """Operation-local error for GetASNInsights."""

    response_error_map = {
        "default": GetASNInsightsUnexpectedError,
    }


class GetGlobalInsightsUnexpectedError(KmiError):
    """Operation-local response error for GetGlobalInsights (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class GetGlobalInsightsError(KmiError):
    """Operation-local error for GetGlobalInsights."""

    response_error_map = {
        "default": GetGlobalInsightsUnexpectedError,
    }


class GetRankingsUnexpectedError(KmiError):
    """Operation-local response error for GetRankings (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class GetRankingsError(KmiError):
    """Operation-local error for GetRankings."""

    response_error_map = {
        "default": GetRankingsUnexpectedError,
    }


class ListMarketsUnexpectedError(KmiError):
    """Operation-local response error for ListMarkets (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class ListMarketsError(KmiError):
    """Operation-local error for ListMarkets."""

    response_error_map = {
        "default": ListMarketsUnexpectedError,
    }


ERROR_BY_OPERATION: dict[str, type[KmiError]] = {
    "GetASNDetails": GetASNDetailsError,
    "GetASNInsights": GetASNInsightsError,
    "GetGlobalInsights": GetGlobalInsightsError,
    "GetRankings": GetRankingsError,
    "ListMarkets": ListMarketsError,
}

__all__ = [
    "KmiError",
    "GetASNDetailsUnexpectedError",
    "GetASNInsightsUnexpectedError",
    "GetGlobalInsightsUnexpectedError",
    "GetRankingsUnexpectedError",
    "ListMarketsUnexpectedError",
    "GetASNDetailsError",
    "GetASNInsightsError",
    "GetGlobalInsightsError",
    "GetRankingsError",
    "ListMarketsError",
    "ERROR_BY_OPERATION",
]
