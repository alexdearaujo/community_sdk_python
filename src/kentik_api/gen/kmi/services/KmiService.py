from typing import Any, Dict, List, Optional

from kentik_api.core.api_config import APIConfig
from kentik_api.core.rest_runtime import request_json

from ..error import (
    GetASNDetailsError,
    GetASNInsightsError,
    GetGlobalInsightsError,
    GetRankingsError,
    ListMarketsError,
)
from ..models import (  # noqa: F401
    ASNDetails,
    CustomerProvider,
    GetASNDetailsResponse,
    GetASNInsightsResponse,
    GetGlobalInsightsResponse,
    GetRankingsResponse,
    Insight,
    KmiServiceGetASNDetailsBody,
    KmiServiceGetRankingsBody,
    ListMarketsResponse,
    Market,
    Peer,
    Ranking,
    protobufAny,
    rpcStatus,
)


def GetGlobalInsights(
    api_config_override: Optional[APIConfig] = None,
    *,
    limit: Optional[int] = None,
    marketId: Optional[str] = None,
    ip: Optional[str] = None,
    lookback: Optional[int] = None,
    types: Optional[List[str]] = None,
    magnitude: Optional[int] = None,
) -> GetGlobalInsightsResponse:
    query_params: Dict[str, Any] = {
        "limit": limit,
        "marketId": marketId,
        "ip": ip,
        "lookback": lookback,
        "types": types,
        "magnitude": magnitude,
    }

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path="/kmi/v202212/insights",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="GetGlobalInsights",
        error_cls=GetGlobalInsightsError,
    )

    return (
        GetGlobalInsightsResponse(**body)
        if body is not None
        else GetGlobalInsightsResponse.model_construct()
    )


def GetASNInsights(
    api_config_override: Optional[APIConfig] = None,
    *,
    asn: str,
    limit: Optional[int] = None,
    marketId: Optional[str] = None,
    ip: Optional[str] = None,
    lookback: Optional[int] = None,
    types: Optional[List[str]] = None,
    magnitude: Optional[int] = None,
) -> GetASNInsightsResponse:
    query_params: Dict[str, Any] = {
        "limit": limit,
        "marketId": marketId,
        "ip": ip,
        "lookback": lookback,
        "types": types,
        "magnitude": magnitude,
    }

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path=f"/kmi/v202212/insights/{asn}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="GetASNInsights",
        error_cls=GetASNInsightsError,
    )

    return (
        GetASNInsightsResponse(**body)
        if body is not None
        else GetASNInsightsResponse.model_construct()
    )


def GetASNDetails(
    api_config_override: Optional[APIConfig] = None,
    *,
    marketId: str,
    asn: str,
    type: str,
    data: KmiServiceGetASNDetailsBody,
) -> GetASNDetailsResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="post",
        path=f"/kmi/v202212/market/{marketId}/network/{asn}/{type}",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(),
        header_params=header_params,
        expected_status=200,
        operation_name="GetASNDetails",
        error_cls=GetASNDetailsError,
    )

    return (
        GetASNDetailsResponse(**body)
        if body is not None
        else GetASNDetailsResponse.model_construct()
    )


def GetRankings(
    api_config_override: Optional[APIConfig] = None,
    *,
    marketId: str,
    rankType: str,
    ip: str,
    data: KmiServiceGetRankingsBody,
) -> GetRankingsResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="post",
        path=f"/kmi/v202212/market/{marketId}/rankings/{rankType}/ip/{ip}",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(),
        header_params=header_params,
        expected_status=200,
        operation_name="GetRankings",
        error_cls=GetRankingsError,
    )

    return (
        GetRankingsResponse(**body)
        if body is not None
        else GetRankingsResponse.model_construct()
    )


def ListMarkets(api_config_override: Optional[APIConfig] = None) -> ListMarketsResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path="/kmi/v202212/markets",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="ListMarkets",
        error_cls=ListMarketsError,
    )

    return (
        ListMarketsResponse(**body)
        if body is not None
        else ListMarketsResponse.model_construct()
    )
