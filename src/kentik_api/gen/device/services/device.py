from typing import Union, cast, Optional
from kentik_api.gen.device import models as rest_models
import kentik_api.gen.device.services.DeviceService as RestDeviceModule1
from kentik_api.transports.grpc_client import GrpcTransport
from kentik_api.transports.rest_client import RestTransport
from google.protobuf.json_format import MessageToDict, ParseDict
from kentik_api.core.grpc_runtime import call_grpc


class DeviceServiceWrapper:
    """AUTO-GENERATED: scripts/generation/wrapper_generation.py, _generate_service_wrappers().
    Rebuilt on every `make generate`. Do not edit by hand.
    Unified Service routing to either gRPC or REST.
    """

    def __init__(self, transport: Union[GrpcTransport, RestTransport]):
        self._transport = transport
        if isinstance(self._transport, GrpcTransport):
            try:
                __import__("kentik_api.gen.pb_companions")
                import kentik_api.gen.device.pb.device_pb2 as _pb2_1_mod
                import kentik_api.gen.device.pb.device_pb2_grpc as _pb2_grpc_1_mod

                self._grpc_pb2_1 = _pb2_1_mod
                self._grpc_stub_1 = _pb2_grpc_1_mod.DeviceServiceStub(
                    self._transport.channel
                )
            except (ImportError, TypeError):
                self._grpc_pb2_1 = None
                self._grpc_stub_1 = None

    def list_devices(
        self, *, querynoCustomColumns: Optional[bool] = None, view: Optional[str] = None
    ) -> rest_models.ListDevicesResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for device service"
                )
            _req = ParseDict(
                {
                    k: v
                    for k, v in {
                        "querynoCustomColumns": querynoCustomColumns,
                        "view": view,
                    }.items()
                    if v is not None
                },
                self._grpc_pb2_1.ListDevicesRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_1.ListDevices, _req)
            return rest_models.ListDevicesResponse.model_validate(MessageToDict(_resp))
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
            if self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for device service"
                )
            _req = ParseDict(
                data.model_dump(by_alias=True, exclude_none=True),
                self._grpc_pb2_1.CreateDeviceRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_1.CreateDevice, _req)
            return rest_models.CreateDeviceResponse.model_validate(MessageToDict(_resp))
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
            if self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for device service"
                )
            _req = ParseDict(
                data.model_dump(by_alias=True, exclude_none=True),
                self._grpc_pb2_1.CreateDevicesRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_1.CreateDevices, _req)
            return rest_models.CreateDevicesResponse.model_validate(
                MessageToDict(_resp)
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
            if self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for device service"
                )
            _req = ParseDict(
                data.model_dump(by_alias=True, exclude_none=True),
                self._grpc_pb2_1.DeleteDevicesRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_1.DeleteDevices, _req)
            return rest_models.DeleteDevicesResponse.model_validate(
                MessageToDict(_resp)
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
            if self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for device service"
                )
            _req = ParseDict(
                data.model_dump(by_alias=True, exclude_none=True),
                self._grpc_pb2_1.UpdateDevicesRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_1.UpdateDevices, _req)
            return rest_models.UpdateDevicesResponse.model_validate(
                MessageToDict(_resp)
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
        self, *, deviceName: str, querynoCustomColumns: Optional[bool] = None
    ) -> rest_models.GetDeviceByNameResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for device service"
                )
            _req = ParseDict(
                {
                    k: v
                    for k, v in {
                        "deviceName": deviceName,
                        "querynoCustomColumns": querynoCustomColumns,
                    }.items()
                    if v is not None
                },
                self._grpc_pb2_1.GetDeviceByNameRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_1.GetDeviceByName, _req)
            return rest_models.GetDeviceByNameResponse.model_validate(
                MessageToDict(_resp)
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
        self, *, deviceid: str, querynoCustomColumns: Optional[bool] = None
    ) -> rest_models.GetDeviceResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for device service"
                )
            _req = ParseDict(
                {
                    k: v
                    for k, v in {
                        "deviceid": deviceid,
                        "querynoCustomColumns": querynoCustomColumns,
                    }.items()
                    if v is not None
                },
                self._grpc_pb2_1.GetDeviceRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_1.GetDevice, _req)
            return rest_models.GetDeviceResponse.model_validate(MessageToDict(_resp))
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
        self, *, deviceid: str, data: rest_models.DeviceServiceUpdateDeviceBody
    ) -> rest_models.UpdateDeviceResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for device service"
                )
            _req_dict = data.model_dump(by_alias=True, exclude_none=True)
            _req_dict.update(
                {k: v for k, v in {"deviceid": deviceid}.items() if v is not None}
            )
            _req = ParseDict(
                _req_dict,
                self._grpc_pb2_1.UpdateDeviceRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_1.UpdateDevice, _req)
            return rest_models.UpdateDeviceResponse.model_validate(MessageToDict(_resp))
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
            if self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for device service"
                )
            _req = ParseDict(
                {k: v for k, v in {"deviceid": deviceid}.items() if v is not None},
                self._grpc_pb2_1.DeleteDeviceRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_1.DeleteDevice, _req)
            return rest_models.DeleteDeviceResponse.model_validate(MessageToDict(_resp))
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
        self, *, id: str, data: rest_models.DeviceServiceUpdateDeviceLabelsBody
    ) -> rest_models.UpdateDeviceLabelsResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for device service"
                )
            _req_dict = data.model_dump(by_alias=True, exclude_none=True)
            _req_dict.update({k: v for k, v in {"id": id}.items() if v is not None})
            _req = ParseDict(
                _req_dict,
                self._grpc_pb2_1.UpdateDeviceLabelsRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_1.UpdateDeviceLabels, _req)
            return rest_models.UpdateDeviceLabelsResponse.model_validate(
                MessageToDict(_resp)
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
