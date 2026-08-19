# Errors (`kentik_api.errors`)

Hand-written. Not touched by `make generate`. This is the one shared
exception hierarchy every generated per-service error class builds on.

## Hierarchy

```mermaid
classDiagram
    class KentikError {
        <<base>>
    }
    class HTTPException {
        +int status_code
        +str message
        +str method
        +str path
        +dict details
        +from_response()
    }
    class GeneratedOperationError {
        <<generated>>
    }
    KentikError <|-- ConfigurationError
    KentikError <|-- AuthenticationError
    KentikError <|-- TransportError
    KentikError <|-- HTTPException
    HTTPException <|-- GeneratedOperationError

    link KentikError "src/kentik_api/errors/__init__.py"
    link ConfigurationError "src/kentik_api/errors/__init__.py"
    link AuthenticationError "src/kentik_api/errors/__init__.py"
    link TransportError "src/kentik_api/errors/__init__.py"
    link HTTPException "src/kentik_api/errors/__init__.py"
    link GeneratedOperationError "src/kentik_api/gen"
```

`GeneratedOperationError` stands in for the per-operation classes each
service generates under `gen/<service>/error/`.

| Class | Raised when |
| --- | --- |
| `KentikError` | Base class for every SDK-specific error. Catch this to handle any SDK failure. |
| `ConfigurationError` | An `APIConfig` value is invalid. |
| `AuthenticationError` | Authentication or authorization fails. |
| `TransportError` | The transport layer fails before a response arrives (raised by [`request_json()`](../core/rest_runtime.py) on an `httpx.RequestError`). |
| `HTTPException` | An HTTP response doesn't match the operation's expected status. Carries `status_code`, `message`, `method`, `path`, and a `details` dict (parsed from the response body when possible). |

## Generated per-operation error classes

Each service's generated `error/__init__.py` declares one `HTTPException`
subclass per operation, plus a `response_error_map` from status code to
class. `request_json()` calls `error_cls.from_response(...)` to build
the right one. See
[`tests/generated/test_endpoint_schema_coverage.py`](../../../tests/generated/test_endpoint_schema_coverage.py)
for how every declared status code gets exercised against this
mapping.

## Adding a new base error

Add it here, alongside the existing four, and export it from
`__all__`. Never add a new error type inside a generated
`gen/<service>/error/` file; that file is fully regenerated on every
`make generate` run.
