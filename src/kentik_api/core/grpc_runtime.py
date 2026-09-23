# HAND-WRITTEN: not modified by `make generate`. Edit directly.
"""Shared gRPC call helper — the gRPC analogue of rest_runtime.request_json.

Every generated gRPC wrapper method routes through call_grpc so error
handling, status-code mapping, and transport failures stay in one place.
"""

import grpc

from kentik_api.errors import AuthenticationError, HTTPException, TransportError

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


def call_grpc(stub_method, proto_request):
    """Calls one unary gRPC method and normalizes errors to the SDK exception hierarchy.

    Only grpc.RpcError is a transport outcome. Anything else the stub raises,
    such as a malformed request, propagates unchanged rather than being
    misreported as a network failure.
    """
    path = _method_label(stub_method)
    try:
        return stub_method(proto_request)
    except grpc.RpcError as exc:
        raise map_grpc_error(exc, method="gRPC", path=path) from exc
