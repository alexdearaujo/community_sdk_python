<!-- HAND-WRITTEN: not modified by [`make generate`](../Makefile). Edit directly. -->

# Quick-start examples for the Kentik Community Python SDK

These scripts demonstrate the v6 SDK against the live Kentik API.
Each script is self-contained and safe to run read-only.

> [!NOTE]
> The [`examples/`](README.md) directory is **hand-written** and is not generated or
> removed by [`make generate`](../Makefile) or [`make clean`](../Makefile). Edit these files directly
> when adding new examples or updating existing ones.

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
`protocol=` argument differs. `common/error_handling.py` is a standalone
example, not a helper module: pass `grpc` as its first argument to run it over
gRPC.

[`tests/smoke/test_examples_import.py`](../tests/smoke/test_examples_import.py)
imports every example and checks each `client.<service>.<method>(...)` call
against the real client, so an example that stops matching the SDK fails
`make test`.

| Directory | Service | REST | gRPC |
| --- | --- | --- | --- |
| [`device/`](device/) | Device management | [`rest.py`](device/rest.py) | [`grpc.py`](device/grpc.py) |
| [`user/`](user/) | User management | [`rest.py`](user/rest.py) | [`grpc.py`](user/grpc.py) |
| [`label/`](label/) | Device labels | [`rest.py`](label/rest.py) | [`grpc.py`](label/grpc.py) |
| [`site/`](site/) | Sites and markets | [`rest.py`](site/rest.py) | [`grpc.py`](site/grpc.py) |
| [`alerting/`](alerting/) | Alerting | [`rest.py`](alerting/rest.py) | [`grpc.py`](alerting/grpc.py) |
| [`synthetics/`](synthetics/) | Synthetic tests | [`rest.py`](synthetics/rest.py) | [`grpc.py`](synthetics/grpc.py) |
| [`common/`](common/) | Error handling on either transport | [`error_handling.py`](common/error_handling.py) | same file, `grpc` argument |

### V5 query and batch examples

[`v5/`](v5/) holds ports of the 1.x query, batch, and analytics examples.
`client.v5` always uses REST, so these scripts have no gRPC variant. See the
[V5 guide](../docs/sphinx/guides/v5.md).

| Script | What it does |
| --- | --- |
| [`v5/query.py`](v5/query.py) | Top-X data, Data Explorer URL, and chart queries. Read-only |
| [`v5/batch.py`](v5/batch.py) | Flow tag batch. A dry run unless you pass `--send`, which writes to your account |
| [`v5/analytics_topx.py`](v5/analytics_topx.py) | Flat-traffic analysis with pandas. Needs `kentik-api[analytics]`. Read-only |

[`tests/smoke/test_examples_v5.py`](../tests/smoke/test_examples_v5.py) runs
each one against a mocked API.

## Transport selection

Both transports return the same Pydantic models. Switch with one argument:

```python
client = KentikAPI(protocol="rest")  # REST transport (default)
client = KentikAPI(protocol="grpc")  # gRPC transport
```

See the [gRPC guide](../docs/sphinx/guides/grpc.md) for transport internals and
sequence diagrams.

## Further reading

- [docs/sphinx/guides/quickstart.md](../docs/sphinx/guides/quickstart.md)
- [docs/sphinx/guides/rest.md](../docs/sphinx/guides/rest.md)
- [docs/sphinx/guides/grpc.md](../docs/sphinx/guides/grpc.md)
- [docs/sphinx/guides/error_handling.md](../docs/sphinx/guides/error_handling.md)
