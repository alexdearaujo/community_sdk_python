# HAND-WRITTEN: not modified by `make generate`. Edit directly.
"""Exact auth wire format for both transports (FR-039).

Kentik rejects a request whose auth key is misspelled with the same 401 as a
wrong token, so these keys are asserted verbatim rather than loosely.
"""

from __future__ import annotations

from kentik_api.auth.credentials import KentikCredentials

CREDENTIALS = KentikCredentials(email="dev@example.com", api_token="secret-token")


def test_grpc_plugin_emits_exact_auth_metadata():
    received = []

    CREDENTIALS.get_grpc_plugin()(
        context=None, callback=lambda md, err: received.append((md, err))
    )

    assert received == [
        (
            (
                ("x-ch-auth-email", "dev@example.com"),
                ("x-ch-auth-api-token", "secret-token"),
            ),
            None,
        )
    ]


def test_rest_headers_carry_exact_auth_keys():
    assert CREDENTIALS.get_rest_headers() == {
        "X-CH-Auth-Email": "dev@example.com",
        "X-CH-Auth-API-Token": "secret-token",
        "Content-Type": "application/json",
    }
