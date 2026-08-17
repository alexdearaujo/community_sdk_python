from typing import Union, cast

import kentik_api.gen.as_group.services.ASGroupService as RestAsGroupModule1
from kentik_api.gen.as_group import models as rest_models
from kentik_api.transports.grpc_client import GrpcTransport
from kentik_api.transports.rest_client import RestTransport


class AsGroupServiceWrapper:
    """Unified Service routing to either gRPC or REST."""

    def __init__(self, transport: Union[GrpcTransport, RestTransport]):
        self._transport = transport
        if isinstance(self._transport, GrpcTransport):
            pass  # TODO: Initialize gRPC stub here

    def list_a_s_groups(
        self,
    ) -> rest_models.ListASGroupsResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for ListASGroups is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestAsGroupModule1.ListASGroups(
                api_config_override=rest_transport.api_config
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def create_a_s_group(
        self, *, data: rest_models.CreateASGroupRequest
    ) -> rest_models.CreateASGroupResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for CreateASGroup is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestAsGroupModule1.CreateASGroup(
                api_config_override=rest_transport.api_config, data=data
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def get_a_s_group(self, *, asGroupid: str) -> rest_models.GetASGroupResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for GetASGroup is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestAsGroupModule1.GetASGroup(
                api_config_override=rest_transport.api_config, asGroupid=asGroupid
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def update_a_s_group(
        self,
        *,
        asGroupid: str,
        data: rest_models.ASGroupServiceUpdateASGroupBody,
    ) -> rest_models.UpdateASGroupResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for UpdateASGroup is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestAsGroupModule1.UpdateASGroup(
                api_config_override=rest_transport.api_config,
                asGroupid=asGroupid,
                data=data,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def delete_a_s_group(self, *, asGroupid: str) -> rest_models.DeleteASGroupResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for DeleteASGroup is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestAsGroupModule1.DeleteASGroup(
                api_config_override=rest_transport.api_config, asGroupid=asGroupid
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )
