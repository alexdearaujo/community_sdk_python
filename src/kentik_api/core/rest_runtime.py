# HAND-WRITTEN: not modified by `make generate`. Edit directly.
from __future__ import annotations

import json
from typing import Any, Dict, Optional
from urllib.parse import quote

import httpx
from kentik_api.auth.credentials import auth_headers
from kentik_api.core.api_config import APIConfig
from kentik_api.core.rate_limit import RateLimit, attach_rate_limit
from kentik_api.errors import (
    AuthenticationError,
    ConfigurationError,
    HTTPException,
    KentikError,
    TransportError,
)

# RFC 3986 pchar minus the unreserved set, which quote() never encodes. Leaving
# these raw matters: grpc-gateway does not decode reserved characters in a path
# parameter, so an encoded ":" in a timestamp would reach the server as "%3A".
_PATH_SEGMENT_SAFE = "!$&'()*+,;=:@"


def path_segment(value: Any) -> str:
    """Encodes one path parameter so its value cannot leave its own segment.

    "/", "?" and "#" are percent-encoded, and the dot segments, which encoding
    cannot neutralize, are refused: `delete_device(deviceid="../../user/7")`
    must not delete a user.
    """
    segment = format(value)
    if segment in ("", ".", ".."):
        raise ValueError(f"{segment!r} is not a valid path parameter value")
    return quote(segment, safe=_PATH_SEGMENT_SAFE)


def request_json(
    method: str,
    path: str,
    *,
    api_config_override: Optional[APIConfig] = None,
    query_params: Optional[Dict[str, Any]] = None,
    json_body: Any = None,
    header_params: Optional[Dict[str, Any]] = None,
    expected_status: int = 200,
    operation_name: str = "request",
    error_cls: type[HTTPException] = HTTPException,
) -> Any:
    """Shared REST request execution for generated service methods."""
    api_config = api_config_override if api_config_override else APIConfig()
    # An override replaces the client's config wholesale, credentials included,
    # so one that omits them must fail here rather than send an unauthenticated
    # request (or, before this check, crash inside httpx on a None header).
    if not api_config.auth_email or not api_config.auth_token:
        raise ConfigurationError(
            f"{operation_name}: the APIConfig for this call has no credentials. An "
            "api_config_override replaces the client's config entirely; build it "
            "with client.api_config.with_timeout(...) or pass auth_email and auth_token."
        )

    headers: Dict[str, Any] = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        **auth_headers(api_config.auth_email, api_config.auth_token),
    }
    if header_params:
        headers.update(
            {
                header_name: header_value
                for (header_name, header_value) in header_params.items()
                if header_value is not None
            }
        )

    clean_query_params = {
        key: value for (key, value) in (query_params or {}).items() if value is not None
    }

    try:
        response = api_config.client.request(
            method.lower(),
            httpx.URL(path),
            headers=headers,
            params=clean_query_params,
            json=json_body,
            # Per request, so a with_timeout() copy sharing this client applies its own.
            timeout=api_config.rest_timeout,
        )
    except httpx.RequestError as exc:
        raise TransportError(
            f"{operation_name} transport failed: {exc}",
        ) from exc

    rate_limit = RateLimit.from_headers(response.headers)
    if rate_limit is not None:
        api_config.rate_limits[path] = rate_limit

    try:
        body = _handle_response(
            response,
            method=method,
            path=path,
            expected_status=expected_status,
            operation_name=operation_name,
            error_cls=error_cls,
        )
    except KentikError as exc:
        exc.rate_limit = rate_limit
        raise
    # A plain dict cannot hold an attribute; a subclass can, and the generated
    # function hands the quota on to the model it builds from this body.
    if isinstance(body, dict):
        body = attach_rate_limit(_ResponseBody(body), rate_limit)
    return body


class _ResponseBody(dict):
    """A parsed JSON object that can also carry the call's quota."""


def _handle_response(
    response: httpx.Response,
    *,
    method: str,
    path: str,
    expected_status: int,
    operation_name: str,
    error_cls: type[HTTPException],
) -> Any:
    def _raise_http_error(message: str, *, details: dict[str, Any]) -> None:
        error_factory = getattr(error_cls, "from_response", None)
        if callable(error_factory):
            built_error = error_factory(
                response,
                operation_name=operation_name,
                method=method.upper(),
                path=path,
            )
            if isinstance(built_error, BaseException):
                raise built_error

        raise error_cls(
            response.status_code,
            message,
            method=method.upper(),
            path=path,
            details=details,
        )

    if response.status_code != expected_status:
        preview = response.text[:200].replace("\n", " ")
        content_type = response.headers.get("content-type", "unknown")
        details: dict[str, Any] = {
            "method": method.upper(),
            "path": path,
            "content_type": content_type,
            "preview": preview,
        }
        message = (
            f"{operation_name} failed with status code: {response.status_code} "
            f"(method={method.upper()}, path={path}, content-type={content_type}, preview={preview!r})"
        )

        try:
            payload = response.json()
        except json.JSONDecodeError:
            payload = None

        if isinstance(payload, dict):
            details["response_json"] = payload
            if payload.get("code") is not None:
                details["code"] = payload.get("code")
            if payload.get("message"):
                message = str(payload.get("message"))
            if payload.get("details") is not None:
                details["details"] = payload.get("details")
        elif payload is not None:
            details["response_json"] = payload

        # Handled here, ahead of the generated error_cls, so REST raises the
        # same type gRPC does for UNAUTHENTICATED without regenerating errors.
        if response.status_code == 401:
            raise AuthenticationError(message)

        _raise_http_error(message, details=details)

    if expected_status == 204:
        return None

    try:
        return response.json()
    except json.JSONDecodeError:
        preview = response.text[:200].replace("\n", " ")
        content_type = response.headers.get("content-type", "unknown")
        _raise_http_error(
            (
                f"{operation_name} returned non-JSON response "
                f"(content-type={content_type}, preview={preview!r})"
            ),
            details={
                "method": method.upper(),
                "path": path,
                "content_type": content_type,
                "preview": preview,
            },
        )
