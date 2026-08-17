from typing import Union, cast

import kentik_api.gen.bgp_monitoring.services.BgpMonitoringAdminService as RestBgpMonitoringModule1
import kentik_api.gen.bgp_monitoring.services.BgpMonitoringDataService as RestBgpMonitoringModule2
from kentik_api.gen.bgp_monitoring import models as rest_models
from kentik_api.transports.grpc_client import GrpcTransport
from kentik_api.transports.rest_client import RestTransport


class BgpMonitoringServiceWrapper:
    """Unified Service routing to either gRPC or REST."""

    def __init__(self, transport: Union[GrpcTransport, RestTransport]):
        self._transport = transport
        if isinstance(self._transport, GrpcTransport):
            pass  # TODO: Initialize gRPC stub here

    def list_monitors(
        self,
    ) -> rest_models.ListMonitorsResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for ListMonitors is not yet implemented."
            )
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
            raise NotImplementedError(
                "gRPC translation for CreateMonitor is not yet implemented."
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
            raise NotImplementedError(
                "gRPC translation for GetMonitor is not yet implemented."
            )
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
        self,
        *,
        id: str,
        data: rest_models.BgpMonitoringAdminServiceUpdateMonitorBody,
    ) -> rest_models.UpdateMonitorResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for UpdateMonitor is not yet implemented."
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
            raise NotImplementedError(
                "gRPC translation for DeleteMonitor is not yet implemented."
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
            raise NotImplementedError(
                "gRPC translation for SetMonitorStatus is not yet implemented."
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
            raise NotImplementedError(
                "gRPC translation for GetMetricsForTarget is not yet implemented."
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
            raise NotImplementedError(
                "gRPC translation for GetRoutesForTarget is not yet implemented."
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
