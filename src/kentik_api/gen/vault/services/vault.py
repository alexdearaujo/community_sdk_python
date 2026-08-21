from typing import Union, cast, List
from kentik_api.gen.vault import models as rest_models
import kentik_api.gen.vault.services.VaultService as RestVaultModule1
from kentik_api.transports.grpc_client import GrpcTransport
from kentik_api.transports.rest_client import RestTransport
from google.protobuf.json_format import MessageToDict, ParseDict
from kentik_api.core.grpc_runtime import call_grpc


class VaultServiceWrapper:
    """AUTO-GENERATED: scripts/generation/wrapper_generation.py, _generate_service_wrappers().
    Rebuilt on every `make generate`. Do not edit by hand.
    Unified Service routing to either gRPC or REST.
    """

    def __init__(self, transport: Union[GrpcTransport, RestTransport]):
        self._transport = transport
        if isinstance(self._transport, GrpcTransport):
            try:
                __import__("kentik_api.gen.pb_companions")
                import kentik_api.gen.vault.pb.vault_pb2 as _pb2_1_mod
                import kentik_api.gen.vault.pb.vault_pb2_grpc as _pb2_grpc_1_mod

                self._grpc_pb2_1 = _pb2_1_mod
                self._grpc_stub_1 = _pb2_grpc_1_mod.VaultServiceStub(
                    self._transport.channel
                )
            except (ImportError, TypeError):
                self._grpc_pb2_1 = None
                self._grpc_stub_1 = None

    def list_secret(self, *, names: List[str]) -> rest_models.ListSecretResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for vault service"
                )
            _req = ParseDict(
                {k: v for k, v in {"names": names}.items() if v is not None},
                self._grpc_pb2_1.ListSecretRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_1.ListSecret, _req)
            return rest_models.ListSecretResponse.model_validate(MessageToDict(_resp))
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestVaultModule1.ListSecret(
                api_config_override=rest_transport.api_config, names=names
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def get_secret(self, *, name: str) -> rest_models.GetSecretResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for vault service"
                )
            _req = ParseDict(
                {k: v for k, v in {"name": name}.items() if v is not None},
                self._grpc_pb2_1.GetSecretRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_1.GetSecret, _req)
            return rest_models.GetSecretResponse.model_validate(MessageToDict(_resp))
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestVaultModule1.GetSecret(
                api_config_override=rest_transport.api_config, name=name
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )
