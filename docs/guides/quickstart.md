<!-- HAND-WRITTEN: not modified by [`make generate`](../../Makefile). Edit directly. -->

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

## Make your first call

<!-- kentik-gen:first-call-example -->
```python
from kentik_api.client import KentikAPI

client = KentikAPI(protocol="rest")
response = client.alerting.list_comments()
print(response)  # AlertServiceListCommentsResponse
```
<!-- /kentik-gen:first-call-example -->

## Switch to gRPC

Change one argument:

<!-- kentik-gen:grpc-call-example -->
```python
client = KentikAPI(protocol="grpc")
response = client.alerting.list_comments()  # same API, same response models
```
<!-- /kentik-gen:grpc-call-example -->

See [grpc.md](grpc.md) for the full gRPC guide.

## Next steps

- [REST transport guide](rest.md)
- [gRPC transport guide](grpc.md)
- [Error handling guide](error_handling.md)
- [Runnable examples](../../examples/README.md)

> [!NOTE]
> Run examples with `python -m` from the project root to avoid module naming
> conflicts: `uv run python -m examples.device.rest`
