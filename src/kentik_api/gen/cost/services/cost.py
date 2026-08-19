from typing import Optional, Union, cast

from google.protobuf.json_format import MessageToDict, ParseDict

import kentik_api.gen.cost.services.CostService as RestCostModule1
from kentik_api.core.grpc_runtime import call_grpc
from kentik_api.gen.cost import models as rest_models
from kentik_api.transports.grpc_client import GrpcTransport
from kentik_api.transports.rest_client import RestTransport


class CostServiceWrapper:
    """AUTO-GENERATED: scripts/generation/wrapper_generation.py, _generate_service_wrappers().
    Rebuilt on every `make generate`. Do not edit by hand.
    Unified Service routing to either gRPC or REST.
    """

    def __init__(self, transport: Union[GrpcTransport, RestTransport]):
        self._transport = transport
        if isinstance(self._transport, GrpcTransport):
            try:
                __import__("kentik_api.gen.pb_companions")
                import kentik_api.gen.cost.pb.cost_pb2 as _pb2_1_mod
                import kentik_api.gen.cost.pb.cost_pb2_grpc as _pb2_grpc_1_mod

                self._grpc_pb2_1 = _pb2_1_mod
                self._grpc_stub_1 = _pb2_grpc_1_mod.CostServiceStub(
                    self._transport.channel
                )
            except (ImportError, TypeError):
                self._grpc_pb2_1 = None
                self._grpc_stub_1 = None

    def list_cost_providers(
        self,
    ) -> rest_models.ListCostProvidersResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for cost service"
                )
            _req = self._grpc_pb2_1.ListCostProvidersRequest()
            _resp = call_grpc(self._grpc_stub_1.ListCostProviders, _req)
            return rest_models.ListCostProvidersResponse.model_validate(
                MessageToDict(_resp)
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
            if self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for cost service"
                )
            _req = ParseDict(
                {k: v for k, v in {"date": date}.items() if v is not None},
                self._grpc_pb2_1.ListCostProviderSummariesRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_1.ListCostProviderSummaries, _req)
            return rest_models.ListCostProviderSummariesResponse.model_validate(
                MessageToDict(_resp)
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
            if self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for cost service"
                )
            _req = ParseDict(
                {k: v for k, v in {"id": id, "date": date}.items() if v is not None},
                self._grpc_pb2_1.GetCostProviderSummaryRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_1.GetCostProviderSummary, _req)
            return rest_models.GetCostProviderSummaryResponse.model_validate(
                MessageToDict(_resp)
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
