# Implementation Plan: V5 Query and Batch Support in the Generated SDK

**Branch**: `feat/005-v5-query-batch` | **Date**: 2026-10-16 | **Spec**: [spec.md](spec.md)

**Input**: Feature specification from `specs/005-v5-query-batch/spec.md`

## Summary

Add the V5 endpoints that have no V6 equivalent (top-X data, top-X chart,
Data Explorer URL, the two batch calls, and batch status) as one generated,
REST-only service, `client.v5`. The input is a hand-maintained OpenAPI 3 file
kept in this repository, which the generator reads as a second schema base
next to the upstream schema. `KentikAPI` builds a second REST transport on the
regional V5 host, and the generated mixin mounts `v5` on it, so the calls
work on gRPC clients too. Small hand-written helpers decode charts, split,
send, and wait for batches, and look up devices. An optional `analytics`
extra brings back the V5 DataFrame, cache, and flat-traffic features. No V5
endpoint that has a V6 equivalent is added. The migration guide maps those.

## Technical Context

**Language/Version**: Python 3.12 to 3.14

**Primary Dependencies**: httpx, Pydantic v2, grpcio, protobuf,
python-dotenv. Generator: `openapi-python-generator` with the templates in
`scripts/openapi_templates/`. New optional extra `analytics`: pandas 2.3 or
later, pyarrow 21 or later, PyYAML 6.0.2 or later.

**Storage**: Local files only. The analytics cache writes Parquet. The device
lookup writes JSON.

**Testing**: pytest with respx (mocked layers), opt-in e2e with `-m e2e`, ty,
ruff, Sphinx with `-W`.

**Target Platform**: Any platform with CPython 3.12 or later.

**Project Type**: Library (generated SDK) with a code generator.

**Performance Goals**: SC-004: 10,000 flow tags in no more than 100 API calls.
At about 100 bytes for each upsert, one 4 MB part holds them all.

**Constraints**:

- Every request goes through `request_json()` (Principle II).
- No hand edit in `gen/` (Principle I).
- No code runs when a definition, cache file, or lookup file is read
  (SC-005).
- V5 sends no quota headers.
- `query/topXchart` did not answer in the live check.

**Scale/Scope**: 1 new service, 6 operations, about 25 models. 3 hand-written
modules. 1 optional package. Changes in 5 generator modules and in
`client.py`.

No item is NEEDS CLARIFICATION. [research.md](research.md) resolves the open
design points. Three points need a check in the first implementation task:
R5 (dict rows), R6 (string body), and R14 (empty quota).

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Status | How the design meets it |
| --- | --- | --- |
| I. Generated code is never hand-edited | Pass | `gen/v5/` and the mixin line come from the generator. The V5 description file is an input, like the upstream schema. Any output fix goes in a phase module or template. |
| II. One shared runtime | Pass | The generated `v5` functions call `request_json()`. The V5 host is a second `APIConfig`, not a second code path. The helpers call the wrapper. No retry code is added. |
| III. Phase modules stay testable | Pass | Changes stay in `parity`, `wrapper_generation`, `api_surface`, `endpoint_docs`, and `docs_rendering`, each with unit tests. Imports stay relative. |
| IV. Exhaustive coverage | Pass | The auto-discovered suites pick up `v5`. Every declared status of the six operations is asserted. The gRPC-stub test exempts `rest_only` services by a recorded flag, not by skipping cases. |
| V. E2E opt-in and safe | Pass | Query e2e is read-only. The chart test is `xfail`. Batch e2e is a separate file with disposable data and cleanup, called out in the pull request. |
| VI. Credentials | Pass | The V5 config reuses the resolved credentials. `v5_base_url` must be `https`. The probe and docs never print `.env`. |
| VII. Compatibility and scope | Pass | Additive only: a new service, a new keyword argument, a new property, and a new extra. `CHANGELOG.md` records them. `api_surface` schema version 8 reads version 7 records. |

Re-check after Phase 1: all pass. No item needs the Complexity Tracking
table.

## Project Structure

### Documentation (this feature)

```text
specs/005-v5-query-batch/
├── spec.md
├── plan.md               # this file
├── research.md           # Phase 0
├── data-model.md         # Phase 1
├── quickstart.md         # Phase 1
├── contracts/            # Phase 1
│   ├── v5-service.md
│   ├── client-config.md
│   ├── helpers.md
│   └── generator.md
├── checklists/requirements.md
└── tasks.md              # Phase 2 (/speckit-tasks)
```

### Source Code (repository root)

```text
schema/openapi/v5/v5/v5.swagger.json      # new: hand-maintained V5 description
scripts/generate_sdk.py                   # read the second base, pass the local set
scripts/generation/
├── parity.py                             # select and validate both bases
├── wrapper_generation.py                 # mount local services on _v5_transport
├── api_surface.py                        # rest_only, SCHEMA_VERSION 8
├── endpoint_docs.py                      # REST-only example text
└── docs_rendering.py                     # REST-only marker, local source note
src/kentik_api/
├── client.py                             # v5_base_url, _v5_transport, v5_api_config
├── v5_tools.py                           # new: decode_chart, split/send/wait batch
├── devices.py                            # new: DeviceLookup (JSON)
├── analytics/                            # new, extra "analytics"
│   ├── __init__.py
│   ├── definitions.py
│   ├── cache.py
│   └── flatness.py
└── gen/v5/                               # generated
examples/v5/                              # new: ported query, batch, analytics examples
docs/sphinx/guides/
├── v5.md                                 # new: bridge guide, manual chart test
├── migrating-from-1x.md                  # full V5 to 2.x map
└── rate_limiting.md                      # V5 has no quota, 429 recipe
tests/
├── generator/                            # second base, rest_only, mixin mount
├── generated/test_grpc_stub_wiring.py    # exempt rest_only
├── runtime/                              # V5 config, empty quota, URL join
├── smoke/                                # helpers, analytics, device lookup
└── e2e/test_v5_query_e2e.py, test_v5_batch_e2e.py
pyproject.toml                            # analytics extra
CHANGELOG.md                              # Unreleased entries
```

**Structure Decision**: Single library project. Generated code goes to
`src/kentik_api/gen/v5/`. Hand-written runtime additions go in `client.py` and
two new top-level modules. The analytics package is separate so that the base
install does not need pandas. Tests follow the existing layers in
`tests/README.md`. Planning for tasks decides whether helper tests get their
own layer or join `tests/smoke/`.

## Phases after this plan

1. Checks: render the V5 file through the generator once, and confirm R5,
   R6, and R14.
2. Generator: second base, union, `rest_only`, mixin mount, docs text.
3. Client: V5 config and transport, `v5_base_url`, `v5_api_config`, close.
4. Description file: all six operations and models, then `make generate
   local` and commit `public_names.json` and `api_surface.json`.
5. Helpers: `v5_tools`, `devices`.
6. Analytics extra.
7. Tests: generator, runtime, generated, helpers, e2e.
8. Docs and examples: the V5 guide with the manual chart test, the migration
   map, the rate limit guide, examples with their test, and `CHANGELOG.md`.

## Risks

| Risk | Effect | Response |
| --- | --- | --- |
| The generator does not render dict rows or a string body | Wrong models | Fix in the template or `fixup.py`, with a generator test (R5, R6). |
| `query/topXchart` never answers | A chart call that times out | Marked not verified, `xfail` e2e, report to Kentik (clarification). |
| Kentik retires V5 | `v5` calls fail with the normal errors | The V6 query service replaces `v5`. Docs say `v5` is a bridge (FR-025). |
| The V5 API changes a shape | Validation errors (502) | The description file is small. The e2e suite shows the change. |
| A batch writes to a real account in tests | Data loss | Batch e2e only with a disposable name, cleanup in `finally`, and called out (Principle V). |

## Complexity Tracking

No constitution violations.
