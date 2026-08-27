<!-- HAND-WRITTEN: not modified by [`make generate`](../../Makefile). Edit directly. -->

# Smoke Tests

Mocked, no network. See the layered strategy in
[../README.md](../README.md) for how this layer fits with the other
four.

## Purpose

`test_client_mounts_and_calls.py` holds lightweight checks for
overall wiring: multi-region endpoint configuration
(`_REGION_ENDPOINTS` for `us`/`eu`, and the `ValueError` raised for an
unrecognized region), that `KentikAPI` mounts the expected service
attributes, and that a call through one mounted wrapper reaches the
generated REST module.

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
