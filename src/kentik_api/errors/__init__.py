# HAND-WRITTEN: not modified by `make generate`. Edit directly.
from __future__ import annotations

from typing import Any, Optional


class KentikError(Exception):
    """Base exception for all SDK-specific errors."""


class ConfigurationError(KentikError):
    """Raised for invalid SDK configuration values."""


class AuthenticationError(KentikError):
    """Raised for authentication/authorization failures."""


class TransportError(KentikError):
    """Raised when the transport layer fails before receiving a valid response."""


class HTTPException(KentikError):
    """Raised when an API HTTP response does not match expectations."""

    def __init__(
        self,
        status_code: int,
        message: str,
        *,
        method: Optional[str] = None,
        path: Optional[str] = None,
        details: Optional[dict[str, Any]] = None,
    ):
        self.status_code = status_code
        self.message = message
        self.method = method
        self.path = path
        self.details = details or {}
        super().__init__(f"{status_code}: {message}")


__all__ = [
    "KentikError",
    "ConfigurationError",
    "AuthenticationError",
    "TransportError",
    "HTTPException",
]
