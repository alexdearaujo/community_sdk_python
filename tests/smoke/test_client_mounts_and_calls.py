# HAND-WRITTEN: not modified by `make generate`. Edit directly.
from __future__ import annotations

import pytest

from kentik_api.client import KentikAPI, _REGION_ENDPOINTS


def test_region_endpoints_us_urls():
    grpc_target, rest_url = _REGION_ENDPOINTS["us"]
    assert grpc_target == "grpc.api.kentik.com:443"
    assert rest_url == "https://grpc.api.kentik.com"


def test_region_endpoints_eu_urls():
    grpc_target, rest_url = _REGION_ENDPOINTS["eu"]
    assert grpc_target == "grpc.api.kentik.eu:443"
    assert rest_url == "https://grpc.api.kentik.eu"


def test_invalid_region_raises_valueerror():
    with pytest.raises(ValueError, match="region"):
        KentikAPI(email="a@b.com", api_token="t", region="apac")


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

        import kentik_api.gen.asset_tags.services.asset_tags as wrapper_module

        def _fake_list_tag_keys(**kwargs):
            return sentinel

        monkeypatch.setattr(
            wrapper_module.RestAssetTagsModule1,
            "ListTagKeys",
            _fake_list_tag_keys,
        )

        result = client.asset_tags.list_tag_keys()
        assert result is sentinel
    finally:
        client.close()
