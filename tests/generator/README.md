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
| `test_error_package.py` | Error class naming, error-response extraction and merging, and the runtime error-dispatch injection seam. |
| `test_wrapper_generation.py` | Annotation qualification and end-to-end wrapper and client-mixin generation against a temp directory. |

## Run

```bash
make test-generator
# or
uv run pytest tests/generator/
```

## Add a test here

Add a test when logic in `scripts/generation/*.py` changes. Each
test builds its own minimal swagger fragment or fake generated-file
fixture with `tmp_path`. None of them need a real or local schema
checkout.

Run this suite first while editing [`scripts/generate_sdk.py`](../../scripts/generate_sdk.py),
[`scripts/generation/`](../../scripts/generation/README.md), or template behavior, before running
[`make test-generated`](../../Makefile) to check the SDK the generator produces.
