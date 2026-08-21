from typing import Union, cast
from kentik_api.gen.as_group import models as rest_models
import kentik_api.gen.as_group.services.ASGroupService as RestAsGroupModule1
from kentik_api.transports.grpc_client import GrpcTransport
from kentik_api.transports.rest_client import RestTransport
from google.protobuf.json_format import MessageToDict, ParseDict
from kentik_api.core.grpc_runtime import call_grpc


class AsGroupServiceWrapper:
    """AUTO-GENERATED: scripts/generation/wrapper_generation.py, _generate_service_wrappers().
    Rebuilt on every `make generate`. Do not edit by hand.
    Unified Service routing to either gRPC or REST.
    """

    def __init__(self, transport: Union[GrpcTransport, RestTransport]):
        self._transport = transport
        if isinstance(self._transport, GrpcTransport):
            try:
                __import__("kentik_api.gen.pb_companions")
                import kentik_api.gen.as_group.pb.as_group_pb2 as _pb2_1_mod
                import kentik_api.gen.as_group.pb.as_group_pb2_grpc as _pb2_grpc_1_mod

                self._grpc_pb2_1 = _pb2_1_mod
                self._grpc_stub_1 = _pb2_grpc_1_mod.ASGroupServiceStub(
                    self._transport.channel
                )
            except (ImportError, TypeError):
                self._grpc_pb2_1 = None
                self._grpc_stub_1 = None

    def list_a_s_groups(
        self,
    ) -> rest_models.ListASGroupsResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for as_group service"
                )
            _req = self._grpc_pb2_1.ListASGroupsRequest()
            _resp = call_grpc(self._grpc_stub_1.ListASGroups, _req)
            return rest_models.ListASGroupsResponse.model_validate(MessageToDict(_resp))
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
            if self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for as_group service"
                )
            _req = ParseDict(
                data.model_dump(by_alias=True, exclude_none=True),
                self._grpc_pb2_1.CreateASGroupRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_1.CreateASGroup, _req)
            return rest_models.CreateASGroupResponse.model_validate(
                MessageToDict(_resp)
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
            if self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for as_group service"
                )
            _req = ParseDict(
                {k: v for k, v in {"asGroupid": asGroupid}.items() if v is not None},
                self._grpc_pb2_1.GetASGroupRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_1.GetASGroup, _req)
            return rest_models.GetASGroupResponse.model_validate(MessageToDict(_resp))
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
        self, *, asGroupid: str, data: rest_models.ASGroupServiceUpdateASGroupBody
    ) -> rest_models.UpdateASGroupResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for as_group service"
                )
            _req_dict = data.model_dump(by_alias=True, exclude_none=True)
            _req_dict.update(
                {k: v for k, v in {"asGroupid": asGroupid}.items() if v is not None}
            )
            _req = ParseDict(
                _req_dict,
                self._grpc_pb2_1.UpdateASGroupRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_1.UpdateASGroup, _req)
            return rest_models.UpdateASGroupResponse.model_validate(
                MessageToDict(_resp)
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
            if self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for as_group service"
                )
            _req = ParseDict(
                {k: v for k, v in {"asGroupid": asGroupid}.items() if v is not None},
                self._grpc_pb2_1.DeleteASGroupRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_1.DeleteASGroup, _req)
            return rest_models.DeleteASGroupResponse.model_validate(
                MessageToDict(_resp)
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
