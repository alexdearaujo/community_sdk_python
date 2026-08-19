<!-- HAND-WRITTEN: not modified by `make generate`. Edit directly. -->

# Local SDK Generation Workflow

This project supports a **project-local generation workflow** so you can
regenerate from updated `api-schema-public` without changing the upstream
`openapi-python-generator` project.

## Why This Is Local-Only

Generation behavior is customized inside this repository:

- Custom templates live in `scripts/openapi_templates/`.
- Shared runtime logic lives in `src/kentik_api/core/rest_runtime.py`.
- The generator entrypoint is `scripts/generate_sdk.py`.

Because the customization is in this repo, upstream generator updates can
still be consumed without maintaining a permanent fork.

For a runtime-level dependency map that shows how the client, mixin,
auth/core/errors, and generated services connect, see
[SDK Runtime Architecture](sdk_runtime_architecture.md).

## Default Regeneration (Local Schema Repo)

From the project root:

```bash
make generate local
```

This uses the default local schema path configured in `Makefile` (`DEFAULT_LOCAL_REPO`).

## Override Schema Location

```bash
make generate LOCAL_REPO=/path/to/api-schema-public
```

## Optional: Test a Forked Generator Temporarily

You can point generation to a fork **without editing code** by using
environment variables.

```bash
OPENAPI_GENERATOR_FROM="git+https://github.com/<org>/openapi-python-generator.git@<branch>" \
make generate local
```

Optional command override (only if your fork exposes a different CLI name):

```bash
OPENAPI_GENERATOR_CMD="openapi-python-generator" make generate local
```

## Update Cycle (Simple Repeatable Flow)

1. Pull latest schema updates in your local `api-schema-public` clone.
2. Run `make generate local`.
3. Review generated changes in `src/kentik_api/gen/`.
4. Run tests/lint as needed (`make test`, `make lint`).

## Notes

- Running `make local` alone is only a marker and prints usage guidance.
- If you need to adjust generated service shape, edit templates in `scripts/openapi_templates/`.
- Keep business/runtime behavior centralized in `src/kentik_api/core/` and
  `src/kentik_api/transports/` instead of editing generated files directly.
