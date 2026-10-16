# HAND-WRITTEN: not modified by `make generate`. Edit directly.
from __future__ import annotations

from typing import Iterator

import pytest

from kentik_api.client import KentikAPI


@pytest.fixture(scope="session")
def real_client() -> Iterator[KentikAPI]:
    """A real KentikAPI client backed by whatever credentials are configured.

    Credential loading is delegated entirely to KentikAPI itself (project-root
    .env or KENTIK_EMAIL/KENTIK_API_TOKEN env vars) rather than duplicated
    here. If none are configured, the whole e2e suite skips rather than
    fails, since these tests are opt-in and not everyone running the mocked
    suites has (or should need) a live Kentik account.
    """
    try:
        client = KentikAPI(protocol="rest")
    except ValueError:
        pytest.skip(
            "No KENTIK_EMAIL/KENTIK_API_TOKEN available -- end-to-end tests "
            "require real credentials in a project-root .env and are opt-in "
            "only (see CLAUDE.md's end-to-end testing requirement)."
        )
    try:
        yield client
    finally:
        client.close()


@pytest.fixture(scope="session")
def grpc_real_client() -> Iterator[KentikAPI]:
    """Same as real_client, but over the gRPC transport (protocol="grpc")."""
    try:
        client = KentikAPI(protocol="grpc")
    except ValueError:
        pytest.skip(
            "No KENTIK_EMAIL/KENTIK_API_TOKEN available -- end-to-end tests "
            "require real credentials in a project-root .env and are opt-in "
            "only (see CLAUDE.md's end-to-end testing requirement)."
        )
    try:
        yield client
    finally:
        client.close()
