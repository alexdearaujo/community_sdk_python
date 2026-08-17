from __future__ import annotations

import argparse
from typing import Any

from kentik_api.client import KentikAPI
from kentik_api.errors import HTTPException


def run_mock_demo(region: str = "us") -> None:
    """Runs a network-free SDK usage demo by patching one generated REST call."""
    import kentik_api.gen.asset_tags.services.asset_tags as asset_tags_wrapper

    client = KentikAPI(
        email="demo@example.com",
        api_token="demo-token",
        protocol="rest",
        region=region,
    )

    original = asset_tags_wrapper.RestAssetTagsModule1.ListTagKeys

    def _fake_list_tag_keys(*, api_config_override: Any):
        return {"tagKeys": [{"id": "tag-1", "name": "env"}]}

    try:
        asset_tags_wrapper.RestAssetTagsModule1.ListTagKeys = _fake_list_tag_keys
        result = client.asset_tags.list_tag_keys()
        if not isinstance(result, dict) or "tagKeys" not in result:
            raise RuntimeError("Unexpected SDK result shape in mock mode")

        print("SDK sample succeeded (mock mode).")
        print(result)
    finally:
        asset_tags_wrapper.RestAssetTagsModule1.ListTagKeys = original
        client.close()


def run_real_call(region: str = "us") -> None:
    """Runs a real API call using explicit credentials or .env/.environment values."""

    client = KentikAPI(
        protocol="rest",
        region=region,
    )
    try:
        failures = []

        # Try the device inventory endpoint first.
        try:
            result = client.device.list_devices()
            print("SDK sample succeeded (real mode): device.list_devices")
            print(result)
            return
        except HTTPException as exc:
            failures.append(f"device.list_devices -> {exc}")

        # Fallback endpoint with broader availability.
        try:
            result = client.user.list_users()
            print("SDK sample succeeded (real mode): user.list_users")
            print(result)
            return
        except HTTPException as exc:
            failures.append(f"user.list_users -> {exc}")

        joined = "\n".join(failures)
        raise RuntimeError(
            "Real-mode calls failed. This often means the endpoint is unavailable "
            "or the account lacks permissions for that service.\n"
            f"Details:\n{joined}"
        )
    finally:
        client.close()


def main() -> None:
    parser = argparse.ArgumentParser(description="Sample SDK consumer script")
    parser.add_argument(
        "--real",
        action="store_true",
        help=(
            "Perform a real API call using explicit args or credentials loaded from "
            ".env (KENTIK_EMAIL/KENTIK_API_TOKEN)"
        ),
    )
    parser.add_argument(
        "--region",
        default="us",
        choices=["us", "eu"],
        help="Kentik region to target",
    )
    args = parser.parse_args()

    if args.real:
        run_real_call(region=args.region)
    else:
        run_mock_demo(region=args.region)


if __name__ == "__main__":
    main()
