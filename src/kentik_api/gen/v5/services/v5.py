from typing import Optional, Union, cast

import kentik_api.gen.v5.services.QueryService as RestV5Module1
from kentik_api.core.api_config import APIConfig
from kentik_api.gen.v5 import models as rest_models
from kentik_api.transports.grpc_client import GrpcTransport
from kentik_api.transports.rest_client import RestTransport


class V5ServiceWrapper:
    """AUTO-GENERATED: scripts/generation/wrapper_generation.py, _generate_service_wrappers().
    Rebuilt on every `make generate`. Do not edit by hand.
    Unified Service routing to either gRPC or REST.
    """

    def __init__(self, transport: Union[GrpcTransport, RestTransport]):
        self._transport = transport
        if isinstance(self._transport, GrpcTransport):
            pass  # gRPC not yet implemented for this service

    def top_x_data(
        self,
        *,
        api_config_override: Optional[APIConfig] = None,
        data: rest_models.QueryRequest,
    ) -> rest_models.TopXDataResponse:
        """
        Top-X data query

        Runs one or more queries on the Kentik Data Engine and returns the result rows of each bucket, with time series for the top-X rows.
        """
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for QueryService_TopXData is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestV5Module1.QueryService_TopXData(
                api_config_override=api_config_override or rest_transport.api_config,
                data=data,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def top_x_chart(
        self,
        *,
        api_config_override: Optional[APIConfig] = None,
        data: rest_models.ChartRequest,
    ) -> rest_models.ChartResponse:
        """
        Top-X chart query

        Runs one or more queries and returns a chart image as a base64 data URI. Not verified: in a live check on 2026-10-16 this endpoint gave no response within 180 seconds. Decode the result with kentik_api.v5_tools.decode_chart().
        """
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for QueryService_TopXChart is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestV5Module1.QueryService_TopXChart(
                api_config_override=api_config_override or rest_transport.api_config,
                data=data,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def query_url(
        self,
        *,
        api_config_override: Optional[APIConfig] = None,
        data: rest_models.QueryRequest,
    ) -> str:
        """
        Data Explorer URL

        Returns a link that opens Data Explorer in the Kentik portal with the sidebar set to the query.
        """
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for QueryService_Url is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestV5Module1.QueryService_Url(
                api_config_override=api_config_override or rest_transport.api_config,
                data=data,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )
