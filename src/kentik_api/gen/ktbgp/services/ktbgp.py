from typing import Union, cast

import kentik_api.gen.ktbgp.services.RouteService as RestKtbgpModule1
from kentik_api.gen.ktbgp import models as rest_models
from kentik_api.transports.grpc_client import GrpcTransport
from kentik_api.transports.rest_client import RestTransport


class KtbgpServiceWrapper:
    """Unified Service routing to either gRPC or REST."""

    def __init__(self, transport: Union[GrpcTransport, RestTransport]):
        self._transport = transport
        if isinstance(self._transport, GrpcTransport):
            pass  # TODO: Initialize gRPC stub here

    def route_service__announce(
        self,
        *,
        data: rest_models.RouteServiceAnnounceRequest,
    ) -> rest_models.RouteServiceAnnounceResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for RouteService_Announce is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestKtbgpModule1.RouteService_Announce(
                api_config_override=rest_transport.api_config, data=data
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def route_service__list(
        self, *, data: rest_models.RouteServiceListRequest
    ) -> rest_models.RouteServiceListResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for RouteService_List is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestKtbgpModule1.RouteService_List(
                api_config_override=rest_transport.api_config, data=data
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def route_service__withdraw(
        self,
        *,
        data: rest_models.RouteServiceWithdrawRequest,
    ) -> rest_models.RouteServiceWithdrawResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for RouteService_Withdraw is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestKtbgpModule1.RouteService_Withdraw(
                api_config_override=rest_transport.api_config, data=data
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )
