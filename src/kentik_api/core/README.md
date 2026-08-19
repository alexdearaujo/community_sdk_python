<!-- HAND-WRITTEN: not modified by [`make generate`](../../../Makefile). Edit directly. -->

# Shared REST Runtime (`kentik_api.core`)

Hand-written. Not touched by [`make generate`](../../../Makefile). This is the most
significant hand-written engineering in the SDK: every generated REST
operation, across every service, routes through the one function in
this folder.

## `APIConfig`

`APIConfig` (in [`api_config.py`](api_config.py)) is the shared config object passed to
every generated call: base URL, auth email, auth token, and TLS
`verify`. Generated wrapper methods build one from
[`KentikCredentials`](../auth/credentials.py) and forward it as
`api_config_override`.

## `request_json()`

`request_json()` (in [`rest_runtime.py`](rest_runtime.py)) is the **only** function that
calls `httpx` for REST traffic in this SDK. Every generated operation,
in every one of the ~38 services under
[`src/kentik_api/gen/`](../gen/), calls this same function through the
`service.jinja2` template. See
[`../../scripts/openapi_templates/README.md`](../../../scripts/openapi_templates/README.md).

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
        else status mismatch
            RJ-->>Op: raise error_cls.from_response(...)
        end
    end
```

`request_json()` centralizes:

- Kentik's auth header scheme (`X-CH-Auth-Email` /
  `X-CH-Auth-API-Token`)
- Query-param cleaning (drops `None` values)
- The request itself, via a short-lived `httpx.Client`
- Transport-failure wrapping into `TransportError`
- Status-code checking against each operation's `expected_status`
- JSON error-body parsing (`code`, `message`, `details`)
- Dispatch into the operation's generated error class via
  `error_cls.from_response`

## Extending this layer

Fix or extend `request_json()` or `APIConfig` here. Never add
per-endpoint HTTP, auth, or retry code to a generated service wrapper,
and never inline request logic to "simplify" one call site. See "The
shared connection handler" in the repository root
[CLAUDE.md](../../../CLAUDE.md) for the full rationale and the commits
that shaped this design.
