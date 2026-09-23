# HAND-WRITTEN: not modified by `make generate`. Edit directly.
import threading
from typing import Optional

import httpx

from kentik_api.errors import ConfigurationError, HTTPException

__all__ = ["APIConfig", "HTTPException"]


def _require_positive(field: str, value: float) -> None:
    # `not value > 0` rather than `value <= 0` so NaN is rejected too.
    if not value > 0:
        raise ConfigurationError(
            f"{field} must be a positive number of seconds, got {value!r}"
        )


class APIConfig:
    """Centralized API Configuration for all generated REST services.

    `timeout` is the one shared default. `rest_timeout` and `grpc_deadline`
    derive from it when omitted, so the two transports cannot drift apart,
    but stay separate because httpx bounds four phases independently while
    gRPC has a single end-to-end deadline.
    """

    def __init__(
        self,
        base_path: str = "https://grpc.api.kentik.com",
        auth_email: Optional[str] = None,
        auth_token: Optional[str] = None,
        verify: bool = True,
        timeout: float = 60.0,
        rest_timeout: httpx.Timeout | float | None = None,
        grpc_deadline: float | None = None,
    ):
        self.base_path = base_path
        self.auth_email = auth_email
        self.auth_token = auth_token
        self.verify = verify

        _require_positive("timeout", timeout)
        self.timeout = timeout

        if rest_timeout is None:
            rest_timeout = timeout
        if not isinstance(rest_timeout, httpx.Timeout):
            rest_timeout = httpx.Timeout(rest_timeout)
        for phase in ("connect", "read", "write", "pool"):
            bound = getattr(rest_timeout, phase)
            # httpx reads None as "wait forever", which is the hang this bound exists to prevent.
            if bound is None:
                raise ConfigurationError(
                    f"rest_timeout.{phase} must be set; None would wait forever"
                )
            _require_positive(f"rest_timeout.{phase}", bound)
        self.rest_timeout: httpx.Timeout = rest_timeout

        if grpc_deadline is None:
            grpc_deadline = timeout
        _require_positive("grpc_deadline", grpc_deadline)
        self.grpc_deadline: float = grpc_deadline

        self._client: httpx.Client | None = None
        self._closed = False
        self._client_lock = threading.Lock()

    @property
    def client(self) -> httpx.Client:
        """The one HTTP client every REST call on this config shares.

        Created on first use so a gRPC-only client never opens one. Reusing it
        keeps one pooled connection per host instead of a TLS handshake per call.
        """
        with self._client_lock:
            if self._closed:
                raise ConfigurationError(
                    "This client was closed with close(); create a new KentikAPI to make more calls."
                )
            if self._client is None:
                self._client = httpx.Client(
                    base_url=self.base_path,
                    verify=self.verify,
                    timeout=self.rest_timeout,
                )
            return self._client

    def close(self) -> None:
        """Releases the HTTP client. Safe to call more than once."""
        with self._client_lock:
            if self._client is not None:
                self._client.close()
                self._client = None
            self._closed = True
