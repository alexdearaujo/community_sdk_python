from typing import Union, cast

import kentik_api.gen.enrichments.services.EnumerationsAdminService as RestEnrichmentsModule1
from kentik_api.gen.enrichments import models as rest_models
from kentik_api.transports.grpc_client import GrpcTransport
from kentik_api.transports.rest_client import RestTransport


class EnrichmentsServiceWrapper:
    """Unified Service routing to either gRPC or REST."""

    def __init__(self, transport: Union[GrpcTransport, RestTransport]):
        self._transport = transport
        if isinstance(self._transport, GrpcTransport):
            pass  # TODO: Initialize gRPC stub here

    def fetch_values_by_ids(
        self, *, data: rest_models.FetchValuesByIdsRequest
    ) -> rest_models.FetchValuesByIdsResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for FetchValuesByIds is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestEnrichmentsModule1.FetchValuesByIds(
                api_config_override=rest_transport.api_config, data=data
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )
