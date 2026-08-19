# HAND-WRITTEN: not modified by `make generate`. Edit directly.
"""List all devices in the account — gRPC transport."""

from kentik_api.client import KentikAPI
from kentik_api.errors import KentikError


def main() -> None:
    client = KentikAPI(protocol="grpc")
    try:
        response = client.device.list_devices()
        devices = [device for device in (response.devices or []) if device is not None]
        print(f"Found {len(devices)} device(s).")
        for device in devices[:5]:
            print(f"  {device.id}: {device.deviceName}")
        if len(devices) > 5:
            print(f"  ... and {len(devices) - 5} more.")
    except KentikError as exc:
        print(f"API error over gRPC: {exc}")


if __name__ == "__main__":
    main()
