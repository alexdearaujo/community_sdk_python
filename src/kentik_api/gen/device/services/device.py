from typing import Optional, Union, cast

import kentik_api.gen.device.services.DeviceService as RestDeviceModule1
from kentik_api.gen.device import models as rest_models
from kentik_api.transports.grpc_client import GrpcTransport
from kentik_api.transports.rest_client import RestTransport


class DeviceServiceWrapper:
    """Unified Service routing to either gRPC or REST."""

    def __init__(self, transport: Union[GrpcTransport, RestTransport]):
        self._transport = transport
        if isinstance(self._transport, GrpcTransport):
            pass  # TODO: Initialize gRPC stub here

    def list_devices(
        self,
        *,
        querynoCustomColumns: Optional[bool] = None,
        view: Optional[str] = None,
    ) -> rest_models.ListDevicesResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for ListDevices is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestDeviceModule1.ListDevices(
                api_config_override=rest_transport.api_config,
                querynoCustomColumns=querynoCustomColumns,
                view=view,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def create_device(
        self, *, data: rest_models.CreateDeviceRequest
    ) -> rest_models.CreateDeviceResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for CreateDevice is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestDeviceModule1.CreateDevice(
                api_config_override=rest_transport.api_config, data=data
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def create_devices(
        self, *, data: rest_models.CreateDevicesRequest
    ) -> rest_models.CreateDevicesResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for CreateDevices is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestDeviceModule1.CreateDevices(
                api_config_override=rest_transport.api_config, data=data
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def delete_devices(
        self, *, data: rest_models.DeleteDevicesRequest
    ) -> rest_models.DeleteDevicesResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for DeleteDevices is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestDeviceModule1.DeleteDevices(
                api_config_override=rest_transport.api_config, data=data
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def update_devices(
        self, *, data: rest_models.UpdateDevicesRequest
    ) -> rest_models.UpdateDevicesResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for UpdateDevices is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestDeviceModule1.UpdateDevices(
                api_config_override=rest_transport.api_config, data=data
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def get_device_by_name(
        self,
        *,
        deviceName: str,
        querynoCustomColumns: Optional[bool] = None,
    ) -> rest_models.GetDeviceByNameResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for GetDeviceByName is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestDeviceModule1.GetDeviceByName(
                api_config_override=rest_transport.api_config,
                deviceName=deviceName,
                querynoCustomColumns=querynoCustomColumns,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def get_device(
        self,
        *,
        deviceid: str,
        querynoCustomColumns: Optional[bool] = None,
    ) -> rest_models.GetDeviceResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for GetDevice is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestDeviceModule1.GetDevice(
                api_config_override=rest_transport.api_config,
                deviceid=deviceid,
                querynoCustomColumns=querynoCustomColumns,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def update_device(
        self,
        *,
        deviceid: str,
        data: rest_models.DeviceServiceUpdateDeviceBody,
    ) -> rest_models.UpdateDeviceResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for UpdateDevice is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestDeviceModule1.UpdateDevice(
                api_config_override=rest_transport.api_config,
                deviceid=deviceid,
                data=data,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def delete_device(self, *, deviceid: str) -> rest_models.DeleteDeviceResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for DeleteDevice is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestDeviceModule1.DeleteDevice(
                api_config_override=rest_transport.api_config, deviceid=deviceid
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def update_device_labels(
        self,
        *,
        id: str,
        data: rest_models.DeviceServiceUpdateDeviceLabelsBody,
    ) -> rest_models.UpdateDeviceLabelsResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for UpdateDeviceLabels is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestDeviceModule1.UpdateDeviceLabels(
                api_config_override=rest_transport.api_config, id=id, data=data
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )
