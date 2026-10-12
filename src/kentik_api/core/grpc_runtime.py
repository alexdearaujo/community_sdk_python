# HAND-WRITTEN: not modified by `make generate`. Edit directly.
"""Shared gRPC call helper — the gRPC analogue of rest_runtime.request_json.

Every generated gRPC wrapper method routes through call_grpc so error
handling, status-code mapping, and transport failures stay in one place.
"""

from typing import Any

import grpc
from google.protobuf.json_format import ParseDict

from kentik_api.core.api_config import APIConfig
from kentik_api.core.rate_limit import RateLimit, rate_limit_of_rpc
from kentik_api.errors import (
    AuthenticationError,
    ConfigurationError,
    HTTPException,
    TransportError,
)

# Every non-OK code is classified explicitly, so none reaches a silent default.
# The HTTP value is the canonical grpc-gateway equivalent, the same status
# Kentik's Envoy transcoder returns to REST callers for that code.
_GRPC_STATUS_TO_HTTP: dict[grpc.StatusCode, int] = {
    grpc.StatusCode.INVALID_ARGUMENT: 400,
    grpc.StatusCode.FAILED_PRECONDITION: 400,
    grpc.StatusCode.OUT_OF_RANGE: 400,
    grpc.StatusCode.PERMISSION_DENIED: 403,
    grpc.StatusCode.NOT_FOUND: 404,
    grpc.StatusCode.ALREADY_EXISTS: 409,
    grpc.StatusCode.ABORTED: 409,
    grpc.StatusCode.RESOURCE_EXHAUSTED: 429,
    grpc.StatusCode.UNKNOWN: 500,
    grpc.StatusCode.INTERNAL: 500,
    grpc.StatusCode.DATA_LOSS: 500,
    grpc.StatusCode.UNIMPLEMENTED: 501,
}

# No response arrived for these, which REST reports as TransportError via
# httpx.RequestError. Claiming an HTTP status here would invent one.
_NO_RESPONSE_CODES: frozenset[grpc.StatusCode] = frozenset(
    {
        grpc.StatusCode.CANCELLED,
        grpc.StatusCode.DEADLINE_EXCEEDED,
        grpc.StatusCode.UNAVAILABLE,
    }
)


def map_grpc_error(
    exc: grpc.RpcError,
    *,
    method: str = "gRPC",
    path: str = "unknown",
) -> AuthenticationError | HTTPException | TransportError:
    """Maps a gRPC RpcError to the SDK exception hierarchy.

    Pure function: no I/O, no side effects. Testable without a gRPC channel.
    """
    code = exc.code()  # ty: ignore[unresolved-attribute]  -- grpcio ships no stubs
    details = exc.details() or ""  # ty: ignore[unresolved-attribute]
    code_name = getattr(code, "name", repr(code))

    if code == grpc.StatusCode.UNAUTHENTICATED:
        return AuthenticationError(details)
    if code in _NO_RESPONSE_CODES:
        return TransportError(f"{method} {path} failed with {code_name}: {details}")

    http_status = _GRPC_STATUS_TO_HTTP.get(code)
    if http_status is None:
        return TransportError(
            f"{method} {path} failed with unrecognized gRPC status {code_name}: {details}"
        )
    return HTTPException(
        status_code=http_status,
        message=details,
        method=method,
        path=path,
        grpc_status_code=code_name,
    )


def build_grpc_request(
    message_cls, body: dict[str, Any] | None, fields: dict[str, Any]
) -> Any:
    """Builds a request message the way grpc-gateway transcodes the REST call.

    `body` is the REST request body, already nested under the field the RPC's
    HTTP rule names. `fields` maps each path and query parameter's dotted field
    path (for example "device.id") to its value; None means unset. The body
    tolerates unknown keys as before, but a field path must resolve: an
    argument that matches no field would otherwise be dropped from the call.
    """
    request = ParseDict(body or {}, message_cls(), ignore_unknown_fields=True)
    nested: dict[str, Any] = {}
    for field_path, value in fields.items():
        if value is None:
            continue
        *parents, leaf = field_path.split(".")
        node = nested
        for parent in parents:
            node = node.setdefault(parent, {})
        node[leaf] = value
    # ParseDict merges into `request`, so path fields land inside the body.
    return ParseDict(nested, request)


def _method_label(stub_method) -> str:
    # Best effort: `_method` is a grpcio implementation detail, and failing to
    # read it must never cost the caller the RpcError it was meant to describe.
    try:
        label = stub_method._method
    except Exception:
        return "unknown"
    if isinstance(label, bytes):
        return label.decode("utf-8", errors="replace")
    return str(label)


def _validate_grpc_override(api_config: APIConfig) -> None:
    # gRPC auth metadata and target are bound to the channel at transport setup.
    # A direct APIConfig(...) passed per call cannot change them safely.
    source = getattr(api_config, "_shares_client_of", None)
    if source is None:
        raise ConfigurationError(
            "gRPC api_config_override must come from client.api_config.with_timeout(...). "
            "Per-call credential, host, or verify overrides are not supported on gRPC."
        )

    if (
        api_config.base_path != source.base_path
        or api_config.auth_email != source.auth_email
        or api_config.auth_token != source.auth_token
        or api_config.verify != source.verify
    ):
        raise ConfigurationError(
            "gRPC api_config_override can only change timeouts. "
            "Credential, host, and verify changes require a new KentikAPI client."
        )


def call_grpc(
    stub_method, proto_request, *, api_config: APIConfig | None = None
) -> tuple[Any, RateLimit | None]:
    """Calls one unary gRPC method; returns the response and the quota it reported.

    Only grpc.RpcError is a transport outcome. Anything else the stub raises,
    such as a malformed request, propagates unchanged rather than being
    misreported as a network failure.

    `api_config` is a per-call override: its grpc_deadline bounds this call,
    ahead of the channel's default. Channel credentials cannot change per call,
    so the override's credentials do not apply on gRPC.
    """
    path = _method_label(stub_method)
    if api_config is not None:
        _validate_grpc_override(api_config)

    kwargs = {} if api_config is None else {"timeout": api_config.grpc_deadline}
    try:
        # with_call exposes the call's initial metadata, where the quota is.
        if isinstance(stub_method, grpc.UnaryUnaryMultiCallable):
            response, call = stub_method.with_call(proto_request, **kwargs)
            return response, rate_limit_of_rpc(call)
        return stub_method(proto_request, **kwargs), None
    except grpc.RpcError as exc:
        error = map_grpc_error(exc, method="gRPC", path=path)
        error.rate_limit = rate_limit_of_rpc(exc)
        raise error from exc
