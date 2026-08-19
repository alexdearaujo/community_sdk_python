# gRPC Transport Implementation Spec

This document records the completed implementation of the `GrpcTransport`
path. Both REST and gRPC are fully functional and production-ready.

## Current state (all phases complete)

| Artifact | Location | Status |
| --- | --- | --- |
| Compiled proto stubs | `gen/<service>/pb/*_pb2.py`, `*_pb2_grpc.py` | Done |
| gRPC channel setup | `src/kentik_api/transports/grpc_client.py` | Done |
| `call_grpc()` shared runtime | `src/kentik_api/core/grpc_runtime.py` | Done |
| Service wrapper (REST path) | `gen/<service>/services/<service>.py` | Done |
| Service wrapper (gRPC path) | same file, each method | Done |
| Proto companion bundles | `gen/pb_companions/` | **Done** |

The generator compiles `protoc-gen-openapiv2/options/*.proto` from the
grpc-gateway vendor directory into `gen/pb_companions/` on every
`make generate` run. The companion registry loads all shared proto
descriptors in the correct order before each service pb2 is imported.

## Using gRPC

```python
from kentik_api.client import KentikAPI

client = KentikAPI(protocol="grpc")
response = client.device.list_devices()
print(f"{len(response.devices)} device(s) via gRPC")
```

See `examples/grpc_usage.py` for a runnable demo.

## Why the conversion is tractable

Kentik designed its proto and REST schemas to share the same JSON
representation. The `*_pb2.py` files carry embedded OpenAPI annotations
(the `\x92\x41` extension bytes visible in the serialized descriptors),
confirming field names and structure are intentionally kept in sync.

`google.protobuf.json_format` exploits this:

- `MessageToDict(proto_response)` returns camelCase keys matching what
  the REST JSON returns.
- `ParseDict(camel_case_dict, ProtoRequest())` reconstructs a proto
  message from the same dict.
- Pydantic models use `validation_alias="camelCaseName"` on every
  field, so `ModelClass.model_validate(camel_case_dict)` works without
  any field remapping.

The full round-trip for one operation is four lines:

```python
from google.protobuf.json_format import MessageToDict, ParseDict

# Pydantic → proto request
req_proto = ParseDict(pydantic_request.model_dump(by_alias=True),
                      pb2.CreateDeviceRequest())

# gRPC call
resp_proto = stub.CreateDevice(req_proto)

# proto → Pydantic response
return rest_models.CreateDeviceResponse.model_validate(
    MessageToDict(resp_proto)
)
```

## Known edge cases to resolve before shipping

| Edge case | Risk | Mitigation |
| --- | --- | --- |
| `google.protobuf.Timestamp` ↔ Python `datetime` | `MessageToDict` serializes as RFC 3339 string; Pydantic v2 parses ISO strings to `datetime` natively | Verify in tests; add a `always_print_fields_with_no_presence=True` flag if needed |
| Enum fields | Proto JSON uses string names by default | `MessageToDict` default is string enum names; matches REST JSON |
| `bytes` fields | Proto JSON base64-encodes bytes | Pydantic field type must be `str` (base64) or `bytes`; check per affected service |
| `oneof` fields | Only one branch present in response dict | Pydantic's `Optional` fields already handle absent keys |
| Proto3 optional vs required | All proto3 fields are optional by default | REST models already default all fields to `None`; no change needed |
| Streaming RPCs | All current stubs are `unary_unary` | No streaming operations in the current schema; revisit when added |

## Implementation plan

### Phase 1: Shared gRPC runtime (hand-written, survives regeneration)

**New file: `src/kentik_api/core/grpc_runtime.py`**

```python
import grpc
from google.protobuf.json_format import MessageToDict, ParseDict
from google.protobuf.message import Message
from kentik_api.errors import AuthenticationError, HTTPException, TransportError

_GRPC_STATUS_TO_HTTP: dict[grpc.StatusCode, int] = {
    grpc.StatusCode.INVALID_ARGUMENT:  400,
    grpc.StatusCode.UNAUTHENTICATED:   401,
    grpc.StatusCode.PERMISSION_DENIED: 403,
    grpc.StatusCode.NOT_FOUND:         404,
    grpc.StatusCode.ALREADY_EXISTS:    409,
    grpc.StatusCode.RESOURCE_EXHAUSTED: 429,
    grpc.StatusCode.UNIMPLEMENTED:     501,
    grpc.StatusCode.UNAVAILABLE:       503,
}

def call_grpc(stub_method, proto_request: Message) -> Message:
    """Calls one unary gRPC method and normalizes errors to the SDK hierarchy."""
    try:
        return stub_method(proto_request)
    except grpc.RpcError as exc:
        code = exc.code()
        http_status = _GRPC_STATUS_TO_HTTP.get(code, 500)
        if code == grpc.StatusCode.UNAUTHENTICATED:
            raise AuthenticationError(exc.details()) from exc
        raise HTTPException(
            status_code=http_status,
            message=exc.details(),
            method="gRPC",
            path=stub_method._method.decode(),
        ) from exc
    except Exception as exc:
        raise TransportError(str(exc)) from exc
```

This function is the gRPC analogue of `rest_runtime.request_json`. Every
generated gRPC call routes through it, so error handling stays in one
place.

### Phase 2: Generator changes

**File: `scripts/generation/wrapper_generation.py`**

Two additions to the code-generation loop:

#### 2a. Stub initialization in `__init__`

Replace:

```python
"        if isinstance(self._transport, GrpcTransport):",
"            pass # TODO: Initialize gRPC stub here",
```

With generated code that imports and instantiates the correct stub:

```python
f"from kentik_api.gen.{service}.pb import {service}_pb2_grpc as grpc_stubs",
...
"        if isinstance(self._transport, GrpcTransport):",
f"            self._grpc_stub = grpc_stubs.{title}ServiceStub(self._transport.channel)",
```

The stub class name follows the pattern `{PascalService}ServiceStub`
(confirmed from `DeviceServiceStub` in `device_pb2_grpc.py`).

#### 2b. gRPC call body for each method

The generator already has `func_name_pascal` (e.g., `ListDevices`) and
the REST return type. It needs to:

1. Identify the proto request class: `pb2.{func_name_pascal}Request`
   (exists for every operation with a request body; for query-param-only
   operations, construct an empty message or pass query params as fields).
2. Call `call_grpc(self._grpc_stub.{func_name_pascal}, proto_req)`.
3. Convert the proto response back to the Pydantic type.

Replace:

```python
"        if isinstance(self._transport, GrpcTransport):",
f'            raise NotImplementedError("gRPC translation for {func_name_pascal} is not yet implemented.")',
```

With:

```python
"        if isinstance(self._transport, GrpcTransport):",
f"            _req = ParseDict(_grpc_request_dict, pb2.{func_name_pascal}Request())",
f"            _resp = call_grpc(self._grpc_stub.{func_name_pascal}, _req)",
f"            return {return_type}.model_validate(MessageToDict(_resp))",
```

Where `_grpc_request_dict` is built from the Pydantic request argument
(if present) via `data.model_dump(by_alias=True)`, or from keyword
arguments assembled into a dict for query-parameter-only operations.

### Phase 3: New generator test

**New file: `tests/generator/test_grpc_wrapper_generation.py`**

Unit test for the gRPC wrapper generation, following the pattern of
`test_wrapper_generation.py`. Provides minimal swagger + fake pb2
module and asserts:

- The `__init__` block initializes the stub.
- Each operation's gRPC branch calls `call_grpc`.
- The return line uses `model_validate(MessageToDict(...))`.

### Phase 4: New mocked gRPC test layer

**New file: `tests/runtime/test_grpc_runtime.py`**

Mirrors `test_rest_runtime.py`. Uses `unittest.mock.patch` on the stub
method to:

- Verify `call_grpc` normalizes each `grpc.StatusCode` to the correct
  SDK exception.
- Verify `TransportError` is raised for non-RPC exceptions.
- Verify a successful proto response converts correctly.

Extend `tests/generated/test_wrapper_contracts.py` to cover the gRPC
branch: mock the stub, call each wrapper method via `GrpcTransport`,
assert the mocked stub method was called.

### Phase 5: E2E gRPC tests

Add `protocol="grpc"` as a parameter to the e2e `real_client` fixture
in `tests/e2e/conftest.py`. Run the same read-only operation discovery
against the gRPC transport. The test body does not change; only the
fixture changes. Gate behind a separate `make test-e2e-grpc` target and
a `grpc` pytest marker so it never runs in `make test`.

### Phase 6: Documentation

- Remove the `protocol="rest"` requirement from `KentikAPI()`
  (restore the argument as optional with no functional default, or
  document both transports as equivalent once gRPC is done).
- Update `src/kentik_api/transports/README.md` gRPC-is-stub section.
- Update `examples/README.md` auth section.
- Update the generated service-page snippets to show both transport
  options.

## Acceptance criteria

- `KentikAPI(protocol="grpc")` runs every read operation without error
  against the real Kentik API.
- All mocked tests pass with both `GrpcTransport` and `RestTransport`.
- `make test` still passes with zero changes to the REST path.
- `make test-e2e-grpc` passes with real credentials.

## Open questions

1. **Query-parameter-only operations**: Operations with no request body
   (e.g., `ListDevices` which takes only optional query params) need
   their params assembled into a proto request dict. The generator must
   detect this case. Prototype with `device.ListDevices` first.
2. **Proto message names**: The spec assumes
   `{PascalOperation}Request/Response` always exists. Verify against a
   few services with non-standard naming before generalizing.
3. **Streaming**: `unary_unary` covers all current operations. If Kentik
   adds server-streaming RPCs in a future schema update, `call_grpc`
   must be extended. Leave a comment in the function.
4. **Timestamp/Duration fields**: Services that use `google.protobuf.Timestamp`
   (e.g., audit logs, alerting) need verified round-trip conversion.
   Add targeted tests for these before marking Phase 2 complete.
