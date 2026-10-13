# HAND-WRITTEN: not modified by `make generate`. Edit directly.
"""A numeric REST timeout bounds the whole call, not each read (R5)."""

from __future__ import annotations

import threading
import time
from collections.abc import Iterator
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from typing import Any

import httpx
import pytest

from kentik_api.core.api_config import APIConfig
from kentik_api.core.rest_runtime import request_json
from kentik_api.errors import TransportError

_DRIP_SECONDS = 0.2
_DRIP_CHUNKS = 15


class _DripHandler(BaseHTTPRequestHandler):
    """Answers at once, then sends the body one byte per interval."""

    def do_GET(self) -> None:
        body = b" " * (_DRIP_CHUNKS - 2) + b"{}"
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        for byte in body:
            self.wfile.write(bytes([byte]))
            self.wfile.flush()
            time.sleep(_DRIP_SECONDS)

    def log_message(self, format: str, *args: Any) -> None:
        pass


@pytest.fixture
def drip_server() -> Iterator[str]:
    server = ThreadingHTTPServer(("127.0.0.1", 0), _DripHandler)
    server.daemon_threads = True
    threading.Thread(target=server.serve_forever, daemon=True).start()
    try:
        yield f"http://127.0.0.1:{server.server_address[1]}"
    finally:
        server.shutdown()
        server.server_close()


@pytest.fixture(autouse=True)
def _no_proxy(monkeypatch: pytest.MonkeyPatch) -> None:
    for name in ("HTTP_PROXY", "HTTPS_PROXY", "ALL_PROXY"):
        monkeypatch.delenv(name, raising=False)
        monkeypatch.delenv(name.lower(), raising=False)


def _config(base_path: str, **timeouts: Any) -> APIConfig:
    return APIConfig(
        base_path=base_path, auth_email="dev@example.com", auth_token="t", **timeouts
    )


def _timed_call(config: APIConfig) -> float:
    started = time.monotonic()
    try:
        request_json("GET", "/v1/test", api_config_override=config)
    finally:
        config.close()
    return time.monotonic() - started


def test_a_trickling_body_cannot_outlast_the_timeout(drip_server):
    config = _config(drip_server, timeout=1.0)

    started = time.monotonic()
    with pytest.raises(TransportError, match="ReadTimeout"):
        _timed_call(config)

    # Each read waits at most 1 s, so the call ends within one read of the deadline.
    assert time.monotonic() - started < 1.0 + _DRIP_SECONDS + 0.5


def test_a_numeric_rest_timeout_is_the_deadline(drip_server):
    with pytest.raises(TransportError):
        _timed_call(_config(drip_server, timeout=60.0, rest_timeout=1.0))


def test_a_per_phase_rest_timeout_bounds_each_read_only(drip_server):
    # An httpx.Timeout keeps httpx's meaning: a slow but live body completes.
    elapsed = _timed_call(_config(drip_server, rest_timeout=httpx.Timeout(1.0)))

    assert elapsed > 1.0


def test_with_timeout_keeps_the_deadline_it_does_not_change():
    base = APIConfig(timeout=60.0, rest_timeout=5.0)

    assert base.with_timeout(grpc_deadline=1.0).rest_deadline == 5.0
    assert base.with_timeout(300).rest_deadline == 300
    assert base.with_timeout(rest_timeout=httpx.Timeout(9.0)).rest_deadline is None
