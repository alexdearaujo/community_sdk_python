# AUTO-GENERATED: scripts/generation/error_package.py, generate_service_error_package()
# Rebuilt on every `make generate`. Do not edit by hand.

from __future__ import annotations

from typing import Any

from kentik_api.errors import HTTPException


class V5Error(HTTPException):
    """Base service-local error for the v5 API."""

    @classmethod
    def _build_error(
        cls, response: Any, *, operation_name: str, method: str, path: str
    ) -> "V5Error":
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
    ) -> "V5Error":
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


class QueryUrlError(V5Error):
    """Operation-local error for client.v5.query_url()."""

    response_error_map: dict[str, type[V5Error]] = {}


class QueryUrlBadRequestError(QueryUrlError):
    """Operation-local response error for query_url (400: The request is not valid, for example a query without device_name. #/components/schemas/V5Error)."""

    pass


class QueryUrlUnauthorizedError(QueryUrlError):
    """Operation-local response error for query_url (401: The credentials are missing or wrong. #/components/schemas/V5Error)."""

    pass


class QueryUrlForbiddenError(QueryUrlError):
    """Operation-local response error for query_url (403: The user may not call this endpoint. #/components/schemas/V5Error)."""

    pass


class QueryUrlNotFoundError(QueryUrlError):
    """Operation-local response error for query_url (404: The resource does not exist. #/components/schemas/V5Error)."""

    pass


class QueryUrlTooManyRequestsError(QueryUrlError):
    """Operation-local response error for query_url (429: The rate limit is exceeded. V5 sends no rate limit headers. #/components/schemas/V5Error)."""

    pass


class QueryUrlInternalServerErrorError(QueryUrlError):
    """Operation-local response error for query_url (500: The API failed. #/components/schemas/V5Error)."""

    pass


QueryUrlError.response_error_map = {
    "400": QueryUrlBadRequestError,
    "401": QueryUrlUnauthorizedError,
    "403": QueryUrlForbiddenError,
    "404": QueryUrlNotFoundError,
    "429": QueryUrlTooManyRequestsError,
    "500": QueryUrlInternalServerErrorError,
}


class TopXChartError(V5Error):
    """Operation-local error for client.v5.top_x_chart()."""

    response_error_map: dict[str, type[V5Error]] = {}


class TopXChartBadRequestError(TopXChartError):
    """Operation-local response error for top_x_chart (400: The request is not valid, for example a query without device_name. #/components/schemas/V5Error)."""

    pass


class TopXChartUnauthorizedError(TopXChartError):
    """Operation-local response error for top_x_chart (401: The credentials are missing or wrong. #/components/schemas/V5Error)."""

    pass


class TopXChartForbiddenError(TopXChartError):
    """Operation-local response error for top_x_chart (403: The user may not call this endpoint. #/components/schemas/V5Error)."""

    pass


class TopXChartNotFoundError(TopXChartError):
    """Operation-local response error for top_x_chart (404: The resource does not exist. #/components/schemas/V5Error)."""

    pass


class TopXChartTooManyRequestsError(TopXChartError):
    """Operation-local response error for top_x_chart (429: The rate limit is exceeded. V5 sends no rate limit headers. #/components/schemas/V5Error)."""

    pass


class TopXChartInternalServerErrorError(TopXChartError):
    """Operation-local response error for top_x_chart (500: The API failed. #/components/schemas/V5Error)."""

    pass


TopXChartError.response_error_map = {
    "400": TopXChartBadRequestError,
    "401": TopXChartUnauthorizedError,
    "403": TopXChartForbiddenError,
    "404": TopXChartNotFoundError,
    "429": TopXChartTooManyRequestsError,
    "500": TopXChartInternalServerErrorError,
}


class TopXDataError(V5Error):
    """Operation-local error for client.v5.top_x_data()."""

    response_error_map: dict[str, type[V5Error]] = {}


class TopXDataBadRequestError(TopXDataError):
    """Operation-local response error for top_x_data (400: The request is not valid, for example a query without device_name. #/components/schemas/V5Error)."""

    pass


class TopXDataUnauthorizedError(TopXDataError):
    """Operation-local response error for top_x_data (401: The credentials are missing or wrong. #/components/schemas/V5Error)."""

    pass


class TopXDataForbiddenError(TopXDataError):
    """Operation-local response error for top_x_data (403: The user may not call this endpoint. #/components/schemas/V5Error)."""

    pass


class TopXDataNotFoundError(TopXDataError):
    """Operation-local response error for top_x_data (404: The resource does not exist. #/components/schemas/V5Error)."""

    pass


class TopXDataTooManyRequestsError(TopXDataError):
    """Operation-local response error for top_x_data (429: The rate limit is exceeded. V5 sends no rate limit headers. #/components/schemas/V5Error)."""

    pass


class TopXDataInternalServerErrorError(TopXDataError):
    """Operation-local response error for top_x_data (500: The API failed. #/components/schemas/V5Error)."""

    pass


TopXDataError.response_error_map = {
    "400": TopXDataBadRequestError,
    "401": TopXDataUnauthorizedError,
    "403": TopXDataForbiddenError,
    "404": TopXDataNotFoundError,
    "429": TopXDataTooManyRequestsError,
    "500": TopXDataInternalServerErrorError,
}

ERROR_BY_METHOD: dict[str, type[V5Error]] = {
    "query_url": QueryUrlError,
    "top_x_chart": TopXChartError,
    "top_x_data": TopXDataError,
}

__all__ = [
    "V5Error",
    "QueryUrlBadRequestError",
    "QueryUrlUnauthorizedError",
    "QueryUrlForbiddenError",
    "QueryUrlNotFoundError",
    "QueryUrlTooManyRequestsError",
    "QueryUrlInternalServerErrorError",
    "TopXChartBadRequestError",
    "TopXChartUnauthorizedError",
    "TopXChartForbiddenError",
    "TopXChartNotFoundError",
    "TopXChartTooManyRequestsError",
    "TopXChartInternalServerErrorError",
    "TopXDataBadRequestError",
    "TopXDataUnauthorizedError",
    "TopXDataForbiddenError",
    "TopXDataNotFoundError",
    "TopXDataTooManyRequestsError",
    "TopXDataInternalServerErrorError",
    "QueryUrlError",
    "TopXChartError",
    "TopXDataError",
    "ERROR_BY_METHOD",
]
