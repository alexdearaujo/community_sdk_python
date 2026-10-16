<!-- HAND-WRITTEN: not modified by [`make generate`](Makefile). Edit directly. -->

# Kentik Community Python SDK

This SDK is a typed Python client for the Kentik API, built on
Pydantic v2. [`scripts/generate_sdk.py`](scripts/generate_sdk.py) generates it from Kentik's
public OpenAPI v3 schema. This context covers the generated SDK's
runtime shape and the generator that builds it.

## Language

**Service**:
A top-level grouping of the Kentik API, for example `device`,
`alerting`, or `synthetics`. Each service maps to one directory
under [`src/kentik_api/gen/`](src/kentik_api/gen/README.md) and one attribute on `KentikAPI`, for
example `client.device`. Not every directory there is a Service: the
generator also writes internal directories for itself, currently
`pb_companions` (the shared proto descriptor registry). `iter_service_dirs()`
in [`scripts/generation/_shared.py`](scripts/generation/_shared.py) is the one
place that decides which is which. A Service with no operations is still a
Service.
_Avoid_: module, package

**Operation**:
A single OpenAPI operation: one `operationId`, unique per HTTP
method and path within a merged service. Each operation becomes one
generated REST function and one method on a service's
`ServiceWrapper`.
_Avoid_: endpoint, function, method

**Swagger family**:
The `(service, namespace, filename)` grouping key that the generator
uses to pick the latest schema version, when multiple versioned
swagger files exist. The generator generates only the newest version
in each family and skips older versions. It also skips a file when
newer files in its service write all of that file's REST modules.

**Phase module**:
One of the independently testable units in [`scripts/generation/`](scripts/generation/README.md)
(`parity`, `error_package`, `fixup`, `wrapper_generation`,
`docs_rendering`, `endpoint_docs`, `api_surface`, `public_names`). Each phase module owns one concern of SDK
generation; [`scripts/generate_sdk.py`](scripts/generate_sdk.py)'s orchestration calls them in
sequence.
_Avoid_: generator step, stage

**Service error package**:
The `error/__init__.py` file that the `error_package` phase module
generates for one service. It defines a base error class, one class
per operation, named after the operation's client method
(`ListLabelsError`), and one leaf class per declared error response.
The runtime dispatches errors through `error_cls.from_response`.

**Parity validation**:
The check that compares the set of generated service directories
against the public names that `public_names.json` gives the top-level
schema service directories. If any
directory doesn't match, the check fails the whole generation run.

**EndpointDocsCollector**:
The object with three methods (`extract()`, `render()`, `write_record()`) that accumulates
per-endpoint documentation. `extract()` runs while swagger files are
available; `render()` builds Sphinx stubs from that documentation
afterward. `render()` must run after wrapper generation, because its
examples read real method signatures that wrapper generation writes.
`write_record()` writes `schema_operations.json`.
_Avoid_: doc builder, doc generator
