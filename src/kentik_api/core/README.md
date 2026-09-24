<!-- HAND-WRITTEN: not modified by [`make generate`](../../../Makefile). Edit directly. -->

# Shared Runtime (`kentik_api.core`)

Hand-written. Not touched by [`make generate`](../../../Makefile). This is the most
significant hand-written engineering in the SDK: every generated
operation, across every service, routes through one function in this
folder: [`request_json()`](rest_runtime.py) for REST, and
[`call_grpc()`](grpc_runtime.py) for gRPC.

## `APIConfig`

`APIConfig` (in [`api_config.py`](api_config.py)) is the shared config object passed to
every generated call: base URL, auth email, auth token, and TLS
`verify`. [`RestTransport`](../transports/rest_client.py) builds one
from [`KentikCredentials`](../auth/credentials.py) once, in `__init__`.
Generated wrapper methods read `api_config` off the transport and
forward it as `api_config_override`.

## `request_json()`

`request_json()` (in [`rest_runtime.py`](rest_runtime.py)) is the **only** function that
calls `httpx` for REST traffic in this SDK. Every generated operation,
in every one of the 35 services mounted on the client, under
[`src/kentik_api/gen/`](../gen/README.md), calls this same function through the
`httpx.jinja2` template. See
[`scripts/openapi_templates/`](../../../scripts/openapi_templates/README.md).

```mermaid
sequenceDiagram
    participant Op as Generated operation
    participant RJ as request_json
    participant HX as httpx.Client
    participant API as Kentik API
    Op->>RJ: api_config, params, expected_status
    RJ->>RJ: add auth headers, clean query params
    alt network failure
        RJ->>HX: send request
        HX-->>RJ: httpx.RequestError
        RJ-->>Op: raise TransportError
    else response received
        RJ->>HX: send request
        HX->>API: HTTP request
        API-->>HX: HTTP response
        HX-->>RJ: response
        alt status == expected
            RJ-->>Op: parsed JSON
        else status == 401
            RJ-->>Op: raise AuthenticationError
        else status mismatch
            RJ-->>Op: raise error_cls.from_response(...)
        end
    end
```

## `map_grpc_error()` and `call_grpc()`

`map_grpc_error()` (in [`grpc_runtime.py`](grpc_runtime.py)) is a pure function:
no I/O, no side effects, testable without a gRPC channel. It maps a
`grpc.RpcError` status code to the SDK exception hierarchy (`AuthenticationError`,
`HTTPException`, or `TransportError`), classifying every non-OK code explicitly. `call_grpc()` is the thin caller that invokes the gRPC stub
and delegates all error mapping to `map_grpc_error()`.

```mermaid
sequenceDiagram
    participant W as Generated wrapper
    participant CG as call_grpc
    participant MG as map_grpc_error
    participant S as gRPC stub
    W->>CG: stub_method, proto_request
    CG->>S: invoke
    alt success
        S-->>CG: proto response
        CG-->>W: proto response
    else grpc.RpcError
        S-->>CG: RpcError
        CG->>MG: exc, method, path
        MG-->>CG: AuthenticationError (UNAUTHENTICATED)<br/>or HTTPException
        CG-->>W: raise
    else other exception
        S-->>CG: Exception
        CG-->>W: raise TransportError
    end
```

`request_json()` centralizes:

- Kentik's auth headers, built by `auth_headers()` in
  [`auth/credentials.py`](../auth/credentials.py), the scheme's single
  definition
- Query-param cleaning (drops `None` values)
- The request itself, via the one `httpx.Client` its `APIConfig` owns, so
  every call through a `KentikAPI` reuses a pooled connection instead of
  opening a new TLS session each time. `KentikAPI.close()` releases it, and
  a call after that raises `ConfigurationError`.
- Transport-failure wrapping into `TransportError`
- Status-code checking against each operation's `expected_status`
- JSON error-body parsing (`code`, `message`, `details`)
- Dispatch into the operation's generated error class via
  `error_cls.from_response`

## Concurrency

`httpx.Client` is thread-safe, so one `KentikAPI` can be shared across
threads. That does not make parallel calls useful: Kentik allows **one
concurrent request** for non-query APIs, where a request counts as concurrent
if it arrives before the previous one is answered. No response header reports
this limit. Throughput is capped by the API, not by this client, so calling
from several threads mostly queues requests on the server.

A caller that invokes a generated REST function directly with no
`api_config_override` gets a fresh `APIConfig`, and therefore a fresh client,
for that one call; `request_json()` closes it afterwards. The mounted
`KentikAPI` wrappers always pass their shared config.

## Extending this layer

Fix or extend `request_json()` or `APIConfig` here. Never add
per-endpoint HTTP, auth, or retry code to a generated service wrapper,
and never inline request logic to "simplify" one call site. See "The
shared connection handler" in the repository root
[CLAUDE.md](../../../CLAUDE.md) for the full rationale and the commits
that shaped this design.
