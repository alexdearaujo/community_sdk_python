from typing import List, Optional, Union, cast

import kentik_api.gen.kmi.services.KmiService as RestKmiModule1
from kentik_api.gen.kmi import models as rest_models
from kentik_api.transports.grpc_client import GrpcTransport
from kentik_api.transports.rest_client import RestTransport


class KmiServiceWrapper:
    """Unified Service routing to either gRPC or REST."""

    def __init__(self, transport: Union[GrpcTransport, RestTransport]):
        self._transport = transport
        if isinstance(self._transport, GrpcTransport):
            pass  # TODO: Initialize gRPC stub here

    def get_global_insights(
        self,
        *,
        limit: Optional[int] = None,
        marketId: Optional[str] = None,
        ip: Optional[str] = None,
        lookback: Optional[int] = None,
        types: Optional[List[str]] = None,
        magnitude: Optional[int] = None,
    ) -> rest_models.GetGlobalInsightsResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for GetGlobalInsights is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestKmiModule1.GetGlobalInsights(
                api_config_override=rest_transport.api_config,
                limit=limit,
                marketId=marketId,
                ip=ip,
                lookback=lookback,
                types=types,
                magnitude=magnitude,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def get_a_s_n_insights(
        self,
        *,
        asn: str,
        limit: Optional[int] = None,
        marketId: Optional[str] = None,
        ip: Optional[str] = None,
        lookback: Optional[int] = None,
        types: Optional[List[str]] = None,
        magnitude: Optional[int] = None,
    ) -> rest_models.GetASNInsightsResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for GetASNInsights is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestKmiModule1.GetASNInsights(
                api_config_override=rest_transport.api_config,
                asn=asn,
                limit=limit,
                marketId=marketId,
                ip=ip,
                lookback=lookback,
                types=types,
                magnitude=magnitude,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def get_a_s_n_details(
        self,
        *,
        marketId: str,
        asn: str,
        type: str,
        data: rest_models.KmiServiceGetASNDetailsBody,
    ) -> rest_models.GetASNDetailsResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for GetASNDetails is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestKmiModule1.GetASNDetails(
                api_config_override=rest_transport.api_config,
                marketId=marketId,
                asn=asn,
                type=type,
                data=data,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def get_rankings(
        self,
        *,
        marketId: str,
        rankType: str,
        ip: str,
        data: rest_models.KmiServiceGetRankingsBody,
    ) -> rest_models.GetRankingsResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for GetRankings is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestKmiModule1.GetRankings(
                api_config_override=rest_transport.api_config,
                marketId=marketId,
                rankType=rankType,
                ip=ip,
                data=data,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def list_markets(
        self,
    ) -> rest_models.ListMarketsResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for ListMarkets is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestKmiModule1.ListMarkets(
                api_config_override=rest_transport.api_config
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )
