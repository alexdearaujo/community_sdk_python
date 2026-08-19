"""List devices using the gRPC transport.

Both REST and gRPC transports are fully supported. This script uses
gRPC. It returns the same Pydantic response models as the REST examples.

Run:
    uv run python examples/grpc_usage.py
"""

from kentik_api.client import KentikAPI
from kentik_api.errors import KentikError


def main() -> None:
    client = KentikAPI(protocol="grpc")

    try:
        response = client.device.list_devices()
        devices = [d for d in (response.devices or []) if d is not None]
        print(f"gRPC: found {len(devices)} device(s).")
        for device in devices[:5]:
            print(f"  {device.id}: {device.deviceName}")
    except KentikError as exc:
        print(f"Kentik API error over gRPC: {exc}")


if __name__ == "__main__":
    main()
