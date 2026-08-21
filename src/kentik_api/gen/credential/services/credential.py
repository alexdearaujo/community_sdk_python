from typing import Union, cast
from kentik_api.gen.credential import models as rest_models
import kentik_api.gen.credential.services.CredentialService as RestCredentialModule1
from kentik_api.transports.grpc_client import GrpcTransport
from kentik_api.transports.rest_client import RestTransport
from google.protobuf.json_format import MessageToDict, ParseDict
from kentik_api.core.grpc_runtime import call_grpc


class CredentialServiceWrapper:
    """AUTO-GENERATED: scripts/generation/wrapper_generation.py, _generate_service_wrappers().
    Rebuilt on every `make generate`. Do not edit by hand.
    Unified Service routing to either gRPC or REST.
    """

    def __init__(self, transport: Union[GrpcTransport, RestTransport]):
        self._transport = transport
        if isinstance(self._transport, GrpcTransport):
            try:
                __import__("kentik_api.gen.pb_companions")
                import kentik_api.gen.credential.pb.credential_pb2 as _pb2_1_mod
                import kentik_api.gen.credential.pb.credential_pb2_grpc as _pb2_grpc_1_mod

                self._grpc_pb2_1 = _pb2_1_mod
                self._grpc_stub_1 = _pb2_grpc_1_mod.CredentialServiceStub(
                    self._transport.channel
                )
            except (ImportError, TypeError):
                self._grpc_pb2_1 = None
                self._grpc_stub_1 = None

    def list_credential_group(
        self,
    ) -> rest_models.ListCredentialGroupResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for credential service"
                )
            _req = self._grpc_pb2_1.ListCredentialGroupRequest()
            _resp = call_grpc(self._grpc_stub_1.ListCredentialGroup, _req)
            return rest_models.ListCredentialGroupResponse.model_validate(
                MessageToDict(_resp)
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestCredentialModule1.ListCredentialGroup(
                api_config_override=rest_transport.api_config
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def get_credential_group(
        self, *, id: str
    ) -> rest_models.GetCredentialGroupResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for credential service"
                )
            _req = ParseDict(
                {k: v for k, v in {"id": id}.items() if v is not None},
                self._grpc_pb2_1.GetCredentialGroupRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_1.GetCredentialGroup, _req)
            return rest_models.GetCredentialGroupResponse.model_validate(
                MessageToDict(_resp)
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestCredentialModule1.GetCredentialGroup(
                api_config_override=rest_transport.api_config, id=id
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )
