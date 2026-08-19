# Quick-start examples for the Kentik Community Python SDK

These scripts demonstrate the v6 SDK against the live Kentik API.
Each script is self-contained and safe to run read-only.

## Setup

1. Create `.env` in the repository root:

    ```bash
    KENTIK_EMAIL=you@example.com
    KENTIK_API_TOKEN=your_api_token
    ```

2. Run any example with `python -m` from the project root (the `-m` flag
   prevents `grpc.py` from shadowing the `grpc` package):

    ```bash
    uv run python -m examples.device.rest
    uv run python -m examples.device.grpc
    ```

## Layout

Each service has a `rest.py` and a `grpc.py` that perform the same
operation over each transport. The API surface is identical; only the
`protocol=` argument differs.

| Directory | Service | REST | gRPC |
| --- | --- | --- | --- |
| [`device/`](device/) | Device management | [`rest.py`](device/rest.py) | [`grpc.py`](device/grpc.py) |
| [`user/`](user/) | User management | [`rest.py`](user/rest.py) | [`grpc.py`](user/grpc.py) |
| [`label/`](label/) | Device labels | [`rest.py`](label/rest.py) | [`grpc.py`](label/grpc.py) |
| [`site/`](site/) | Sites and markets | [`rest.py`](site/rest.py) | [`grpc.py`](site/grpc.py) |
| [`alerting/`](alerting/) | Alerting | [`rest.py`](alerting/rest.py) | [`grpc.py`](alerting/grpc.py) |
| [`synthetics/`](synthetics/) | Synthetic tests | [`rest.py`](synthetics/rest.py) | [`grpc.py`](synthetics/grpc.py) |
| [`common/`](common/) | Shared helpers | [`utils.py`](common/utils.py) | [`error_handling.py`](common/error_handling.py) |

## Transport selection

Both transports return the same Pydantic models. Switch with one argument:

```python
client = KentikAPI(protocol="rest")  # REST transport (default)
client = KentikAPI(protocol="grpc")  # gRPC transport
```

See the [gRPC guide](../docs/guides/grpc.md) for transport internals and
sequence diagrams.

## Further reading

- [docs/guides/quickstart.md](../docs/guides/quickstart.md)
- [docs/guides/rest.md](../docs/guides/rest.md)
- [docs/guides/grpc.md](../docs/guides/grpc.md)
- [docs/guides/error_handling.md](../docs/guides/error_handling.md)

```
