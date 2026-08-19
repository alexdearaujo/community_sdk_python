"""Demonstrate SDK error handling — works identically for REST and gRPC."""

from kentik_api.client import KentikAPI
from kentik_api.errors import AuthenticationError, HTTPException, TransportError


def main(protocol: str = "rest") -> None:
    client = KentikAPI(protocol=protocol)

    try:
        devices = client.device.list_devices()
        print(f"Retrieved {len(devices.devices or [])} device(s).")
    except AuthenticationError as exc:
        print(f"Authentication failed: {exc}")
    except HTTPException as exc:
        # Carries status_code, method, path, message, and a details dict.
        print(f"HTTP {exc.status_code} on {exc.method} {exc.path}: {exc.message}")
    except TransportError as exc:
        # Raised when the network request itself fails before a response arrives.
        print(f"Network error: {exc}")


if __name__ == "__main__":
    import sys

    main(protocol=sys.argv[1] if len(sys.argv) > 1 else "rest")
