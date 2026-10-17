# HAND-WRITTEN: not modified by `uv run poe generate`. Edit directly.
from __future__ import annotations

from collections.abc import Callable
from typing import Any

import grpc
import pytest


class FakeRpcError(grpc.RpcError):
    """Stands in for a grpc.RpcError raised by a stub, with no channel."""

    def __init__(self, code: Any, details: str | None = None) -> None:
        self._code = code
        self._details = details

    def code(self) -> Any:
        return self._code

    def details(self) -> str | None:
        return self._details


@pytest.fixture
def rpc_error() -> Callable[..., FakeRpcError]:
    return FakeRpcError
