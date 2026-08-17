from typing import Optional, Union, cast

import kentik_api.gen.cost.services.CostService as RestCostModule1
from kentik_api.gen.cost import models as rest_models
from kentik_api.transports.grpc_client import GrpcTransport
from kentik_api.transports.rest_client import RestTransport


class CostServiceWrapper:
    """Unified Service routing to either gRPC or REST."""

    def __init__(self, transport: Union[GrpcTransport, RestTransport]):
        self._transport = transport
        if isinstance(self._transport, GrpcTransport):
            pass  # TODO: Initialize gRPC stub here

    def list_cost_providers(
        self,
    ) -> rest_models.ListCostProvidersResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for ListCostProviders is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestCostModule1.ListCostProviders(
                api_config_override=rest_transport.api_config
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def list_cost_provider_summaries(
        self, *, date: Optional[str] = None
    ) -> rest_models.ListCostProviderSummariesResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for ListCostProviderSummaries is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestCostModule1.ListCostProviderSummaries(
                api_config_override=rest_transport.api_config, date=date
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def get_cost_provider_summary(
        self,
        *,
        id: str,
        date: Optional[str] = None,
    ) -> rest_models.GetCostProviderSummaryResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for GetCostProviderSummary is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestCostModule1.GetCostProviderSummary(
                api_config_override=rest_transport.api_config, id=id, date=date
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )
