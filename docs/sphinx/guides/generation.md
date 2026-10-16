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

# Fetch the pinned schema commit from GitHub (no local checkout needed)
make generate

# Fetch schema HEAD from GitHub and move the pin
make sync-schema
```

`schema.lock` holds the schema commit that the committed tree was
generated from. Every completed run writes the commit it used to that
file, so commit it with the regenerated output. CI regenerates at that
commit, so a schema change upstream cannot fail a pull request. The
scheduled `schema-sync` workflow runs `make sync-schema` every week and
opens a pull request when the output changes.

### Automated update pull requests

Two bots open pull requests against the default branch:

| Bot | Schedule | What it changes |
| --- | --- | --- |
| [`schema-sync.yml`](../../../.github/workflows/schema-sync.yml) | Mondays, or by hand from the Actions tab | `schema.lock` and the regenerated tree |
| [Dependabot](../../../.github/dependabot.yml) | Weekly | Action SHA pins in `.github/workflows/`, and `uv.lock` |

Before `schema-sync` can open a pull request, a repository admin must
turn on **Settings > Actions > General > Allow GitHub Actions to create
and approve pull requests**. Without it, the job fails at the
`gh pr create` step.

When a `schema-sync` pull request opens, do these steps:

1. Close the pull request and reopen it. A pull request that the
   workflow token opens starts no CI, and the reopen starts it.
2. Read the API surface changes in the pull request description.
3. For each breaking change, add a `CHANGELOG.md` entry to the branch.
   The `changelog` job fails until each one is named.
4. Merge when CI passes.

If the workflow run fails, the new schema breaks generation. Reproduce
the failure with `make sync-schema`, and fix the generator.

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

## Keep public names stable

[`public_names.json`](https://github.com/kentik/community_sdk_python/blob/main/public_names.json)
sets the public name of every Service, client method, and model. Each entry
maps a public name to what the schema calls that thing today:

```json
"label": {
  "upstream": "label",
  "methods": {"list_labels": "GET /label/<version>/labels"},
  "models": {"Label": "label<version>Label"}
}
```

- `upstream` is the Service's schema directory. The public name is the
  `client.<service>` attribute and the `kentik_api.gen.<service>` package.
- A method's value is its HTTP verb and path. `<version>` replaces the path
  version, and `{}` replaces each path parameter.
- A model's value is its schema name, with `<version>` in place of the
  version.

These rules apply on every run:

- A version bump, a new operationId, or a renamed path parameter does not
  change a public name. Their values ignore those parts.
- A new Service, operation, or model gets an entry with its default name. The
  run writes the entry into the file. Commit the file with the regenerated
  code.
- A run never changes an existing entry.

### Fix a public name that no longer matches the schema

When upstream renames or moves something that an entry points at, generation
fails before it changes any file. The error names the entry and lists the
values that have no entry yet:

```text
NameDriftError: public_names.json, label methods: the schema no longer has
`delete_label` ('DELETE /label/<version>/labels/{}'). The schema has these
unnamed: 'DELETE /label/<version>/labels/{}:remove'. Point each entry at its
new value, or delete it if upstream removed it.
```

1. Open `public_names.json` and find the entry from the error.
2. If upstream moved the thing, set the entry's value to the new value from
   the error. Users keep the same name.
3. If upstream removed the thing, delete the entry. Record the removal as a
   breaking change in `CHANGELOG.md`.
4. Run `make generate` again.

To give a new thing a name other than its default, add its entry before you
run `make generate`. To rename an existing public name, change the key. That
is a breaking change for users, so record it in `CHANGELOG.md`.

> [!NOTE]
> Each operation's error classes follow its client method name
> (`list_labels` raises `ListLabelsError`), so this file names them too.
> Parameter names, model fields, and enum values come from the schema.
> `make check-changelog` reports their changes.

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
- A service is no longer mounted on the client.
- A client method is renamed, or an operation no longer routes to gRPC.
- An operation raises a different error class, or loses the error class for
  a status code.
- An operation requires a new parameter, drops a parameter, or changes a
  parameter or return type.
- A field changes its type.
- A field becomes required, or a new field is required.
- A dependency requirement narrows, or a new dependency is required.

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
