# Quick-start examples for the Kentik Community Python SDK

These scripts demonstrate the v6 SDK against the live Kentik API.
Each script is self-contained and safe to run read-only.
Mutating operations (create, update, delete) are clearly marked and
commented out by default.

## Setup

1. Create a `.env` file in the repository root:

    ```bash
    KENTIK_EMAIL=you@example.com
    KENTIK_API_TOKEN=your_api_token
    ```

2. Run any example:

    ```bash
    uv run python examples/device/list_devices.py
    uv run python examples/user/list_users.py
    ```

## Layout

| Directory | Service |
| --- | --- |
| `device/` | Device management |
| `user/` | User management |
| `label/` | Device labels |
| `site/` | Sites and site markets |
| `alerting/` | Alerting (alert listing, suppression) |
| `synthetics/` | Synthetic tests and agents |
| `error_handling.py` | Catching SDK errors |
| `utils.py` | Shared helpers used by all scripts |
| `grpc_usage.py` | gRPC transport demo and proto-dep explanation |

## Transport selection

All examples default to REST. gRPC support is generated and the bridge
code is in place, but two proto companion packages are not yet bundled
(see [grpc_implementation_spec.md](../docs/source/grpc_implementation_spec.md)
for the remaining steps). Until they are, every gRPC call raises
`NotImplementedError`. Switch transports by changing the `protocol` arg:

```python
client = KentikAPI(protocol="rest")   # fully supported today
client = KentikAPI(protocol="grpc")   # bridge ready; see grpc_usage.py
```

## Authentication

`KentikAPI()` loads `KENTIK_EMAIL` and `KENTIK_API_TOKEN` from the
nearest `.env` file. Pass credentials explicitly to override:

```python
from kentik_api.client import KentikAPI

client = KentikAPI(protocol="rest", email="you@example.com", api_token="...")
```
