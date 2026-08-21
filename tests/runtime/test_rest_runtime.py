# HAND-WRITTEN: not modified by `make generate`. Edit directly.
from __future__ import annotations

import httpx
import pytest

from kentik_api.core.api_config import APIConfig, HTTPException
from kentik_api.core.rest_runtime import request_json


def test_request_json_success_builds_headers_and_filters_query(
    monkeypatch: pytest.MonkeyPatch,
):
    captured = {}

    def _fake_request(self, method, url, headers=None, params=None, json=None):
        captured["method"] = method
        captured["url"] = str(url)
        captured["headers"] = headers
        captured["params"] = params
        captured["json"] = json
        return httpx.Response(200, json={"ok": True})

    monkeypatch.setattr(httpx.Client, "request", _fake_request)

    cfg = APIConfig(
        base_path="https://api.example.com",
        auth_email="dev@example.com",
        auth_token="token",
        verify=True,
    )

    result = request_json(
        method="POST",
        path="/v1/test",
        api_config_override=cfg,
        query_params={"keep": 1, "drop": None},
        json_body={"hello": "world"},
        expected_status=200,
        operation_name="UnitTest",
    )

    assert result == {"ok": True}
    assert captured["method"] == "post"
    assert captured["url"] == "/v1/test"
    assert captured["headers"]["X-CH-Auth-Email"] == "dev@example.com"
    assert captured["headers"]["X-CH-Auth-API-Token"] == "token"
    assert captured["params"] == {"keep": 1}
    assert captured["json"] == {"hello": "world"}


def test_request_json_returns_none_for_204(monkeypatch: pytest.MonkeyPatch):
    def _fake_request(self, method, url, headers=None, params=None, json=None):
        return httpx.Response(204)

    monkeypatch.setattr(httpx.Client, "request", _fake_request)

    result = request_json(method="GET", path="/v1/no-content", expected_status=204)
    assert result is None


def test_request_json_raises_http_exception_on_unexpected_status(
    monkeypatch: pytest.MonkeyPatch,
):
    def _fake_request(self, method, url, headers=None, params=None, json=None):
        return httpx.Response(500, json={"error": "boom"})

    monkeypatch.setattr(httpx.Client, "request", _fake_request)

    with pytest.raises(HTTPException) as exc:
        request_json(
            method="GET",
            path="/v1/fail",
            expected_status=200,
            operation_name="FailingOp",
        )

    assert exc.value.status_code == 500
    assert "FailingOp failed with status code: 500" in str(exc.value)


# ---------------------------------------------------------------------------
# Injected http_client path (via APIConfig.http_client)
# ---------------------------------------------------------------------------


def test_request_json_uses_injected_client_when_set():
    """When api_config.http_client is set, request_json must use it (no new client)."""
    captured: dict = {}

    transport = httpx.MockTransport(
        lambda req: (
            captured.__setitem__("called", True)
            or httpx.Response(200, json={"ok": True})
        )
    )
    client = httpx.Client(base_url="https://api.example.com", transport=transport)

    cfg = APIConfig(
        base_path="https://api.example.com",
        auth_email="dev@example.com",
        auth_token="token",
        http_client=client,
    )

    result = request_json(method="GET", path="/v1/test", api_config_override=cfg)
    assert result == {"ok": True}
    assert captured.get("called"), "Injected client was not used"
    client.close()


def test_rest_transport_close_closes_owned_client():
    """RestTransport.close() must close the internal httpx.Client."""
    from kentik_api.auth.credentials import KentikCredentials
    from kentik_api.transports.rest_client import RestTransport

    transport = RestTransport(
        KentikCredentials("a@b.com", "token"), base_url="https://api.example.com"
    )
    assert not transport._client.is_closed
    transport.close()
    assert transport._client.is_closed
