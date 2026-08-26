<!--
Sync Impact Report
Version change: 1.0.0 → 1.1.0
Rationale: Materially expanded guidance under "Development Workflow & Quality
Gates" — a new guardrail bullet on verifying local schema-checkout integrity
before trusting `make generate local`, learned first-hand while fixing the
acronym-splitting bug (fix/acronym-splitting-in-generated-names, 2026-08-26):
a locally corrupted `../api-schema-public/` checkout silently dropped the
`kagent` and `monitoring` services because the parity check compares
generated output only against that same (corrupted) checkout. No core
principle changed — the acronym fix itself was a clean demonstration of
Principles I and III already working as intended, not a gap in them.
Modified principles: none
Added sections: none (bullet added to existing "Development Workflow &
  Quality Gates" section)
Removed sections: n/a
Deferred TODOs: the gRPC stub-vs-implemented doc drift flagged at v1.0.0 in
  "Architecture & Generation Pipeline" remains open and unrelated to this
  amendment.
-->

# Kentik Community Python SDK Constitution

## Core Principles

### I. Generated Code Is Never Hand-Edited
`src/kentik_api/gen/`, `client_mixin.py`, and the generated docs pages under
`docs/sphinx/services/` and `docs/sphinx/sdk_runtime_architecture.md` are wiped
and rebuilt by `make generate` on every run. MUST NOT hand-edit any generated
file. If generated output is wrong, fix `scripts/generate_sdk.py`, the
responsible phase module in `scripts/generation/`, or the Jinja2 templates in
`scripts/openapi_templates/`, then regenerate. A parity check
(`parity.validate_generated_service_parity()`) fails the whole generation run
when generated service directories don't match the schema's service
directories; partial or manual patches do not survive it.

### II. One Shared Runtime for Every Endpoint
Every REST call MUST go through `request_json()` in
`src/kentik_api/core/rest_runtime.py`; every gRPC call MUST go through
`call_grpc()` in `src/kentik_api/core/grpc_runtime.py`. These centralize auth
headers, request execution, transport-failure wrapping, status checking, and
error-class dispatch for every service. MUST NOT generate, hand-write, or
suggest per-endpoint connection, auth, or retry code, and MUST NOT inline
request logic into individual service wrappers. Extend `request_json`,
`call_grpc`, or `APIConfig` instead.

### III. Generator Phase Modules Stay Independently Testable
`scripts/generation/` is split into single-concern phase modules (`parity`,
`error_package`, `fixup`, `wrapper_generation`, `docs_rendering`,
`endpoint_docs`), each independently unit-tested under `tests/generator/`.
Intra-subpackage imports MUST stay relative (`from ._shared import ...`); MUST
NOT switch to absolute `scripts.generation.*` imports, since
`generate_sdk.py`'s own direct-execution import path depends on the relative
form. A helper used by only one phase module stays local to that module rather
than moving into `_shared.py` "for consistency."

### IV. Test Coverage Must Be Exhaustive, Not Representative
Generated and contract tests MUST exercise every endpoint and every option
discoverable from the OpenAPI schemas: every operationId (path × method),
every declared request parameter and body field, and every declared response
status code, including error responses. This is a standing rule, re-verified
every time the schema grows or `gen/` is regenerated, not a one-time task.
Incomplete endpoint or option coverage is a bug in the test suite or the
generator, not an acceptable gap.

### V. End-to-End Tests Are Opt-In and Safe-by-Default
`tests/e2e/` runs against the real Kentik API and MUST NOT run as part of
`make test`, `make all`, or default CI. It MUST stay gated behind an explicit
opt-in (`make test-e2e`, a `-m e2e` marker, or both). Coverage MUST default to
non-mutating List/Get operations; Create/Update/Delete coverage against a real
account is only acceptable against a disposable, sandboxed resource with
guaranteed cleanup (e.g. create-then-delete in a `finally`/fixture teardown),
and adding such coverage MUST be called out explicitly rather than added as a
side effect of other work.

### VI. Credentials Never Enter Code, Logs, or Prompts
Credentials load only from the project-root `.env` (`KENTIK_EMAIL`,
`KENTIK_API_TOKEN`) via `find_dotenv`/`load_dotenv`, with explicit constructor
args to `KentikAPI(...)` overriding env values. MUST NOT hardcode credentials
in tests or examples, and MUST NOT read or print `.env` contents in code,
tests, or agent output.

### VII. Compatibility and Scope Discipline
MUST NOT introduce breaking API surface changes without calling them out
explicitly. Changes MUST stay focused; unrelated refactors belong in a
separate change. Known generator warnings are non-blocking but MUST be
tracked and reduced over time, not silently ignored.

## Architecture & Generation Pipeline

- The SDK is generated end-to-end from Kentik's public OpenAPI v3 schema
  (`kentik/api-schema-public`), defaulting to the local sibling checkout
  `../api-schema-public/` and falling back to cloning it when absent.
- When multiple versioned swagger files exist for the same `(service,
  namespace, filename)` family, the generator MUST use only the newest
  version per family.
- Transport is dual-protocol: REST (default, `protocol="rest"`) and gRPC
  (`protocol="grpc"`) both route through the same generated
  `*ServiceWrapper`, bridging via `ParseDict` → `call_grpc()` →
  `MessageToDict` → `model_validate()`, and both MUST return the same
  Pydantic models. **Known drift, resolve when next touching this area**:
  `CLAUDE.md` currently describes gRPC as "intentionally a stub" with
  wrapper methods "raising `NotImplementedError` for `GrpcTransport`," but
  the generated wrappers (e.g. `gen/device/services/device.py`) show
  `call_grpc()` fully wired against compiled proto companions
  (`gen/pb_companions/`), with `NotImplementedError` reserved for the
  fallback case where proto dependencies fail to import for one service.
  Verify current status in code before restating either claim, and correct
  whichever side is stale.
- Two files look hand-written but are fully regenerated every run and MUST
  NOT be hand-edited: `src/kentik_api/client_mixin.py` and
  `docs/sphinx/sdk_runtime_architecture.md` (plus
  `src/kentik_api/gen/README.md`).
- `error_package.inject_service_error_handling()` wires each generated
  service to the shared runtime by string-matching the `from
  kentik_api.core.rest_runtime import request_json` import line. Renaming or
  relocating `request_json` requires updating
  `scripts/generation/error_package.py` in lockstep, or injection fails
  loudly (`ValueError`) rather than silently skipping.

## Development Workflow & Quality Gates

- Standard pipeline: `make` / `make all` runs `services docs tests` in
  sequence.
- After any change to generation output: regenerate (`make generate local`),
  run the relevant focused test layer, then run the full `make test` before
  opening a PR.
- `make lint` (`ruff check --fix` + `ruff format`) and `make typecheck` (`ty
  check` on hand-written code) MUST stay clean.
- `make test` MUST stay mocked-only and fast enough to run anywhere; `make
  test-e2e` MUST stay a separate, explicit, opt-in target (see Principle V).
- `make generate local` trusts the local `../api-schema-public/` checkout as
  found. The parity check only compares generated output against whatever
  that checkout currently contains, so a corrupted or stale local checkout
  (e.g. locally modified or truncated swagger files) can silently drop
  entire services without failing any check. Before relying on `make
  generate local` output, verify the checkout is clean (`git -C
  ../api-schema-public status`), or regenerate from a clean canonical clone
  with `make generate` (no `local`) instead.

## Governance

This constitution governs planning, analysis, and review for all Spec Kit
workflows in this repository; it takes precedence over ad hoc practice when
the two conflict. `CLAUDE.md` (and its `AGENTS.md` symlink) remains the
detailed, day-to-day reference this constitution distills principles from —
if the two visibly diverge on a factual claim about the architecture, treat
that as a documentation-drift bug to fix, not a reason to silently pick one
(see the gRPC example above).

Amendments: propose the change, update this file, increment the version
below per semantic versioning (MAJOR: incompatible principle
removal/redefinition; MINOR: new principle or materially expanded guidance;
PATCH: wording/typo clarifications), and record the change in a Sync Impact
Report comment at the top of this file. `/speckit-plan`, `/speckit-tasks`,
and `/speckit-analyze` MUST treat this constitution as authoritative context;
complexity or deviation from it MUST be justified explicitly in the relevant
plan, not silently introduced.

**Version**: 1.1.0 | **Ratified**: 2026-08-25 | **Last Amended**: 2026-08-26
