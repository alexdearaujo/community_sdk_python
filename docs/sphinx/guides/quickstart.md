<!-- HAND-WRITTEN prose, except the `kentik-gen` marker blocks, which [`make generate`](../../../Makefile) rewrites. Fix those in scripts/generation/docs_rendering.py. -->

# Quick Start

Install the SDK and make your first API call in under five minutes.

## Prerequisites

- Python 3.12 or later
- [uv](https://github.com/astral-sh/uv) package manager

## Install

```bash
pip install kentik-api
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
response = client.as_group.list_as_groups()
print(response)  # ListASGroupsResponse
```
<!-- /kentik-gen:first-call-example -->

## Switch to gRPC

Change one argument:

<!-- kentik-gen:grpc-call-example -->
```python
client = KentikAPI(protocol="grpc")
response = client.as_group.list_as_groups()  # same API, same response models
```
<!-- /kentik-gen:grpc-call-example -->

See [grpc.md](grpc.md) for the full gRPC guide.

## Set a timeout

Every call is bounded: 60 seconds by default, on both transports. Set it for the
whole client:

```python
client = KentikAPI(timeout=10)
```

Or give one slow call more time, without a second client:

```python
slow = client.api_config.with_timeout(300)
response = client.device.list_devices(api_config_override=slow)
```

`with_timeout()` copies the client's configuration and can change only the
timeouts. It shares the client's connection and credentials. A config passed as
`api_config_override` replaces the client's for that one call, so an override
built any other way must carry its own credentials.

## Next steps

- [REST transport guide](rest.md)
- [gRPC transport guide](grpc.md)
- [Error handling guide](error_handling.md)
- [Runnable examples](https://github.com/kentik/community_sdk_python/blob/main/examples/README.md)

> [!NOTE]
> Run examples with `python -m` from the project root to avoid module naming
> conflicts: `uv run python -m examples.device.rest`
