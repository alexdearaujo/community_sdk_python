# HAND-WRITTEN: not modified by `make generate`. Edit directly.
"""Shared gRPC call helper — the gRPC analogue of rest_runtime.request_json.

Every generated gRPC wrapper method routes through call_grpc so error
handling, status-code mapping, and transport failures stay in one place.
"""

import grpc

from kentik_api.errors import AuthenticationError, HTTPException, TransportError

_GRPC_STATUS_TO_HTTP: dict[grpc.StatusCode, int] = {
    grpc.StatusCode.INVALID_ARGUMENT: 400,
    grpc.StatusCode.UNAUTHENTICATED: 401,
    grpc.StatusCode.PERMISSION_DENIED: 403,
    grpc.StatusCode.NOT_FOUND: 404,
    grpc.StatusCode.ALREADY_EXISTS: 409,
    grpc.StatusCode.RESOURCE_EXHAUSTED: 429,
    grpc.StatusCode.UNIMPLEMENTED: 501,
    grpc.StatusCode.UNAVAILABLE: 503,
}


def map_grpc_error(
    exc: grpc.RpcError,
    *,
    method: str = "gRPC",
    path: str = "unknown",
) -> AuthenticationError | HTTPException:
    """Maps a gRPC RpcError to the SDK exception hierarchy.

    Pure function: no I/O, no side effects. Testable without a gRPC channel.
    """
    code = exc.code()  # ty: ignore[unresolved-attribute]  -- grpcio ships no stubs
    details = exc.details() or ""  # ty: ignore[unresolved-attribute]

    if code == grpc.StatusCode.UNAUTHENTICATED:
        return AuthenticationError(details)

    http_status = _GRPC_STATUS_TO_HTTP.get(code, 500)
    return HTTPException(
        status_code=http_status,
        message=details,
        method=method,
        path=path,
    )


def call_grpc(stub_method, proto_request):
    """Calls one unary gRPC method and normalizes errors to the SDK exception hierarchy."""
    try:
        return stub_method(proto_request)
    except grpc.RpcError as exc:
        raise map_grpc_error(
            exc,
            method="gRPC",
            path=getattr(stub_method, "_method", b"unknown").decode(
                "utf-8", errors="replace"
            ),
        ) from exc
    except Exception as exc:
        raise TransportError(str(exc)) from exc
