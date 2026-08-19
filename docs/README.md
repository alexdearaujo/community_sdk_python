# Kentik Community Python SDK — Documentation

All documentation for the SDK is in or linked from this directory.

## Where to start

| Document | What it covers |
| --- | --- |
| [Quick start](guides/quickstart.md) | Install, configure credentials, make your first call |
| [REST transport guide](guides/rest.md) | HTTP/REST usage, pagination, and tips |
| [gRPC transport guide](guides/grpc.md) | gRPC usage, sequence diagrams, and transport comparison |
| [Error handling guide](guides/error_handling.md) | Exception hierarchy and how to catch each type |
| [SDK generation workflow](guides/generation.md) | How to regenerate the SDK from the OpenAPI schema |

## Examples

Runnable scripts live in [examples/](../examples/README.md). Each service has
a REST and a gRPC variant side by side:

```
examples/
  device/   rest.py  grpc.py
  user/     rest.py  grpc.py
  label/    rest.py  grpc.py
  site/     rest.py  grpc.py
  alerting/ rest.py  grpc.py
  synthetics/ rest.py  grpc.py
  common/   utils.py  error_handling.py
```

## Sphinx HTML documentation

Run [`make docs`](../Makefile) to build the full HTML reference from
[docs/sphinx/](sphinx/README.md). The HTML output includes per-endpoint
parameter tables, response tables, model schemas, and interactive Mermaid
diagrams.

## Source code documentation

Each package directory has a README that explains its role:

- [src/kentik_api/](../src/kentik_api/README.md) — package overview and request flow
- [src/kentik_api/auth/](../src/kentik_api/auth/README.md) — credential loading
- [src/kentik_api/core/](../src/kentik_api/core/README.md) — shared REST/gRPC runtime
- [src/kentik_api/errors/](../src/kentik_api/errors/README.md) — exception hierarchy
- [src/kentik_api/transports/](../src/kentik_api/transports/README.md) — transport layer
- [src/kentik_api/gen/](../src/kentik_api/gen/README.md) — generated services
- [scripts/](../scripts/README.md) — SDK generator and tooling
- [tests/](../tests/README.md) — test suite structure
