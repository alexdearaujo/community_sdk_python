# AUTO-GENERATED: scripts/openapi_templates/service.jinja2 via openapi-python-generator
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Any, Dict, Optional

from kentik_api.core.api_config import APIConfig
from kentik_api.core.rest_runtime import (
    parse_response_model,
    path_segment,
    request_json,
)

from ..error import (
    CreateSiteError,
    CreateSiteMarketError,
    DeleteSiteError,
    DeleteSiteMarketError,
    GetSiteError,
    GetSiteMarketError,
    ListSiteMarketsError,
    ListSitesError,
    UpdateSiteError,
    UpdateSiteMarketError,
)
from ..models import (  # noqa: F401
    CreateSiteMarketRequest,
    CreateSiteMarketResponse,
    CreateSiteRequest,
    CreateSiteResponse,
    DeleteSiteMarketResponse,
    DeleteSiteResponse,
    GetSiteMarketResponse,
    GetSiteResponse,
    Layer,
    LayerSet,
    ListSiteMarketsResponse,
    ListSitesResponse,
    PeeringDBSiteMapping,
    PostalAddress,
    Site,
    SiteIpAddressClassification,
    SiteMarket,
    SiteServiceUpdateSiteBody,
    SiteServiceUpdateSiteMarketBody,
    SiteType,
    UpdateSiteMarketResponse,
    UpdateSiteResponse,
    protobufAny,
    rpcStatus,
)


def ListSiteMarkets(
    api_config_override: Optional[APIConfig] = None,
) -> ListSiteMarketsResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path="/site/v202509/site_markets",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="ListSiteMarkets",
        error_cls=ListSiteMarketsError,
    )

    return parse_response_model(
        ListSiteMarketsResponse,
        body,
        operation_name="ListSiteMarkets",
        method="get",
        path="/site/v202509/site_markets",
    )


def CreateSiteMarket(
    api_config_override: Optional[APIConfig] = None, *, data: CreateSiteMarketRequest
) -> CreateSiteMarketResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="post",
        path="/site/v202509/site_markets",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(by_alias=True, exclude_unset=True),
        header_params=header_params,
        expected_status=200,
        operation_name="CreateSiteMarket",
        error_cls=CreateSiteMarketError,
    )

    return parse_response_model(
        CreateSiteMarketResponse,
        body,
        operation_name="CreateSiteMarket",
        method="post",
        path="/site/v202509/site_markets",
    )


def GetSiteMarket(
    api_config_override: Optional[APIConfig] = None, *, id: str
) -> GetSiteMarketResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path=f"/site/v202509/site_markets/{path_segment(id)}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="GetSiteMarket",
        error_cls=GetSiteMarketError,
    )

    return parse_response_model(
        GetSiteMarketResponse,
        body,
        operation_name="GetSiteMarket",
        method="get",
        path="/site/v202509/site_markets/{id}",
    )


def UpdateSiteMarket(
    api_config_override: Optional[APIConfig] = None,
    *,
    id: str,
    data: SiteServiceUpdateSiteMarketBody,
) -> UpdateSiteMarketResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="put",
        path=f"/site/v202509/site_markets/{path_segment(id)}",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(by_alias=True, exclude_unset=True),
        header_params=header_params,
        expected_status=200,
        operation_name="UpdateSiteMarket",
        error_cls=UpdateSiteMarketError,
    )

    return parse_response_model(
        UpdateSiteMarketResponse,
        body,
        operation_name="UpdateSiteMarket",
        method="put",
        path="/site/v202509/site_markets/{id}",
    )


def DeleteSiteMarket(
    api_config_override: Optional[APIConfig] = None, *, id: str
) -> DeleteSiteMarketResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="delete",
        path=f"/site/v202509/site_markets/{path_segment(id)}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="DeleteSiteMarket",
        error_cls=DeleteSiteMarketError,
    )

    return parse_response_model(
        DeleteSiteMarketResponse,
        body,
        operation_name="DeleteSiteMarket",
        method="delete",
        path="/site/v202509/site_markets/{id}",
    )


def ListSites(api_config_override: Optional[APIConfig] = None) -> ListSitesResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path="/site/v202509/sites",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="ListSites",
        error_cls=ListSitesError,
    )

    return parse_response_model(
        ListSitesResponse,
        body,
        operation_name="ListSites",
        method="get",
        path="/site/v202509/sites",
    )


def CreateSite(
    api_config_override: Optional[APIConfig] = None, *, data: CreateSiteRequest
) -> CreateSiteResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="post",
        path="/site/v202509/sites",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(by_alias=True, exclude_unset=True),
        header_params=header_params,
        expected_status=200,
        operation_name="CreateSite",
        error_cls=CreateSiteError,
    )

    return parse_response_model(
        CreateSiteResponse,
        body,
        operation_name="CreateSite",
        method="post",
        path="/site/v202509/sites",
    )


def GetSite(
    api_config_override: Optional[APIConfig] = None, *, id: str
) -> GetSiteResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path=f"/site/v202509/sites/{path_segment(id)}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="GetSite",
        error_cls=GetSiteError,
    )

    return parse_response_model(
        GetSiteResponse,
        body,
        operation_name="GetSite",
        method="get",
        path="/site/v202509/sites/{id}",
    )


def UpdateSite(
    api_config_override: Optional[APIConfig] = None,
    *,
    id: str,
    data: SiteServiceUpdateSiteBody,
) -> UpdateSiteResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="put",
        path=f"/site/v202509/sites/{path_segment(id)}",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(by_alias=True, exclude_unset=True),
        header_params=header_params,
        expected_status=200,
        operation_name="UpdateSite",
        error_cls=UpdateSiteError,
    )

    return parse_response_model(
        UpdateSiteResponse,
        body,
        operation_name="UpdateSite",
        method="put",
        path="/site/v202509/sites/{id}",
    )


def DeleteSite(
    api_config_override: Optional[APIConfig] = None, *, id: str
) -> DeleteSiteResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="delete",
        path=f"/site/v202509/sites/{path_segment(id)}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="DeleteSite",
        error_cls=DeleteSiteError,
    )

    return parse_response_model(
        DeleteSiteResponse,
        body,
        operation_name="DeleteSite",
        method="delete",
        path="/site/v202509/sites/{id}",
    )
