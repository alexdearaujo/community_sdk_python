# CLAUDE.md

Guidance for Claude Code when working in this repository.

## What this project is

`kentik-api` (v2.0.0) is the Kentik Community Python SDK — a modern, type-safe client for the Kentik API v6, built on Pydantic v2 and HTTPX. The SDK is **not hand-written**: it is generated end-to-end from Kentik's public OpenAPI v3 schema (`kentik/api-schema-public`) by `scripts/generate_sdk.py`, which orchestrates the phase modules in `scripts/generation/` (see "The generator's phase modules" below). The environment is managed with `uv` (build backend `uv_build`, lockfile `uv.lock`).

## Architecture: hand-written vs. generated

This split is the single most important thing to respect in this repo.

**Hand-written, preserved across every regeneration:**

- `src/kentik_api/client.py` — `KentikAPI`, the main entrypoint
- `src/kentik_api/auth/` — credentials
- `src/kentik_api/core/` — `api_config.py`, `rest_runtime.py` (shared runtime logic)
- `src/kentik_api/errors/` — base exception types
- `src/kentik_api/transports/` — REST/gRPC transport base classes
- `scripts/openapi_templates/` — custom Jinja2 templates fed into the generator
- `scripts/generation/` — the generator's phase modules (`parity.py`, `error_package.py`, `wrapper_generation.py`, `docs_rendering.py`, `endpoint_docs.py`, `_shared.py`), orchestrated by `scripts/generate_sdk.py`

**Fully generated, wiped and rebuilt on every `make generate` run:**

- `src/kentik_api/client_mixin.py` — mounts every generated service wrapper onto the client
- `src/kentik_api/gen/<service>/` — one directory per API service, each with `models/`, `services/` (raw REST functions + a unified `<Service>ServiceWrapper`), `error/`, `pb/` (gRPC stubs), and a `README.md`
- `docs/source/architecture/sdk_runtime_dependencies.puml` and `docs/source/sdk_runtime_architecture.md`

**Rule: never hand-edit generated files.** If output is wrong, fix the generator, a phase module in `scripts/generation/`, or a template in `scripts/openapi_templates/`, then regenerate. A parity check (`parity.validate_generated_service_parity()`) fails the whole generation run if generated service directories don't exactly match the schema's service directories, so partial/manual patches don't survive anyway.

gRPC transport is intentionally a stub today — generated wrapper methods raise `NotImplementedError` for `GrpcTransport`; only REST is fully wired.

### The generator's phase modules

`scripts/generate_sdk.py` is the entrypoint: CLI parsing (`--local-repo`) and the top-level orchestration loop in `generate_modular_sdk()`. It calls out to `scripts/generation/`, a subpackage of independently testable phase modules (see `tests/generator/`):

- `parity.py` — swagger file selection (latest version per service/namespace/filename) and the generated/schema directory parity check. Fully independent of the other phase modules.
- `error_package.py` — per-service error class generation (`generate_service_error_package()`) and the runtime error-dispatch injection (`inject_service_error_handling()`, see the fragile-coupling note below).
- `wrapper_generation.py` — service wrapper + client mixin generation, collapsed into a single `generate()` entrypoint (wrappers first, then the mixin that imports them).
- `docs_rendering.py` — runtime architecture diagram, rendered PlantUML/SVG, and per-service READMEs, collapsed into a single `generate()` entrypoint.
- `endpoint_docs.py` — exposes `EndpointDocsCollector`, not a plain function. Per-endpoint docs must be extracted while each swagger file is still available (`collector.extract(service, swagger_path)`, called once per file during `generate_modular_sdk()`'s schema-availability window), but rendered as Sphinx MyST stubs later (`collector.render()`), only after `wrapper_generation.generate()` has run — the Sphinx example snippets are built by statically reading the real generated wrapper method signatures off disk. The two-method interface makes that ordering constraint visible instead of relying on caller discipline.
- `_shared.py` — `PROJECT_ROOT`, `SDK_OUTPUT_DIR`, and the two helpers genuinely used by more than one phase module (`discover_service_model_classes`, `service_to_pascal_case`). Everything else stays local to the one phase module (or `generate_sdk.py` itself) that calls it — resist the urge to move a single-consumer helper here "for consistency."

`scripts/generate_sdk.py` runs as a script (`uv run python scripts/generate_sdk.py`), so `scripts/` is on `sys.path` at runtime and it imports the subpackage as `from generation import ...`. Tests import the same modules as `from scripts.generation import ...` (repo root on `sys.path` via `pythonpath = ["."]` in `pyproject.toml`, plus `scripts/__init__.py`) — this works because every intra-subpackage import inside `scripts/generation/*.py` is relative (`from ._shared import ...`), so the same file resolves correctly under either top-level name. Never switch those relative imports to absolute `scripts.generation.*` imports; that would break the script's own direct-execution import path.

## The shared connection handler — protect this, do not undo it

The single most significant piece of hand-written engineering in this repo is the **shared REST runtime**: a deliberate choice to route every generated endpoint, across all ~38 services, through one connection/execution path instead of generating (or hand-writing) bespoke per-endpoint HTTP code. Verified directly in the source, this is not a convention, it's structural:

- `src/kentik_api/core/rest_runtime.py` — `request_json()` is the *only* function that ever calls `httpx` for REST traffic. Every generated operation in every service calls this same function. It centralizes: Kentik's auth header scheme (`X-CH-Auth-Email` / `X-CH-Auth-API-Token`), query-param cleaning, the request itself, transport-failure wrapping (`TransportError`), status-code checking, JSON error-body parsing, and dispatch into per-operation error classes via `error_cls.from_response`.
- `src/kentik_api/core/api_config.py` — `APIConfig` is the one shared config object (base URL, auth email/token, TLS verify) threaded through every call.
- `src/kentik_api/errors/__init__.py` — one shared exception hierarchy (`KentikError` → `ConfigurationError`, `AuthenticationError`, `TransportError`, `HTTPException`) that every service's generated per-operation error classes build on.
- `src/kentik_api/transports/{base,rest_client,grpc_client}.py` — thin transport selection/credential wiring, not per-endpoint logic.

This design took several dedicated commits to get right — `264cf74`, `713d4e5`, `da92874` (introducing and refining error handling inside `request_json`, including `TransportError` and `_raise_http_error`), `8f262ae` (`.env`-based auth), `90e65c6` (`scripts/sample_consume_sdk.py`, which proves the whole path end-to-end against both a mocked and a real API call). **Never regress this pattern**: don't generate, hand-write, or suggest per-endpoint connection/auth/retry code, and don't "simplify" by inlining request logic into individual service wrappers — fix or extend `request_json`/`APIConfig` instead, since it's shared by every endpoint in every service.

### Why this survives `make generate` / `scripts/generate_sdk.py`

Confirmed in `generate_modular_sdk()`: the cleanup step that wipes prior output only iterates `SDK_OUTPUT_DIR` (`src/kentik_api/gen/`) and removes subdirectories there. It never touches `core/`, `errors/`, `transports/`, `auth/`, or `client.py` — those paths are outside the directory the wipe loop walks, so they survive regeneration structurally, not just by convention or discipline.

### Two files that look hand-written but are fully regenerated — never hand-edit

- **`src/kentik_api/client_mixin.py`** — lives outside `gen/`, but `wrapper_generation.generate()` calls `mixin_file.write_text(...)`, a full overwrite, on every run. Manual edits here are silently lost on the next `make generate`.
- **`docs/source/sdk_runtime_architecture.md`** and **`docs/source/architecture/*.puml` / `*.svg`** — fully rewritten every run by `docs_rendering.generate()`. By contrast, `docs/source/index.md` is genuinely hand-written; the generator only *inserts* a toctree line into it if missing (non-destructive append, not an overwrite).

### A fragile coupling worth knowing about

`error_package.inject_service_error_handling()` wires each freshly generated per-service REST module to the shared runtime by literally string-matching the line `from kentik_api.core.rest_runtime import request_json` in the generated file content, then inserting the corresponding `from ..error import ...` line right after it. If `request_json` is ever renamed or relocated, or that exact import line's text changes, this injection silently stops firing for every service. Update `scripts/generation/error_package.py` in lockstep with any such rename.

## Generation pipeline

- Schema source defaults to the local sibling repo `../api-schema-public/`; falls back to cloning `https://github.com/kentik/api-schema-public.git` if not present.
- Only the newest version per service/schema-family is used when multiple versioned swagger files exist.
- Full details, including how to test a forked `openapi-python-generator` via env vars without editing code: `docs/source/local_generation_workflow.md`.
- Runtime architecture (module dependency graph, generated vs. hand-written boundary): `docs/source/sdk_runtime_architecture.md`.

### Per-service API docs: real MyST text, not PlantUML images

`docs/source/services/<service>.md` (generated by `endpoint_docs.EndpointDocsCollector.render()`) is real Sphinx/MyST text, not diagrams — deliberately, after PlantUML-rendered "API table" and model-class-diagram images turned out unreadable/uncopyable once a service had more than a handful of operations or models (e.g. `alerting`'s model diagram was 4329×1686px).

- **Endpoints**: one section per operation (parameter table, response table, an auto-generated Python usage example), built from `extract_endpoint_docs()` — parsed straight from each swagger file's `paths`, accumulated per-service inside `EndpointDocsCollector` via `.extract(service, swagger_path)`, called once per file *during* the per-swagger-file loop (schema files are only available inside the `with get_schema_root(...)` block). Swagger files with zero operations (common in multi-file services — `alerting` merges 20 files and 12 have none) correctly contribute no endpoint section at all.
- **Data Models**: `sphinxcontrib.autodoc_pydantic` (`autopydantic_model`) renders every model as a real field table + JSON schema instead of a diagram. Enum classes (`class X(str, Enum)`) must use `autoclass` instead — feeding one into `autopydantic_model` crashes the whole Sphinx build (`AttributeError: ... __pydantic_decorators__`), so `_autodoc_directive_for_model()` checks each class's base list first.
- **The auto-generated example snippets are matched by `(method, path)`, never by `operationId` alone.** Multi-swagger-file services legitimately reuse generic operationIds across different underlying REST modules — `alerting`'s `AlertService`, `SuppressionService`, and `MitigationsService` each declare an operation literally named `List`. Matching by operationId silently picks whichever wrapper method was parsed last, producing a real-looking but wrong example (wrong method, wrong request model). Method+path is unique per operation within a merged service; `_parse_wrapper_method_signatures()` (in `scripts/generation/endpoint_docs.py`) resolves it by statically reading the wrapper's import aliases (no import/execution of generated code from the generator itself — that's deliberately kept test-only, see `tests/_discovery.py`).

## Key commands

- `make` / `make all` — full pipeline: `services docs tests`
- `make services` (alias for `make generate`) — regenerate SDK from schema
- `make generate local` — regenerate from the local `../api-schema-public/` checkout
- `make generate LOCAL_REPO=/path/to/api-schema-public` — regenerate from an arbitrary local schema path
- `make docs` — build Sphinx docs (`docs/source` → `docs/build/html`)
- `make test` / `make tests` — full pytest run (mocked layers only — never wires in `tests/e2e/`)
- `make test-generated` / `make test-runtime` / `make test-smoke` / `make test-generator` — one mocked test layer at a time
- `make test-e2e` (required addition, see Testing strategy) — opt-in end-to-end suite against the real Kentik API; must never be included in `make test` / `make all`
- `make lint` — `ruff check --fix` + `ruff format`
- `make clean` — removes `src/kentik_api/gen/`, `docs/build/`, generated `docs/source/services/*.md` (preserves `scripts/openapi_templates/`, `src/kentik_api/core/`, `docs/source/local_generation_workflow.md`)
- `make deep-clean` — `clean` plus `.venv`, `uv.lock`, `.pytest_cache/`, `.ruff_cache/`

## Testing strategy (5 layers, see `tests/README.md`)

Mocked/offline layers (no network, safe to run anywhere, part of `make test`):

- `tests/generated/test_wrapper_contracts.py` — **auto-discovers** every `*ServiceWrapper` method by AST-parsing `src/kentik_api/gen/*/services/*.py`, then runs parametrized contract tests (forwarding behavior, gRPC-unimplemented check, kwarg validation, full-option forwarding). New services/endpoints are picked up automatically — only add logic here when the wrapper contract itself changes globally.
- `tests/generated/test_endpoint_schema_coverage.py` — for every discovered endpoint, drives the real `request_json` runtime and generated error classes (via `respx`-mocked HTTP) against every declared response status code (success + every entry in that service's generated `error/__init__.py::response_error_map`). Shared discovery/sample-building helpers live in `tests/_discovery.py` (tests-root, not layer-specific, since `tests/e2e/` now imports it too), imported by every generated/e2e file so they can't drift apart.
- `tests/runtime/test_rest_runtime.py` — shared request/auth/error behavior in `src/kentik_api/core`.
- `tests/smoke/test_client_mounts_and_calls.py` — lightweight client-wiring checks; keep this suite small and fast.
- `tests/generator/` — unit tests for `scripts/generation/*.py` (see "The generator's phase modules" above): `test_parity.py`, `test_error_package.py`, `test_wrapper_generation.py`. These test the generator itself, not the SDK it produces, so they build minimal swagger/fixture data with `tmp_path` rather than needing a real or local schema checkout.
- Prefer deterministic unit tests (monkeypatch/mocks) over live network calls for all five of the above.
- If generation output changed, regenerate first (`make generate local`), then run the relevant focused suite, then `make test` before opening a PR.

Live layer (real network, opt-in only, **not** part of `make test`):

- `tests/e2e/` — end-to-end tests against the real Kentik API. See the requirement below; this directory/target is a required addition, not optional polish.

### Test coverage requirement

Generated/contract tests must exercise **every endpoint and every option** discoverable from the OpenAPI schemas for each service: every `operationId` (path × HTTP method), every declared request parameter and request-body field, and every declared response status code (including error responses) — not a representative subset. This is a standing rule, not a one-time task: it applies every time tests are added or regenerated for `gen/`, including whenever a schema update adds new services, endpoints, or parameters. Treat incomplete endpoint/option coverage as a bug in the test/generator, not an acceptable gap.

This mocked coverage only proves the SDK is internally self-consistent (every status the schema declares is handled correctly). It cannot prove the SDK still matches the real API's actual current behavior — that requires the end-to-end layer below.

### End-to-end testing requirement

Generating and running end-to-end tests against the **real** Kentik API is also required, not optional — a standing rule alongside the mocked coverage requirement above, not a one-time task.

- Location: `tests/e2e/`, mirroring the auto-discovery style already used in `tests/generated/` — derive the endpoint list from `tests/_discovery.py` rather than hand-listing operations, so new endpoints get e2e coverage automatically as the schema grows.
- Credentials: the real project-root `.env` (`KENTIK_EMAIL`/`KENTIK_API_TOKEN`), loaded the same way `KentikAPI()` already loads them. Never hardcode credentials in test code and never read/print `.env` contents (see Auth/config below).
- **Opt-in only — never part of the default pipeline.** `.env` holds real credentials against a real account, so e2e tests must not run automatically via `make test`, `make all`, or CI without explicit opt-in. Gate them behind a dedicated `make test-e2e` target and/or a pytest marker (e.g. `-m e2e`) excluded by default; `make test`/`make all` must keep passing without ever touching this layer.
- **Default to safe, non-mutating operations** (List/Get-style reads). Create/Update/Delete calls against a real account are hard to reverse and can corrupt real data — only cover mutating endpoints against a disposable/sandboxed resource with guaranteed cleanup (e.g. create-then-delete in a `finally`/fixture teardown), and call out adding such coverage explicitly rather than doing it silently as a side effect of other work.
- If a real response no longer matches the generated models or error classes, that's a genuine bug to fix (schema sync or generator) — never paper over it inside the e2e test itself.

## Auth/config

Credentials come from a project-root `.env` (`KENTIK_EMAIL`, `KENTIK_API_TOKEN`), loaded via `find_dotenv`/`load_dotenv`. Explicit constructor args to `KentikAPI(...)` override env values. Never read or print `.env` contents — it holds real credentials.

## Constraints

- Do not introduce breaking API surface changes without calling them out explicitly.
- Keep changes focused; avoid unrelated refactors.
- Known generator warnings are non-blocking but should be tracked and reduced over time, not silently ignored.
