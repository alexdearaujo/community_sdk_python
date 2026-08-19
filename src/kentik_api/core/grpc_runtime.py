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


def call_grpc(stub_method, proto_request):
    """Calls one unary gRPC method and normalizes errors to the SDK exception hierarchy."""
    try:
        return stub_method(proto_request)
    except grpc.RpcError as exc:
        code = exc.code()
        if code == grpc.StatusCode.UNAUTHENTICATED:
            raise AuthenticationError(exc.details()) from exc
        http_status = _GRPC_STATUS_TO_HTTP.get(code, 500)
        raise HTTPException(
            status_code=http_status,
            message=exc.details(),
            method="gRPC",
            path=getattr(stub_method, "_method", b"unknown").decode(
                "utf-8", errors="replace"
            ),
        ) from exc
    except Exception as exc:
        raise TransportError(str(exc)) from exc
