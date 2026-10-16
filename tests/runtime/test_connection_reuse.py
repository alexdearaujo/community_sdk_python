# HAND-WRITTEN: not modified by `make generate`. Edit directly.
"""One HTTP client per KentikAPI, released by close() (FR-013, FR-014, SC-009)."""

from __future__ import annotations

import ssl
import urllib.request

import httpcore
import httpx
import pytest

from kentik_api.auth.credentials import KentikCredentials
from kentik_api.core.api_config import APIConfig
from kentik_api.core.rest_runtime import request_json
from kentik_api.errors import ConfigurationError
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
    config = APIConfig(base_path="https://api.example.com", rest_timeout=phases)
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


def test_call_without_a_config_fails_before_opening_a_connection(client_count):
    # With no config there are no credentials, so nothing is sent and no
    # client is created that would then need closing.
    with pytest.raises(ConfigurationError):
        _call(None)

    assert client_count == []


def test_with_timeout_copy_shares_the_origin_connection(client_count):
    transport = RestTransport(KentikCredentials("dev@example.com", "t"))
    slow = transport.api_config.with_timeout(300)

    _call(transport.api_config)
    _call(slow)

    assert len(client_count) == 1
    assert slow.client is transport.api_config.client
    assert slow.rate_limits is transport.api_config.rate_limits


def test_closing_a_copy_leaves_the_origin_open_and_closing_the_origin_ends_both(
    client_count,
):
    transport = RestTransport(KentikCredentials("dev@example.com", "t"))
    slow = transport.api_config.with_timeout(300)
    _call(slow)

    slow.close()
    _call(transport.api_config)
    transport.close()

    with pytest.raises(ConfigurationError, match=r"close\(\)"):
        _call(slow)


def test_shared_client_retries_failed_connection_attempts_only():
    config = APIConfig(base_path="https://api.example.com")
    try:
        transport = config.client._transport
        assert isinstance(transport, httpx.HTTPTransport)
        assert isinstance(transport._pool, httpcore.ConnectionPool)
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


@pytest.fixture
def no_proxy_env(monkeypatch):
    for name in (
        "HTTP_PROXY",
        "HTTPS_PROXY",
        "ALL_PROXY",
        "NO_PROXY",
        "http_proxy",
        "https_proxy",
        "all_proxy",
        "no_proxy",
    ):
        monkeypatch.delenv(name, raising=False)
    # getproxies() also reads macOS and Windows system settings; keep to the env.
    monkeypatch.setattr(
        "httpx._utils.getproxies", urllib.request.getproxies_environment
    )
    return monkeypatch


def _transport_for(config: APIConfig, url: str) -> httpx.HTTPTransport:
    transport = config.client._transport_for_url(httpx.URL(url))
    assert isinstance(transport, httpx.HTTPTransport)
    return transport


def test_rest_goes_direct_without_proxy_variables(no_proxy_env):
    config = APIConfig(base_path="https://api.example.com")
    try:
        assert _transport_for(config, "https://api.example.com/x") is (
            config.client._transport
        )
    finally:
        config.close()


def test_rest_honors_https_proxy(no_proxy_env):
    no_proxy_env.setenv("HTTPS_PROXY", "http://proxy.internal:3128")
    config = APIConfig(base_path="https://api.example.com")
    try:
        pool = _transport_for(config, "https://api.example.com/x")._pool
        assert isinstance(pool, httpcore.HTTPProxy)
        assert pool._proxy_url.host == b"proxy.internal"
        assert pool._ssl_context is not None
        assert pool._ssl_context.verify_mode is ssl.CERT_REQUIRED
    finally:
        config.close()


def test_rest_skips_the_proxy_for_no_proxy_hosts(no_proxy_env):
    no_proxy_env.setenv("HTTPS_PROXY", "http://proxy.internal:3128")
    no_proxy_env.setenv("NO_PROXY", "api.example.com")
    config = APIConfig(base_path="https://api.example.com")
    try:
        assert _transport_for(config, "https://api.example.com/x") is (
            config.client._transport
        )
    finally:
        config.close()


def test_rest_proxy_also_applies_to_a_with_timeout_copy(no_proxy_env):
    no_proxy_env.setenv("HTTPS_PROXY", "http://proxy.internal:3128")
    config = APIConfig(base_path="https://api.example.com")
    try:
        slow = config.with_timeout(300)
        transport = _transport_for(slow, "https://api.example.com/x")
        assert isinstance(transport._pool, httpcore.HTTPProxy)
    finally:
        config.close()
