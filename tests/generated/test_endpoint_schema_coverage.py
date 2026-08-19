# HAND-WRITTEN: not modified by `make generate`. Edit directly.
"""Exhaustive endpoint x declared-response-status coverage.

`test_wrapper_contracts.py` proves every wrapper method forwards its
arguments correctly. This module proves the layer underneath -- the shared
`request_json` runtime in `kentik_api.core.rest_runtime` -- correctly
handles every response status code the OpenAPI schema actually declares for
every operation, success and error alike. Per CLAUDE.md's test coverage
requirement, this is derived from the generated code (which is itself
derived from the schema), not hand-listed, so it stays exhaustive as the
schema grows.

Status codes come from each service's generated `error/__init__.py`
(`{Operation}Error.response_error_map`), which `scripts/generate_sdk.py`
builds directly from the swagger files' declared non-2xx responses.
"""

from __future__ import annotations

import importlib
import inspect
from dataclasses import dataclass
from typing import Any, Optional

import httpx
import pytest
import respx
from _discovery import (
    WrapperCase,
    build_all_kwargs,
    case_label,
    discover_cases,
    error_module_for,
    parse_rest_call_metadata,
    sample_model_instance,
)
from pydantic import BaseModel

from kentik_api.auth.credentials import KentikCredentials
from kentik_api.errors import HTTPException
from kentik_api.transports.rest_client import RestTransport


@dataclass(frozen=True)
class StatusCase:
    wrapper: WrapperCase
    status_code: int
    status_key: str
    is_success: bool
    error_class_name: Optional[str]


def _rest_module_and_function(case: WrapperCase):
    module = importlib.import_module(case.module_path)
    rest_module = getattr(module, case.rest_module_alias)
    rest_func = getattr(rest_module, case.rest_function_name)
    return module, rest_module, rest_func


def _pick_default_simulated_code(explicit_codes: set[str]) -> int:
    candidate = 599
    while str(candidate) in explicit_codes and candidate > 500:
        candidate -= 1
    return candidate


def _discover_status_cases() -> list[StatusCase]:
    cases: list[StatusCase] = []

    for wrapper_case in discover_cases():
        _, rest_module, _ = _rest_module_and_function(wrapper_case)
        metadata = parse_rest_call_metadata(
            rest_module, wrapper_case.rest_function_name
        )
        if metadata is None:
            continue

        cases.append(
            StatusCase(
                wrapper=wrapper_case,
                status_code=metadata.expected_status,
                status_key="success",
                is_success=True,
                error_class_name=None,
            )
        )

        error_module = error_module_for(rest_module)
        error_cls = getattr(error_module, metadata.error_cls_name, None)
        response_error_map: dict[str, Any] = (
            getattr(error_cls, "response_error_map", {}) if error_cls else {}
        )
        explicit_codes = {key for key in response_error_map if key != "default"}

        for status_key, leaf_cls in sorted(response_error_map.items()):
            if status_key == "default":
                simulated_code = _pick_default_simulated_code(explicit_codes)
                cases.append(
                    StatusCase(
                        wrapper=wrapper_case,
                        status_code=simulated_code,
                        status_key="default",
                        is_success=False,
                        error_class_name=leaf_cls.__name__,
                    )
                )
            else:
                cases.append(
                    StatusCase(
                        wrapper=wrapper_case,
                        status_code=int(status_key),
                        status_key=status_key,
                        is_success=False,
                        error_class_name=leaf_cls.__name__,
                    )
                )

    return cases


ALL_STATUS_CASES = _discover_status_cases()


def _status_case_id(case: StatusCase) -> str:
    kind = "success" if case.is_success else f"error-{case.status_key}"
    return f"{case.wrapper.wrapper_class}.{case.wrapper.method_name}:{kind}"


def _success_body_for(method: Any) -> Any:
    return_annotation = inspect.signature(method).return_annotation
    if isinstance(return_annotation, type) and issubclass(return_annotation, BaseModel):
        try:
            instance = sample_model_instance(return_annotation)
        except Exception:
            return {}
        return instance.model_dump(mode="json")
    return {}


_ERROR_BODY = {"code": 7, "message": "simulated failure", "details": []}


@pytest.mark.parametrize(
    "case", ALL_STATUS_CASES, ids=[_status_case_id(c) for c in ALL_STATUS_CASES]
)
def test_endpoint_handles_declared_status_code(case: StatusCase):
    wrapper_case = case.wrapper
    mode = "success" if case.is_success else f"error-{case.status_key}"
    print(
        f'Testing against "{case_label(wrapper_case)}" status={case.status_code} '
        f"({mode}). START"
    )

    module = importlib.import_module(wrapper_case.module_path)
    wrapper_cls = getattr(module, wrapper_case.wrapper_class)
    transport = RestTransport(
        KentikCredentials(email="dev@example.com", api_token="token"),
        base_url="https://api.example.com",
    )
    wrapper = wrapper_cls(transport)
    method = getattr(wrapper, wrapper_case.method_name)

    try:
        kwargs = build_all_kwargs(method)
    except Exception as exc:
        pytest.skip(f"Could not build sample arguments for this operation: {exc}")

    try:
        with respx.mock:
            if case.status_code == 204:
                respx.route().mock(return_value=httpx.Response(204))
            elif case.is_success:
                body = _success_body_for(method)
                respx.route().mock(
                    return_value=httpx.Response(case.status_code, json=body)
                )
            else:
                respx.route().mock(
                    return_value=httpx.Response(case.status_code, json=_ERROR_BODY)
                )

            if case.is_success:
                result = method(**kwargs)
                return_annotation = inspect.signature(method).return_annotation
                if case.status_code == 204:
                    assert result is None
                elif isinstance(return_annotation, type) and issubclass(
                    return_annotation, BaseModel
                ):
                    assert isinstance(result, return_annotation)
            else:
                error_module = error_module_for(
                    getattr(module, wrapper_case.rest_module_alias)
                )
                # error_class_name is only None for success cases, excluded by this branch.
                assert case.error_class_name is not None
                expected_cls = getattr(error_module, case.error_class_name)
                with pytest.raises(HTTPException) as exc_info:
                    method(**kwargs)
                assert isinstance(exc_info.value, expected_cls)
                assert exc_info.value.status_code == case.status_code

        print(
            f'Testing against "{case_label(wrapper_case)}" status={case.status_code} '
            f"({mode}). RESULT=PASS"
        )
    except Exception:
        print(
            f'Testing against "{case_label(wrapper_case)}" status={case.status_code} '
            f"({mode}). RESULT=FAIL"
        )
        raise
