from typing import Optional, Union, cast

from google.protobuf.json_format import MessageToDict

import kentik_api.gen.as_group.services.ASGroupService as RestAsGroupModule1
from kentik_api.core.api_config import APIConfig
from kentik_api.core.grpc_runtime import build_grpc_request, call_grpc
from kentik_api.core.rate_limit import attach_rate_limit
from kentik_api.gen.as_group import models as rest_models
from kentik_api.transports.grpc_client import GrpcTransport
from kentik_api.transports.rest_client import RestTransport


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
            except (ImportError, TypeError) as exc:
                self._grpc_pb2_1 = None
                self._grpc_stub_1 = None
                self._grpc_import_error_1 = exc

    def list_as_groups(
        self, *, api_config_override: Optional[APIConfig] = None
    ) -> rest_models.ListASGroupsResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_1 is None or self._grpc_stub_1 is None:
                raise NotImplementedError(
                    f"gRPC proto modules for as_group service failed to import: {self._grpc_import_error_1!r}"
                ) from self._grpc_import_error_1
            _req = build_grpc_request(self._grpc_pb2_1.ListASGroupsRequest, None, {})
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_1.ListASGroups,
                _req,
                api_config=api_config_override,
                error_cls=RestAsGroupModule1.ListASGroupsError,
            )
            return attach_rate_limit(
                rest_models.ListASGroupsResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestAsGroupModule1.ListASGroups(
                api_config_override=api_config_override or rest_transport.api_config
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def create_as_group(
        self,
        *,
        api_config_override: Optional[APIConfig] = None,
        data: rest_models.CreateASGroupRequest,
    ) -> rest_models.CreateASGroupResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_1 is None or self._grpc_stub_1 is None:
                raise NotImplementedError(
                    f"gRPC proto modules for as_group service failed to import: {self._grpc_import_error_1!r}"
                ) from self._grpc_import_error_1
            _req = build_grpc_request(
                self._grpc_pb2_1.CreateASGroupRequest,
                data.model_dump(by_alias=True, exclude_unset=True),
                {},
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_1.CreateASGroup,
                _req,
                api_config=api_config_override,
                error_cls=RestAsGroupModule1.CreateASGroupError,
            )
            return attach_rate_limit(
                rest_models.CreateASGroupResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestAsGroupModule1.CreateASGroup(
                api_config_override=api_config_override or rest_transport.api_config,
                data=data,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def get_as_group(
        self, *, api_config_override: Optional[APIConfig] = None, asGroupid: str
    ) -> rest_models.GetASGroupResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_1 is None or self._grpc_stub_1 is None:
                raise NotImplementedError(
                    f"gRPC proto modules for as_group service failed to import: {self._grpc_import_error_1!r}"
                ) from self._grpc_import_error_1
            _req = build_grpc_request(
                self._grpc_pb2_1.GetASGroupRequest, None, {"id": asGroupid}
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_1.GetASGroup,
                _req,
                api_config=api_config_override,
                error_cls=RestAsGroupModule1.GetASGroupError,
            )
            return attach_rate_limit(
                rest_models.GetASGroupResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestAsGroupModule1.GetASGroup(
                api_config_override=api_config_override or rest_transport.api_config,
                asGroupid=asGroupid,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def update_as_group(
        self,
        *,
        api_config_override: Optional[APIConfig] = None,
        asGroupid: str,
        data: rest_models.ASGroupServiceUpdateASGroupBody,
    ) -> rest_models.UpdateASGroupResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_1 is None or self._grpc_stub_1 is None:
                raise NotImplementedError(
                    f"gRPC proto modules for as_group service failed to import: {self._grpc_import_error_1!r}"
                ) from self._grpc_import_error_1
            _req = build_grpc_request(
                self._grpc_pb2_1.UpdateASGroupRequest,
                data.model_dump(by_alias=True, exclude_unset=True),
                {"as_group.id": asGroupid},
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_1.UpdateASGroup,
                _req,
                api_config=api_config_override,
                error_cls=RestAsGroupModule1.UpdateASGroupError,
            )
            return attach_rate_limit(
                rest_models.UpdateASGroupResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestAsGroupModule1.UpdateASGroup(
                api_config_override=api_config_override or rest_transport.api_config,
                asGroupid=asGroupid,
                data=data,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def delete_as_group(
        self, *, api_config_override: Optional[APIConfig] = None, asGroupid: str
    ) -> rest_models.DeleteASGroupResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_1 is None or self._grpc_stub_1 is None:
                raise NotImplementedError(
                    f"gRPC proto modules for as_group service failed to import: {self._grpc_import_error_1!r}"
                ) from self._grpc_import_error_1
            _req = build_grpc_request(
                self._grpc_pb2_1.DeleteASGroupRequest, None, {"id": asGroupid}
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_1.DeleteASGroup,
                _req,
                api_config=api_config_override,
                error_cls=RestAsGroupModule1.DeleteASGroupError,
            )
            return attach_rate_limit(
                rest_models.DeleteASGroupResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestAsGroupModule1.DeleteASGroup(
                api_config_override=api_config_override or rest_transport.api_config,
                asGroupid=asGroupid,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )
