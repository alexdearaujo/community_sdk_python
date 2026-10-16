<!-- HAND-WRITTEN: not modified by [`make generate`](../../Makefile). Edit directly. -->

# Runtime Tests

Mocked, no network. See the layered strategy in
[../README.md](../README.md) for how this layer fits with the other
four.

## Purpose

`test_rest_runtime.py` tests
[`request_json()`](../../src/kentik_api/core/rest_runtime.py), the one
function every generated REST operation calls. It monkeypatches
`httpx.Client.request` and asserts on the captured method, URL,
headers, params, and body.

`test_grpc_runtime.py` tests
[`map_grpc_error()`](../../src/kentik_api/core/grpc_runtime.py), the
pure function that maps `grpc.RpcError` status codes to SDK exceptions.
It uses a minimal `FakeRpcError` stub and requires no live gRPC channel.

The other files in this layer:

| File | Covers |
| --- | --- |
| `test_api_config.py` | `APIConfig` timeout derivation and validation. |
| `test_connection_reuse.py` | One HTTP client per `KentikAPI`, released by `close()`. |
| `test_credentials.py` | The exact auth wire format for both transports. |
| `test_grpc_end_to_end.py` | A generated wrapper call over a real gRPC channel to an in-process server (T2). |
| `test_grpc_transport.py` | The gRPC transport bounds every call with a deadline. |
| `test_rate_limit.py` | Quota parsing and capture on both transports. |
| `test_rest_deadline.py` | A numeric REST timeout bounds the whole call, not each read. |
| `test_transport_symmetry.py` | The same failure raises the same SDK exception on both transports. |

## Run

```bash
make test-runtime
# or
uv run pytest tests/runtime/
```

## Add a test here

Add a test when shared runtime behavior changes, such as:

1. Header construction
2. Query filtering (dropping `None` values)
3. Expected-status handling
4. Error-raising behavior (`TransportError`, `HTTPException`, and
   generated error-class dispatch)

Run this suite first while editing shared request, auth, or error
behavior in [`src/kentik_api/core`](../../src/kentik_api/core/README.md), before running the broader
[`make test-generated`](../../Makefile) suite.
