# HAND-WRITTEN: not modified by `make generate`. Edit directly.
"""One HTTP client per KentikAPI, released by close() (FR-013, FR-014, SC-009)."""

from __future__ import annotations

import httpx
import pytest

from kentik_api.auth.credentials import KentikCredentials
from kentik_api.core.api_config import APIConfig
from kentik_api.core.rest_runtime import request_json
from kentik_api.errors import ConfigurationError, TransportError
from kentik_api.transports.rest_client import RestTransport


@pytest.fixture
def client_count(monkeypatch: pytest.MonkeyPatch) -> list[httpx.Client]:
    """Records every httpx.Client created, with requests answered in memory."""
    created: list[httpx.Client] = []
    real_init = httpx.Client.__init__

    def _counting_init(self, *args, **kwargs):
        real_init(self, *args, **kwargs)
        created.append(self)

    monkeypatch.setattr(httpx.Client, "__init__", _counting_init)
    monkeypatch.setattr(
        httpx.Client, "request", lambda self, *a, **k: httpx.Response(200, json={})
    )
    return created


def _call(config: APIConfig | None) -> None:
    request_json("GET", "/v1/test", api_config_override=config)


def test_repeat_calls_on_one_transport_share_one_client(client_count):
    transport = RestTransport(KentikCredentials("dev@example.com", "t"))

    for _ in range(5):
        _call(transport.api_config)

    assert len(client_count) == 1
    assert transport.api_config.client is client_count[0]


def test_shared_client_honours_the_configured_timeout_and_base_url():
    phases = httpx.Timeout(connect=2.0, read=300.0, write=10.0, pool=5.0)
    config = APIConfig(
        base_path="https://api.example.com", rest_timeout=phases, verify=False
    )
    try:
        assert config.client.timeout == phases
        assert str(config.client.base_url) == "https://api.example.com"
    finally:
        config.close()


def test_no_client_is_created_until_a_rest_call_needs_one(client_count):
    APIConfig()

    assert client_count == []


def test_close_releases_the_client_and_is_idempotent():
    transport = RestTransport(KentikCredentials("dev@example.com", "t"))
    client = transport.api_config.client

    transport.close()
    transport.close()

    assert client.is_closed


def test_closing_an_unused_transport_is_harmless():
    RestTransport(KentikCredentials("dev@example.com", "t")).close()


def test_use_after_close_raises_configuration_error_naming_close(client_count):
    transport = RestTransport(KentikCredentials("dev@example.com", "t"))
    transport.close()

    with pytest.raises(ConfigurationError, match=r"close\(\)"):
        _call(transport.api_config)


def test_one_off_config_is_closed_after_its_single_call(client_count):
    _call(None)
    _call(None)

    # The fallback path makes a fresh config each call, and must not leak it.
    assert len(client_count) == 2
    assert all(client.is_closed for client in client_count)


def test_one_off_config_is_closed_even_when_the_call_fails(monkeypatch):
    created: list[httpx.Client] = []
    real_init = httpx.Client.__init__

    def _counting_init(self, *args, **kwargs):
        real_init(self, *args, **kwargs)
        created.append(self)

    def _fail(self, *args, **kwargs):
        raise httpx.ConnectError("refused")

    monkeypatch.setattr(httpx.Client, "__init__", _counting_init)
    monkeypatch.setattr(httpx.Client, "request", _fail)

    with pytest.raises(TransportError):
        _call(None)

    assert created and created[0].is_closed


def test_shared_client_retries_failed_connection_attempts_only():
    config = APIConfig(base_path="https://api.example.com")
    try:
        transport = config.client._transport
        assert isinstance(transport, httpx.HTTPTransport)
        # httpcore retries connection establishment only; a sent request is never replayed.
        assert transport._pool._retries == 2
    finally:
        config.close()


def test_transports_expose_quota_per_endpoint_from_their_config():
    from kentik_api.transports.grpc_client import GrpcTransport

    rest = RestTransport(KentikCredentials("dev@example.com", "t"))
    grpc_transport = GrpcTransport(
        KentikCredentials("dev@example.com", "t"), target="127.0.0.1:1"
    )
    try:
        assert rest.rate_limits is rest.api_config.rate_limits
        assert grpc_transport.rate_limits is grpc_transport.api_config.rate_limits
    finally:
        rest.close()
        grpc_transport.close()
