"""APIConfig timeout derivation and validation (FR-002, FR-015, FR-016, FR-017)."""

import math

import httpx
import pytest

from kentik_api.core.api_config import APIConfig
from kentik_api.errors import ConfigurationError, HTTPException, KentikError


def test_defaults_keep_the_previous_sixty_seconds_on_both_transports():
    config = APIConfig()

    assert config.timeout == 60.0
    assert config.rest_timeout == httpx.Timeout(60.0)
    assert config.grpc_deadline == 60.0


def test_omitted_refinements_derive_from_the_shared_timeout():
    config = APIConfig(timeout=5.0)

    assert config.rest_timeout == httpx.Timeout(5.0)
    assert config.grpc_deadline == 5.0


def test_scalar_rest_timeout_sets_all_four_phases():
    config = APIConfig(rest_timeout=7.0)

    assert (config.rest_timeout.connect, config.rest_timeout.read) == (7.0, 7.0)
    assert (config.rest_timeout.write, config.rest_timeout.pool) == (7.0, 7.0)


def test_phase_bounds_are_honoured_independently():
    phases = httpx.Timeout(connect=2.0, read=300.0, write=10.0, pool=5.0)

    config = APIConfig(rest_timeout=phases)

    assert config.rest_timeout is phases
    # A long read tolerance must not stretch the gRPC deadline or the shared default.
    assert config.grpc_deadline == 60.0


def test_grpc_deadline_is_independent_of_rest_timeout():
    config = APIConfig(timeout=30.0, rest_timeout=2.0, grpc_deadline=120.0)

    assert config.rest_timeout == httpx.Timeout(2.0)
    assert config.grpc_deadline == 120.0


@pytest.mark.parametrize("bad", [0, -1.0, math.nan])
@pytest.mark.parametrize(
    ("kwargs_for", "field"),
    [
        (lambda v: {"timeout": v}, "timeout"),
        (lambda v: {"grpc_deadline": v}, "grpc_deadline"),
        (lambda v: {"rest_timeout": v}, "rest_timeout.connect"),
        (
            lambda v: {"rest_timeout": httpx.Timeout(5.0, connect=v)},
            "rest_timeout.connect",
        ),
        (lambda v: {"rest_timeout": httpx.Timeout(5.0, read=v)}, "rest_timeout.read"),
        (lambda v: {"rest_timeout": httpx.Timeout(5.0, write=v)}, "rest_timeout.write"),
        (lambda v: {"rest_timeout": httpx.Timeout(5.0, pool=v)}, "rest_timeout.pool"),
    ],
)
def test_non_positive_bounds_are_rejected_naming_field_and_value(
    kwargs_for, field, bad
):
    with pytest.raises(ConfigurationError) as exc_info:
        APIConfig(**kwargs_for(bad))

    assert field in str(exc_info.value)
    assert repr(bad) in str(exc_info.value)


def test_unbounded_rest_phase_is_rejected():
    with pytest.raises(ConfigurationError, match="rest_timeout.read"):
        APIConfig(rest_timeout=httpx.Timeout(5.0, read=None))


def test_every_sdk_error_carries_a_rate_limit_slot():
    assert KentikError("x").rate_limit is None
    assert ConfigurationError("x").rate_limit is None


def test_http_exception_keeps_the_verbatim_grpc_code():
    exc = HTTPException(404, "not found", grpc_status_code="NOT_FOUND")

    assert exc.grpc_status_code == "NOT_FOUND"
    assert HTTPException(404, "not found").grpc_status_code is None
