# HAND-WRITTEN: not modified by `make generate`. Edit directly.
from __future__ import annotations

import grpc

from kentik_api.core.grpc_runtime import map_grpc_error
from kentik_api.errors import AuthenticationError, HTTPException


class FakeRpcError(grpc.RpcError):
    def __init__(self, code: grpc.StatusCode, details: str | None = None) -> None:
        self._code = code
        self._details = details

    def code(self) -> grpc.StatusCode:
        return self._code

    def details(self) -> str | None:
        return self._details


def test_unauthenticated_raises_auth_error():
    exc = FakeRpcError(grpc.StatusCode.UNAUTHENTICATED, "bad token")
    result = map_grpc_error(exc)
    assert isinstance(result, AuthenticationError)
    assert "bad token" in str(result)


def test_not_found_maps_to_404():
    exc = FakeRpcError(grpc.StatusCode.NOT_FOUND, "missing")
    result = map_grpc_error(exc, method="GET", path="/things/1")
    assert isinstance(result, HTTPException)
    assert result.status_code == 404
    assert "missing" in str(result)


def test_details_none_guard():
    # details() returning None must not raise TypeError
    exc = FakeRpcError(grpc.StatusCode.NOT_FOUND, None)
    result = map_grpc_error(exc)
    assert isinstance(result, HTTPException)
    assert result.status_code == 404


def test_unknown_status_maps_to_500():
    exc = FakeRpcError(grpc.StatusCode.CANCELLED, "cancelled")
    result = map_grpc_error(exc)
    assert isinstance(result, HTTPException)
    assert result.status_code == 500


def test_permission_denied_maps_to_403():
    exc = FakeRpcError(grpc.StatusCode.PERMISSION_DENIED, "no")
    result = map_grpc_error(exc)
    assert isinstance(result, HTTPException)
    assert result.status_code == 403


def test_resource_exhausted_maps_to_429():
    exc = FakeRpcError(grpc.StatusCode.RESOURCE_EXHAUSTED, "rate")
    result = map_grpc_error(exc)
    assert isinstance(result, HTTPException)
    assert result.status_code == 429
