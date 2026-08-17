from typing import Union, cast

import kentik_api.gen.journeys.services.JourneysDataService as RestJourneysModule1
from kentik_api.gen.journeys import models as rest_models
from kentik_api.transports.grpc_client import GrpcTransport
from kentik_api.transports.rest_client import RestTransport


class JourneysServiceWrapper:
    """Unified Service routing to either gRPC or REST."""

    def __init__(self, transport: Union[GrpcTransport, RestTransport]):
        self._transport = transport
        if isinstance(self._transport, GrpcTransport):
            pass  # TODO: Initialize gRPC stub here

    def get_journeys_nlq(self, *, prompt: str) -> rest_models.GetJourneysNlqResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for GetJourneysNlq is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestJourneysModule1.GetJourneysNlq(
                api_config_override=rest_transport.api_config, prompt=prompt
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )
