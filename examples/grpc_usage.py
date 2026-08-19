"""Demonstrate the gRPC transport and explain what is still needed to use it fully.

The SDK generates a complete gRPC bridge for every service:
- proto stubs (pb2 / pb2_grpc) in gen/<service>/pb/
- call_grpc() in core/grpc_runtime.py, the gRPC analogue of request_json()
- service wrappers that route GrpcTransport calls through those stubs

The bridge code is in place.  Two proto dependency groups are not yet
bundled with the SDK:
  1. protoc-gen-openapiv2/options/annotations.proto (from grpc-gateway)
  2. kentik/core/v202303/annotations.proto (Kentik-internal)

Until those are compiled and included, every gRPC call raises:
  NotImplementedError("gRPC proto dependencies not installed for <svc> service")

Once the proto companions are bundled, the call below will work without
any code change -- just swap protocol="rest" for protocol="grpc".

See docs/source/grpc_implementation_spec.md for the full implementation plan.
"""

from kentik_api.client import KentikAPI
from kentik_api.errors import KentikError


def main() -> None:
    # Instantiate with gRPC transport.  The channel opens successfully;
    # the stub load fails silently if proto companions are missing.
    client = KentikAPI(protocol="grpc")

    try:
        response = client.device.list_devices()
        devices = [d for d in (response.devices or []) if d is not None]
        print(f"gRPC: found {len(devices)} device(s).")
        for device in devices[:5]:
            print(f"  {device.id}: {device.deviceName}")
    except NotImplementedError as exc:
        print(f"gRPC not yet available: {exc}")
        print(
            "Install the missing proto companions (see "
            "docs/source/grpc_implementation_spec.md Phase 3) to enable gRPC."
        )
    except KentikError as exc:
        print(f"Kentik API error over gRPC: {exc}")


if __name__ == "__main__":
    main()
