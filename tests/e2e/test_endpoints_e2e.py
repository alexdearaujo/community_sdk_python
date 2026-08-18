"""End-to-end coverage against the real Kentik API.

Every other suite under tests/generated/ proves the SDK is internally
self-consistent using mocked HTTP responses. This module is the one place
that calls the real API, so it can catch the one thing mocks structurally
cannot: the real API's behavior drifting from what the schema (and therefore
the generated code) assumes.

Scope, by design (see CLAUDE.md's end-to-end testing requirement):
  - Only GET (read-only, non-mutating) operations are auto-covered and
    actually called here. Discovered the same way as every other generated
    suite -- via tests/_discovery.py -- so new read endpoints get e2e
    coverage automatically as the schema grows.
  - Create/Update/Delete operations are intentionally NOT auto-covered
    (see test_mutating_endpoint_excluded_from_e2e below): they are hard to
    reverse against a real account and need a purpose-built, cleaned-up
    fixture per operation, added deliberately rather than as a side effect
    of this file existing.
  - A read call passes if it returns a correctly-typed response OR raises a
    generated KentikError subclass -- both prove the real request/response/
    error path still matches the schema. Only a truly unexpected exception
    (e.g. a raw pydantic.ValidationError, or anything outside the SDK's own
    error hierarchy) is a failure, since we don't control what data exists in
    the real account being tested against.

Opt-in only: excluded from `make test`/`make all` by the `e2e` pytest marker
(see pyproject.toml's addopts) and only actually run via `make test-e2e` or
`pytest -m e2e`. The `real_client` fixture (tests/e2e/conftest.py) skips the
whole module if no real credentials are configured.
"""

from __future__ import annotations

import importlib
from dataclasses import dataclass

import pytest
from _discovery import (
    WrapperCase,
    build_all_kwargs,
    case_label,
    discover_cases,
    parse_rest_call_metadata,
)

from kentik_api.errors import KentikError

pytestmark = pytest.mark.e2e


@dataclass(frozen=True)
class EndpointCase:
    wrapper: WrapperCase
    operation_name: str
    method: str


def _rest_module(case: WrapperCase):
    module = importlib.import_module(case.module_path)
    return getattr(module, case.rest_module_alias)


def _discover_endpoint_cases() -> list[EndpointCase]:
    cases: list[EndpointCase] = []
    for wrapper_case in discover_cases():
        rest_module = _rest_module(wrapper_case)
        metadata = parse_rest_call_metadata(
            rest_module, wrapper_case.rest_function_name
        )
        if metadata is None:
            continue
        cases.append(
            EndpointCase(
                wrapper=wrapper_case,
                operation_name=metadata.operation_name,
                method=metadata.method.lower(),
            )
        )
    return cases


_ALL_ENDPOINT_CASES = _discover_endpoint_cases()
READ_CASES = [c for c in _ALL_ENDPOINT_CASES if c.method == "get"]
MUTATING_CASES = [c for c in _ALL_ENDPOINT_CASES if c.method != "get"]


def _service_attr(case: EndpointCase) -> str:
    # module_path is "kentik_api.gen.<service>.<services|service>.<service>";
    # KentikClientMixin mounts wrappers as self.<service> using that same name.
    return case.wrapper.module_path.split(".")[2]


@pytest.mark.parametrize(
    "case",
    READ_CASES,
    ids=[f"{c.wrapper.wrapper_class}.{c.wrapper.method_name}" for c in READ_CASES],
)
def test_read_endpoint_against_real_api(case: EndpointCase, real_client):
    service_client = getattr(real_client, _service_attr(case))
    method = getattr(service_client, case.wrapper.method_name)
    kwargs = build_all_kwargs(method)

    label = f"{case_label(case.wrapper)} ({case.operation_name})"
    print(f'E2E: calling "{label}" against the real API. START')
    try:
        method(**kwargs)
    except KentikError as exc:
        print(
            f'E2E: "{label}" raised {type(exc).__name__} '
            f"(status={getattr(exc, 'status_code', 'n/a')}) -- a real, "
            "generated error response is a valid outcome. RESULT=PASS"
        )
        return
    except Exception:
        print(f'E2E: "{label}" raised an UNEXPECTED exception. RESULT=FAIL')
        raise
    print(f'E2E: "{label}" returned a typed response. RESULT=PASS')


@pytest.mark.skip(
    reason=(
        "Mutating (non-GET) operations are intentionally excluded from "
        "automatic e2e coverage -- see CLAUDE.md's end-to-end testing "
        "requirement. Add a dedicated test with real setup/teardown for this "
        "specific operation if you need live coverage here."
    )
)
@pytest.mark.parametrize(
    "case",
    MUTATING_CASES,
    ids=[f"{c.wrapper.wrapper_class}.{c.wrapper.method_name}" for c in MUTATING_CASES],
)
def test_mutating_endpoint_excluded_from_e2e(case: EndpointCase, real_client):
    raise NotImplementedError(
        "Not auto-implemented by design -- see the skip reason above."
    )
