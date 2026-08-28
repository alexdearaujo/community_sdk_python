<!-- HAND-WRITTEN: not modified by `make generate`. Edit directly. -->

# CLAUDE.md

Guidance for Claude Code when working in this repository.

## What this project is

`kentik-api` is the Kentik Community Python SDK: a
type-safe client for the Kentik API v6, built on Pydantic v2 and
HTTPX. This SDK is **not hand-written**. `scripts/generate_sdk.py`
generates it end-to-end from Kentik's public OpenAPI v3 schema
(`kentik/api-schema-public`). It orchestrates the phase modules in
`scripts/generation/` (see "The generator's phase modules" below).
This project uses `uv` to manage the environment and dependencies
(lockfile `uv.lock`); the build backend is `hatchling` with
`hatch-vcs` for dynamic versioning from git tags.

## Architecture: hand-written vs. generated

This split is the single most important thing to respect in this
repo.

**Hand-written, preserved across every regeneration:**

- `src/kentik_api/client.py` — `KentikAPI`, the main entrypoint
- `src/kentik_api/auth/` — credentials
- `src/kentik_api/core/` — `api_config.py`, `rest_runtime.py`,
  `grpc_runtime.py` (shared runtime logic)
- `src/kentik_api/errors/` — base exception types
- `src/kentik_api/transports/` — REST/gRPC transport base classes
- `scripts/openapi_templates/` — custom Jinja2 templates fed into
  the generator
- `scripts/generation/` — the generator's phase modules
  (`parity.py`, `error_package.py`, `fixup.py`,
  `wrapper_generation.py`, `docs_rendering.py`, `endpoint_docs.py`,
  `_shared.py`), orchestrated by `scripts/generate_sdk.py`

**Fully generated, wiped and rebuilt on every `make generate` run:**

- `src/kentik_api/client_mixin.py` — mounts every generated service
  wrapper onto the client
- `src/kentik_api/gen/<service>/` — one directory per API service,
  each with `models/`, `services/` (raw REST functions + a unified
  `<Service>ServiceWrapper`), `error/`, `pb/` (gRPC stubs), and a
  `README.md`
- `src/kentik_api/gen/README.md` — the `gen/` root README
- `docs/sphinx/sdk_runtime_architecture.md` — the runtime
  architecture page, with an inline Mermaid dependency graph
- `docs/sphinx/services/<service>.md` — one reference page per
  service, written by `endpoint_docs.EndpointDocsCollector.render()`
- the `<!-- kentik-gen:... -->` marker blocks inside
  `docs/guides/{quickstart,rest,grpc,generation}.md` and
  `docs/sphinx/README.md` — rewritten by
  `docs_rendering._update_guide_snippets()`. The surrounding prose in
  those files is hand-written; only the marker blocks are generated.

**Rule: never hand-edit generated files.** If output is wrong, fix
the generator, a phase module in `scripts/generation/`, or a
template in `scripts/openapi_templates/`. Then regenerate. A parity
check (`parity.validate_generated_service_parity()`) fails the whole
generation run when generated service directories don't exactly
match the schema's service directories. Partial or manual patches
don't survive this check.

gRPC transport is fully implemented, not a stub. Every generated
wrapper method routes a `GrpcTransport` call through `call_grpc()`
when the generator found a gRPC method matching that REST
operation's name, bridging via `ParseDict` → `call_grpc()` →
`MessageToDict` → `model_validate()` against proto companions
compiled into `gen/pb_companions/`. A wrapper method raises
`NotImplementedError` for `GrpcTransport` in exactly two cases: the
service's proto companions failed to import at wrapper `__init__`
time ("gRPC proto dependencies not installed for `<service>`
service"), or no matching gRPC method name was found for that REST
operation ("gRPC translation for `<Operation>` is not yet
implemented"). Both REST and gRPC return identical Pydantic models
for every operation gRPC covers.

### The generator's phase modules

`scripts/generate_sdk.py` is the entrypoint: CLI parsing
(`--local-repo`) and the top-level orchestration loop in
`generate_modular_sdk()`. It calls out to `scripts/generation/`, a
subpackage of independently testable phase modules (see
`tests/generator/`):

- `parity.py` — swagger file selection (latest version per service,
  namespace, and filename) and the directory parity check between
  generated output and the schema. Fully independent of the other
  phase modules.
- `error_package.py` — per-service error class generation
  (`generate_service_error_package()`) and the error-dispatch
  injection (`inject_service_error_handling()`; see the
  fragile-coupling note below).
- `fixup.py` — generated-code post-processing, called once per
  service directory after the schema availability window closes.
  Single public entrypoint: `fix_generated_service(service_dir)`.
  Internally: rebuilds `models/__init__.py` from a full directory
  scan, replaces wildcard exports with explicit named imports, and
  applies all file-level content patches (import aliases, auth
  headers, path parameter sanitization, docstring normalization,
  duplicate function renaming, and error-handling injection).
- `wrapper_generation.py` — generates service wrappers and the
  client mixin, collapsed into a single `generate()` entrypoint
  (wrappers first, then the mixin that imports them).
- `docs_rendering.py` — generates the runtime architecture page with
  an inline Mermaid dependency graph, writes the `gen/` root README,
  and writes per-service READMEs, collapsed into a single
  `generate()` entrypoint.
- `endpoint_docs.py` — exposes `EndpointDocsCollector`, not a plain
  function. `collector.extract(service, swagger_path)` must run once
  per swagger file, while the file is still available, during
  `generate_modular_sdk()`'s schema-availability window.
  `collector.render()` must run afterward, and only after
  `wrapper_generation.generate()` runs. `render()` builds Sphinx
  MyST stubs whose example snippets statically read the real
  generated wrapper method signatures off disk. The two-method
  interface makes this ordering constraint visible instead of
  relying on caller discipline.
- `_shared.py` — `PROJECT_ROOT`, `SDK_OUTPUT_DIR`, and the two
  helpers that more than one phase module genuinely uses
  (`discover_service_model_classes`, `service_to_pascal_case`).
  Everything else stays local to the one phase module (or
  `generate_sdk.py` itself) that calls it. Resist the urge to move a
  single-consumer helper here "for consistency."

`scripts/generate_sdk.py` runs as a script: `uv run python
scripts/generate_sdk.py`. This puts `scripts/` on `sys.path` at
runtime. `generate_sdk.py` then imports the subpackage as `from
generation import ...`. Tests import the same modules as `from
scripts.generation import ...`. `pythonpath = ["."]` in
`pyproject.toml`, plus `scripts/__init__.py`, puts the repo root on
`sys.path` for tests. Both import styles work because every
intra-subpackage import inside `scripts/generation/*.py` is relative
(`from ._shared import ...`). A relative import resolves correctly
under either top-level name. Never switch those relative imports to
absolute `scripts.generation.*` imports — that would break the
script's own direct-execution import path.

## The shared connection handler — protect this, do not undo it

The **shared REST runtime** is the single most significant piece of
hand-written engineering in this repo. It routes every generated
endpoint, across all ~39 services, through one connection path
instead of generating or hand-writing bespoke per-endpoint HTTP
code. This is not just a convention. It's structural. The source
code confirms it directly:

- `src/kentik_api/core/rest_runtime.py` — `request_json()` is the
  *only* function that ever calls `httpx` for REST traffic. Every
  generated operation in every service calls this same function. It
  centralizes:
  - Kentik's auth header scheme (`X-CH-Auth-Email` /
    `X-CH-Auth-API-Token`)
  - query-param cleaning
  - the request itself
  - transport-failure wrapping (`TransportError`)
  - status-code checking
  - JSON error-body parsing
  - dispatch into per-operation error classes via
    `error_cls.from_response`
- `src/kentik_api/core/grpc_runtime.py` — `call_grpc()` is the gRPC
  analogue of `request_json()`. It routes every generated gRPC wrapper
  call through one place. `map_grpc_error()` is extracted as a pure
  function (no I/O, no side effects) that maps a `grpc.RpcError` status
  code to `AuthenticationError` or `HTTPException`. Testable without a
  gRPC channel.
- `src/kentik_api/core/api_config.py` — `APIConfig` is the one
  shared config object (base URL, auth email/token, TLS verify) used
  in every call.
- `src/kentik_api/errors/__init__.py` — one shared exception
  hierarchy (`KentikError` → `ConfigurationError`,
  `AuthenticationError`, `TransportError`, `HTTPException`) that
  every service's generated per-operation error classes build on.
- `src/kentik_api/transports/{base,rest_client,grpc_client}.py` —
  thin transport-selection and credential-wiring code, not
  per-endpoint logic.

This design took several dedicated commits to get right:

- `264cf74`, `713d4e5`, `da92874` — introduced and refined error
  handling inside `request_json`, including `TransportError` and
  `_raise_http_error`
- `8f262ae` — added `.env`-based auth
- `90e65c6` — added `scripts/sample_consume_sdk.py`, which proves
  the whole path end-to-end against both a mocked and a real API
  call

**Never regress this pattern.** Don't generate, hand-write, or
suggest per-endpoint connection, auth, or retry code. Don't
"simplify" by inlining request logic into individual service
wrappers. Instead, fix or extend `request_json` or `APIConfig` —
every endpoint in every service shares them.

### Why this survives `make generate` / `scripts/generate_sdk.py`

You can confirm this by reading `generate_modular_sdk()`. Its
cleanup step only iterates `SDK_OUTPUT_DIR` (`src/kentik_api/gen/`)
and removes subdirectories there. It never touches `core/`,
`errors/`, `transports/`, `auth/`, or `client.py`, because the wipe
loop never walks those paths. These files survive regeneration
structurally, not just by convention or discipline.

### Two files that look hand-written but are fully regenerated — never hand-edit

- **`src/kentik_api/client_mixin.py`** lives outside `gen/`, but
  `wrapper_generation.generate()` calls `mixin_file.write_text(...)`
  — a full overwrite, on every run. The next `make generate` silently
  overwrites any manual edits here.
- **`docs/sphinx/sdk_runtime_architecture.md`** and
  **`src/kentik_api/gen/README.md`** — `docs_rendering.generate()`
  fully rewrites these every run. The architecture page embeds its
  dependency graph as an inline Mermaid fence, so there are no
  separate diagram artifacts to track. By contrast,
  `docs/sphinx/index.md` is genuinely hand-written. The generator
  only *inserts* a toctree line into it if missing — a
  non-destructive append, not an overwrite.

### A guarded coupling worth knowing about

`error_package.inject_service_error_handling()` wires each freshly
generated per-service REST module to the shared runtime. It does
this by string-matching the line `from kentik_api.core.rest_runtime
import request_json` in the generated file content. It then inserts
the corresponding `from ..error import ...` line right after it. If
`request_json` is ever renamed or relocated, or if that exact import
line's text changes, the function now raises `ValueError` immediately
(when there are operations to inject), rather than silently skipping
injection. Update `scripts/generation/error_package.py` in lockstep
with any such rename.

## Generation pipeline

- Schema source defaults to the local sibling repo
  `../api-schema-public/`. If that repo is not present, the
  generator falls back to cloning
  `https://github.com/kentik/api-schema-public.git`.
- The generator uses only the newest version per swagger family (see
  CONTEXT.md) when multiple versioned swagger files exist.
- See `docs/sphinx/local_generation_workflow.md` for full details,
  including how to test a forked `openapi-python-generator` via env
  vars without editing code.
- See `docs/sphinx/sdk_runtime_architecture.md` for the runtime
  architecture: the module dependency graph and the
  generated-vs-hand-written boundary.

### Per-service API docs: real MyST text, not rendered diagram images

`endpoint_docs.EndpointDocsCollector.render()` generates
`docs/sphinx/services/<service>.md` as real Sphinx/MyST text, not
rendered diagram images. This is deliberate. A rendered "API table"
and model-class-diagram image become unreadable and uncopyable once
a service has more than a handful of operations or models. For
example, an image of `alerting`'s model diagram runs to 4329×1686px.

- **Endpoints**: one section per operation, with a parameter table,
  a response table, and an auto-generated Python usage example.
  `extract_endpoint_docs()` builds each section by parsing each
  swagger file's `paths` directly. `EndpointDocsCollector.extract(
  service, swagger_path)` accumulates these sections per service. It
  runs once per file, during the per-swagger-file loop, because
  schema files are only available inside the `with
  get_schema_root(...)` block. Swagger files with zero operations
  correctly contribute no endpoint section at all. This is common in
  multi-file services — `alerting` merges 20 files, and 12 of them
  have none.
- **Data Models**: `sphinxcontrib.autodoc_pydantic`
  (`autopydantic_model`) renders every model as a real field table
  and JSON schema, instead of a diagram. Enum classes (`class X(str,
  Enum)`) must use `autoclass` instead. Feeding an enum class into
  `autopydantic_model` crashes the whole Sphinx build
  (`AttributeError: ... __pydantic_decorators__`).
  `_autodoc_directive_for_model()` checks each class's base list
  first, to avoid this.
- **The generator matches each example snippet to its endpoint by
  `(method, path)`, never by `operationId` alone.** Multi-swagger-file
  services legitimately reuse generic operationIds across different
  underlying REST modules. For example, `alerting`'s `AlertService`,
  `SuppressionService`, and `MitigationsService` each declare an
  operation literally named `List`. Matching by operationId alone
  would silently pick whichever wrapper method was parsed last,
  producing a real-looking but wrong example (wrong method, wrong
  request model). Method and path together are unique per operation
  within a merged service. `_parse_wrapper_method_signatures()` (in
  `scripts/generation/endpoint_docs.py`) resolves this by statically
  reading the wrapper's import aliases. The generator itself never
  imports or executes generated code — that stays test-only by
  design (see `tests/_discovery.py`).

## Key commands

- `make` / `make all` — full pipeline: `services docs tests`
- `make services` (alias for `make generate`) — regenerate SDK from
  schema
- `make generate local` — regenerate from the local
  `../api-schema-public/` checkout
- `make generate LOCAL_REPO=/path/to/api-schema-public` —
  regenerate from an arbitrary local schema path
- `make docs` — build Sphinx docs (`docs/sphinx` → `docs/build/html`)
- `make test` / `make tests` — full pytest run (mocked layers only —
  never wires in `tests/e2e/`)
- `make test-generated` / `make test-runtime` / `make test-smoke` /
  `make test-generator` — one mocked test layer at a time
- `make test-e2e` / `make test-e2e-grpc` (required addition, see
  Testing strategy) — opt-in end-to-end suites against the real
  Kentik API, REST and gRPC transports respectively. Must never
  appear in `make test` or `make all`.
- `make lint` — `ruff check --fix` + `ruff format`
- `make clean` — removes `src/kentik_api/gen/`, `docs/build/`,
  generated `docs/sphinx/services/*.md` (preserves
  `scripts/openapi_templates/`, `src/kentik_api/core/`,
  `docs/sphinx/local_generation_workflow.md`)
- `make deep-clean` — `clean` plus `.venv`, `uv.lock`,
  `.pytest_cache/`, `.ruff_cache/`

## Testing strategy (5 layers, see `tests/README.md`)

Mocked/offline layers (no network, safe to run anywhere, part of
`make test`):

- `tests/generated/test_wrapper_contracts.py` — **auto-discovers**
  every `*ServiceWrapper` method by AST-parsing
  `src/kentik_api/gen/*/services/*.py`. It then runs parametrized
  contract tests (forwarding behavior, gRPC-unimplemented check,
  kwarg validation, full-option forwarding). This auto-discovery
  picks up new services and endpoints automatically. Only add logic
  here when the wrapper contract itself changes globally.
- `tests/generated/test_endpoint_schema_coverage.py` — for every
  discovered endpoint, drives the real `request_json` runtime and
  generated error classes (via `respx`-mocked HTTP) against every
  declared response status code. This includes both the success
  status and every entry in that service's generated
  `error/__init__.py::response_error_map`. Shared discovery and
  sample-building helpers live in `tests/_discovery.py` (at the
  tests root, not inside one layer, since `tests/e2e/` imports it
  too). Every generated and e2e test file imports these helpers, so
  they can't drift apart.
- `tests/runtime/test_rest_runtime.py` — shared request/auth/error
  behavior in `src/kentik_api/core`.
- `tests/smoke/test_client_mounts_and_calls.py` — lightweight
  client-wiring checks; keep this suite small and fast.
- `tests/generator/` — unit tests for `scripts/generation/*.py`
  (see "The generator's phase modules" above): `test_parity.py`,
  `test_error_package.py`, `test_wrapper_generation.py`. These test
  the generator itself, not the SDK it produces. They build minimal
  swagger or fixture data with `tmp_path`, instead of needing a real
  or local schema checkout.
- Prefer deterministic unit tests (monkeypatch/mocks) over live
  network calls for all five of the above.
- If generation output changed, follow these steps before opening a
  PR:
  1. Regenerate: `make generate local`.
  2. Run the relevant focused suite.
  3. Run `make test`.

Live layer (real network, opt-in only, **not** part of `make test`):

- `tests/e2e/` — end-to-end tests against the real Kentik API. See
  the requirement below. This directory and target are a required
  addition, not optional polish.
- `tests/e2e/test_endpoints_e2e_grpc.py` (`make test-e2e-grpc`, `-m
  e2e_grpc`) — the gRPC-transport variant of the same read-only
  coverage. A `NotImplementedError` counts as a passing outcome here
  (see "gRPC transport is fully implemented" above): it means this
  particular operation has no gRPC translation yet, not a bug.

### Test coverage requirement

Generated and contract tests must exercise **every endpoint and
every option** discoverable from the OpenAPI schemas for each
service. This means every `operationId` (path × HTTP method), every
declared request parameter and request-body field, and every
declared response status code, including error responses — not a
representative subset. This is a standing rule, not a one-time task.
It applies every time someone adds tests or regenerates `gen/`,
including whenever a schema update adds new services, endpoints, or
parameters. Treat incomplete endpoint or option coverage as a bug in
the test suite or the generator, not an acceptable gap.

This mocked coverage only proves the SDK is internally
self-consistent — it correctly handles every status the schema
declares. It cannot prove the SDK still matches the real API's
current behavior. That requires the end-to-end layer below.

### End-to-end testing requirement

Generating and running end-to-end tests against the **real** Kentik
API is also required, not optional. This is a standing rule
alongside the mocked coverage requirement above, not a one-time
task.

- Location: `tests/e2e/`, mirroring the auto-discovery style
  `tests/generated/` already uses. Derive the endpoint list from
  `tests/_discovery.py`, rather than hand-listing operations. This
  way, new endpoints get e2e coverage automatically as the schema
  grows.
- Credentials: the real project-root `.env` (`KENTIK_EMAIL` and
  `KENTIK_API_TOKEN`). Tests load these the same way `KentikAPI()`
  does. Never hardcode credentials in test code. Never read or print
  `.env` contents (see Auth/config below).
- **Opt-in only — never part of the default pipeline.** `.env`
  holds real credentials against a real account. e2e tests must not
  run automatically via `make test`, `make all`, or CI, without
  explicit opt-in. Gate them behind a dedicated `make test-e2e` /
  `make test-e2e-grpc` target, a pytest marker (for example `-m
  e2e`/`-m e2e_grpc`) excluded by default, or both. `make test` and
  `make all` must keep passing without ever touching this layer.
- **Default to safe, non-mutating operations** (List- and Get-style
  reads). Create, Update, and Delete calls against a real account
  are hard to reverse, and they can corrupt real data. Only cover
  mutating endpoints against a disposable, sandboxed resource with
  guaranteed cleanup — for example, create-then-delete in a
  `finally` block or fixture teardown. Call out adding such coverage
  explicitly. Don't add it silently as a side effect of other work.
- If a real response no longer matches the generated models or
  error classes, that's a genuine bug to fix (schema sync or
  generator) — never paper over it inside the e2e test itself.

## Auth/config

The SDK loads credentials from a project-root `.env` file
(`KENTIK_EMAIL`, `KENTIK_API_TOKEN`) via `find_dotenv` and
`load_dotenv`. Explicit constructor args to `KentikAPI(...)` override
env values. Never read or print `.env` contents — it holds real
credentials.

## Constraints

- Do not introduce breaking API surface changes without calling
  them out explicitly.
- Keep changes focused. Avoid unrelated refactors.
- Known generator warnings are non-blocking. Track and reduce them
  over time — don't ignore them silently.

## Branch naming (exception to the shared rule below)

Jira creates every branch in this repo automatically from its
ticket, using the ticket key and title as-is (for example
`FA-2-Update-the-python-SDK-from-V5-to-V6`). This repo does not use
the `<category>/<short-kebab-description>` convention from the
shared agent rules below. Use the Jira-generated branch name as-is,
even though it does not match that pattern.

<!-- shared-rules:start -->
<!-- Synced from ~/.claude/CLAUDE.md; regenerate by re-running the
     agents-md skill instead of hand-editing this block. AGENTS.md
     is a symlink to this file, so every tool that reads AGENTS.md
     sees this section too. -->

## Shared agent rules

These rules apply in every project, regardless of which coding
agent is being used.

### Git branching

Never commit directly to the default branch (`main`/`master`).
Every unit of work gets its own branch, created from an up-to-date
default branch, and named `<category>/<short-kebab-description>`.

Branch categories, by the primary intent of the change:

| Prefix | Use for |
| --- | --- |
| `feat/` | New capability or user-visible functionality |
| `fix/` | Correcting broken behavior |
| `refactor/` | Restructuring with no behavior change |
| `perf/` | Optimization where observable behavior is unchanged |
| `docs/` | Documentation, comments, README/design docs only |
| `test/` | Adding or fixing tests only |
| `chore/` | Deps, tooling, CI, config, `.gitignore`, release prep |
| `security/` | Fixing a vulnerability or hardening a boundary |

Branch hygiene:

- One concern per branch. If a change needs "and" to describe it,
  it is probably two branches.
- Name the change, not the component. `fix/env-parse-order` beats
  `fix/cli`. Keep it under ~40 characters.
- Phased or numbered work carries the phase in the name, when a
  project plan uses one: `feat/phase-4-config-backup`.
- Delete the branch after it merges.
- Ask before force-pushing, rebasing shared history, or deleting a
  branch that was pushed to a remote.

Merging: where a remote supports pull requests, push the branch,
open a PR, and let the platform merge it, instead of merging
locally.

- Squash and merge: the default for most PRs. Collapses the branch
  into one commit on the default branch.
- Rebase and merge: use when the branch's commits are each clean
  and meaningful on their own, worth preserving separately.
- Merge commit (`--no-ff`): use for a long-lived branch worth
  keeping visible in history.
- For a purely local merge outside a PR platform, default to
  `--no-ff` over a plain fast-forward, unless the project's own
  instructions say otherwise.

Push and open a pull request: treat "opened a pull request," not
"committed," as the finish line for any repo with a remote you
don't solely maintain. Confirm with the user before pushing or
opening a PR, unless they have given standing authorization for
that repo. Skip this step for a personal, single-maintainer repo,
or once the user says they will handle it themselves.

### Writing style

- Never use em dashes: neither the `—` character nor a `--`
  stand-in used as punctuation. This applies everywhere: code, docs,
  docstrings, commit messages, agent instruction files, chat
  replies, in any project. Rewrite with a comma, a colon,
  parentheses, or a second sentence instead. Exception: `--` is fine
  as a literal CLI argument or flag separator, for example
  `git commit -- file` or `some-command --flag`.
- Comments and docstrings should be concise: state the WHY, not the
  WHAT, and skip restating what already-readable code shows.

<!-- shared-rules:end -->
