# Kentik Community Python SDK

A typed, Pydantic-based Python client for the Kentik API, generated end-to-end from Kentik's public OpenAPI v3 schema. This context covers both the generated SDK's runtime shape and the generator that produces it.

## Language

**Service**:
A top-level grouping of the Kentik API (e.g. `device`, `alerting`, `synthetics`), corresponding to one directory under `src/kentik_api/gen/` and one attribute on `KentikAPI` (e.g. `client.device`).
_Avoid_: module, package

**Operation**:
A single OpenAPI operation — one `operationId`, unique per HTTP method + path within a merged service — that becomes one generated REST function and one method on a service's `ServiceWrapper`.
_Avoid_: endpoint, function, method

**Swagger family**:
The `(service, namespace, filename)` grouping key used to pick the latest version when multiple versioned swagger files exist for the same underlying schema. Only the newest `version` within a family is generated; older versions are ignored.

**Phase module**:
One of the independently testable units in `scripts/generation/` (`parity`, `error_package`, `wrapper_generation`, `docs_rendering`, `endpoint_docs`), each owning one concern of SDK generation and called in sequence by `scripts/generate_sdk.py`'s orchestration.
_Avoid_: generator step, stage

**Service error package**:
The `error/__init__.py` that the `error_package` phase module generates for one service — a base error class, one leaf class per declared error response, and one class per operation, dispatched at runtime via `error_cls.from_response`.

**Parity validation**:
The check that the set of generated service directories exactly matches the set of top-level schema service directories, failing the whole generation run on any mismatch.

**EndpointDocsCollector**:
The two-method object (`extract()`, `render()`) that accumulates per-endpoint documentation while swagger files are available, and renders it as Sphinx stubs only once wrapper generation has produced the real method signatures the rendered examples read from.
_Avoid_: doc builder, doc generator
