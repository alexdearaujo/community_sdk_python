from typing import Union, cast
from kentik_api.gen.ai_advisor import models as rest_models
import kentik_api.gen.ai_advisor.services.AiAdvisorDataService as RestAiAdvisorModule1
from kentik_api.transports.grpc_client import GrpcTransport
from kentik_api.transports.rest_client import RestTransport
from google.protobuf.json_format import MessageToDict, ParseDict
from kentik_api.core.grpc_runtime import call_grpc


class AiAdvisorServiceWrapper:
    """AUTO-GENERATED: scripts/generation/wrapper_generation.py, _generate_service_wrappers().
    Rebuilt on every `make generate`. Do not edit by hand.
    Unified Service routing to either gRPC or REST.
    """

    def __init__(self, transport: Union[GrpcTransport, RestTransport]):
        self._transport = transport
        if isinstance(self._transport, GrpcTransport):
            try:
                __import__("kentik_api.gen.pb_companions")
                import kentik_api.gen.ai_advisor.pb.ai_advisor_pb2 as _pb2_1_mod
                import kentik_api.gen.ai_advisor.pb.ai_advisor_pb2_grpc as _pb2_grpc_1_mod

                self._grpc_pb2_1 = _pb2_1_mod
                self._grpc_stub_1 = _pb2_grpc_1_mod.AiAdvisorDataServiceStub(
                    self._transport.channel
                )
            except (ImportError, TypeError):
                self._grpc_pb2_1 = None
                self._grpc_stub_1 = None

    def create_chat_session(
        self, *, data: rest_models.CreateChatSessionRequest
    ) -> rest_models.CreateChatSessionResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for ai_advisor service"
                )
            _req = ParseDict(
                data.model_dump(by_alias=True, exclude_none=True),
                self._grpc_pb2_1.CreateChatSessionRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_1.CreateChatSession, _req)
            return rest_models.CreateChatSessionResponse.model_validate(
                MessageToDict(_resp)
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestAiAdvisorModule1.CreateChatSession(
                api_config_override=rest_transport.api_config, data=data
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def update_chat_session(
        self, *, data: rest_models.UpdateChatSessionRequest
    ) -> rest_models.UpdateChatSessionResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for ai_advisor service"
                )
            _req = ParseDict(
                data.model_dump(by_alias=True, exclude_none=True),
                self._grpc_pb2_1.UpdateChatSessionRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_1.UpdateChatSession, _req)
            return rest_models.UpdateChatSessionResponse.model_validate(
                MessageToDict(_resp)
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestAiAdvisorModule1.UpdateChatSession(
                api_config_override=rest_transport.api_config, data=data
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def get_chat_session(self, *, id: str) -> rest_models.GetChatSessionResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for ai_advisor service"
                )
            _req = ParseDict(
                {k: v for k, v in {"id": id}.items() if v is not None},
                self._grpc_pb2_1.GetChatSessionRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_1.GetChatSession, _req)
            return rest_models.GetChatSessionResponse.model_validate(
                MessageToDict(_resp)
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestAiAdvisorModule1.GetChatSession(
                api_config_override=rest_transport.api_config, id=id
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )
