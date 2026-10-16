<!-- HAND-WRITTEN: not modified by [`make generate`](../../Makefile). Edit directly. -->

# Smoke Tests

Mocked, no network. See the layered strategy in
[../README.md](../README.md) for how this layer fits with the other
four.

## Purpose

`test_client_mounts_and_calls.py` holds lightweight checks for
overall wiring: multi-region endpoint configuration
(`_REGION_ENDPOINTS` for `us`/`eu`, and the `ConfigurationError` raised for an
unrecognized region), that `KentikAPI` mounts the expected service
attributes, and that a call through one mounted wrapper reaches the
generated REST module.

The other files in this layer:

| File | Covers |
| --- | --- |
| `test_docs_contract.py` | Documentation and tooling facts the audit found wrong (findings D7 to D10). |
| `test_examples_import.py` | Each example imports, and its `client.<service>.<method>(...)` calls resolve against a real client. Nothing is sent. |
| `test_packaging_contract.py` | Packaging metadata the published artifacts depend on (audit findings K4 to K9, K11). |

## Run

```bash
make test-smoke
# or
uv run pytest tests/smoke/
```

## Add a test here

Add only small, high-value checks. Keep this suite minimal and fast;
put detailed per-operation or per-status-code coverage in
[`tests/generated/`](../generated/README.md) instead.
