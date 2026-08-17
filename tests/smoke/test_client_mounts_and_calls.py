from __future__ import annotations

from kentik_api.client import KentikAPI


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
