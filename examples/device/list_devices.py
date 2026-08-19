"""List all devices in the account."""

from kentik_api.client import KentikAPI


def main() -> None:
    client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL / KENTIK_API_TOKEN from .env
    response = client.device.list_devices()
    devices = [device for device in (response.devices or []) if device is not None]
    print(f"Found {len(devices)} device(s).")
    for device in devices[:5]:  # show first five
        print(f"  {device.id}: {device.deviceName}")
    if len(devices) > 5:
        print(f"  ... and {len(devices) - 5} more.")


if __name__ == "__main__":
    main()
