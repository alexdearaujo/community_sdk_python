from typing import List, Optional, Union, cast

from google.protobuf.json_format import MessageToDict, ParseDict

import kentik_api.gen.interface.services.InterfaceService as RestInterfaceModule1
from kentik_api.core.grpc_runtime import call_grpc
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
        filterstext: Optional[str] = None,
        filtersdeviceIds: Optional[List[str]] = None,
        filtersconnectivityTypes: Optional[List[str]] = None,
        filtersnetworkBoundaries: Optional[List[str]] = None,
        filtersproviders: Optional[List[str]] = None,
        filterssnmpSpeeds: Optional[List[int]] = None,
        filtersipTypes: Optional[List[str]] = None,
    ) -> rest_models.ListInterfaceResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for interface service"
                )
            _req = ParseDict(
                {
                    k: v
                    for k, v in {
                        "filterstext": filterstext,
                        "filtersdeviceIds": filtersdeviceIds,
                        "filtersconnectivityTypes": filtersconnectivityTypes,
                        "filtersnetworkBoundaries": filtersnetworkBoundaries,
                        "filtersproviders": filtersproviders,
                        "filterssnmpSpeeds": filterssnmpSpeeds,
                        "filtersipTypes": filtersipTypes,
                    }.items()
                    if v is not None
                },
                self._grpc_pb2_1.ListInterfaceRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_1.ListInterface, _req)
            return rest_models.ListInterfaceResponse.model_validate(
                MessageToDict(_resp)
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestInterfaceModule1.ListInterface(
                api_config_override=rest_transport.api_config,
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
        self, *, data: rest_models.CreateInterfaceRequest
    ) -> rest_models.CreateInterfaceResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for InterfaceCreate is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestInterfaceModule1.InterfaceCreate(
                api_config_override=rest_transport.api_config, data=data
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def interface_get(self, *, id: str) -> rest_models.GetInterfaceResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for InterfaceGet is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestInterfaceModule1.InterfaceGet(
                api_config_override=rest_transport.api_config, id=id
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def interface_update(
        self,
        *,
        id: str,
        data: rest_models.InterfaceServiceUpdateInterfaceBody,
    ) -> rest_models.UpdateInterfaceResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for InterfaceUpdate is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestInterfaceModule1.InterfaceUpdate(
                api_config_override=rest_transport.api_config, id=id, data=data
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def interface_delete(self, *, id: str) -> rest_models.DeleteInterfaceResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for InterfaceDelete is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestInterfaceModule1.InterfaceDelete(
                api_config_override=rest_transport.api_config, id=id
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def manual_classify(
        self, *, data: rest_models.ManualClassifyRequest
    ) -> rest_models.ManualClassifyResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for interface service"
                )
            _req = ParseDict(
                data.model_dump(by_alias=True, exclude_none=True),
                self._grpc_pb2_1.ManualClassifyRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_1.ManualClassify, _req)
            return rest_models.ManualClassifyResponse.model_validate(
                MessageToDict(_resp)
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestInterfaceModule1.ManualClassify(
                api_config_override=rest_transport.api_config, data=data
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )
