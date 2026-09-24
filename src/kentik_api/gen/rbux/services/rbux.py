from typing import Any, Dict, Optional, Union, cast

from google.protobuf.json_format import MessageToDict, ParseDict

import kentik_api.gen.rbux.services.ScopeService as RestRbuxModule1
from kentik_api.core.api_config import APIConfig
from kentik_api.core.grpc_runtime import call_grpc
from kentik_api.core.rate_limit import attach_rate_limit
from kentik_api.gen.rbux import models as rest_models
from kentik_api.transports.grpc_client import GrpcTransport
from kentik_api.transports.rest_client import RestTransport


class RbuxServiceWrapper:
    """AUTO-GENERATED: scripts/generation/wrapper_generation.py, _generate_service_wrappers().
    Rebuilt on every `make generate`. Do not edit by hand.
    Unified Service routing to either gRPC or REST.
    """

    def __init__(self, transport: Union[GrpcTransport, RestTransport]):
        self._transport = transport
        if isinstance(self._transport, GrpcTransport):
            try:
                __import__("kentik_api.gen.pb_companions")
                import kentik_api.gen.rbux.pb.scope_pb2 as _pb2_1_mod
                import kentik_api.gen.rbux.pb.scope_pb2_grpc as _pb2_grpc_1_mod

                self._grpc_pb2_1 = _pb2_1_mod
                self._grpc_stub_1 = _pb2_grpc_1_mod.ScopeServiceStub(
                    self._transport.channel
                )
            except (ImportError, TypeError):
                self._grpc_pb2_1 = None
                self._grpc_stub_1 = None

    def list_scopes(
        self, *, api_config_override: Optional[APIConfig] = None
    ) -> rest_models.ListScopesResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_1 is None or self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for rbux service"
                )
            _req = self._grpc_pb2_1.ListScopesRequest()
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_1.ListScopes, _req, api_config=api_config_override
            )
            return attach_rate_limit(
                rest_models.ListScopesResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestRbuxModule1.ListScopes(
                api_config_override=api_config_override or rest_transport.api_config
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def create_scope(
        self,
        *,
        api_config_override: Optional[APIConfig] = None,
        data: rest_models.Scope,
    ) -> rest_models.CreateScopeResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_1 is None or self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for rbux service"
                )
            _req = ParseDict(
                data.model_dump(by_alias=True, exclude_none=True),
                self._grpc_pb2_1.CreateScopeRequest(),
                ignore_unknown_fields=True,
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_1.CreateScope, _req, api_config=api_config_override
            )
            return attach_rate_limit(
                rest_models.CreateScopeResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestRbuxModule1.CreateScope(
                api_config_override=api_config_override or rest_transport.api_config,
                data=data,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def get_scope(
        self, *, api_config_override: Optional[APIConfig] = None, id: str
    ) -> rest_models.GetScopeResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_1 is None or self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for rbux service"
                )
            _req = ParseDict(
                {k: v for k, v in {"id": id}.items() if v is not None},
                self._grpc_pb2_1.GetScopeRequest(),
                ignore_unknown_fields=True,
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_1.GetScope, _req, api_config=api_config_override
            )
            return attach_rate_limit(
                rest_models.GetScopeResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestRbuxModule1.GetScope(
                api_config_override=api_config_override or rest_transport.api_config,
                id=id,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def update_scope(
        self,
        *,
        api_config_override: Optional[APIConfig] = None,
        id: str,
        data: Dict[str, Any],
    ) -> rest_models.UpdateScopeResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_1 is None or self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for rbux service"
                )
            _req_dict = dict(data)
            _req_dict.update({k: v for k, v in {"id": id}.items() if v is not None})
            _req = ParseDict(
                _req_dict,
                self._grpc_pb2_1.UpdateScopeRequest(),
                ignore_unknown_fields=True,
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_1.UpdateScope, _req, api_config=api_config_override
            )
            return attach_rate_limit(
                rest_models.UpdateScopeResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestRbuxModule1.UpdateScope(
                api_config_override=api_config_override or rest_transport.api_config,
                id=id,
                data=data,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def delete_scope(
        self, *, api_config_override: Optional[APIConfig] = None, id: str
    ) -> rest_models.DeleteScopeResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_1 is None or self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for rbux service"
                )
            _req = ParseDict(
                {k: v for k, v in {"id": id}.items() if v is not None},
                self._grpc_pb2_1.DeleteScopeRequest(),
                ignore_unknown_fields=True,
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_1.DeleteScope, _req, api_config=api_config_override
            )
            return attach_rate_limit(
                rest_models.DeleteScopeResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestRbuxModule1.DeleteScope(
                api_config_override=api_config_override or rest_transport.api_config,
                id=id,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )
