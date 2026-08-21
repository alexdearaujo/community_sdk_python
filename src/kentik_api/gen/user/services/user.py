from typing import Union, cast
from kentik_api.gen.user import models as rest_models
import kentik_api.gen.user.services.UserService as RestUserModule1
from kentik_api.transports.grpc_client import GrpcTransport
from kentik_api.transports.rest_client import RestTransport
from google.protobuf.json_format import MessageToDict, ParseDict
from kentik_api.core.grpc_runtime import call_grpc


class UserServiceWrapper:
    """AUTO-GENERATED: scripts/generation/wrapper_generation.py, _generate_service_wrappers().
    Rebuilt on every `make generate`. Do not edit by hand.
    Unified Service routing to either gRPC or REST.
    """

    def __init__(self, transport: Union[GrpcTransport, RestTransport]):
        self._transport = transport
        if isinstance(self._transport, GrpcTransport):
            try:
                __import__("kentik_api.gen.pb_companions")
                import kentik_api.gen.user.pb.user_pb2 as _pb2_1_mod
                import kentik_api.gen.user.pb.user_pb2_grpc as _pb2_grpc_1_mod

                self._grpc_pb2_1 = _pb2_1_mod
                self._grpc_stub_1 = _pb2_grpc_1_mod.UserServiceStub(
                    self._transport.channel
                )
            except (ImportError, TypeError):
                self._grpc_pb2_1 = None
                self._grpc_stub_1 = None

    def list_users(
        self,
    ) -> rest_models.ListUsersResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for user service"
                )
            _req = self._grpc_pb2_1.ListUsersRequest()
            _resp = call_grpc(self._grpc_stub_1.ListUsers, _req)
            return rest_models.ListUsersResponse.model_validate(MessageToDict(_resp))
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestUserModule1.ListUsers(
                api_config_override=rest_transport.api_config
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def create_user(
        self, *, data: rest_models.CreateUserRequest
    ) -> rest_models.CreateUserResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for user service"
                )
            _req = ParseDict(
                data.model_dump(by_alias=True, exclude_none=True),
                self._grpc_pb2_1.CreateUserRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_1.CreateUser, _req)
            return rest_models.CreateUserResponse.model_validate(MessageToDict(_resp))
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestUserModule1.CreateUser(
                api_config_override=rest_transport.api_config, data=data
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def get_user(self, *, id: str) -> rest_models.GetUserResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for user service"
                )
            _req = ParseDict(
                {k: v for k, v in {"id": id}.items() if v is not None},
                self._grpc_pb2_1.GetUserRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_1.GetUser, _req)
            return rest_models.GetUserResponse.model_validate(MessageToDict(_resp))
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestUserModule1.GetUser(
                api_config_override=rest_transport.api_config, id=id
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def update_user(
        self, *, id: str, data: rest_models.UserServiceUpdateUserBody
    ) -> rest_models.UpdateUserResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for user service"
                )
            _req_dict = data.model_dump(by_alias=True, exclude_none=True)
            _req_dict.update({k: v for k, v in {"id": id}.items() if v is not None})
            _req = ParseDict(
                _req_dict,
                self._grpc_pb2_1.UpdateUserRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_1.UpdateUser, _req)
            return rest_models.UpdateUserResponse.model_validate(MessageToDict(_resp))
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestUserModule1.UpdateUser(
                api_config_override=rest_transport.api_config, id=id, data=data
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def delete_user(self, *, id: str) -> rest_models.DeleteUserResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for user service"
                )
            _req = ParseDict(
                {k: v for k, v in {"id": id}.items() if v is not None},
                self._grpc_pb2_1.DeleteUserRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_1.DeleteUser, _req)
            return rest_models.DeleteUserResponse.model_validate(MessageToDict(_resp))
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestUserModule1.DeleteUser(
                api_config_override=rest_transport.api_config, id=id
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def reset_active_sessions(
        self, *, id: str
    ) -> rest_models.ResetActiveSessionsResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for user service"
                )
            _req = ParseDict(
                {k: v for k, v in {"id": id}.items() if v is not None},
                self._grpc_pb2_1.ResetActiveSessionsRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_1.ResetActiveSessions, _req)
            return rest_models.ResetActiveSessionsResponse.model_validate(
                MessageToDict(_resp)
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestUserModule1.ResetActiveSessions(
                api_config_override=rest_transport.api_config, id=id
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def reset_api_token(self, *, id: str) -> rest_models.ResetApiTokenResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for user service"
                )
            _req = ParseDict(
                {k: v for k, v in {"id": id}.items() if v is not None},
                self._grpc_pb2_1.ResetApiTokenRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_1.ResetApiToken, _req)
            return rest_models.ResetApiTokenResponse.model_validate(
                MessageToDict(_resp)
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestUserModule1.ResetApiToken(
                api_config_override=rest_transport.api_config, id=id
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )
