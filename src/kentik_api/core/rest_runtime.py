# HAND-WRITTEN: not modified by `make generate`. Edit directly.
from __future__ import annotations

import json
from typing import Any, Dict, Optional

import httpx
from kentik_api.auth.credentials import auth_headers
from kentik_api.core.api_config import APIConfig
from kentik_api.core.rate_limit import RateLimit
from kentik_api.errors import (
    AuthenticationError,
    HTTPException,
    KentikError,
    TransportError,
)


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
    # A config made here is used for one call only, so this call must close it.
    owns_config = not api_config_override
    api_config = api_config_override if api_config_override else APIConfig()

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
        )
    except httpx.RequestError as exc:
        raise TransportError(
            f"{operation_name} transport failed: {exc}",
        ) from exc
    finally:
        if owns_config:
            api_config.close()

    rate_limit = RateLimit.from_headers(response.headers)
    if rate_limit is not None:
        api_config.rate_limits[path] = rate_limit

    try:
        return _handle_response(
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
