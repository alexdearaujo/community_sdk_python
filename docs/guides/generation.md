<!-- HAND-WRITTEN prose, except the `kentik-gen` marker blocks, which [`make generate`](../../Makefile) rewrites. Fix those in scripts/generation/docs_rendering.py. -->

# SDK Generation Workflow

The SDK is generated from Kentik's public OpenAPI v3 schema in
[`api-schema-public`](https://github.com/kentik/api-schema-public). This guide
explains how to regenerate after a schema update.

## Prerequisites

- The local schema repo checked out at `../api-schema-public/`
  (sibling directory of this repo), OR internet access to clone it.

## Regenerate the SDK

```bash
# Use the local schema checkout (fastest)
make generate local

# Override the schema path
make generate LOCAL_REPO=/path/to/api-schema-public

# Fetch the latest schema from GitHub (slower, no local checkout needed)
make generate
```

See [`scripts/generate_sdk.py`](../../scripts/generate_sdk.py) for the
entrypoint and [`scripts/generation/`](../../scripts/generation/README.md)
for the phase module documentation.

## What gets regenerated

Every [`make generate`](../../Makefile) run wipes and rebuilds:

- [`src/kentik_api/gen/`](../../src/kentik_api/gen/README.md) — all <!-- kentik-gen:service-count -->40<!-- /kentik-gen:service-count --> services
- [`src/kentik_api/client_mixin.py`](../../src/kentik_api/client_mixin.py)
- [`docs/sphinx/sdk_runtime_architecture.md`](../sphinx/sdk_runtime_architecture.md)
- [`docs/sphinx/services/*.md`](../sphinx/services/README.md) — all <!-- kentik-gen:service-count -->40<!-- /kentik-gen:service-count --> service pages

These files are **never hand-edited**.

## What survives regeneration

Hand-written code that [`make generate`](../../Makefile) never touches:

- [`src/kentik_api/client.py`](../../src/kentik_api/client.py)
- [`src/kentik_api/auth/`](../../src/kentik_api/auth/README.md)
- [`src/kentik_api/core/`](../../src/kentik_api/core/README.md)
- [`src/kentik_api/errors/`](../../src/kentik_api/errors/README.md)
- [`src/kentik_api/transports/`](../../src/kentik_api/transports/README.md)
- [`scripts/openapi_templates/`](../../scripts/openapi_templates/README.md)
- [`scripts/generation/`](../../scripts/generation/README.md)

## Test after regeneration

```bash
make test          # full mocked suite (no network)
make test-e2e      # opt-in: live API tests (needs .env)
```

## Using a forked generator

Test a fork of `openapi-python-generator` without editing code:

```bash
OPENAPI_GENERATOR_FROM="git+https://github.com/<org>/openapi-python-generator.git@<branch>" \
make generate local
```
