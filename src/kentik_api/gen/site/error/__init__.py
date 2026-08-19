# AUTO-GENERATED: scripts/generation/error_package.py, generate_service_error_package()
# Rebuilt on every `make generate`. Do not edit by hand.

from __future__ import annotations

from typing import Any

from kentik_api.errors import HTTPException

from ..models import rpcStatus


class SiteError(HTTPException):
    """Base service-local error for the site API."""

    @classmethod
    def _build_error(
        cls, response: Any, *, operation_name: str, method: str, path: str
    ) -> "SiteError":
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
    ) -> "SiteError":
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


class CreateSiteUnexpectedError(SiteError):
    """Operation-local response error for CreateSite (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class CreateSiteError(SiteError):
    """Operation-local error for CreateSite."""

    response_error_map = {
        "default": CreateSiteUnexpectedError,
    }


class CreateSiteMarketUnexpectedError(SiteError):
    """Operation-local response error for CreateSiteMarket (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class CreateSiteMarketError(SiteError):
    """Operation-local error for CreateSiteMarket."""

    response_error_map = {
        "default": CreateSiteMarketUnexpectedError,
    }


class DeleteSiteUnexpectedError(SiteError):
    """Operation-local response error for DeleteSite (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class DeleteSiteError(SiteError):
    """Operation-local error for DeleteSite."""

    response_error_map = {
        "default": DeleteSiteUnexpectedError,
    }


class DeleteSiteMarketUnexpectedError(SiteError):
    """Operation-local response error for DeleteSiteMarket (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class DeleteSiteMarketError(SiteError):
    """Operation-local error for DeleteSiteMarket."""

    response_error_map = {
        "default": DeleteSiteMarketUnexpectedError,
    }


class GetSiteUnexpectedError(SiteError):
    """Operation-local response error for GetSite (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class GetSiteError(SiteError):
    """Operation-local error for GetSite."""

    response_error_map = {
        "default": GetSiteUnexpectedError,
    }


class GetSiteMarketUnexpectedError(SiteError):
    """Operation-local response error for GetSiteMarket (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class GetSiteMarketError(SiteError):
    """Operation-local error for GetSiteMarket."""

    response_error_map = {
        "default": GetSiteMarketUnexpectedError,
    }


class ListSiteMarketsUnexpectedError(SiteError):
    """Operation-local response error for ListSiteMarkets (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class ListSiteMarketsError(SiteError):
    """Operation-local error for ListSiteMarkets."""

    response_error_map = {
        "default": ListSiteMarketsUnexpectedError,
    }


class ListSitesUnexpectedError(SiteError):
    """Operation-local response error for ListSites (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class ListSitesError(SiteError):
    """Operation-local error for ListSites."""

    response_error_map = {
        "default": ListSitesUnexpectedError,
    }


class UpdateSiteUnexpectedError(SiteError):
    """Operation-local response error for UpdateSite (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class UpdateSiteError(SiteError):
    """Operation-local error for UpdateSite."""

    response_error_map = {
        "default": UpdateSiteUnexpectedError,
    }


class UpdateSiteMarketUnexpectedError(SiteError):
    """Operation-local response error for UpdateSiteMarket (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


class UpdateSiteMarketError(SiteError):
    """Operation-local error for UpdateSiteMarket."""

    response_error_map = {
        "default": UpdateSiteMarketUnexpectedError,
    }


ERROR_BY_OPERATION: dict[str, type[SiteError]] = {
    "CreateSite": CreateSiteError,
    "CreateSiteMarket": CreateSiteMarketError,
    "DeleteSite": DeleteSiteError,
    "DeleteSiteMarket": DeleteSiteMarketError,
    "GetSite": GetSiteError,
    "GetSiteMarket": GetSiteMarketError,
    "ListSiteMarkets": ListSiteMarketsError,
    "ListSites": ListSitesError,
    "UpdateSite": UpdateSiteError,
    "UpdateSiteMarket": UpdateSiteMarketError,
}

__all__ = [
    "SiteError",
    "CreateSiteUnexpectedError",
    "CreateSiteMarketUnexpectedError",
    "DeleteSiteUnexpectedError",
    "DeleteSiteMarketUnexpectedError",
    "GetSiteUnexpectedError",
    "GetSiteMarketUnexpectedError",
    "ListSiteMarketsUnexpectedError",
    "ListSitesUnexpectedError",
    "UpdateSiteUnexpectedError",
    "UpdateSiteMarketUnexpectedError",
    "CreateSiteError",
    "CreateSiteMarketError",
    "DeleteSiteError",
    "DeleteSiteMarketError",
    "GetSiteError",
    "GetSiteMarketError",
    "ListSiteMarketsError",
    "ListSitesError",
    "UpdateSiteError",
    "UpdateSiteMarketError",
    "ERROR_BY_OPERATION",
]
