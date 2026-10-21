<!-- HAND-WRITTEN prose, except the `kentik-gen` marker blocks, which [`uv run poe generate`](../../../pyproject.toml) rewrites. Fix those in scripts/generation/docs_rendering.py. -->

# Quick Start

Install the SDK and make your first API call in under five minutes.

## Prerequisites

- Python 3.12 or later
- [uv](https://github.com/astral-sh/uv) package manager

## Install

```bash
pip install -U "kentik-api>=2"
```

Or with uv in a project:

```bash
uv add kentik-api
```

## Configure credentials

Create `.env` at your project root:

```bash
KENTIK_EMAIL=you@example.com
KENTIK_API_TOKEN=your_api_token
```

The SDK loads these automatically. You can also pass them explicitly:

```python
from kentik_api.client import KentikAPI

client = KentikAPI(
    email="you@example.com",
    api_token="your_api_token",
    protocol="rest",
)
```

To keep credentials encrypted instead of in a plaintext `.env`, see
[Authentication](../authentication.md).

## Make your first call

<!-- kentik-gen:first-call-example -->
```python
from kentik_api.client import KentikAPI

client = KentikAPI(protocol="rest")
response = client.as_group.list()
print(response)  # ListASGroupsResponse
```
<!-- /kentik-gen:first-call-example -->

## Switch to gRPC

Change one argument:

<!-- kentik-gen:grpc-call-example -->
```python
client = KentikAPI(protocol="grpc")
response = client.as_group.list()  # same API, same response models
```
<!-- /kentik-gen:grpc-call-example -->

See [grpc.md](grpc.md) for the full gRPC guide.

## Set a timeout

Every call uses a timeout: 60 seconds by default, on both transports.
Set it for the whole client:

```python
client = KentikAPI(timeout=10)
```

Or give one slow call more time, without a second client:

```python
slow = client.api_config.with_timeout(300)
response = client.device.list(api_config_override=slow)
```

`with_timeout()` copies the client's configuration and can change only the
timeouts. It shares the client's connection and credentials. A config passed as
`api_config_override` replaces the client's for that one call, so an override
built any other way must carry its own credentials.

Timeout settings are read-only. The SDK copies any supplied
`httpx.Timeout`, and `client.api_config.rest_timeout` returns a detached
snapshot. Changing either object does not change active settings.
Use `with_timeout()` rather than changing the returned timeout object.

A number is a total deadline for the call. To bound each REST phase separately
instead, as httpx does, pass `rest_timeout=httpx.Timeout(...)`: a slow body then
keeps the call open for as long as each read arrives in time.
REST total deadlines are cooperative. A blocking operation can finish
after the deadline rather than stopping at an exact wall-clock instant.

## Next steps

- [REST transport guide](rest.md)
- [gRPC transport guide](grpc.md)
- [Error handling guide](error_handling.md)
- [Runnable examples](https://github.com/kentik/community_sdk_python/blob/main/examples/README.md)

> [!NOTE]
> Run examples with `python -m` from the project root to avoid module naming
> conflicts: `uv run python -m examples.device.rest`
