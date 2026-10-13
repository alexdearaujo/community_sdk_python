from typing import Optional, Union, cast

from google.protobuf.json_format import MessageToDict

import kentik_api.gen.enrichments.services.EnumerationsAdminService as RestEnrichmentsModule1
from kentik_api.core.api_config import APIConfig
from kentik_api.core.grpc_runtime import build_grpc_request, call_grpc
from kentik_api.core.rate_limit import attach_rate_limit
from kentik_api.gen.enrichments import models as rest_models
from kentik_api.transports.grpc_client import GrpcTransport
from kentik_api.transports.rest_client import RestTransport


class EnrichmentsServiceWrapper:
    """AUTO-GENERATED: scripts/generation/wrapper_generation.py, _generate_service_wrappers().
    Rebuilt on every `make generate`. Do not edit by hand.
    Unified Service routing to either gRPC or REST.
    """

    def __init__(self, transport: Union[GrpcTransport, RestTransport]):
        self._transport = transport
        if isinstance(self._transport, GrpcTransport):
            try:
                __import__("kentik_api.gen.pb_companions")
                import kentik_api.gen.enrichments.pb.enumerations_pb2 as _pb2_1_mod
                import kentik_api.gen.enrichments.pb.enumerations_pb2_grpc as _pb2_grpc_1_mod

                self._grpc_pb2_1 = _pb2_1_mod
                self._grpc_stub_1 = _pb2_grpc_1_mod.EnumerationsAdminServiceStub(
                    self._transport.channel
                )
            except (ImportError, TypeError):
                self._grpc_pb2_1 = None
                self._grpc_stub_1 = None

    def fetch_values_by_ids(
        self,
        *,
        api_config_override: Optional[APIConfig] = None,
        data: rest_models.FetchValuesByIdsRequest,
    ) -> rest_models.FetchValuesByIdsResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_1 is None or self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for enrichments service"
                )
            _req = build_grpc_request(
                self._grpc_pb2_1.FetchValuesByIdsRequest,
                data.model_dump(by_alias=True, exclude_unset=True),
                {},
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_1.FetchValuesByIds,
                _req,
                api_config=api_config_override,
                error_cls=RestEnrichmentsModule1.FetchValuesByIdsError,
            )
            return attach_rate_limit(
                rest_models.FetchValuesByIdsResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestEnrichmentsModule1.FetchValuesByIds(
                api_config_override=api_config_override or rest_transport.api_config,
                data=data,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )
