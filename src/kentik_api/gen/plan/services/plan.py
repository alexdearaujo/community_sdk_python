from typing import Union, cast

import kentik_api.gen.plan.services.PlanService as RestPlanModule1
from kentik_api.gen.plan import models as rest_models
from kentik_api.transports.grpc_client import GrpcTransport
from kentik_api.transports.rest_client import RestTransport


class PlanServiceWrapper:
    """Unified Service routing to either gRPC or REST."""

    def __init__(self, transport: Union[GrpcTransport, RestTransport]):
        self._transport = transport
        if isinstance(self._transport, GrpcTransport):
            pass  # TODO: Initialize gRPC stub here

    def list_plans(
        self,
    ) -> rest_models.ListPlansResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for ListPlans is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestPlanModule1.ListPlans(
                api_config_override=rest_transport.api_config
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )
