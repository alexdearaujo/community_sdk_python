<!-- HAND-WRITTEN: not modified by [`make generate`](../../Makefile). Edit directly. -->

# Local SDK Generation Workflow

This project supports a **project-local generation workflow** so you can
regenerate from updated `api-schema-public` without changing the upstream
`openapi-python-generator` project.

## Why This Is Local-Only

Generation behavior is customized inside this repository:

- Custom templates live in [`scripts/openapi_templates/`](https://github.com/kentik/community_sdk_python/blob/main/scripts/openapi_templates/README.md).
- Shared runtime logic lives in [`src/kentik_api/core/rest_runtime.py`](../../src/kentik_api/core/rest_runtime.py).
- The generator entrypoint is [`scripts/generate_sdk.py`](../../scripts/generate_sdk.py).

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

This uses the default local schema path configured in [`Makefile`](../../Makefile) (`DEFAULT_LOCAL_REPO`).

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
2. Run `make generate local`. It writes the checkout's commit to
   `schema.lock`; commit that file with the generated changes.
3. Review generated changes in [`src/kentik_api/gen/`](https://github.com/kentik/community_sdk_python/blob/main/src/kentik_api/gen/README.md).
4. Run tests/lint as needed ([`make test`](../../Makefile), [`make lint`](../../Makefile)).
5. Required: read the message at the end of the `make generate` output. If
   it says `⚠️ API SURFACE CHANGED`, update [`CHANGELOG.md`](https://github.com/kentik/community_sdk_python/blob/main/CHANGELOG.md)
   and run `make check-changelog SINCE=HEAD` before you commit. The steps are
   in "Update the release notes after every regeneration" in the
   [generation guide](guides/generation.md).
6. Optional: run [`make impact-report`](../../Makefile) before you commit.
   It writes `reports/regeneration-impact-<date>.html` with the schema commit,
   the changed files by kind, the API surface delta, the toolchain floors, and
   the test, lint, and type-check results. Proto stubs that changed only their
   protoc version stamp are counted apart from real schema changes. Add
   `SINCE=<ref>` to compare against an earlier commit, or `CHECKS=0` to skip
   the checks. The report leaves its Findings section for you to fill in.

## Notes

- Running [`make local`](../../Makefile) alone is only a marker and prints usage guidance.
- If you need to adjust generated service shape, edit templates in [`scripts/openapi_templates/`](https://github.com/kentik/community_sdk_python/blob/main/scripts/openapi_templates/README.md).
- Keep business/runtime behavior centralized in [`src/kentik_api/core/`](https://github.com/kentik/community_sdk_python/blob/main/src/kentik_api/core/README.md) and
  [`src/kentik_api/transports/`](https://github.com/kentik/community_sdk_python/blob/main/src/kentik_api/transports/README.md) instead of editing generated files directly.
