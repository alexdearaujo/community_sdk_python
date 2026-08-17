# Test Suite Guide

This folder uses a layered testing strategy so generation changes can be validated quickly while still keeping full end-to-end confidence.

## Test Layout

- generated: contract tests for all generated snake_case service wrappers, plus exhaustive per-endpoint/per-status-code schema coverage. Mocked, no network.
- runtime: focused tests for shared runtime helpers used by generated code. Mocked, no network.
- smoke: lightweight checks for client wiring and selected wrapper call paths. Mocked, no network.
- generator: unit tests for the SDK generator's phase modules (`scripts/generation/`) -- error package generation, swagger selection/parity validation, wrapper generation. Mocked, no network.
- e2e: end-to-end tests against the **real** Kentik API. Opt-in only -- never part of `make test`/`make all`. See section 4 below before touching this one.

`tests/_discovery.py` (at the tests/ root, not inside any one layer) holds the schema/wrapper discovery helpers shared by `generated/` and `e2e/`, so they can't drift apart. `tests/conftest.py` puts `tests/` on `sys.path` so `import _discovery` resolves the same way no matter which layer pytest is invoked against. Neither file is itself a test file.

## How To Run Tests

From the repository root:

- Run everything (mocked layers only):
  make test
- Run generated wrapper contract tests only:
  make test-generated
- Run runtime tests only:
  make test-runtime
- Run smoke tests only:
  make test-smoke
- Run generator unit tests only:
  make test-generator
- Run end-to-end tests against the real API (opt-in, needs a real .env):
  make test-e2e

You can also call pytest directly:

- uv run pytest tests/
- uv run pytest tests/generated/
- uv run pytest tests/runtime/
- uv run pytest tests/smoke/
- uv run pytest tests/generator/
- uv run pytest -m e2e tests/e2e/

`pyproject.toml` registers the `e2e` marker with `addopts = "-m 'not e2e'"`, so plain `pytest tests/` (and therefore `make test`) always deselects `tests/e2e/` -- you have to opt in explicitly with `-m e2e`.

## When To Run Which Suite

- While editing scripts/generate_sdk.py, scripts/generation/, or template behavior:
  use test-generator for fast feedback on the generator itself, then test-generated to check the SDK it produces.
- While editing shared request/auth/error behavior in src/kentik_api/core:
  use test-runtime first.
- Before opening a PR or merging:
  run make test.
- Before trusting a schema sync or a change to error/response handling against production behavior:
  run make test-e2e (requires real credentials; read section 4 first).

## How To Add New Tests

### 1) Generated wrapper contract tests

Primary file:

- tests/generated/test_wrapper_contracts.py

Add logic here only when the wrapper contract changes globally (for example argument forwarding rules, transport branching behavior, or discovery rules). This suite auto-discovers wrapper modules, so you usually do not add per-service files manually.

Shared discovery helpers (wrapper/endpoint discovery, sample-value and sample-Pydantic-model builders) live in `tests/_discovery.py` so this file, the schema coverage suite below, and the e2e suite all stay in sync automatically.

### 1b) Endpoint/schema coverage tests

Primary file:

- tests/generated/test_endpoint_schema_coverage.py

Exercises every operation discovered via `_discovery.py` against every response status code declared for it in the OpenAPI schema (read back from each service's generated `error/__init__.py::{Operation}Error.response_error_map`, plus the success `expected_status`), using `respx` to mock the HTTP layer so the real `request_json` runtime and generated error classes run for real. This is what CLAUDE.md's test coverage requirement ("every endpoint, every option, every declared status code") maps to concretely. Because it drives the actual generated code end-to-end (not monkeypatched at the wrapper boundary like the contract tests above), it also catches generator bugs that only manifest at runtime (e.g. a model import silently resolving to the wrong object). Add logic here only when the status/error coverage strategy itself changes; new services/operations/status codes are picked up automatically on the next `make generate`.

### 2) Runtime tests

Primary file:

- tests/runtime/test_rest_runtime.py

Add tests when shared runtime behavior changes, such as:

- header construction
- query filtering
- expected status handling
- error raising behavior

### 3) Smoke tests

Primary file:

- tests/smoke/test_client_mounts_and_calls.py

Add small high-value checks for overall wiring. Keep this suite small and fast.

### 4) Generator tests

Primary files:

- tests/generator/test_parity.py -- swagger selection and generated/schema directory parity
- tests/generator/test_error_package.py -- error class naming, error-response extraction/merging, and the runtime error-dispatch injection seam
- tests/generator/test_wrapper_generation.py -- annotation qualification and end-to-end wrapper/client-mixin generation against a temp directory

Add tests here when `scripts/generation/*.py` logic changes. These are unit tests against the generator itself (not the SDK it produces), so they don't need a real or local schema checkout -- build minimal swagger fragments or fake generated-file fixtures with `tmp_path` instead.

### 5) End-to-end tests (real API, opt-in)

Primary files:

- tests/e2e/conftest.py -- the `real_client` fixture. Credential loading is delegated entirely to `KentikAPI()` (project-root `.env` or `KENTIK_EMAIL`/`KENTIK_API_TOKEN`); the fixture just skips the whole suite if none are configured.
- tests/e2e/test_endpoints_e2e.py

Like the other generated-style suites, endpoint discovery comes from `tests/_discovery.py`, not a hand-written list. Two things make this suite different from the mocked ones:

- Only GET (read-only) operations are actually called automatically. A read call passes if it returns a correctly-typed response *or* raises a generated `KentikError` subclass -- both prove the real request/response/error path still matches what the schema says it should. Only a genuinely unexpected exception is a failure, since the test has no control over what data exists in the real account.
- Create/Update/Delete operations are deliberately **not** auto-called (`test_mutating_endpoint_excluded_from_e2e` is `@pytest.mark.skip`'d on purpose) -- they're hard to reverse against a real account. If you need live coverage for a specific mutating endpoint, add a dedicated test with its own setup/teardown against a disposable resource; don't wire it into the auto-discovered path.

Never run this suite by accident: it is excluded by default (see `addopts` in `pyproject.toml`) and only runs via `make test-e2e` / `-m e2e`. Never hardcode credentials in test code, and never read or print `.env` contents.

## Guidelines

- Prefer deterministic unit tests over network calls for the generated/runtime/smoke layers.
- Use monkeypatch/mocks (or `respx` for HTTP-level mocking) for those three layers.
- Keep smoke tests minimal.
- The e2e layer is the one intentional exception to "no network calls" -- keep it opt-in, read-only by default, and separate from the rest of the pipeline.
- If generation output changes, regenerate first:
  make generate local
- Then run the relevant focused suite, and finally make test.
