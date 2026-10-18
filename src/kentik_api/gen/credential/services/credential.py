from typing import Optional, Union, cast

import kentik_api.gen.credential.services.CredentialService as RestCredentialModule1
from kentik_api.core.api_config import APIConfig
from kentik_api.core.grpc_runtime import (
    build_grpc_request,
    call_grpc,
    parse_grpc_response,
)
from kentik_api.gen.credential import models as rest_models
from kentik_api.transports.grpc_client import GrpcTransport
from kentik_api.transports.rest_client import RestTransport


class CredentialServiceWrapper:
    """AUTO-GENERATED: scripts/generation/wrapper_generation.py, _generate_service_wrappers().
    Rebuilt on every `uv run poe generate`. Do not edit by hand.
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
            except (ImportError, TypeError) as exc:
                self._grpc_pb2_1 = None
                self._grpc_stub_1 = None
                self._grpc_import_error_1 = exc

    def list_group(
        self, *, api_config_override: Optional[APIConfig] = None
    ) -> rest_models.ListCredentialGroupResponse:
        """
        List credential groups.

        Returns list of credential group information in Kentik vault.
        """
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_1 is None or self._grpc_stub_1 is None:
                raise NotImplementedError(
                    f"gRPC proto modules for credential service failed to import: {self._grpc_import_error_1!r}"
                ) from self._grpc_import_error_1
            _req = build_grpc_request(
                self._grpc_pb2_1.ListCredentialGroupRequest, None, {}
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_1.ListCredentialGroup,
                _req,
                api_config=api_config_override,
                error_cls=RestCredentialModule1.ListGroupError,
            )
            return parse_grpc_response(
                rest_models.ListCredentialGroupResponse,
                _resp,
                _rate_limit,
                stub_method=self._grpc_stub_1.ListCredentialGroup,
                operation_name="ListCredentialGroup",
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestCredentialModule1.ListCredentialGroup(
                api_config_override=api_config_override or rest_transport.api_config
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def get_group(
        self, *, api_config_override: Optional[APIConfig] = None, id: str
    ) -> rest_models.GetCredentialGroupResponse:
        """
        Get a credential group by id.

        Returns specific credential group information in Kentik vault.
        """
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_1 is None or self._grpc_stub_1 is None:
                raise NotImplementedError(
                    f"gRPC proto modules for credential service failed to import: {self._grpc_import_error_1!r}"
                ) from self._grpc_import_error_1
            _req = build_grpc_request(
                self._grpc_pb2_1.GetCredentialGroupRequest, None, {"id": id}
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_1.GetCredentialGroup,
                _req,
                api_config=api_config_override,
                error_cls=RestCredentialModule1.GetGroupError,
            )
            return parse_grpc_response(
                rest_models.GetCredentialGroupResponse,
                _resp,
                _rate_limit,
                stub_method=self._grpc_stub_1.GetCredentialGroup,
                operation_name="GetCredentialGroup",
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestCredentialModule1.GetCredentialGroup(
                api_config_override=api_config_override or rest_transport.api_config,
                id=id,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )
