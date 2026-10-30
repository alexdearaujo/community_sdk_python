<!-- HAND-WRITTEN: not modified by [`uv run poe generate`](../../../pyproject.toml). Edit directly. -->

# Errors (`kentik_api.errors`)

This folder is hand-written. [`uv run poe generate`](../../../pyproject.toml) does not touch it.
It holds the one shared exception hierarchy that every generated per-service error class builds on.

## Hierarchy

```mermaid
%%{init: {"fontFamily": "ui-monospace, SFMono-Regular, Menlo, monospace", "flowchart": {"curve": "step", "nodeSpacing": 30, "rankSpacing": 70, "wrappingWidth": 400}}}%%
classDiagram
    class KentikError {
        <<base>>
        +RateLimit rate_limit
    }
    class HTTPException {
        +int status_code
        +str message
        +str method
        +str path
        +dict details
        +str grpc_status_code
    }
    class GeneratedOperationError {
        <<generated>>
        +from_response()
    }
    KentikError <|-- ConfigurationError
    KentikError <|-- AuthenticationError
    KentikError <|-- TransportError
    KentikError <|-- HTTPException
    HTTPException <|-- GeneratedOperationError
    link KentikError "__init__.py"
    link ConfigurationError "__init__.py"
    link AuthenticationError "__init__.py"
    link TransportError "__init__.py"
    link HTTPException "__init__.py"
```

`GeneratedOperationError` stands in for the per-operation classes that each
service generates under `gen/<service>/error/`.

| Class | Raised when |
| --- | --- |
| `KentikError` | Base class for every SDK-specific error. Catch this to handle any SDK failure. |
| `ConfigurationError` | `KentikAPI(...)` gets missing or empty credentials, an unknown region or protocol, or a timeout that is not a positive number. `APIConfig(...)` gets a timeout that is not a positive number. A gRPC call gets an unknown body key or enum name, or an `api_config_override` that `with_timeout()` did not build. A call runs after `close()`. |
| `AuthenticationError` | The API rejects the credentials on either transport. [`request_json()`](../core/rest_runtime.py) raises it for a REST 401, ahead of the generated error class, and `map_grpc_error()` for a gRPC `UNAUTHENTICATED` status. |
| `TransportError` | No response arrived: `request_json()` on an `httpx.RequestError`, or `map_grpc_error()` for `CANCELLED`, `DEADLINE_EXCEEDED`, `UNAVAILABLE`, an unrecognized code, or a gRPC response over the receive limit. |
| `HTTPException` | The API responded with a fault. Carries `status_code`, `message`, `method`, `path`, a `details` dict (parsed from the response body when possible), and on gRPC the verbatim `grpc_status_code`. A success status with an unusable body raises a plain `HTTPException` with status 502. `details["rpc_status"]` holds the server's `google.rpc.Status` on either transport. |

Every class inherits a `rate_limit` attribute from `KentikError`. The shared
runtimes set it to the quota the API reported on the failing call, or leave it
`None` when no response arrived.

## Generated per-operation error classes

Each service's generated `error/__init__.py` declares a service base class,
such as `DeviceError`. It declares one class for each operation, named after
the client method, such as `ListError` for `device.list`. It also declares a subclass for
each status that the schema declares for that operation. Each operation class
has a `response_error_map` from status code to subclass. `ERROR_BY_METHOD`
maps each client method name to its class.
[`request_json()`](../core/rest_runtime.py) calls `error_cls.from_response(...)`.
[`call_grpc()`](../core/grpc_runtime.py) reads the same map, so both
transports raise the same class. See
[`tests/generated/test_endpoint_schema_coverage.py`](../../../tests/generated/test_endpoint_schema_coverage.py)
for the test that exercises every declared status code against this
mapping.

## Adding a new base error

Add it to [`__init__.py`](__init__.py), next to the existing four, and export it from
`__all__`. Never add a new error type inside a generated
`gen/<service>/error/` file. Every
[`uv run poe generate`](../../../pyproject.toml) run rewrites that file fully.
