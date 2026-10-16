<!-- HAND-WRITTEN: not modified by [`make generate`](../../Makefile). Edit directly. -->

# OpenAPI Generator Templates

Custom Jinja2 templates fed into `openapi-python-generator` via
`--custom-template-path` (see `openapi_generator_cmd()` in
[../generate_sdk.py](../generate_sdk.py)). They override the
generator's default per-operation and per-module output so every
generated call routes through the shared REST runtime instead of
hand-rolled HTTP code.

## Files

| Template | Replaces | Purpose |
| --- | --- | --- |
| `httpx.jinja2` | Per-operation function body | Writes the operation summary and description as the docstring, builds `query_params`/`header_params`, calls `request_json(...)`, and converts the raw JSON body into the declared Pydantic model or list. The service wrapper copies that docstring. |
| `service.jinja2` | Per-service module header | Imports `request_json` and the wildcard model/`typing` imports every generated operation needs. |
| `models_pydantic_2.jinja2` | Per-model class | Writes the schema title and description as the docstring, and each field's schema text as `Field(description=...)`. |
| `_macros.jinja2` | Nothing (imported) | `docstring()` and `string()` turn schema text into Python literals. |

The generator renders with `autoescape=True`, which writes `"` as `&#34;`.
Schema text must go through a `_macros.jinja2` macro, which escapes it for
Python and marks it `safe`.

## Why these exist

Without a custom template, `openapi-python-generator` emits a direct
`httpx` call per operation. That duplicates auth headers, error
handling, and status checks across every generated
service. `httpx.jinja2` instead calls
[`request_json()`](../../src/kentik_api/core/rest_runtime.py), the
single shared function that owns all of that. See the "shared
connection handler" section of the repository root
[CLAUDE.md](../../CLAUDE.md) for why this pattern must not regress.

```mermaid
flowchart LR
    A[httpx.jinja2] -->|renders per operation| B["def operation(...)"]
    SV[service.jinja2] -->|renders module header| H["import request_json<br/># __ERROR_IMPORTS_PLACEHOLDER__"]
    H -->|"sentinel replaced by<br/>inject_service_error_handling"| EI["from ..error import ..."]
    B -->|calls| C["request_json()"]
    C --> D[httpx.Client]

```

## Editing a template

1. Change the `.jinja2` file here, not the generated output.
2. Regenerate: `uv run python scripts/generate_sdk.py --local-repo
   ../api-schema-public`.
3. Diff a generated service module to confirm the new output shape.
4. Run [`make test-generated`](../../Makefile) to confirm generated calls still exercise
   `request_json` and every declared response status.

> [!WARNING]
> `service.jinja2` must keep emitting both the
> `from kentik_api.core.rest_runtime import request_json` import line and
> the `# __ERROR_IMPORTS_PLACEHOLDER__` sentinel right after it.
> `error_package.inject_service_error_handling()` replaces that sentinel to
> wire in per-service error classes. When the sentinel is missing, it falls
> back to the `request_json` import line. `fixup._fix_path_parameters()` also
> matches that line. When the anchor is missing, generation fails with
> `ValueError`. Rename either anchor only together with both functions.
