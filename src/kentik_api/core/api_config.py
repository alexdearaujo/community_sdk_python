# HAND-WRITTEN: not modified by `make generate`. Edit directly.
import ipaddress
import math
import os
import threading
import time
import urllib.request
from typing import Optional, cast

import httpx

from kentik_api.core.rate_limit import RateLimit
from kentik_api.errors import ConfigurationError, HTTPException

__all__ = ["APIConfig", "HTTPException"]

# Retries only a failed connection attempt, which never reached the server, so
# no request can be replayed (FR-032). A response of any status is never retried.
_CONNECT_RETRIES = 2

# A request extension holding the call's time.monotonic() deadline.
DEADLINE_EXTENSION = "kentik_deadline"


class _DeadlineStream(httpx.SyncByteStream):
    def __init__(
        self, stream: httpx.SyncByteStream, deadline: float, request: httpx.Request
    ):
        self._stream = stream
        self._deadline = deadline
        self._request = request

    def __iter__(self):
        for chunk in self._stream:
            _check_deadline(self._deadline, self._request)
            yield chunk

    def close(self) -> None:
        self._stream.close()


def _check_deadline(deadline: float, request: httpx.Request) -> None:
    if time.monotonic() > deadline:
        raise httpx.ReadTimeout("the call's total deadline passed", request=request)


class _DeadlineTransport(httpx.HTTPTransport):
    """Holds a call to its total deadline while the response arrives.

    httpx's read timeout restarts on every chunk, so a server that keeps
    trickling bytes would otherwise hold the call open indefinitely.
    """

    def handle_request(self, request: httpx.Request) -> httpx.Response:
        response = super().handle_request(request)
        deadline = request.extensions.get(DEADLINE_EXTENSION)
        if deadline is None:
            return response
        try:
            _check_deadline(deadline, request)
        except httpx.ReadTimeout:
            response.close()
            raise
        stream = cast(httpx.SyncByteStream, response.stream)
        response.stream = _DeadlineStream(stream, deadline, request)
        return response


def _environment_proxies() -> dict[str, str | None]:
    """Maps httpx mount patterns to a proxy URL, or None for a host that goes direct.

    Mirrors what httpx builds from the environment, with public APIs only, so an
    httpx release that moves its private helpers cannot break the import.
    """
    info = urllib.request.getproxies()
    routes: dict[str, str | None] = {}
    for scheme in ("http", "https", "all"):
        if url := info.get(scheme):
            routes[f"{scheme}://"] = url if "://" in url else f"http://{url}"

    for host in (h.strip() for h in info.get("no", "").split(",")):
        if host == "*":
            return {}
        if not host:
            continue
        try:
            ipaddress.ip_address(host.strip("[]"))
            exact = True
        except ValueError:
            exact = host.lower() == "localhost"
        routes[f"all://{host if exact else '*' + host}"] = None
    return routes


def _require_positive(field: str, value: float) -> None:
    # `not value > 0` rather than `value <= 0` so NaN is rejected too.
    if not value > 0 or math.isinf(value):
        raise ConfigurationError(
            f"{field} must be a finite positive number of seconds, got {value!r}"
        )


class APIConfig:
    """Centralized API Configuration for all generated REST services.

    `timeout` is the one shared default. `rest_timeout` and `grpc_deadline`
    derive from it when omitted, so the two transports cannot drift apart.

    A number bounds the whole call on either transport. A `rest_timeout`
    given as an `httpx.Timeout` keeps httpx's meaning instead: it bounds
    each phase, and each read, separately, with no total deadline.
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
        self.rest_deadline: float | None = None
        if not isinstance(rest_timeout, httpx.Timeout):
            self.rest_deadline = rest_timeout
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

        # Keyed by endpoint (REST path or gRPC method), the granularity Kentik
        # enforces quota at; one client-wide value would mix budgets.
        self.rate_limits: dict[str, RateLimit] = {}

        self._client: httpx.Client | None = None
        self._closed = False
        self._client_lock = threading.Lock()
        self._pid = os.getpid()
        # Set on a with_timeout() copy, which borrows its origin's connection.
        self._shares_client_of: APIConfig | None = None

    def with_timeout(
        self,
        timeout: float | None = None,
        *,
        rest_timeout: httpx.Timeout | float | None = None,
        grpc_deadline: float | None = None,
    ) -> "APIConfig":
        """A copy of this config with different timeouts, for one slow call.

        Deliberately cannot change base_path, the credentials, or verify: a
        helper that copied credentials AND changed the host would silently send
        them somewhere new. Changing those four needs an explicit APIConfig(...).

        `timeout` resets both transports' bounds; `rest_timeout` and
        `grpc_deadline` refine one each, keeping this config's value otherwise.
        The copy shares this config's connection and quota tracking.
        """
        if timeout is None and rest_timeout is None and grpc_deadline is None:
            raise ConfigurationError(
                "with_timeout() needs at least one timeout to change"
            )
        if timeout is None:
            timeout = self.timeout
            if rest_timeout is None:
                rest_timeout = self.rest_deadline or self.rest_timeout
            grpc_deadline = (
                self.grpc_deadline if grpc_deadline is None else grpc_deadline
            )
        copy = APIConfig(
            base_path=self.base_path,
            auth_email=self.auth_email,
            auth_token=self.auth_token,
            verify=self.verify,
            timeout=timeout,
            rest_timeout=rest_timeout,
            grpc_deadline=grpc_deadline,
        )
        copy.rate_limits = self.rate_limits
        copy._shares_client_of = self._shares_client_of or self
        return copy

    @property
    def client(self) -> httpx.Client:
        """The one HTTP client every REST call on this config shares.

        Created on first use so a gRPC-only client never opens one. Reusing it
        keeps one pooled connection per host instead of a TLS handshake per call.
        """
        if self._shares_client_of is not None:
            return self._shares_client_of.client
        if self._pid != os.getpid():
            # A forked child must not write to the parent's sockets, and may have
            # inherited the lock held. The old client is dropped, not closed:
            # closing it would send a TLS close_notify on the parent's connection.
            self._pid = os.getpid()
            self._client_lock = threading.Lock()
            self._client = None
        with self._client_lock:
            if self._closed:
                raise ConfigurationError(
                    "This client was closed with close(); create a new KentikAPI to make more calls."
                )
            if self._client is None:
                self._client = httpx.Client(
                    base_url=self.base_path,
                    timeout=self.rest_timeout,
                    # verify belongs on the transport: a Client given one ignores its own.
                    transport=self._transport(),
                    mounts=self._proxy_mounts(),
                )
            return self._client

    def _transport(self, proxy: str | None = None) -> httpx.HTTPTransport:
        return _DeadlineTransport(
            verify=self.verify, retries=_CONNECT_RETRIES, proxy=proxy
        )

    def _proxy_mounts(self) -> dict[str, httpx.HTTPTransport | None]:
        """Routes REST through HTTP(S)_PROXY / ALL_PROXY, honoring NO_PROXY.

        httpx reads these itself only when it builds its own transport. Passing
        one, for the connection retries, turns that off, so rebuild the same
        routing here. None sends a host direct. Proxied calls get no connection
        retries: httpcore 1.0 drops `retries` for proxy connections.
        """
        return {
            pattern: None if proxy is None else self._transport(proxy)
            for pattern, proxy in _environment_proxies().items()
        }

    def close(self) -> None:
        """Releases the HTTP client. Safe to call more than once.

        A with_timeout() copy does not own its connection, so closing it is a
        no-op; close the config it came from.
        """
        if self._shares_client_of is not None:
            return
        with self._client_lock:
            if self._client is not None:
                self._client.close()
                self._client = None
            self._closed = True
