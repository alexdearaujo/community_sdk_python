from typing import List, Optional, Union, cast

import kentik_api.gen.interface.services.InterfaceService as RestInterfaceModule1
from kentik_api.gen.interface import models as rest_models
from kentik_api.transports.grpc_client import GrpcTransport
from kentik_api.transports.rest_client import RestTransport


class InterfaceServiceWrapper:
    """Unified Service routing to either gRPC or REST."""

    def __init__(self, transport: Union[GrpcTransport, RestTransport]):
        self._transport = transport
        if isinstance(self._transport, GrpcTransport):
            pass  # TODO: Initialize gRPC stub here

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
            raise NotImplementedError(
                "gRPC translation for ListInterface is not yet implemented."
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
            raise NotImplementedError(
                "gRPC translation for ManualClassify is not yet implemented."
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
