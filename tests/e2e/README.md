<!-- HAND-WRITTEN: not modified by [`make generate`](../../Makefile). Edit directly. -->

# End-to-End Tests (Real API, Opt-In)

Runs against the real Kentik API. Not part of [`make test`](../../Makefile) or
[`make all`](../../Makefile). See the layered strategy in
[../README.md](../README.md) for how this layer fits with the other
four mocked ones.

> [!WARNING]
> This suite calls a real Kentik account. Read this whole file
> before you add a test here.

## Files

| File | Role |
| --- | --- |
| `conftest.py` | The `real_client` (REST) and `grpc_real_client` (gRPC) fixtures. Both delegate all credential loading to `KentikAPI()` (a project-root `.env` file, or `KENTIK_EMAIL`/`KENTIK_API_TOKEN`). Either fixture skips the whole suite when no credentials are configured. |
| `test_endpoints_e2e.py` | The end-to-end operation tests, REST transport. |
| `test_endpoints_e2e_grpc.py` | The same coverage over the gRPC transport. Additionally treats `NotImplementedError` as a passing outcome, since gRPC translation is only implemented for a subset of operations (see CLAUDE.md's "gRPC transport is fully implemented" section). |

Endpoint discovery comes from
[`tests/_discovery.py`](../_discovery.py) (`discover_endpoint_cases()`), which builds on
the same `discover_cases()`/`WrapperCase` discovery [`tests/generated/`](../generated/README.md) uses, not a hand-written list. Both files above
share the identical discovered cases and GET-vs-mutating split.

## How read and mutating operations differ

```mermaid
flowchart TD
    A[Discovered operation] --> B{HTTP method}
    B -->|GET| T{Transport}
    T -->|"REST<br/>test_endpoints_e2e.py"| C[Call automatically]
    T -->|"gRPC<br/>test_endpoints_e2e_grpc.py"| C
    C --> D{Result}
    D -->|Correctly-typed response| E[Pass]
    D -->|Generated KentikError subclass| E
    D -->|"NotImplementedError<br/>(gRPC suite only)"| E
    D -->|Any other exception| F[Fail]
    B -->|POST / PUT / PATCH / DELETE| G["Skip automatically<br/>(@pytest.mark.skip,<br/>both transports)"]
    G --> H["Add a dedicated test with its own<br/>setup/teardown against a disposable<br/>resource, if you need live coverage"]

```

Only GET (read-only) operations run automatically. A read call
passes when it returns a correctly-typed response, or when it raises
a generated `KentikError` subclass. Either outcome proves the real
request, response, and error path still matches what the schema
declares. Only a genuinely unexpected exception counts as a failure,
since the test cannot control what data exists in the real account.

Create, Update, and Delete operations are deliberately not
auto-called. `test_mutating_endpoint_excluded_from_e2e` and its gRPC
twin `test_mutating_endpoint_excluded_from_e2e_grpc` each carry a
`@pytest.mark.skip` marker on purpose, because a mutating call
against a real account is hard to reverse. To add live coverage for
one mutating endpoint, write a dedicated test with its own setup and
teardown against a disposable resource. Do not wire it into the
auto-discovered path.

## Run

```bash
make test-e2e       # REST transport
make test-e2e-grpc  # gRPC transport
```

Neither suite runs by accident. `addopts` in `pyproject.toml`
excludes both by default; only `make test-e2e`/`-m e2e` (REST) or
`make test-e2e-grpc`/`-m e2e_grpc` (gRPC) runs them.

## Credentials

Set `KENTIK_EMAIL` and `KENTIK_API_TOKEN` in a project-root `.env`
file. Never hardcode credentials in test code. Never read or print
`.env` contents.
