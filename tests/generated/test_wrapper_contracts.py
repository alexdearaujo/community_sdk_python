# HAND-WRITTEN: not modified by `uv run poe generate`. Edit directly.
from __future__ import annotations

import importlib
from typing import Any
from unittest.mock import MagicMock

import pytest
from _discovery import (
    WrapperCase,
    build_all_kwargs,
    build_required_kwargs,
    case_label,
    discover_cases,
    print_case_result,
    print_case_start,
    recorded_grpc_route,
    sample_grpc_response,
)
from google.protobuf.json_format import ParseDict

from kentik_api.auth.credentials import KentikCredentials
from kentik_api.core.api_config import APIConfig
from kentik_api.transports.grpc_client import GrpcTransport
from kentik_api.transports.rest_client import RestTransport

ALL_CASES = discover_cases()
# Every discovered wrapper case is exercised for every test below, including
# the negative-path ones: with only ~200 endpoints today this stays fast
# (sub-second), and AGENTS.md's test coverage requirement rules out sampling.
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
        # Override omitted: the client's own config, unchanged (FR-020).
        assert captured["api_config_override"] is transport.api_config
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
    exercises the full option surface for the operation, per AGENTS.md's test
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
        # Override supplied: it replaces the client's config wholesale (FR-021).
        assert isinstance(kwargs["api_config_override"], APIConfig)
        assert captured["api_config_override"] is kwargs["api_config_override"]
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
def test_wrapper_raises_for_grpc_unimplemented(
    case: WrapperCase, monkeypatch: pytest.MonkeyPatch
):
    """Verify gRPC wrappers either route through call_grpc (implemented) or raise
    NotImplementedError (no stub yet). Uses a mock transport with a mock channel
    so wrapper __init__ succeeds without a real gRPC server.
    """
    print_case_start(case, mode="grpc-not-implemented")
    module = importlib.import_module(case.module_path)
    wrapper_cls = getattr(module, case.wrapper_class)

    # MagicMock satisfies isinstance(x, GrpcTransport) checks and provides a
    # mock .channel attribute so stub initialization in __init__ succeeds.
    grpc_transport = MagicMock(spec=GrpcTransport)
    grpc_transport.channel = MagicMock()
    wrapper = wrapper_cls(grpc_transport)
    method = getattr(wrapper, case.method_name)
    kwargs = build_required_kwargs(method)

    _grpc_was_called = False
    override = APIConfig(auth_email="o@example.com", auth_token="t", grpc_deadline=7.0)
    kwargs["api_config_override"] = override

    received_configs: list[Any] = []
    route = recorded_grpc_route(case)
    response = sample_grpc_response(case) if route else None

    def _mock_call_grpc(stub_method, request, *, api_config=None, error_cls=None):
        nonlocal _grpc_was_called
        _grpc_was_called = True
        received_configs.append(api_config)
        return response, None  # every field set, no quota

    # Patch call_grpc so the gRPC branch runs without a real server.
    if hasattr(module, "call_grpc"):
        monkeypatch.setattr(module, "call_grpc", _mock_call_grpc)
    # Patch request building so sample kwargs (e.g. "view_value" for an enum)
    # never hit real proto parsing; test_grpc_request_mapping.py covers that.
    if hasattr(module, "build_grpc_request"):
        monkeypatch.setattr(module, "build_grpc_request", lambda *a, **kw: MagicMock())

    try:
        result = method(**kwargs)
    except NotImplementedError as exc:
        # Two different conditions raise this. "not yet implemented" means the
        # generator found no gRPC method for this operation, which is fine.
        # "failed to import" means __init__ swallowed an ImportError or
        # TypeError and the service has no gRPC at all.
        assert "failed to import" not in str(exc), (
            f"{case.wrapper_class}.{case.method_name} reported gRPC as unavailable "
            f"because its stub is None, not because the operation lacks a gRPC "
            f"translation. See tests/generated/test_grpc_stub_wiring.py for the "
            f"underlying import error. Original message: {exc}"
        )
        assert route is None, f"api_surface.json routes this method to {route}"
        assert not _grpc_was_called
        print_case_result(case, mode="grpc-not-implemented", result="PASS")
        return

    assert _grpc_was_called, "Expected gRPC call to route through call_grpc"
    # The override must reach call_grpc, where it sets this call's deadline (FR-019).
    assert received_configs == [override]
    if result is not None:
        assert response is not None
        # Every value the server sent survives parsing; a dropped field fails here.
        dumped = result.model_dump(mode="json", by_alias=True, exclude_none=True)
        assert ParseDict(dumped, type(response)()) == response
    print_case_result(case, mode="grpc-not-implemented", result="PASS")


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

    missing_key = min(kwargs)
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
