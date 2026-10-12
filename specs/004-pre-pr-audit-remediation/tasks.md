---
description: "Task list for feature 004: pre-PR audit remediation"
---

# Tasks: Pre-PR Audit Remediation

**Input**: Design documents from `/specs/004-pre-pr-audit-remediation/`

**Prerequisites**: [plan.md](plan.md), [spec.md](spec.md), [research.md](research.md), [data-model.md](data-model.md), [contracts/remediation-contract.md](contracts/remediation-contract.md), [quickstart.md](quickstart.md)

**Tests**: Tests are required for this feature because remediation acceptance depends on reproducible verification gates and regression detection.

**Organization**: Tasks are grouped by user story so each story can be implemented and verified independently.

## Format: `[ID] [P?] [Story] Description`

- [P] marks tasks that can run in parallel.
- [Story] maps each task to a user story (US1-US5).
- Every task includes an explicit file path.

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Establish remediation tracking, batch sequencing, and evidence logging scaffolding.

- [X] T001 Create remediation execution header and blocker ordering section in reports/pre-pr-audit-2026-10-10/validation.md
- [X] T002 Create deferred-risk ledger template in reports/pre-pr-audit-2026-10-10/deferred-risks.md
- [X] T003 [P] Create remediation batch tracker table in reports/pre-pr-audit-2026-10-10/report.md
- [X] T004 [P] Add execution and verification workflow notes to specs/004-pre-pr-audit-remediation/quickstart.md

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Put in place shared rules and harness updates needed by all stories.

**Critical**: No user story implementation starts before these tasks are complete.

- [X] T005 Freeze source-of-truth finding IDs and statuses in reports/pre-pr-audit-2026-10-10/validation.md
- [X] T006 Enforce generated-output editing rule in specs/004-pre-pr-audit-remediation/contracts/remediation-contract.md
- [X] T007 [P] Extend reports/pre-pr-audit-2026-10-10/run_manual_spot_check.py with per-finding remediation-state recording hooks
- [X] T008 [P] Add spot-check replay and artifact retention policy to reports/pre-pr-audit-2026-10-10/manual-spot-checks.md
- [X] T009 Add remediation state fields and validation rules in specs/004-pre-pr-audit-remediation/data-model.md
- [X] T010 Define batch verification command catalog in specs/004-pre-pr-audit-remediation/quickstart.md

**Checkpoint**: Batch tracking, deferred-risk schema, and verification harness are ready.

---

## Phase 3: User Story 1 - Release-critical blockers are resolved first (Priority: P1) 🎯 MVP

**Goal**: Fix or explicitly defer all validated blockers B1-B13 with one-by-one verification.

**Independent Test**: Blocker evidence scripts no longer reproduce fixed defects, and every deferred blocker is documented with owner and mitigation.

### Tests for User Story 1

- [X] T011 [P] [US1] Add blocker verification regression tests for B5 and B6 in tests/runtime/test_rest_runtime.py
- [X] T012 [P] [US1] Add blocker verification regression tests for B7 in tests/runtime/test_grpc_runtime.py
- [X] T013 [P] [US1] Add enum regression tests for B1 and B10 in tests/generated/test_endpoint_schema_coverage.py
- [X] T014 [P] [US1] Add e2e-host and pass-rule assertions for B13 in tests/e2e/test_endpoints_e2e.py

### Implementation for User Story 1

- [X] T015 [US1] Implement credential-redaction and malformed-header failure hardening for B5 in src/kentik_api/core/rest_runtime.py
- [X] T016 [US1] Implement catchable closed-channel behavior for B6 in src/kentik_api/transports/grpc_client.py
- [X] T017 [US1] Implement gRPC override consistency or explicit configuration failure for B7 in src/kentik_api/core/grpc_runtime.py
- [X] T018 [US1] Implement enum evolution-safe response parsing for B1 in src/kentik_api/core/rest_runtime.py
- [X] T019 [US1] Implement robust enum wire encoding for path and query for B10 in scripts/openapi_templates/service.jinja2
- [X] T020 [US1] Fix e2e target host and false-pass logic for B13 in tests/e2e/conftest.py
- [X] T021 [US1] Regenerate and validate template-driven blocker changes with make generate local, updating src/kentik_api/gen/README.md if generated docs change
- [X] T022 [US1] Record B1-B13 fixed or deferred states with evidence links in reports/pre-pr-audit-2026-10-10/validation.md
- [X] T023 [US1] Record any deferred blocker risks with owner and mitigation in reports/pre-pr-audit-2026-10-10/deferred-risks.md

**Checkpoint**: All blockers are fixed or deferred with explicit risk records.

---

## Phase 4: User Story 2 - Generator and release gates prevent silent regressions (Priority: P1)

**Goal**: Ensure generator and release tooling fail loudly for validated break classes.

**Independent Test**: Generator and release repro scripts for targeted P/L findings fail before fixes and pass after fixes.

### Tests for User Story 2

- [X] T024 [P] [US2] Add generator failure-mode tests for P1 and P4 in tests/generator/test_parity.py
- [X] T025 [P] [US2] Add version ordering and deterministic output tests for P5 and P7 in tests/generator/test_wrapper_generation.py
- [X] T026 [P] [US2] Add changelog/surface break enforcement tests for P6 in tests/generator/test_release_notes.py

### Implementation for User Story 2

- [ ] T027 [US2] Harden schema and parity gate behavior for P1 in scripts/generation/parity.py
- [ ] T028 [US2] Harden protoc error propagation for P4 in scripts/generate_sdk.py
- [ ] T029 [US2] Fix latest-version selection reliability for P5 in scripts/generation/parity.py
- [ ] T030 [US2] Harden release-note and changelog mismatch detection for P6 in scripts/release_notes.py
- [ ] T031 [US2] Ensure stable generation ordering and deterministic writes for P7 in scripts/generation/wrapper_generation.py
- [ ] T032 [US2] Triage L1-L13 into fix-now versus defer with rationale in reports/pre-pr-audit-2026-10-10/validation.md
- [ ] T033 [US2] Implement selected latent-hazard fixes from L1-L13 in scripts/generation/fixup.py
- [ ] T034 [US2] Run and record generator/release verification outcomes in reports/pre-pr-audit-2026-10-10/validation.md

**Checkpoint**: Generator and release-tooling defects are guarded by deterministic checks.

---

## Phase 5: User Story 3 - Runtime behavior is transport-consistent and safe (Priority: P1)

**Goal**: Make REST and gRPC runtime behavior safe, consistent, and free of known crash/leak paths.

**Independent Test**: Runtime evidence scripts for targeted B and R findings show fixed behavior.

### Tests for User Story 3

- [ ] T035 [P] [US3] Add runtime symmetry and error-contract tests for remaining R findings in tests/runtime/test_transport_symmetry.py
- [ ] T036 [P] [US3] Add non-UTF8, timeout, and response-path regression tests for R1-R3 and R8 in tests/runtime/test_rest_runtime.py
- [ ] T037 [P] [US3] Add grpc freeform and pool conflict regression tests for R11 and R14 in tests/runtime/test_grpc_runtime.py

### Implementation for User Story 3

- [ ] T038 [US3] Implement runtime fixes for remaining high-impact R findings in src/kentik_api/core/rest_runtime.py
- [ ] T039 [US3] Implement grpc runtime fixes for remaining high-impact R findings in src/kentik_api/core/grpc_runtime.py
- [ ] T040 [US3] Implement transport lifecycle and pooling fixes for runtime defects in src/kentik_api/transports/rest_client.py
- [ ] T041 [US3] Resolve partial runtime findings R10, R13, and R15 with focused investigation notes in reports/pre-pr-audit-2026-10-10/validation.md
- [ ] T042 [US3] Capture runtime verification gate outcomes and updated finding states in reports/pre-pr-audit-2026-10-10/validation.md

**Checkpoint**: Runtime behavior is consistent, catchable, and validated across transports.

---

## Phase 6: User Story 4 - Test suite catches the defects it is expected to guard (Priority: P2)

**Goal**: Close validated test-gap classes so CI catches the same defect types found by the audit.

**Independent Test**: Seeded regressions for T1-T10 are detected by at least one corresponding test.

### Tests for User Story 4

- [ ] T043 [P] [US4] Add explicit coverage for request-body blind spots for T1 in tests/generated/test_endpoint_schema_coverage.py
- [ ] T044 [P] [US4] Add auth metadata assertion coverage for T2 in tests/runtime/test_credentials.py
- [ ] T045 [P] [US4] Add grpc contract and request bridge assertions for T3 and T4 in tests/generated/test_grpc_stub_wiring.py
- [ ] T046 [P] [US4] Add retry-eligibility and kwargs propagation assertions for T8 and T9 in tests/generated/test_retry_eligibility.py
- [ ] T047 [P] [US4] Add CI-context guard assertions for T7 in tests/smoke/test_ci_guards.py

### Implementation for User Story 4

- [ ] T048 [US4] Align generated and runtime tests to close T1-T10 gaps in tests/generated/test_wrapper_contracts.py
- [ ] T049 [US4] Add negative seeded-regression fixtures to prove failure behavior in tests/generated/fixtures/
- [ ] T050 [US4] Update test strategy guidance for new regression gates in tests/README.md
- [ ] T051 [US4] Record T1-T10 closure status and residual risks in reports/pre-pr-audit-2026-10-10/validation.md

**Checkpoint**: CI-relevant test gaps are closed and demonstrably detecting regressions.

---

## Phase 7: User Story 5 - Packaging and docs are release-ready and accurate (Priority: P2)

**Goal**: Resolve packaging and documentation findings so published artifacts and guidance are reliable.

**Independent Test**: Packaging and docs checks for targeted K and D findings pass cleanly.

### Tests for User Story 5

- [ ] T052 [P] [US5] Add packaging metadata and lock integrity checks for K findings in tests/smoke/test_packaging_contract.py
- [ ] T053 [P] [US5] Add documentation expectation checks for D findings in tests/smoke/test_docs_contract.py

### Implementation for User Story 5

- [ ] T054 [US5] Resolve packaging and workflow findings K1-K12 in pyproject.toml
- [ ] T055 [US5] Resolve CI release gating findings for K2, K7, and K8 in .github/workflows/release.yml
- [ ] T056 [US5] Resolve remaining packaging command findings in Makefile
- [ ] T057 [US5] Resolve docs findings D1-D12 in docs/sphinx/guides/quickstart.md
- [ ] T058 [US5] Resolve generated-doc ownership findings via templates in scripts/generation/docs_rendering.py
- [ ] T059 [US5] Run docs and packaging verification commands and record outcomes in reports/pre-pr-audit-2026-10-10/validation.md

**Checkpoint**: Packaging and documentation findings are resolved or explicitly deferred.

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Finalize quality gates, deferred-risk communication, and PR readiness.

- [ ] T060 Run full verification gates and record results in reports/pre-pr-audit-2026-10-10/validation.md
- [ ] T061 [P] Re-run manual spot checks C1-C5 and archive final artifacts in reports/pre-pr-audit-2026-10-10/manual-spot-check-artifacts/
- [ ] T062 [P] Finalize deferred-risk entries and ownership in reports/pre-pr-audit-2026-10-10/deferred-risks.md
- [ ] T063 Add PR-ready deferred-risk summary block in reports/pre-pr-audit-2026-10-10/report.md
- [ ] T064 Update feature closure notes and completion evidence in specs/004-pre-pr-audit-remediation/quickstart.md

---

## Dependencies & Execution Order

### Phase Dependencies

- Setup (Phase 1) has no dependencies.
- Foundational (Phase 2) depends on Setup.
- User stories (Phases 3-7) depend on Foundational.
- Polish (Phase 8) depends on all selected story phases.

### User Story Dependencies

- US1 (P1) starts first and defines blocker closure.
- US2 (P1) can run in parallel with US3 after US1 checkpoint planning, but should complete before final CI sign-off.
- US3 (P1) can run after Foundational, with blocker overlap tracked via US1 updates.
- US4 (P2) depends on stable behavior from US1-US3.
- US5 (P2) can begin after US2 and US3 produce stable generator/runtime behavior.

### Within Each User Story

- Verification tests are created before or alongside implementation changes.
- Runtime and generator source updates precede regeneration and docs refresh.
- Validation ledger updates happen at the end of each story phase.

---

## Parallel Execution Examples

## US1 parallel example

```bash
Task: "T011 [US1] tests/runtime/test_rest_runtime.py"
Task: "T012 [US1] tests/runtime/test_grpc_runtime.py"
Task: "T013 [US1] tests/generated/test_endpoint_schema_coverage.py"
Task: "T014 [US1] tests/e2e/test_endpoints_e2e.py"
```

## US2 parallel example

```bash
Task: "T024 [US2] tests/generator/test_parity.py"
Task: "T025 [US2] tests/generator/test_wrapper_generation.py"
Task: "T026 [US2] tests/generator/test_release_notes.py"
```

## US4 parallel example

```bash
Task: "T043 [US4] tests/generated/test_endpoint_schema_coverage.py"
Task: "T044 [US4] tests/runtime/test_credentials.py"
Task: "T047 [US4] tests/smoke/test_ci_guards.py"
```

---

## Implementation Strategy

### MVP First

1. Complete Phase 1 and Phase 2.
2. Complete Phase 3 (US1 blockers).
3. Validate blocker outcomes and deferred-risk records.
4. Stop and review before expanding scope.

### Incremental Delivery

1. US1 blockers.
2. US2 generator/release hardening.
3. US3 runtime safety and consistency.
4. US4 test-gap closure.
5. US5 packaging/docs closure.
6. Final polish and PR-ready reporting.

### Quality Gate

- Each story phase ends by updating [reports/pre-pr-audit-2026-10-10/validation.md](../../reports/pre-pr-audit-2026-10-10/validation.md) with fixed or deferred status and verification evidence.
