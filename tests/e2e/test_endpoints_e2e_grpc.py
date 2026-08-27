# HAND-WRITTEN: not modified by `make generate`. Edit directly.
"""End-to-end gRPC coverage against the real Kentik API.

Mirrors test_endpoints_e2e.py but drives every discovered read (GET)
operation through protocol="grpc" instead of REST. Endpoint discovery and
the GET-vs-mutating split are shared with the REST suite via
tests/_discovery.py (discover_endpoint_cases()), so both suites classify
the same operations the same way.

gRPC coverage is per-operation, not per-service (see CLAUDE.md's "gRPC
transport is fully implemented" section): a wrapper method raises
NotImplementedError when the service's proto companions failed to import,
or when the generator found no gRPC method matching that REST operation's
name. Neither case is a bug -- both count as a passing outcome here, same
as a correctly-typed response or a generated KentikError subclass.

Opt-in only: excluded from `make test`/`make all`/`make test-e2e` by the
`e2e_grpc` pytest marker (see pyproject.toml's addopts) and only actually
run via `make test-e2e-grpc` or `pytest -m e2e_grpc`. The
`grpc_real_client` fixture (tests/e2e/conftest.py) skips the whole module
if no real credentials are configured.
"""

from __future__ import annotations

import pytest
from _discovery import (
    EndpointCase,
    build_all_kwargs,
    case_label,
    discover_endpoint_cases,
    service_attr,
)

from kentik_api.errors import KentikError

pytestmark = pytest.mark.e2e_grpc

_ALL_ENDPOINT_CASES = discover_endpoint_cases()
READ_CASES = [c for c in _ALL_ENDPOINT_CASES if c.method == "get"]
MUTATING_CASES = [c for c in _ALL_ENDPOINT_CASES if c.method != "get"]


@pytest.mark.parametrize(
    "case",
    READ_CASES,
    ids=[f"{c.wrapper.wrapper_class}.{c.wrapper.method_name}" for c in READ_CASES],
)
def test_read_endpoint_against_real_api_grpc(case: EndpointCase, grpc_real_client):
    service_client = getattr(grpc_real_client, service_attr(case))
    method = getattr(service_client, case.wrapper.method_name)
    kwargs = build_all_kwargs(method)

    label = f"{case_label(case.wrapper)} ({case.operation_name})"
    print(f'E2E-gRPC: calling "{label}" against the real API. START')
    try:
        method(**kwargs)
    except NotImplementedError as exc:
        print(
            f'E2E-gRPC: "{label}" has no gRPC translation yet ({exc}) -- '
            "expected, not a bug. RESULT=PASS"
        )
        return
    except KentikError as exc:
        print(
            f'E2E-gRPC: "{label}" raised {type(exc).__name__} '
            f"(status={getattr(exc, 'status_code', 'n/a')}) -- a real, "
            "generated error response is a valid outcome. RESULT=PASS"
        )
        return
    except Exception:
        print(f'E2E-gRPC: "{label}" raised an UNEXPECTED exception. RESULT=FAIL')
        raise
    print(f'E2E-gRPC: "{label}" returned a typed response. RESULT=PASS')


@pytest.mark.skip(
    reason=(
        "Mutating (non-GET) operations are intentionally excluded from "
        "automatic e2e coverage, gRPC included -- see CLAUDE.md's "
        "end-to-end testing requirement. Add a dedicated test with real "
        "setup/teardown for this specific operation if you need live gRPC "
        "coverage here."
    )
)
@pytest.mark.parametrize(
    "case",
    MUTATING_CASES,
    ids=[f"{c.wrapper.wrapper_class}.{c.wrapper.method_name}" for c in MUTATING_CASES],
)
def test_mutating_endpoint_excluded_from_e2e_grpc(case: EndpointCase, grpc_real_client):
    raise NotImplementedError(
        "Not auto-implemented by design -- see the skip reason above."
    )
