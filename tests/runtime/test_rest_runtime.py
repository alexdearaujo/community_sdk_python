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
