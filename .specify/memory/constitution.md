<!--
Sync Impact Report
Version change: 1.2.1 → 1.3.0
Rationale: Principle IV assumed every declared response status would be
observed through a generated per-operation error class, because that was
the only dispatch path when the principle was written. Feature 003
(specs/003-harden-runtime-and-ci/) establishes that some statuses are
better handled in the shared runtime before per-operation dispatch: a 401
must raise AuthenticationError on both transports, and routing that in
`request_json()` keeps all 35 generated error packages byte-identical
(Principle II). Under the previous wording, a suite updated to assert the
new runtime behavior could be read as violating Principle IV, and the
tempting "fix" would be to narrow the suite instead. Principle IV is
therefore expanded to state that coverage means asserting the SDK's actual
observable behavior for every declared status, whichever layer produces
it, and to add an explicit anti-narrowing rule. No principle is removed or
redefined, so this is MINOR rather than MAJOR.
Modified principles: IV (materially expanded, not redefined)
Added sections: none
Removed sections: n/a
Also in this revision: replaced four em dashes with ordinary punctuation, to
match the repository's writing-style rule. Wording only, no meaning changed;
folded into this MINOR bump rather than issued as a separate PATCH because
1.3.0 is not yet committed.
Deferred TODOs: none
Prior report (1.2.0 → 1.2.1, retained for history): resolved the "Known
drift" TODO under "Architecture & Generation Pipeline" by rewriting the
gRPC bullet with the actual, fully-implemented behavior (two distinct
NotImplementedError cases, not one), replacing the stale "intentionally a
stub" claim. CLAUDE.md and src/kentik_api/gen/README.md's generator
template corrected in lockstep, plus a new
tests/e2e/test_endpoints_e2e_grpc.py (`make test-e2e-grpc`).
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

Coverage of a status code means asserting the **SDK's actual observable
behavior** for that status, not asserting that a particular layer produced it.
A status MAY be handled in the shared runtime before per-operation dispatch,
in which case the generated per-operation error class never sees it and the
suite MUST assert the runtime's behavior instead. Handling a cross-cutting
status once in the runtime is the Principle II answer and MUST NOT be read as
a coverage gap. What is forbidden is the status going unasserted.

A suite MUST NOT be narrowed, skipped, parameterized away, or made
status-agnostic in order to make a change pass. When a runtime change shifts
the expected behavior for many endpoints at once, the suite is updated to the
new expectation for **every** affected endpoint. Whoever makes such a change
MUST demonstrate the suite still detects regressions, by reverting the change
and confirming the suite fails, and MUST record that result in the pull
request. A suite that stays green with the change reverted has been narrowed
and does not satisfy this principle.

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
  Pydantic models for every operation gRPC covers. gRPC coverage is
  per-operation, not per-service or all-or-nothing: a wrapper method
  raises `NotImplementedError` for `GrpcTransport` either when that
  service's proto companions failed to import (`gen/pb_companions/`) at
  wrapper `__init__` time, or when the generator found no gRPC method
  matching that REST operation's name. Neither case is a bug by itself.
  `tests/e2e/test_endpoints_e2e_grpc.py` (`make test-e2e-grpc`) treats
  `NotImplementedError` as an expected, passing outcome for exactly this
  reason. (This bullet previously flagged a drift against CLAUDE.md's
  stale "intentionally a stub" claim; resolved 2026-08-26, and both now
  agree.)
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
- `make generate local` and `make generate` both call
  `parity.validate_schema_files_or_raise()` before touching any existing
  generated output: every discovered swagger file MUST parse as JSON and
  declare the expected top-level OpenAPI keys, or the run aborts with a
  non-zero exit and names every offending file
  (specs/001-validate-schema-checkout/). This catches a corrupted or
  truncated schema *file*. It does NOT catch a whole service *directory*
  silently missing from the schema tree (a discovery-time gap, not a
  content one). For that, still verify the local `../api-schema-public/`
  checkout is clean (`git -C ../api-schema-public status`) before trusting
  `make generate local`, or regenerate from a clean canonical clone with
  `make generate` (no `local`) instead.

## Governance

This constitution governs planning, analysis, and review for all Spec Kit
workflows in this repository; it takes precedence over ad hoc practice when
the two conflict. `CLAUDE.md` (and its `AGENTS.md` symlink) remains the
detailed, day-to-day reference this constitution distills principles from.
If the two visibly diverge on a factual claim about the architecture, treat
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

**Version**: 1.3.0 | **Ratified**: 2026-08-25 | **Last Amended**: 2026-09-21
