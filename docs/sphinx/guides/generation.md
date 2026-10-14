<!-- HAND-WRITTEN prose, except the `kentik-gen` marker blocks, which [`make generate`](../../../Makefile) rewrites. Fix those in scripts/generation/docs_rendering.py. -->

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

> [!WARNING]
> `make generate` does not write release notes. When a run changes the API
> surface, the run is not done until you update
> [`CHANGELOG.md`](https://github.com/kentik/community_sdk_python/blob/main/CHANGELOG.md). The run prints a
> `⚠️ API SURFACE CHANGED` alert when this applies. See
> "Update the release notes after every regeneration" below.

See [`scripts/generate_sdk.py`](../../../scripts/generate_sdk.py) for the
entrypoint and [`scripts/generation/`](https://github.com/kentik/community_sdk_python/blob/main/scripts/generation/README.md)
for the phase module documentation.

## What gets regenerated

Every [`make generate`](../../../Makefile) run wipes and rebuilds:

- [`src/kentik_api/gen/`](https://github.com/kentik/community_sdk_python/blob/main/src/kentik_api/gen/README.md) — all <!-- kentik-gen:service-count -->42<!-- /kentik-gen:service-count --> services
- [`src/kentik_api/client_mixin.py`](../../../src/kentik_api/client_mixin.py)
- [`docs/sphinx/sdk_runtime_architecture.md`](../sdk_runtime_architecture.md)
- [`docs/sphinx/services/*.md`](../services/index.md) — all <!-- kentik-gen:service-count -->42<!-- /kentik-gen:service-count --> service pages

These files are **never hand-edited**.

## What survives regeneration

Hand-written code that [`make generate`](../../../Makefile) never touches:

- [`src/kentik_api/client.py`](../../../src/kentik_api/client.py)
- [`src/kentik_api/auth/`](https://github.com/kentik/community_sdk_python/blob/main/src/kentik_api/auth/README.md)
- [`src/kentik_api/core/`](https://github.com/kentik/community_sdk_python/blob/main/src/kentik_api/core/README.md)
- [`src/kentik_api/errors/`](https://github.com/kentik/community_sdk_python/blob/main/src/kentik_api/errors/README.md)
- [`src/kentik_api/transports/`](https://github.com/kentik/community_sdk_python/blob/main/src/kentik_api/transports/README.md)
- [`scripts/openapi_templates/`](https://github.com/kentik/community_sdk_python/blob/main/scripts/openapi_templates/README.md)
- [`scripts/generation/`](https://github.com/kentik/community_sdk_python/blob/main/scripts/generation/README.md)

## Test after regeneration

```bash
make test          # full mocked suite (no network)
make test-e2e      # opt-in: live API tests (needs .env)
```

## Update the release notes after every regeneration

This step is required. Do it every time you run `make generate`, with a local
schema or with the schema from GitHub.

`make generate` records the public API surface in
[`api_surface.json`](../../../api_surface.json). The record holds every
service, operation, model field, and enum value, and the gRPC method each
operation calls. At the end of the run, the
generator compares the new record with the record committed at `HEAD`. It
then prints one of three messages:

| Message at the end of the run | What it means | What you do |
| --- | --- | --- |
| `API surface unchanged since HEAD.` | No caller can see a difference. | Nothing. |
| `⚠️ API SURFACE CHANGED since HEAD` | Callers can see the changes listed under the alert. | Do all the steps below before you commit. |
| `No api_surface.json is committed at HEAD` | There is no baseline to compare with. | Run `make release-notes SINCE=<ref>` with an earlier ref. |

This is the alert for the `kmeta` field rename in schema `e205184`:

```text
========================================================================
⚠️  API SURFACE CHANGED since HEAD: 1 BREAKING change
========================================================================
### Breaking changes

- `kmeta`: field removed, `ServiceNowConfig.credentialVaultId`

### Changed services

- **kmeta**
  - field added, `ServiceNowConfig.credentialVaultName` (`Optional[str]`)
  - **field removed**, `ServiceNowConfig.credentialVaultId`
========================================================================
```

When you see the alert, do these steps:

1. Open [`CHANGELOG.md`](https://github.com/kentik/community_sdk_python/blob/main/CHANGELOG.md) and find the `## Unreleased`
   section.
2. Write an entry for each change in the alert. Put each breaking change in
   the "Breaking changes" table. Put each addition under "Added".
3. In each breaking-change entry, use the exact name that the alert shows,
   for example `ServiceNowConfig.credentialVaultId`. The check in the next
   step looks for that name.
4. Run `make check-changelog SINCE=HEAD`. It fails and names each breaking
   change that `CHANGELOG.md` does not mention.
5. Run `make release-notes SINCE=HEAD` to see the list that the release
   will publish.
6. Commit `api_surface.json`, the regenerated code, and `CHANGELOG.md`
   together.

### What counts as a breaking change

The alert lists a change as breaking when it can stop existing caller code
from working:

- A service, operation, model, field, or enum value is removed.
- A field changes its type.
- A field becomes required, or a new field is required.
- An operation requires a new parameter.
- A dependency floor goes up, or a new dependency is required.

A renamed field shows as one removed field and one added field. The removed
name is the breaking change.

### What runs automatically

| Step | Who does it | When |
| --- | --- | --- |
| Record the surface in `api_surface.json` | `make generate` | Every run |
| Print the alert | `make generate` | Every run |
| Write the `CHANGELOG.md` entry | You | Before you commit the regeneration |
| Fail when a breaking change has no entry | The `changelog` job in [`tests.yml`](../../../.github/workflows/tests.yml) | Every pull request |
| Add the surface changes to the GitHub release notes | The `notes` job in [`release.yml`](../../../.github/workflows/release.yml) | When you publish a release |

`make generate` does not write `CHANGELOG.md` or a release notes file. The
CHANGELOG tells a caller what to do about a change, so a person writes it.
The release notes compare the surface with the previous release tag. That
comparison belongs to the release, not to each regeneration.

## Using a forked generator

Test a fork of `openapi-python-generator` without editing code:

```bash
OPENAPI_GENERATOR_FROM="git+https://github.com/<org>/openapi-python-generator.git@<branch>" \
make generate local
```
