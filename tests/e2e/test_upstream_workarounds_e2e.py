# HAND-WRITTEN: not modified by `uv run poe generate`. Edit directly.
"""Canaries for upstream bugs that the SDK works around. MUTATING: writes to the real account.

Each test sends the request the published schema documents, bypassing the
workaround, and is a strict xfail. When upstream fixes the bug, the test passes,
strict xfail turns that into a failure, and the reason names the workaround to
remove (AGENTS.md, "Upstream workarounds").

Run with the other mutating tests: `uv run poe test-e2e-mutating`.
"""

from __future__ import annotations

import grpc
import pytest
from ledger import Ledger

from kentik_api.auth.credentials import KentikCredentials
from kentik_api.client import KentikAPI
from kentik_api.core.rest_runtime import request_json
from kentik_api.errors import HTTPException
from kentik_api.gen.as_group.models import ASGroupConcise, CreateASGroupRequest
from kentik_api.gen.site.models import CreateSiteMarketRequest, SiteMarket

pytestmark = pytest.mark.e2e_mutating

rest_body_keys_bug = pytest.mark.xfail(
    raises=HTTPException,
    strict=True,
    reason=(
        "Upstream REST drops a camelCase body key when the URL sets a field "
        "inside it. If this passes, remove send_proto_body_keys() and its call "
        "in generate_sdk.py, regenerate, and update AGENTS.md."
    ),
)


class DeadlineCrashesServer(Exception):
    pass


grpc_deadline_bug = pytest.mark.xfail(
    raises=DeadlineCrashesServer,
    strict=True,
    reason=(
        "Upstream gRPC fails every call with a deadline on this service. If this "
        "passes, remove the service from _NO_SERVER_DEADLINE in "
        "transports/grpc_client.py and update AGENTS.md."
    ),
)


def _put_documented_body(client: KentikAPI, path: str, body: dict) -> dict:
    return request_json(
        method="put",
        path=path,
        path_template=path,
        api_config_override=client.api_config,
        query_params={},
        json_body=body,
        header_params={},
        expected_status=200,
        operation_name="canary",
    )


@rest_body_keys_bug
def test_update_as_group_reads_the_documented_camel_case_body(
    real_client: KentikAPI, ledger: Ledger
):
    name = ledger.new_name()
    created = real_client.as_group.create(
        data=CreateASGroupRequest(asGroup=ASGroupConcise(name=name, asn=["36459"]))
    )
    assert created.asGroup is not None
    id = ledger.owned("as_group", ledger.created("as_group", created.asGroup.id, name))

    body = {"asGroup": {"name": name, "asn": ["36459", "46489"]}}
    _put_documented_body(real_client, f"/as_group/v202212/as_group/{id}", body)


@rest_body_keys_bug
def test_update_site_market_reads_the_documented_camel_case_body(
    real_client: KentikAPI, ledger: Ledger
):
    name = ledger.new_name()
    created = real_client.site.create_market(
        data=CreateSiteMarketRequest(siteMarket=SiteMarket(name=name))
    )
    assert created.siteMarket is not None
    id = ledger.owned(
        "site_market", ledger.created("site_market", created.siteMarket.id, name)
    )

    body = {"siteMarket": {"name": name, "description": "camel"}}
    _put_documented_body(real_client, f"/site/v202509/site_markets/{id}", body)


# One read per service in _NO_SERVER_DEADLINE. A new proto version gives
# UNIMPLEMENTED, which fails the test so the path here gets updated.
@grpc_deadline_bug
@pytest.mark.parametrize(
    "method",
    [
        "/kentik.alerting.public.v202505.MitigationMethodsService/List",
        "/kentik.audit.public.v202601.AuditService/ListAuditEvents",
        "/kentik.custom_application.v202501alpha1.CustomApplicationService/ListCustomApplications",
        "/kentik.custom_dimension.v202411alpha1.CustomDimensionService/ListCustomDimensions",
        "/kentik.plan.v202501alpha1.PlanService/ListPlans",
        "/kentik.saved_filter.v202501alpha1.SavedFilterService/ListSavedFilters",
    ],
)
def test_grpc_call_with_a_deadline_succeeds(real_client: KentikAPI, method: str):
    config = real_client.api_config
    assert config.auth_email and config.auth_token
    plugin = KentikCredentials(config.auth_email, config.auth_token).get_grpc_plugin()
    credentials = grpc.composite_channel_credentials(
        grpc.ssl_channel_credentials(), grpc.metadata_call_credentials(plugin)
    )
    # A plain channel: the SDK's own channel would not send the deadline.
    with grpc.secure_channel("grpc.api.kentik.com:443", credentials) as channel:
        call = channel.unary_unary(
            method,
            request_serializer=lambda _: b"",
            response_deserializer=lambda raw: raw,
        )
        try:
            call(b"", timeout=30)
        except grpc.RpcError as exc:
            details = exc.details() or ""  # ty: ignore[unresolved-attribute]
            if "name:RangeError" in details:
                raise DeadlineCrashesServer(details) from exc
            raise
