"""List all devices in the account."""

from kentik_api.client import KentikAPI


def main() -> None:
    client = KentikAPI()  # loads KENTIK_EMAIL / KENTIK_API_TOKEN from .env
    response = client.device.list_devices()
    devices = response.devices or []
    print(f"Found {len(devices)} device(s).")
    for device in devices[:5]:  # show first five
        print(f"  {device.id}: {device.deviceName}")
    if len(devices) > 5:
        print(f"  ... and {len(devices) - 5} more.")


if __name__ == "__main__":
    main()
