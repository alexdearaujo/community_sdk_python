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
