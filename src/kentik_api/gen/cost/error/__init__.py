from __future__ import annotations

from typing import Any

from kentik_api.errors import HTTPException


class CostError(HTTPException):
    """Base service-local error for the cost API."""

    @classmethod
    def _build_error(
        cls, response: Any, *, operation_name: str, method: str, path: str
    ) -> "CostError":
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
    ) -> "CostError":
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


class GetCostProviderSummaryUnexpectedError(CostError):
    """Operation-local response error for GetCostProviderSummary (default: An unexpected error response. #/components/schemas/googlerpcStatus)."""

    pass


class GetCostProviderSummaryError(CostError):
    """Operation-local error for GetCostProviderSummary."""

    response_error_map = {
        "default": GetCostProviderSummaryUnexpectedError,
    }


class ListCostProviderSummariesUnexpectedError(CostError):
    """Operation-local response error for ListCostProviderSummaries (default: An unexpected error response. #/components/schemas/googlerpcStatus)."""

    pass


class ListCostProviderSummariesError(CostError):
    """Operation-local error for ListCostProviderSummaries."""

    response_error_map = {
        "default": ListCostProviderSummariesUnexpectedError,
    }


class ListCostProvidersUnexpectedError(CostError):
    """Operation-local response error for ListCostProviders (default: An unexpected error response. #/components/schemas/googlerpcStatus)."""

    pass


class ListCostProvidersError(CostError):
    """Operation-local error for ListCostProviders."""

    response_error_map = {
        "default": ListCostProvidersUnexpectedError,
    }


ERROR_BY_OPERATION: dict[str, type[CostError]] = {
    "GetCostProviderSummary": GetCostProviderSummaryError,
    "ListCostProviderSummaries": ListCostProviderSummariesError,
    "ListCostProviders": ListCostProvidersError,
}

__all__ = [
    "CostError",
    "GetCostProviderSummaryUnexpectedError",
    "ListCostProviderSummariesUnexpectedError",
    "ListCostProvidersUnexpectedError",
    "GetCostProviderSummaryError",
    "ListCostProviderSummariesError",
    "ListCostProvidersError",
    "ERROR_BY_OPERATION",
]
