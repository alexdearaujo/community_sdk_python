from typing import Any, Dict, Optional

from kentik_api.core.api_config import APIConfig
from kentik_api.core.rest_runtime import request_json

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

    return (
        ListSiteMarketsResponse(**body)
        if body is not None
        else ListSiteMarketsResponse.model_construct()
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
        json_body=data.model_dump(),
        header_params=header_params,
        expected_status=200,
        operation_name="CreateSiteMarket",
        error_cls=CreateSiteMarketError,
    )

    return (
        CreateSiteMarketResponse(**body)
        if body is not None
        else CreateSiteMarketResponse.model_construct()
    )


def GetSiteMarket(
    api_config_override: Optional[APIConfig] = None, *, id: str
) -> GetSiteMarketResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path=f"/site/v202509/site_markets/{id}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="GetSiteMarket",
        error_cls=GetSiteMarketError,
    )

    return (
        GetSiteMarketResponse(**body)
        if body is not None
        else GetSiteMarketResponse.model_construct()
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
        path=f"/site/v202509/site_markets/{id}",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(),
        header_params=header_params,
        expected_status=200,
        operation_name="UpdateSiteMarket",
        error_cls=UpdateSiteMarketError,
    )

    return (
        UpdateSiteMarketResponse(**body)
        if body is not None
        else UpdateSiteMarketResponse.model_construct()
    )


def DeleteSiteMarket(
    api_config_override: Optional[APIConfig] = None, *, id: str
) -> DeleteSiteMarketResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="delete",
        path=f"/site/v202509/site_markets/{id}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="DeleteSiteMarket",
        error_cls=DeleteSiteMarketError,
    )

    return (
        DeleteSiteMarketResponse(**body)
        if body is not None
        else DeleteSiteMarketResponse.model_construct()
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

    return (
        ListSitesResponse(**body)
        if body is not None
        else ListSitesResponse.model_construct()
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
        json_body=data.model_dump(),
        header_params=header_params,
        expected_status=200,
        operation_name="CreateSite",
        error_cls=CreateSiteError,
    )

    return (
        CreateSiteResponse(**body)
        if body is not None
        else CreateSiteResponse.model_construct()
    )


def GetSite(
    api_config_override: Optional[APIConfig] = None, *, id: str
) -> GetSiteResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path=f"/site/v202509/sites/{id}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="GetSite",
        error_cls=GetSiteError,
    )

    return (
        GetSiteResponse(**body)
        if body is not None
        else GetSiteResponse.model_construct()
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
        path=f"/site/v202509/sites/{id}",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(),
        header_params=header_params,
        expected_status=200,
        operation_name="UpdateSite",
        error_cls=UpdateSiteError,
    )

    return (
        UpdateSiteResponse(**body)
        if body is not None
        else UpdateSiteResponse.model_construct()
    )


def DeleteSite(
    api_config_override: Optional[APIConfig] = None, *, id: str
) -> DeleteSiteResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="delete",
        path=f"/site/v202509/sites/{id}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="DeleteSite",
        error_cls=DeleteSiteError,
    )

    return (
        DeleteSiteResponse(**body)
        if body is not None
        else DeleteSiteResponse.model_construct()
    )
