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


class CreateMarketError(SiteError):
    """Operation-local error for client.site.create_market()."""

    response_error_map: dict[str, type[SiteError]] = {}


class CreateMarketUnexpectedError(CreateMarketError):
    """Operation-local response error for create_market (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


CreateMarketError.response_error_map = {
    "default": CreateMarketUnexpectedError,
}


class CreateSiteError(SiteError):
    """Operation-local error for client.site.create_site()."""

    response_error_map: dict[str, type[SiteError]] = {}


class CreateSiteUnexpectedError(CreateSiteError):
    """Operation-local response error for create_site (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


CreateSiteError.response_error_map = {
    "default": CreateSiteUnexpectedError,
}


class DeleteMarketError(SiteError):
    """Operation-local error for client.site.delete_market()."""

    response_error_map: dict[str, type[SiteError]] = {}


class DeleteMarketUnexpectedError(DeleteMarketError):
    """Operation-local response error for delete_market (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


DeleteMarketError.response_error_map = {
    "default": DeleteMarketUnexpectedError,
}


class DeleteSiteError(SiteError):
    """Operation-local error for client.site.delete_site()."""

    response_error_map: dict[str, type[SiteError]] = {}


class DeleteSiteUnexpectedError(DeleteSiteError):
    """Operation-local response error for delete_site (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


DeleteSiteError.response_error_map = {
    "default": DeleteSiteUnexpectedError,
}


class GetMarketError(SiteError):
    """Operation-local error for client.site.get_market()."""

    response_error_map: dict[str, type[SiteError]] = {}


class GetMarketUnexpectedError(GetMarketError):
    """Operation-local response error for get_market (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


GetMarketError.response_error_map = {
    "default": GetMarketUnexpectedError,
}


class GetSiteError(SiteError):
    """Operation-local error for client.site.get_site()."""

    response_error_map: dict[str, type[SiteError]] = {}


class GetSiteUnexpectedError(GetSiteError):
    """Operation-local response error for get_site (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


GetSiteError.response_error_map = {
    "default": GetSiteUnexpectedError,
}


class ListMarketsError(SiteError):
    """Operation-local error for client.site.list_markets()."""

    response_error_map: dict[str, type[SiteError]] = {}


class ListMarketsUnexpectedError(ListMarketsError):
    """Operation-local response error for list_markets (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


ListMarketsError.response_error_map = {
    "default": ListMarketsUnexpectedError,
}


class ListSitesError(SiteError):
    """Operation-local error for client.site.list_sites()."""

    response_error_map: dict[str, type[SiteError]] = {}


class ListSitesUnexpectedError(ListSitesError):
    """Operation-local response error for list_sites (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


ListSitesError.response_error_map = {
    "default": ListSitesUnexpectedError,
}


class UpdateMarketError(SiteError):
    """Operation-local error for client.site.update_market()."""

    response_error_map: dict[str, type[SiteError]] = {}


class UpdateMarketUnexpectedError(UpdateMarketError):
    """Operation-local response error for update_market (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


UpdateMarketError.response_error_map = {
    "default": UpdateMarketUnexpectedError,
}


class UpdateSiteError(SiteError):
    """Operation-local error for client.site.update_site()."""

    response_error_map: dict[str, type[SiteError]] = {}


class UpdateSiteUnexpectedError(UpdateSiteError):
    """Operation-local response error for update_site (default: An unexpected error response. #/components/schemas/rpcStatus)."""

    pass


UpdateSiteError.response_error_map = {
    "default": UpdateSiteUnexpectedError,
}

ERROR_BY_METHOD: dict[str, type[SiteError]] = {
    "create_market": CreateMarketError,
    "create_site": CreateSiteError,
    "delete_market": DeleteMarketError,
    "delete_site": DeleteSiteError,
    "get_market": GetMarketError,
    "get_site": GetSiteError,
    "list_markets": ListMarketsError,
    "list_sites": ListSitesError,
    "update_market": UpdateMarketError,
    "update_site": UpdateSiteError,
}

__all__ = [
    "SiteError",
    "CreateMarketUnexpectedError",
    "CreateSiteUnexpectedError",
    "DeleteMarketUnexpectedError",
    "DeleteSiteUnexpectedError",
    "GetMarketUnexpectedError",
    "GetSiteUnexpectedError",
    "ListMarketsUnexpectedError",
    "ListSitesUnexpectedError",
    "UpdateMarketUnexpectedError",
    "UpdateSiteUnexpectedError",
    "CreateMarketError",
    "CreateSiteError",
    "DeleteMarketError",
    "DeleteSiteError",
    "GetMarketError",
    "GetSiteError",
    "ListMarketsError",
    "ListSitesError",
    "UpdateMarketError",
    "UpdateSiteError",
    "ERROR_BY_METHOD",
]
