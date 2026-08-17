from __future__ import annotations

import importlib
from typing import Any

import pytest

from kentik_api.auth.credentials import KentikCredentials
from kentik_api.transports.grpc_client import GrpcTransport
from kentik_api.transports.rest_client import RestTransport

from _discovery import (
    WrapperCase,
    build_all_kwargs,
    build_required_kwargs,
    case_label,
    discover_cases,
    print_case_result,
    print_case_start,
)

ALL_CASES = discover_cases()
# Every discovered wrapper case is exercised for every test below, including
# the negative-path ones: with only ~200 endpoints today this stays fast
# (sub-second), and CLAUDE.md's test coverage requirement rules out sampling.
NEGATIVE_CASES = ALL_CASES


@pytest.mark.parametrize(
    "case",
    ALL_CASES,
    ids=[f"{case.wrapper_class}.{case.method_name}" for case in ALL_CASES],
)
def test_wrapper_forwards_to_rest_module(
    case: WrapperCase, monkeypatch: pytest.MonkeyPatch
):
    print_case_start(case, mode="rest-forward")
    module = importlib.import_module(case.module_path)
    wrapper_cls = getattr(module, case.wrapper_class)

    transport = RestTransport(
        KentikCredentials(email="dev@example.com", api_token="token"),
        base_url="https://api.example.com",
    )
    wrapper = wrapper_cls(transport)
    method = getattr(wrapper, case.method_name)
    kwargs = build_required_kwargs(method)

    rest_module = getattr(module, case.rest_module_alias)
    sentinel = object()
    captured: dict[str, Any] = {}

    def _fake_rest_call(**called_kwargs: Any) -> Any:
        print(
            f'Testing against "{case_label(case)}". '
            f"Intercepted REST call with args={sorted(called_kwargs.keys())}"
        )
        captured.update(called_kwargs)
        return sentinel

    monkeypatch.setattr(rest_module, case.rest_function_name, _fake_rest_call)

    try:
        result = method(**kwargs)

        assert result is sentinel
        assert "api_config_override" in captured
        for key, value in kwargs.items():
            assert key in captured
            assert captured[key] is value
        print_case_result(case, mode="rest-forward", result="PASS")
    except Exception:
        print_case_result(case, mode="rest-forward", result="FAIL")
        raise


@pytest.mark.parametrize(
    "case",
    ALL_CASES,
    ids=[f"all-options:{case.wrapper_class}.{case.method_name}" for case in ALL_CASES],
)
def test_wrapper_forwards_all_declared_options(
    case: WrapperCase, monkeypatch: pytest.MonkeyPatch
):
    """Every declared parameter (required AND optional) must reach the REST call.

    `test_wrapper_forwards_to_rest_module` only populates required kwargs; this
    exercises the full option surface for the operation, per CLAUDE.md's test
    coverage requirement.
    """
    print_case_start(case, mode="all-options-forward")
    module = importlib.import_module(case.module_path)
    wrapper_cls = getattr(module, case.wrapper_class)

    transport = RestTransport(
        KentikCredentials(email="dev@example.com", api_token="token"),
        base_url="https://api.example.com",
    )
    wrapper = wrapper_cls(transport)
    method = getattr(wrapper, case.method_name)
    kwargs = build_all_kwargs(method)

    rest_module = getattr(module, case.rest_module_alias)
    sentinel = object()
    captured: dict[str, Any] = {}

    def _fake_rest_call(**called_kwargs: Any) -> Any:
        captured.update(called_kwargs)
        return sentinel

    monkeypatch.setattr(rest_module, case.rest_function_name, _fake_rest_call)

    try:
        result = method(**kwargs)

        assert result is sentinel
        assert "api_config_override" in captured
        for key, value in kwargs.items():
            assert key in captured
            assert captured[key] is value
        print_case_result(case, mode="all-options-forward", result="PASS")
    except Exception:
        print_case_result(case, mode="all-options-forward", result="FAIL")
        raise


@pytest.mark.parametrize(
    "case",
    ALL_CASES,
    ids=[f"grpc:{case.wrapper_class}.{case.method_name}" for case in ALL_CASES],
)
def test_wrapper_raises_for_grpc_unimplemented(case: WrapperCase):
    print_case_start(case, mode="grpc-not-implemented")
    module = importlib.import_module(case.module_path)
    wrapper_cls = getattr(module, case.wrapper_class)

    grpc_transport = GrpcTransport.__new__(GrpcTransport)
    wrapper = wrapper_cls(grpc_transport)
    method = getattr(wrapper, case.method_name)
    kwargs = build_required_kwargs(method)

    try:
        with pytest.raises(NotImplementedError):
            method(**kwargs)
        print_case_result(case, mode="grpc-not-implemented", result="PASS")
    except Exception:
        print_case_result(case, mode="grpc-not-implemented", result="FAIL")
        raise


@pytest.mark.parametrize(
    "case",
    NEGATIVE_CASES,
    ids=[f"bad-kw:{case.wrapper_class}.{case.method_name}" for case in NEGATIVE_CASES],
)
def test_wrapper_rejects_unexpected_kwarg(case: WrapperCase):
    print_case_start(case, mode="bad-kwarg")
    module = importlib.import_module(case.module_path)
    wrapper_cls = getattr(module, case.wrapper_class)

    transport = RestTransport(
        KentikCredentials(email="dev@example.com", api_token="token"),
        base_url="https://api.example.com",
    )
    wrapper = wrapper_cls(transport)
    method = getattr(wrapper, case.method_name)
    kwargs = build_required_kwargs(method)
    kwargs["__unexpected_test_kwarg"] = "bad-value"

    try:
        with pytest.raises(TypeError):
            method(**kwargs)
        print_case_result(case, mode="bad-kwarg", result="PASS")
    except Exception:
        print_case_result(case, mode="bad-kwarg", result="FAIL")
        raise


@pytest.mark.parametrize(
    "case",
    NEGATIVE_CASES,
    ids=[
        f"missing-required:{case.wrapper_class}.{case.method_name}"
        for case in NEGATIVE_CASES
    ],
)
def test_wrapper_rejects_missing_required_argument(case: WrapperCase):
    print_case_start(case, mode="missing-required")
    module = importlib.import_module(case.module_path)
    wrapper_cls = getattr(module, case.wrapper_class)

    transport = RestTransport(
        KentikCredentials(email="dev@example.com", api_token="token"),
        base_url="https://api.example.com",
    )
    wrapper = wrapper_cls(transport)
    method = getattr(wrapper, case.method_name)
    kwargs = build_required_kwargs(method)

    if not kwargs:
        pytest.skip("No required arguments for this wrapper method.")

    missing_key = sorted(kwargs.keys())[0]
    bad_kwargs = {k: v for k, v in kwargs.items() if k != missing_key}

    try:
        with pytest.raises(TypeError):
            method(**bad_kwargs)
        print_case_result(case, mode="missing-required", result="PASS")
    except Exception:
        print_case_result(case, mode="missing-required", result="FAIL")
        raise


@pytest.mark.parametrize(
    "case",
    NEGATIVE_CASES,
    ids=[
        f"unsupported-transport:{case.wrapper_class}.{case.method_name}"
        for case in NEGATIVE_CASES
    ],
)
def test_wrapper_rejects_unsupported_transport(case: WrapperCase):
    print_case_start(case, mode="unsupported-transport")
    module = importlib.import_module(case.module_path)
    wrapper_cls = getattr(module, case.wrapper_class)

    wrapper = wrapper_cls(object())
    method = getattr(wrapper, case.method_name)
    kwargs = build_required_kwargs(method)

    try:
        with pytest.raises(TypeError, match="Unsupported transport type"):
            method(**kwargs)
        print_case_result(case, mode="unsupported-transport", result="PASS")
    except Exception:
        print_case_result(case, mode="unsupported-transport", result="FAIL")
        raise
