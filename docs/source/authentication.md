# Authentication

The SDK supports loading Kentik API credentials from a project-level `.env` file.

For a runtime-level dependency map that shows how credentials and transports
connect to generated services, see
[SDK Runtime Architecture](sdk_runtime_architecture.md).

## .env Setup

Create `.env` at your project root:

```bash
KENTIK_EMAIL=you@example.com
KENTIK_API_TOKEN=your_api_token
```

## How Credentials Are Resolved

When you initialize `KentikAPI`:

```python
from kentik_api.client import KentikAPI

client = KentikAPI(protocol="rest", region="us")
```

the client will:

1. Load the nearest `.env` from the current working directory.
2. Read `KENTIK_EMAIL` and `KENTIK_API_TOKEN`.

You can also pass credentials directly:

```python
client = KentikAPI(
    email="you@example.com",
    api_token="your_api_token",
    protocol="rest",
    region="us",
)
```

If both are provided, explicit constructor values are used.

## Required Variables

- `KENTIK_EMAIL`
- `KENTIK_API_TOKEN`

If neither explicit credentials nor environment values are available,
client initialization raises an error.
