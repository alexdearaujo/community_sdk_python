# HAND-WRITTEN: not modified by `make generate`. Edit directly.
from __future__ import annotations

import httpx
import pytest

from kentik_api.client import _REGION_ENDPOINTS, KentikAPI
from kentik_api.errors import ConfigurationError, KentikError


def test_region_endpoints_us_urls():
    grpc_target, rest_url = _REGION_ENDPOINTS["us"]
    assert grpc_target == "grpc.api.kentik.com:443"
    assert rest_url == "https://grpc.api.kentik.com"


def test_region_endpoints_eu_urls():
    grpc_target, rest_url = _REGION_ENDPOINTS["eu"]
    assert grpc_target == "grpc.api.kentik.eu:443"
    assert rest_url == "https://grpc.api.kentik.eu"


def test_invalid_region_raises_configuration_error_naming_it():
    with pytest.raises(ConfigurationError, match="apac") as exc_info:
        KentikAPI(email="a@b.com", api_token="t", region="apac")

    assert isinstance(exc_info.value, KentikError)
    assert not isinstance(exc_info.value, ValueError)


def test_invalid_protocol_raises_configuration_error_naming_it():
    with pytest.raises(ConfigurationError, match="carrier-pigeon"):
        KentikAPI(email="a@b.com", api_token="t", protocol="carrier-pigeon")


def test_missing_credentials_raise_configuration_error(monkeypatch, tmp_path):
    # Run from a directory with no .env above it, so the real one is never loaded.
    monkeypatch.chdir(tmp_path)
    monkeypatch.delenv("KENTIK_EMAIL", raising=False)
    monkeypatch.delenv("KENTIK_API_TOKEN", raising=False)

    with pytest.raises(KentikError, match="KENTIK_EMAIL") as exc_info:
        KentikAPI()

    assert type(exc_info.value) is ConfigurationError


def test_client_mounts_selected_services():
    client = KentikAPI(
        email="dev@example.com",
        api_token="token",
        protocol="rest",
        region="us",
    )
    try:
        assert hasattr(client, "asset_tags")
        assert hasattr(client, "custom_dimension")
        assert hasattr(client, "user")
    finally:
        client.close()


def test_smoke_wrapper_call_through_client(monkeypatch):
    client = KentikAPI(
        email="dev@example.com",
        api_token="token",
        protocol="rest",
        region="us",
    )

    try:
        sentinel = object()

        import kentik_api.gen.asset_tags.services.AssetTagsService as asset_tags_rest

        def _fake_list_tag_keys(**kwargs):
            return sentinel

        monkeypatch.setattr(asset_tags_rest, "ListTagKeys", _fake_list_tag_keys)

        result = client.asset_tags.list_tag_keys()
        assert result is sentinel
    finally:
        client.close()


def test_client_timeout_defaults_to_sixty_seconds_on_both_transports():
    for protocol in ("rest", "grpc"):
        with KentikAPI(email="a@b.com", api_token="t", protocol=protocol) as client:
            config = client._transport.api_config
            assert config.rest_timeout == httpx.Timeout(60.0)
            assert config.grpc_deadline == 60.0


@pytest.mark.parametrize("protocol", ["rest", "grpc"])
def test_client_timeout_reaches_the_transport(protocol):
    with KentikAPI(
        email="a@b.com", api_token="t", protocol=protocol, timeout=5.0
    ) as client:
        config = client._transport.api_config
        assert config.rest_timeout == httpx.Timeout(5.0)
        assert config.grpc_deadline == 5.0
        assert config.base_path == "https://grpc.api.kentik.com"
        assert (config.auth_email, config.auth_token) == ("a@b.com", "t")


def test_client_accepts_per_transport_refinements():
    phases = httpx.Timeout(connect=2.0, read=300.0, write=10.0, pool=5.0)

    with KentikAPI(
        email="a@b.com", api_token="t", rest_timeout=phases, grpc_deadline=120.0
    ) as client:
        assert client._transport.api_config.rest_timeout is phases
        assert client._transport.api_config.grpc_deadline == 120.0


def test_client_rejects_a_non_positive_timeout():
    with pytest.raises(ConfigurationError, match="timeout"):
        KentikAPI(email="a@b.com", api_token="t", timeout=0)
