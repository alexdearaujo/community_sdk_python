from typing import Union, cast

from google.protobuf.json_format import MessageToDict, ParseDict

import kentik_api.gen.capacity_plan.services.CapacityPlanService as RestCapacityPlanModule1
from kentik_api.core.grpc_runtime import call_grpc
from kentik_api.gen.capacity_plan import models as rest_models
from kentik_api.transports.grpc_client import GrpcTransport
from kentik_api.transports.rest_client import RestTransport


class CapacityPlanServiceWrapper:
    """Unified Service routing to either gRPC or REST."""

    def __init__(self, transport: Union[GrpcTransport, RestTransport]):
        self._transport = transport
        if isinstance(self._transport, GrpcTransport):
            try:
                import kentik_api.gen.capacity_plan.pb.capacity_plan_pb2 as _pb2_1_mod
                import kentik_api.gen.capacity_plan.pb.capacity_plan_pb2_grpc as _pb2_grpc_1_mod

                self._grpc_pb2_1 = _pb2_1_mod
                self._grpc_stub_1 = _pb2_grpc_1_mod.CapacityPlanServiceStub(
                    self._transport.channel
                )
            except (ImportError, TypeError):
                self._grpc_pb2_1 = None
                self._grpc_stub_1 = None

    def list_capacity_plans(
        self,
    ) -> rest_models.ListCapacityPlansResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for capacity_plan service"
                )
            _req = self._grpc_pb2_1.ListCapacityPlansRequest()
            _resp = call_grpc(self._grpc_stub_1.ListCapacityPlans, _req)
            return rest_models.ListCapacityPlansResponse.model_validate(
                MessageToDict(_resp)
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestCapacityPlanModule1.ListCapacityPlans(
                api_config_override=rest_transport.api_config
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def list_capacity_summaries(
        self,
    ) -> rest_models.ListCapacitySummariesResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for capacity_plan service"
                )
            _req = self._grpc_pb2_1.ListCapacitySummariesRequest()
            _resp = call_grpc(self._grpc_stub_1.ListCapacitySummaries, _req)
            return rest_models.ListCapacitySummariesResponse.model_validate(
                MessageToDict(_resp)
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestCapacityPlanModule1.ListCapacitySummaries(
                api_config_override=rest_transport.api_config
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def get_capacity_plan(self, *, id: str) -> rest_models.GetCapacityPlanResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for capacity_plan service"
                )
            _req = ParseDict(
                {k: v for k, v in {"id": id}.items() if v is not None},
                self._grpc_pb2_1.GetCapacityPlanRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_1.GetCapacityPlan, _req)
            return rest_models.GetCapacityPlanResponse.model_validate(
                MessageToDict(_resp)
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestCapacityPlanModule1.GetCapacityPlan(
                api_config_override=rest_transport.api_config, id=id
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def get_capacity_summary(
        self, *, id: str
    ) -> rest_models.GetCapacitySummaryResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for capacity_plan service"
                )
            _req = ParseDict(
                {k: v for k, v in {"id": id}.items() if v is not None},
                self._grpc_pb2_1.GetCapacitySummaryRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_1.GetCapacitySummary, _req)
            return rest_models.GetCapacitySummaryResponse.model_validate(
                MessageToDict(_resp)
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestCapacityPlanModule1.GetCapacitySummary(
                api_config_override=rest_transport.api_config, id=id
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )
