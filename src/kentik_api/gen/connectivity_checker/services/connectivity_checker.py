from typing import Union, cast

import kentik_api.gen.connectivity_checker.services.ConnectivityCheckerAdminService as RestConnectivityCheckerModule1
from kentik_api.gen.connectivity_checker import models as rest_models
from kentik_api.transports.grpc_client import GrpcTransport
from kentik_api.transports.rest_client import RestTransport


class ConnectivityCheckerServiceWrapper:
    """Unified Service routing to either gRPC or REST."""

    def __init__(self, transport: Union[GrpcTransport, RestTransport]):
        self._transport = transport
        if isinstance(self._transport, GrpcTransport):
            pass  # TODO: Initialize gRPC stub here

    def create_connectivity_report(
        self,
        *,
        data: rest_models.CreateConnectivityReportRequest,
    ) -> rest_models.CreateConnectivityReportResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for CreateConnectivityReport is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestConnectivityCheckerModule1.CreateConnectivityReport(
                api_config_override=rest_transport.api_config, data=data
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )
