<!-- HAND-WRITTEN: not modified by [`make generate`](../../Makefile). Edit directly. -->

# Dependencies

This page lists each package that `pyproject.toml` declares, why the project
needs it, and what the last audit decided. The audit on 2026-10-17 read the
release notes of each package and probed this repository.
`tests/smoke/test_declared_dependencies.py` fails when this table and
`pyproject.toml` disagree, or when code imports a package that no group
declares.

Groups:

- **runtime**: installed with the SDK.
- **analytics**: the optional `kentik-api[analytics]` extra.
- **dev**, **test**, **docs**: dependency groups for contributors. They are
  not part of the published package.
- **build**: the build backend in `[build-system]`.

| Dependency | Group | Purpose | Decision (audit 2026-10-17) |
| --- | --- | --- | --- |
| python-dotenv | runtime | Reads `.env` credentials into a dict, never into the environment | Keep. Floor 1.2.4: earlier versions drop the first variable after a byte order mark and read `KEY= # comment` as the comment text |
| googleapis-common-protos | runtime | Google API proto types that the gRPC stubs import | Keep |
| grpcio | runtime | gRPC transport | Keep |
| protobuf | runtime | Proto messages for the gRPC transport | Keep. It ships no type information, so `types-protobuf` stays |
| httpx | runtime | REST transport, used only by `request_json()` | Keep the `<1` cap. No release since 2024-12-06 |
| pydantic | runtime | Request and response models | Keep. Floor 2.14.0: thread-safe model rebuild, constant-time secret comparison |
| pandas | analytics | DataFrames in `kentik_api.analytics` | Keep |
| pyarrow | analytics | Reads and writes the Parquet cache | Keep |
| pyyaml | analytics | Reads query definition files | Keep |
| grpcio-tools | dev | Compiles the protos during generation | Keep, pinned to the `grpcio` version |
| types-protobuf | dev | Type information for protobuf | Keep |
| ty | dev | Type checker (`make typecheck`) | Keep. Floor 0.0.84: fixes advisory GHSA-vxvm-j4xq-q7m4 |
| ruff | dev | Lints Python, formats Python and the Python blocks in Markdown | Keep, pinned. 0.17 default rules adopted for hand-written code |
| openapi-python-generator | dev | Generates the REST modules and models | Keep, pinned. See the openapi-python-generator section below |
| packaging | dev | Version and requirement parsing in the release scripts and tests | Keep |
| rumdl | dev | Markdown linter that reads `.markdownlint-cli2.jsonc` and needs no Node | Added, pinned |
| markdown-it-py | dev | Renders the impact report to HTML in `scripts/impact_report.py` | Declared: it was imported but installed only through Sphinx |
| poethepoet | dev | Task runner: every project task runs as `uv run poe <task>` on any OS | Added, pinned. Its agent skill in `.claude/skills/poethepoet/` must match this version |
| pytest | test | Test runner, in strict mode | Keep |
| respx | test | Mocks HTTP for the mocked test layers | Keep. Replacing it needs a transport seam in the protected runtime |
| jinja2 | test | Renders the generator templates in `tests/generator/` | Declared: it was imported but installed only through other packages |
| httpcore | test | Checks the httpx connection pool in `tests/runtime/` | Declared: it was imported but installed only through httpx |
| autodoc-pydantic | docs | Renders model field tables in the service pages | Keep. Last release 2024-04-27, but the repository is active |
| myst-parser | docs | Markdown pages in Sphinx, with GitHub alerts | Keep. Floor 5.1.0: first release with the `alert` extension |
| sphinx | docs | Builds the docs | Keep |
| sphinx-book-theme | docs | Docs theme | Keep |
| sphinxcontrib-mermaid | docs | Renders Mermaid diagrams | Keep. 1.0.0 builds with Sphinx 9.1.0 |
| hatchling | build | Build backend | Keep. `uv_build` has no documented VCS version source |
| hatch-vcs | build | Version from the git tag | Keep |

## openapi-python-generator

The generator always installs Black, isort, and orjson, but this project
calls it with `--formatter none` and formats with Ruff, so the three
packages are unused. They are in the dev group only, so no SDK user
installs them.

Upstream had no release or merge from 2025-09-29 to the audit. The project
keeps the exact pin, and neither forks it nor sends it a pull request for
this finding. Fork it when one of these is true:

- A needed generator fix is not possible in `scripts/openapi_templates/` or
  `scripts/generation/fixup.py`, and upstream does not answer a pull request.
- A security advisory affects the generator or a dependency it requires,
  and upstream publishes no fix.
- Fixing problems at the source would retire a large part of `fixup.py`.

To try a fork without a code change, set `OPENAPI_GENERATOR_FROM` (see
[Local generation workflow](local_generation_workflow.md)).

## Markdown rules

rumdl checks Markdown in `make lint` and in CI. An editor with the
markdownlint extension reads the same `.markdownlint-cli2.jsonc`, but can
report a different result, for example on table style. The CI result
decides.
