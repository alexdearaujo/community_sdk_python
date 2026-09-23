# HAND-WRITTEN: not modified by `make generate`. Edit directly.
"""The gRPC transport bounds every call with a deadline (FR-001, FR-002, SC-001)."""

from __future__ import annotations

import socket
import threading
import time
from types import SimpleNamespace

import pytest

from kentik_api.auth.credentials import KentikCredentials
from kentik_api.core.api_config import APIConfig
from kentik_api.core.grpc_runtime import call_grpc
from kentik_api.errors import TransportError
from kentik_api.transports.grpc_client import GrpcTransport, _DefaultDeadlineInterceptor

CREDENTIALS = KentikCredentials(email="dev@example.com", api_token="token")


def _details(timeout: float | None) -> SimpleNamespace:
    return SimpleNamespace(
        method="/svc.Service/Op",
        timeout=timeout,
        metadata=None,
        credentials=None,
        wait_for_ready=None,
        compression=None,
    )


def _intercepted_timeout(
    api_config: APIConfig, call_timeout: float | None
) -> float | None:
    seen = {}

    def continuation(details, request):
        seen["timeout"] = details.timeout
        seen["method"] = details.method
        return "response"

    result = _DefaultDeadlineInterceptor(api_config).intercept_unary_unary(
        continuation, _details(call_timeout), request=object()
    )
    assert result == "response"
    assert seen["method"] == "/svc.Service/Op"
    return seen["timeout"]


def test_call_without_a_deadline_gets_the_configured_one():
    assert _intercepted_timeout(APIConfig(grpc_deadline=7.5), None) == 7.5


def test_deadline_derives_from_the_shared_timeout_by_default():
    assert _intercepted_timeout(APIConfig(timeout=12.0), None) == 12.0


def test_call_that_already_carries_a_deadline_keeps_it():
    assert _intercepted_timeout(APIConfig(grpc_deadline=7.5), 300.0) == 300.0


def test_transport_uses_the_config_it_is_given():
    config = APIConfig(grpc_deadline=3.0)
    transport = GrpcTransport(CREDENTIALS, target="127.0.0.1:1", api_config=config)
    try:
        assert transport.api_config is config
    finally:
        transport.close()


def test_transport_defaults_to_a_config_carrying_its_credentials():
    transport = GrpcTransport(CREDENTIALS, target="127.0.0.1:1")
    try:
        assert transport.api_config.auth_email == "dev@example.com"
        assert transport.api_config.grpc_deadline == 60.0
    finally:
        transport.close()


@pytest.fixture
def black_hole_target():
    """A local port that accepts connections and never replies."""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("127.0.0.1", 0))
    server.listen()
    accepted: list[socket.socket] = []
    stop = threading.Event()

    def accept_forever() -> None:
        server.settimeout(0.1)
        while not stop.is_set():
            try:
                accepted.append(server.accept()[0])
            except OSError:
                continue

    thread = threading.Thread(target=accept_forever, daemon=True)
    thread.start()
    yield f"127.0.0.1:{server.getsockname()[1]}"
    stop.set()
    thread.join()
    for conn in accepted:
        conn.close()
    server.close()


def test_unresponsive_server_fails_at_the_deadline_instead_of_hanging(
    black_hole_target,
):
    transport = GrpcTransport(
        CREDENTIALS, target=black_hole_target, api_config=APIConfig(grpc_deadline=0.5)
    )
    stub = transport.channel.unary_unary(
        "/svc.Service/Op",
        request_serializer=lambda _: b"",
        response_deserializer=lambda raw: raw,
    )
    try:
        started = time.monotonic()
        with pytest.raises(TransportError, match="DEADLINE_EXCEEDED"):
            call_grpc(stub, object())
        assert time.monotonic() - started < 5.0
    finally:
        transport.close()
