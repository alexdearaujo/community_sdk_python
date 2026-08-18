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

## Authentication

`KentikAPI()` with no arguments loads `KENTIK_EMAIL` and
`KENTIK_API_TOKEN` from the nearest `.env` file.
Pass them explicitly to override:

```python
from kentik_api.client import KentikAPI

client = KentikAPI(email="you@example.com", api_token="...")
```
