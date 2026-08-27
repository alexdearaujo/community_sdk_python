<!-- HAND-WRITTEN: not modified by [`make generate`](../../Makefile). Edit directly. -->

# Generator Tests

Mocked, no network. Unit tests for the SDK generator itself (see
[scripts/generation/README.md](../../scripts/generation/README.md)),
not for the SDK it produces. See the layered strategy in
[../README.md](../README.md) for how this layer fits with the other
four.

## Files

| File | Covers |
| --- | --- |
| `test_parity.py` | Swagger selection and generated/schema directory parity. |
| `test_error_package.py` | Error class naming, error-response extraction and merging, and the runtime error-dispatch injection seam (including the `ValueError` guard when the anchor is absent). |
| `test_fixup.py` | Post-generation fixups: `models/__init__.py` rebuild, wildcard-export replacement, file-level content patches, function deduplication, and docstring normalization. |
| `test_wrapper_generation.py` | Annotation qualification and end-to-end wrapper and client-mixin generation against a temp directory. |
| `test_rest_module_parser.py` | `scripts/generation/_shared.py`'s `parse_generated_rest_module()`, the shared REST-operation parser `tests/_discovery.py` also uses. |
| `test_endpoint_docs.py` | `parse_wrapper_methods()`/wrapper-signature parsing in `scripts/generation/endpoint_docs.py` and `_shared.py`. |
| `test_docs_rendering.py` | `scripts/generation/docs_rendering.py`'s `_GROUP_CONFIG`/`_module_group`/`_LAYER_NAMES` consistency (architecture-diagram module grouping). |
| `test_generate_sdk.py` | `scripts/generate_sdk.py`'s top-level helpers: schema-name cleanup, request-body `$ref` inlining, generated gRPC import rewriting, and the validate-before-clean ordering guard. |

## Run

```bash
make test-generator
# or
uv run pytest tests/generator/
```

## Add a test here

Add a test when logic in `scripts/generation/*.py` changes. Most
tests build their own minimal swagger fragment or fake generated-file
fixture with `tmp_path` and need no schema checkout. One exception:
`test_schema_request_body_coverage` in `test_generate_sdk.py`
cross-checks generated code against the real local `../api-schema-public`
checkout and is skipped automatically when that checkout is absent.

Run this suite first while editing [`scripts/generate_sdk.py`](../../scripts/generate_sdk.py),
[`scripts/generation/`](../../scripts/generation/README.md), or template behavior, before running
[`make test-generated`](../../Makefile) to check the SDK the generator produces.
