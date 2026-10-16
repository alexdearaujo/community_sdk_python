from typing import Optional, Union, cast

from google.protobuf.json_format import MessageToDict

import kentik_api.gen.journeys.services.JourneysDataService as RestJourneysModule1
from kentik_api.core.api_config import APIConfig
from kentik_api.core.grpc_runtime import build_grpc_request, call_grpc
from kentik_api.core.rate_limit import attach_rate_limit
from kentik_api.gen.journeys import models as rest_models
from kentik_api.transports.grpc_client import GrpcTransport
from kentik_api.transports.rest_client import RestTransport


class JourneysServiceWrapper:
    """AUTO-GENERATED: scripts/generation/wrapper_generation.py, _generate_service_wrappers().
    Rebuilt on every `make generate`. Do not edit by hand.
    Unified Service routing to either gRPC or REST.
    """

    def __init__(self, transport: Union[GrpcTransport, RestTransport]):
        self._transport = transport
        if isinstance(self._transport, GrpcTransport):
            try:
                __import__("kentik_api.gen.pb_companions")
                import kentik_api.gen.journeys.pb.journeys_pb2 as _pb2_1_mod
                import kentik_api.gen.journeys.pb.journeys_pb2_grpc as _pb2_grpc_1_mod

                self._grpc_pb2_1 = _pb2_1_mod
                self._grpc_stub_1 = _pb2_grpc_1_mod.JourneysDataServiceStub(
                    self._transport.channel
                )
            except (ImportError, TypeError):
                self._grpc_pb2_1 = None
                self._grpc_stub_1 = None

    def get_nlq(
        self, *, api_config_override: Optional[APIConfig] = None, prompt: str
    ) -> rest_models.GetJourneysNlqResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_1 is None or self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for journeys service"
                )
            _req = build_grpc_request(
                self._grpc_pb2_1.GetJourneysNlqRequest, None, {"prompt": prompt}
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_1.GetJourneysNlq,
                _req,
                api_config=api_config_override,
                error_cls=RestJourneysModule1.GetJourneysNlqError,
            )
            return attach_rate_limit(
                rest_models.GetJourneysNlqResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestJourneysModule1.GetJourneysNlq(
                api_config_override=api_config_override or rest_transport.api_config,
                prompt=prompt,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )
