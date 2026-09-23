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


def test_request_json_applies_the_configured_rest_timeout(
    monkeypatch: pytest.MonkeyPatch,
):
    captured = {}
    real_init = httpx.Client.__init__

    def _spy_init(self, *args, **kwargs):
        captured["timeout"] = kwargs.get("timeout")
        real_init(self, *args, **kwargs)

    monkeypatch.setattr(httpx.Client, "__init__", _spy_init)
    monkeypatch.setattr(
        httpx.Client, "request", lambda self, *a, **k: httpx.Response(200, json={})
    )
    phases = httpx.Timeout(connect=2.0, read=300.0, write=10.0, pool=5.0)

    request_json(
        "GET",
        "/v1/test",
        api_config_override=APIConfig(
            base_path="https://api.example.com", rest_timeout=phases
        ),
    )

    assert captured["timeout"] is phases


# Kentik slows responses by 1.5s past the per-minute soft limit rather than
# failing them (FR-037). Measured healthy latency is about 0.6s.
SOFT_LIMIT_DELAY_SECONDS = 1.5


def test_default_timeout_absorbs_the_soft_limit_delay():
    import threading
    import time
    from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

    class _ThrottledHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            time.sleep(SOFT_LIMIT_DELAY_SECONDS + 0.1)
            body = b'{"ok": true}'
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def log_message(self, *args):
            pass

    server = ThreadingHTTPServer(("127.0.0.1", 0), _ThrottledHandler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    config = APIConfig(
        base_path=f"http://127.0.0.1:{server.server_address[1]}",
        auth_email="dev@example.com",
        auth_token="token",
    )
    try:
        # A throttled call is slow, not failed; it must not surface as TransportError.
        assert request_json("GET", "/v1/test", api_config_override=config) == {
            "ok": True
        }
    finally:
        config.close()
        server.shutdown()
        server.server_close()
