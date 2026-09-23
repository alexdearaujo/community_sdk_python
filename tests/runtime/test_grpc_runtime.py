# HAND-WRITTEN: not modified by `make generate`. Edit directly.
from __future__ import annotations

import grpc
import pytest

from kentik_api.core.grpc_runtime import map_grpc_error
from kentik_api.errors import AuthenticationError, HTTPException, TransportError

# The table in contracts/runtime-api.md section 3, restated so a change to the
# runtime's mapping has to be made deliberately in two places.
HTTP_MAPPED = {
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
NO_RESPONSE = [
    grpc.StatusCode.CANCELLED,
    grpc.StatusCode.DEADLINE_EXCEEDED,
    grpc.StatusCode.UNAVAILABLE,
]


def test_classification_covers_every_non_ok_code():
    classified = set(HTTP_MAPPED) | set(NO_RESPONSE) | {grpc.StatusCode.UNAUTHENTICATED}

    assert classified == set(grpc.StatusCode) - {grpc.StatusCode.OK}
    assert len(classified) == 16


def test_unauthenticated_raises_auth_error(rpc_error):
    result = map_grpc_error(rpc_error(grpc.StatusCode.UNAUTHENTICATED, "bad token"))

    assert isinstance(result, AuthenticationError)
    assert "bad token" in str(result)


@pytest.mark.parametrize(
    ("code", "http_status"), HTTP_MAPPED.items(), ids=lambda v: str(v)
)
def test_api_faults_map_to_http_exception_keeping_the_grpc_code(
    rpc_error, code, http_status
):
    result = map_grpc_error(rpc_error(code, "fault"), method="gRPC", path="/svc/Op")

    assert type(result) is HTTPException
    assert result.status_code == http_status
    assert result.grpc_status_code == code.name
    assert (result.method, result.path) == ("gRPC", "/svc/Op")
    assert "fault" in str(result)


@pytest.mark.parametrize("code", NO_RESPONSE, ids=lambda c: c.name)
def test_no_response_codes_raise_transport_error_without_an_http_status(
    rpc_error, code
):
    result = map_grpc_error(rpc_error(code, "gone"), path="/svc/Op")

    assert type(result) is TransportError
    assert code.name in str(result)
    assert "/svc/Op" in str(result)


def test_unrecognized_code_raises_transport_error_naming_it(rpc_error):
    result = map_grpc_error(rpc_error("SOMETHING_NEW", "?"))

    assert type(result) is TransportError
    assert "SOMETHING_NEW" in str(result)


def test_details_none_guard(rpc_error):
    result = map_grpc_error(rpc_error(grpc.StatusCode.NOT_FOUND, None))

    assert isinstance(result, HTTPException)
    assert result.status_code == 404
