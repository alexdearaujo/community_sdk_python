from typing import Union, cast

from google.protobuf.json_format import MessageToDict, ParseDict

import kentik_api.gen.bgp_monitoring.services.BgpMonitoringAdminService as RestBgpMonitoringModule1
import kentik_api.gen.bgp_monitoring.services.BgpMonitoringDataService as RestBgpMonitoringModule2
from kentik_api.core.grpc_runtime import call_grpc
from kentik_api.gen.bgp_monitoring import models as rest_models
from kentik_api.transports.grpc_client import GrpcTransport
from kentik_api.transports.rest_client import RestTransport


class BgpMonitoringServiceWrapper:
    """AUTO-GENERATED: scripts/generation/wrapper_generation.py, _generate_service_wrappers().
    Rebuilt on every `make generate`. Do not edit by hand.
    Unified Service routing to either gRPC or REST.
    """

    def __init__(self, transport: Union[GrpcTransport, RestTransport]):
        self._transport = transport
        if isinstance(self._transport, GrpcTransport):
            try:
                __import__("kentik_api.gen.pb_companions")
                import kentik_api.gen.bgp_monitoring.pb.bgp_monitoring_pb2 as _pb2_1_mod
                import kentik_api.gen.bgp_monitoring.pb.bgp_monitoring_pb2_grpc as _pb2_grpc_1_mod

                self._grpc_pb2_1 = _pb2_1_mod
                self._grpc_stub_1 = _pb2_grpc_1_mod.BgpMonitoringAdminServiceStub(
                    self._transport.channel
                )
            except (ImportError, TypeError):
                self._grpc_pb2_1 = None
                self._grpc_stub_1 = None
            try:
                __import__("kentik_api.gen.pb_companions")
                import kentik_api.gen.bgp_monitoring.pb.bgp_monitoring_pb2 as _pb2_2_mod
                import kentik_api.gen.bgp_monitoring.pb.bgp_monitoring_pb2_grpc as _pb2_grpc_2_mod

                self._grpc_pb2_2 = _pb2_2_mod
                self._grpc_stub_2 = _pb2_grpc_2_mod.BgpMonitoringDataServiceStub(
                    self._transport.channel
                )
            except (ImportError, TypeError):
                self._grpc_pb2_2 = None
                self._grpc_stub_2 = None

    def list_monitors(
        self,
    ) -> rest_models.ListMonitorsResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for bgp_monitoring service"
                )
            _req = self._grpc_pb2_1.ListMonitorsRequest()
            _resp = call_grpc(self._grpc_stub_1.ListMonitors, _req)
            return rest_models.ListMonitorsResponse.model_validate(MessageToDict(_resp))
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestBgpMonitoringModule1.ListMonitors(
                api_config_override=rest_transport.api_config
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def create_monitor(
        self, *, data: rest_models.CreateMonitorRequest
    ) -> rest_models.CreateMonitorResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for bgp_monitoring service"
                )
            _req = ParseDict(
                data.model_dump(by_alias=True, exclude_none=True),
                self._grpc_pb2_1.CreateMonitorRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_1.CreateMonitor, _req)
            return rest_models.CreateMonitorResponse.model_validate(
                MessageToDict(_resp)
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestBgpMonitoringModule1.CreateMonitor(
                api_config_override=rest_transport.api_config, data=data
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def get_monitor(self, *, id: str) -> rest_models.GetMonitorResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for bgp_monitoring service"
                )
            _req = ParseDict(
                {k: v for k, v in {"id": id}.items() if v is not None},
                self._grpc_pb2_1.GetMonitorRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_1.GetMonitor, _req)
            return rest_models.GetMonitorResponse.model_validate(MessageToDict(_resp))
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestBgpMonitoringModule1.GetMonitor(
                api_config_override=rest_transport.api_config, id=id
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def update_monitor(
        self, *, id: str, data: rest_models.BgpMonitoringAdminServiceUpdateMonitorBody
    ) -> rest_models.UpdateMonitorResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for bgp_monitoring service"
                )
            _req_dict = data.model_dump(by_alias=True, exclude_none=True)
            _req_dict.update({k: v for k, v in {"id": id}.items() if v is not None})
            _req = ParseDict(
                _req_dict,
                self._grpc_pb2_1.UpdateMonitorRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_1.UpdateMonitor, _req)
            return rest_models.UpdateMonitorResponse.model_validate(
                MessageToDict(_resp)
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestBgpMonitoringModule1.UpdateMonitor(
                api_config_override=rest_transport.api_config, id=id, data=data
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def delete_monitor(self, *, id: str) -> rest_models.DeleteMonitorResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for bgp_monitoring service"
                )
            _req = ParseDict(
                {k: v for k, v in {"id": id}.items() if v is not None},
                self._grpc_pb2_1.DeleteMonitorRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_1.DeleteMonitor, _req)
            return rest_models.DeleteMonitorResponse.model_validate(
                MessageToDict(_resp)
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestBgpMonitoringModule1.DeleteMonitor(
                api_config_override=rest_transport.api_config, id=id
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def set_monitor_status(
        self,
        *,
        id: str,
        data: rest_models.BgpMonitoringAdminServiceSetMonitorStatusBody,
    ) -> rest_models.SetMonitorStatusResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for bgp_monitoring service"
                )
            _req_dict = data.model_dump(by_alias=True, exclude_none=True)
            _req_dict.update({k: v for k, v in {"id": id}.items() if v is not None})
            _req = ParseDict(
                _req_dict,
                self._grpc_pb2_1.SetMonitorStatusRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_1.SetMonitorStatus, _req)
            return rest_models.SetMonitorStatusResponse.model_validate(
                MessageToDict(_resp)
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestBgpMonitoringModule1.SetMonitorStatus(
                api_config_override=rest_transport.api_config, id=id, data=data
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def get_metrics_for_target(
        self, *, data: rest_models.GetMetricsForTargetRequest
    ) -> rest_models.GetMetricsForTargetResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_2 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for bgp_monitoring service"
                )
            _req = ParseDict(
                data.model_dump(by_alias=True, exclude_none=True),
                self._grpc_pb2_2.GetMetricsForTargetRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_2.GetMetricsForTarget, _req)
            return rest_models.GetMetricsForTargetResponse.model_validate(
                MessageToDict(_resp)
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestBgpMonitoringModule2.GetMetricsForTarget(
                api_config_override=rest_transport.api_config, data=data
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def get_routes_for_target(
        self, *, data: rest_models.GetRoutesForTargetRequest
    ) -> rest_models.GetRoutesForTargetResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_2 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for bgp_monitoring service"
                )
            _req = ParseDict(
                data.model_dump(by_alias=True, exclude_none=True),
                self._grpc_pb2_2.GetRoutesForTargetRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_2.GetRoutesForTarget, _req)
            return rest_models.GetRoutesForTargetResponse.model_validate(
                MessageToDict(_resp)
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestBgpMonitoringModule2.GetRoutesForTarget(
                api_config_override=rest_transport.api_config, data=data
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )
