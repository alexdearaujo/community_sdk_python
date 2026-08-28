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
example `client.device`.
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
in each family and skips older versions.

**Phase module**:
One of the independently testable units in [`scripts/generation/`](scripts/generation/README.md)
(`parity`, `error_package`, `fixup`, `wrapper_generation`,
`docs_rendering`, `endpoint_docs`). Each phase module owns one concern of SDK
generation; [`scripts/generate_sdk.py`](scripts/generate_sdk.py)'s orchestration calls them in
sequence.
_Avoid_: generator step, stage

**Service error package**:
The `error/__init__.py` file that the `error_package` phase module
generates for one service. It defines a base error class, one leaf
class per declared error response, and one class per operation. The
runtime dispatches errors through `error_cls.from_response`.

**Parity validation**:
The check that compares the set of generated service directories
against the set of top-level schema service directories. If any
directory doesn't match, the check fails the whole generation run.

**EndpointDocsCollector**:
The two-method object (`extract()`, `render()`) that accumulates
per-endpoint documentation. `extract()` runs while swagger files are
available; `render()` builds Sphinx stubs from that documentation
afterward. `render()` must run after wrapper generation, because its
examples read real method signatures that wrapper generation writes.
_Avoid_: doc builder, doc generator
