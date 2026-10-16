from typing import List, Optional, Union, cast

from google.protobuf.json_format import MessageToDict

import kentik_api.gen.interface.services.InterfaceService as RestInterfaceModule1
from kentik_api.core.api_config import APIConfig
from kentik_api.core.grpc_runtime import build_grpc_request, call_grpc
from kentik_api.core.rate_limit import attach_rate_limit
from kentik_api.gen.interface import models as rest_models
from kentik_api.transports.grpc_client import GrpcTransport
from kentik_api.transports.rest_client import RestTransport


class InterfaceServiceWrapper:
    """AUTO-GENERATED: scripts/generation/wrapper_generation.py, _generate_service_wrappers().
    Rebuilt on every `make generate`. Do not edit by hand.
    Unified Service routing to either gRPC or REST.
    """

    def __init__(self, transport: Union[GrpcTransport, RestTransport]):
        self._transport = transport
        if isinstance(self._transport, GrpcTransport):
            try:
                __import__("kentik_api.gen.pb_companions")
                import kentik_api.gen.interface.pb.interface_pb2 as _pb2_1_mod
                import kentik_api.gen.interface.pb.interface_pb2_grpc as _pb2_grpc_1_mod

                self._grpc_pb2_1 = _pb2_1_mod
                self._grpc_stub_1 = _pb2_grpc_1_mod.InterfaceServiceStub(
                    self._transport.channel
                )
            except (ImportError, TypeError):
                self._grpc_pb2_1 = None
                self._grpc_stub_1 = None

    def list_interface(
        self,
        *,
        api_config_override: Optional[APIConfig] = None,
        filterstext: Optional[str] = None,
        filtersdeviceIds: Optional[List[str]] = None,
        filtersconnectivityTypes: Optional[List[str]] = None,
        filtersnetworkBoundaries: Optional[List[str]] = None,
        filtersproviders: Optional[List[str]] = None,
        filterssnmpSpeeds: Optional[List[int]] = None,
        filtersipTypes: Optional[List[str]] = None,
    ) -> rest_models.ListInterfaceResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_1 is None or self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for interface service"
                )
            _req = build_grpc_request(
                self._grpc_pb2_1.ListInterfaceRequest,
                None,
                {
                    "filters.text": filterstext,
                    "filters.deviceIds": filtersdeviceIds,
                    "filters.connectivityTypes": filtersconnectivityTypes,
                    "filters.networkBoundaries": filtersnetworkBoundaries,
                    "filters.providers": filtersproviders,
                    "filters.snmpSpeeds": filterssnmpSpeeds,
                    "filters.ipTypes": filtersipTypes,
                },
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_1.ListInterface,
                _req,
                api_config=api_config_override,
                error_cls=RestInterfaceModule1.ListInterfaceError,
            )
            return attach_rate_limit(
                rest_models.ListInterfaceResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestInterfaceModule1.ListInterface(
                api_config_override=api_config_override or rest_transport.api_config,
                filterstext=filterstext,
                filtersdeviceIds=filtersdeviceIds,
                filtersconnectivityTypes=filtersconnectivityTypes,
                filtersnetworkBoundaries=filtersnetworkBoundaries,
                filtersproviders=filtersproviders,
                filterssnmpSpeeds=filterssnmpSpeeds,
                filtersipTypes=filtersipTypes,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def interface_create(
        self,
        *,
        api_config_override: Optional[APIConfig] = None,
        data: rest_models.CreateInterfaceRequest,
    ) -> rest_models.CreateInterfaceResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_1 is None or self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for interface service"
                )
            _req = build_grpc_request(
                self._grpc_pb2_1.CreateInterfaceRequest,
                data.model_dump(by_alias=True, exclude_none=True),
                {},
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_1.CreateInterface,
                _req,
                api_config=api_config_override,
                error_cls=RestInterfaceModule1.InterfaceCreateError,
            )
            return attach_rate_limit(
                rest_models.CreateInterfaceResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestInterfaceModule1.InterfaceCreate(
                api_config_override=api_config_override or rest_transport.api_config,
                data=data,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def interface_get(
        self, *, api_config_override: Optional[APIConfig] = None, id: str
    ) -> rest_models.GetInterfaceResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_1 is None or self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for interface service"
                )
            _req = build_grpc_request(
                self._grpc_pb2_1.GetInterfaceRequest, None, {"id": id}
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_1.GetInterface,
                _req,
                api_config=api_config_override,
                error_cls=RestInterfaceModule1.InterfaceGetError,
            )
            return attach_rate_limit(
                rest_models.GetInterfaceResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestInterfaceModule1.InterfaceGet(
                api_config_override=api_config_override or rest_transport.api_config,
                id=id,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def interface_update(
        self,
        *,
        api_config_override: Optional[APIConfig] = None,
        id: str,
        data: rest_models.InterfaceServiceUpdateInterfaceBody,
    ) -> rest_models.UpdateInterfaceResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_1 is None or self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for interface service"
                )
            _req = build_grpc_request(
                self._grpc_pb2_1.UpdateInterfaceRequest,
                data.model_dump(by_alias=True, exclude_none=True),
                {"interface.id": id},
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_1.UpdateInterface,
                _req,
                api_config=api_config_override,
                error_cls=RestInterfaceModule1.InterfaceUpdateError,
            )
            return attach_rate_limit(
                rest_models.UpdateInterfaceResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestInterfaceModule1.InterfaceUpdate(
                api_config_override=api_config_override or rest_transport.api_config,
                id=id,
                data=data,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def interface_delete(
        self, *, api_config_override: Optional[APIConfig] = None, id: str
    ) -> rest_models.DeleteInterfaceResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_1 is None or self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for interface service"
                )
            _req = build_grpc_request(
                self._grpc_pb2_1.DeleteInterfaceRequest, None, {"id": id}
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_1.DeleteInterface,
                _req,
                api_config=api_config_override,
                error_cls=RestInterfaceModule1.InterfaceDeleteError,
            )
            return attach_rate_limit(
                rest_models.DeleteInterfaceResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestInterfaceModule1.InterfaceDelete(
                api_config_override=api_config_override or rest_transport.api_config,
                id=id,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def manual_classify(
        self,
        *,
        api_config_override: Optional[APIConfig] = None,
        data: rest_models.ManualClassifyRequest,
    ) -> rest_models.ManualClassifyResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_1 is None or self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for interface service"
                )
            _req = build_grpc_request(
                self._grpc_pb2_1.ManualClassifyRequest,
                data.model_dump(by_alias=True, exclude_none=True),
                {},
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_1.ManualClassify,
                _req,
                api_config=api_config_override,
                error_cls=RestInterfaceModule1.ManualClassifyError,
            )
            return attach_rate_limit(
                rest_models.ManualClassifyResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestInterfaceModule1.ManualClassify(
                api_config_override=api_config_override or rest_transport.api_config,
                data=data,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )
