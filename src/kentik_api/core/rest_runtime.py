from __future__ import annotations

import json
from typing import Any, Dict, Optional

import httpx

from kentik_api.core.api_config import APIConfig
from kentik_api.errors import HTTPException, TransportError


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

    headers: Dict[str, Any] = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-CH-Auth-Email": api_config.auth_email,
        "X-CH-Auth-API-Token": api_config.auth_token,
    }
    if header_params:
        headers.update({k: v for (k, v) in header_params.items() if v is not None})

    clean_query_params = {
        key: value for (key, value) in (query_params or {}).items() if value is not None
    }

    try:
        with httpx.Client(
            base_url=api_config.base_path, verify=api_config.verify
        ) as client:
            response = client.request(
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
