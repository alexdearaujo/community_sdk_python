# HAND-WRITTEN: not modified by `make generate`. Edit directly.
"""Verifies each gRPC wrapper call reaches the right RPC with every argument set.

Mocked forwarding tests cannot see either failure this file guards against:
a call routed to another proto service's RPC of the same name (alerting's
AlertAutoAck `Delete` once went to SuppressionService), and an argument that
matches no request field (`get_device(deviceid=...)` once sent an empty `id`).
"""

from __future__ import annotations

import importlib
from typing import Any
from unittest.mock import MagicMock

import pytest
from _discovery import WrapperCase, build_all_kwargs, discover_cases, proto_field

from kentik_api.transports.grpc_client import GrpcTransport

ALL_CASES = discover_cases()


class _Stop(Exception):
    """Ends the call once the request is captured, before the response is parsed."""


def _grpc_wrapper(module: Any, wrapper_class: str) -> Any:
    transport = MagicMock(spec=GrpcTransport)
    transport.channel = MagicMock()
    # Each stub attribute becomes its RPC's full method path, so a test can see
    # which RPC a call reached.
    transport.channel.unary_unary.side_effect = lambda path, *a, **kw: path
    return getattr(module, wrapper_class)(transport)


def _capture_rpc(monkeypatch: pytest.MonkeyPatch, module: Any) -> dict[str, Any]:
    captured: dict[str, Any] = {}

    def _call_grpc(rpc_path, request, *, api_config=None):
        captured["rpc_path"] = rpc_path
        captured["request"] = request
        raise _Stop

    monkeypatch.setattr(module, "call_grpc", _call_grpc)
    return captured


@pytest.mark.parametrize(
    "case",
    ALL_CASES,
    ids=[f"{case.wrapper_class}.{case.method_name}" for case in ALL_CASES],
)
def test_every_argument_reaches_a_field_of_its_own_rpc(
    case: WrapperCase, monkeypatch: pytest.MonkeyPatch
):
    module = importlib.import_module(case.module_path)
    if not hasattr(module, "build_grpc_request"):
        pytest.skip("service has no gRPC stubs")
    wrapper = _grpc_wrapper(module, case.wrapper_class)
    method = getattr(wrapper, case.method_name)
    kwargs = build_all_kwargs(method)

    built: dict[str, Any] = {}

    def _build(message_cls, body, fields):
        built.update(message_cls=message_cls, body=body, fields=fields)
        return message_cls()

    monkeypatch.setattr(module, "build_grpc_request", _build)
    captured = _capture_rpc(monkeypatch, module)

    try:
        method(**kwargs)
    except _Stop:
        pass
    except NotImplementedError as exc:
        assert "not yet implemented" in str(exc)
        return

    request_descriptor = built["message_cls"].DESCRIPTOR
    # "/kentik.alerting.v202303.AlertAutoAckService/Delete"
    service_name, rpc_name = captured["rpc_path"].rsplit(".", 1)[1].split("/")
    rpc = request_descriptor.file.services_by_name[service_name].methods_by_name[
        rpc_name
    ]
    rest_module = getattr(module, case.rest_module_alias).__name__.rsplit(".", 1)[1]
    assert service_name == rest_module
    assert rpc.input_type is request_descriptor

    fields = built["fields"]
    unresolved = [
        path for path in fields if proto_field(request_descriptor, path) is None
    ]
    assert not unresolved, f"no {request_descriptor.name} field for {unresolved}"

    arguments = {
        name: value
        for name, value in kwargs.items()
        if name not in ("api_config_override", "data")
    }
    assert len(fields) == len(arguments)
    for name, value in arguments.items():
        assert any(v is value for v in fields.values()), f"{name} is not sent"
    assert (built["body"] is not None) == ("data" in kwargs)


def _sent_device_request(monkeypatch, method_name: str, **kwargs) -> Any:
    module = importlib.import_module("kentik_api.gen.device.services.device")
    wrapper = _grpc_wrapper(module, "DeviceServiceWrapper")
    captured = _capture_rpc(monkeypatch, module)
    with pytest.raises(_Stop):
        getattr(wrapper, method_name)(**kwargs)
    return captured


def test_get_device_sends_the_id_and_query_options(monkeypatch):
    sent = _sent_device_request(
        monkeypatch, "get_device", deviceid="42", querynoCustomColumns=True
    )

    assert sent["rpc_path"].endswith("DeviceService/GetDevice")
    assert sent["request"].id == "42"
    assert sent["request"].query.no_custom_columns is True


def test_delete_device_sends_the_id(monkeypatch):
    sent = _sent_device_request(monkeypatch, "delete_device", deviceid="42")

    assert sent["rpc_path"].endswith("DeviceService/DeleteDevice")
    assert sent["request"].id == "42"
