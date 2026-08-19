from typing import List, Optional, Union, cast

from google.protobuf.json_format import MessageToDict, ParseDict

import kentik_api.gen.kmi.services.KmiService as RestKmiModule1
from kentik_api.core.grpc_runtime import call_grpc
from kentik_api.gen.kmi import models as rest_models
from kentik_api.transports.grpc_client import GrpcTransport
from kentik_api.transports.rest_client import RestTransport


class KmiServiceWrapper:
    """AUTO-GENERATED: scripts/generation/wrapper_generation.py, _generate_service_wrappers().
    Rebuilt on every `make generate`. Do not edit by hand.
    Unified Service routing to either gRPC or REST.
    """

    def __init__(self, transport: Union[GrpcTransport, RestTransport]):
        self._transport = transport
        if isinstance(self._transport, GrpcTransport):
            try:
                __import__("kentik_api.gen.pb_companions")
                import kentik_api.gen.kmi.pb.kmi_pb2 as _pb2_1_mod
                import kentik_api.gen.kmi.pb.kmi_pb2_grpc as _pb2_grpc_1_mod

                self._grpc_pb2_1 = _pb2_1_mod
                self._grpc_stub_1 = _pb2_grpc_1_mod.KmiServiceStub(
                    self._transport.channel
                )
            except (ImportError, TypeError):
                self._grpc_pb2_1 = None
                self._grpc_stub_1 = None

    def get_global_insights(
        self,
        *,
        limit: Optional[int] = None,
        marketId: Optional[str] = None,
        ip: Optional[str] = None,
        lookback: Optional[int] = None,
        types: Optional[List[str]] = None,
        magnitude: Optional[int] = None,
    ) -> rest_models.GetGlobalInsightsResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for kmi service"
                )
            _req = ParseDict(
                {
                    k: v
                    for k, v in {
                        "limit": limit,
                        "marketId": marketId,
                        "ip": ip,
                        "lookback": lookback,
                        "types": types,
                        "magnitude": magnitude,
                    }.items()
                    if v is not None
                },
                self._grpc_pb2_1.GetGlobalInsightsRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_1.GetGlobalInsights, _req)
            return rest_models.GetGlobalInsightsResponse.model_validate(
                MessageToDict(_resp)
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestKmiModule1.GetGlobalInsights(
                api_config_override=rest_transport.api_config,
                limit=limit,
                marketId=marketId,
                ip=ip,
                lookback=lookback,
                types=types,
                magnitude=magnitude,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def get_a_s_n_insights(
        self,
        *,
        asn: str,
        limit: Optional[int] = None,
        marketId: Optional[str] = None,
        ip: Optional[str] = None,
        lookback: Optional[int] = None,
        types: Optional[List[str]] = None,
        magnitude: Optional[int] = None,
    ) -> rest_models.GetASNInsightsResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for kmi service"
                )
            _req = ParseDict(
                {
                    k: v
                    for k, v in {
                        "asn": asn,
                        "limit": limit,
                        "marketId": marketId,
                        "ip": ip,
                        "lookback": lookback,
                        "types": types,
                        "magnitude": magnitude,
                    }.items()
                    if v is not None
                },
                self._grpc_pb2_1.GetASNInsightsRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_1.GetASNInsights, _req)
            return rest_models.GetASNInsightsResponse.model_validate(
                MessageToDict(_resp)
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestKmiModule1.GetASNInsights(
                api_config_override=rest_transport.api_config,
                asn=asn,
                limit=limit,
                marketId=marketId,
                ip=ip,
                lookback=lookback,
                types=types,
                magnitude=magnitude,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def get_a_s_n_details(
        self,
        *,
        marketId: str,
        asn: str,
        type: str,
        data: rest_models.KmiServiceGetASNDetailsBody,
    ) -> rest_models.GetASNDetailsResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for kmi service"
                )
            _req_dict = data.model_dump(by_alias=True, exclude_none=True)
            _req_dict.update(
                {
                    k: v
                    for k, v in {"marketId": marketId, "asn": asn, "type": type}.items()
                    if v is not None
                }
            )
            _req = ParseDict(
                _req_dict,
                self._grpc_pb2_1.GetASNDetailsRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_1.GetASNDetails, _req)
            return rest_models.GetASNDetailsResponse.model_validate(
                MessageToDict(_resp)
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestKmiModule1.GetASNDetails(
                api_config_override=rest_transport.api_config,
                marketId=marketId,
                asn=asn,
                type=type,
                data=data,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def get_rankings(
        self,
        *,
        marketId: str,
        rankType: str,
        ip: str,
        data: rest_models.KmiServiceGetRankingsBody,
    ) -> rest_models.GetRankingsResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for kmi service"
                )
            _req_dict = data.model_dump(by_alias=True, exclude_none=True)
            _req_dict.update(
                {
                    k: v
                    for k, v in {
                        "marketId": marketId,
                        "rankType": rankType,
                        "ip": ip,
                    }.items()
                    if v is not None
                }
            )
            _req = ParseDict(
                _req_dict,
                self._grpc_pb2_1.GetRankingsRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_1.GetRankings, _req)
            return rest_models.GetRankingsResponse.model_validate(MessageToDict(_resp))
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestKmiModule1.GetRankings(
                api_config_override=rest_transport.api_config,
                marketId=marketId,
                rankType=rankType,
                ip=ip,
                data=data,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def list_markets(
        self,
    ) -> rest_models.ListMarketsResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for kmi service"
                )
            _req = self._grpc_pb2_1.ListMarketsRequest()
            _resp = call_grpc(self._grpc_stub_1.ListMarkets, _req)
            return rest_models.ListMarketsResponse.model_validate(MessageToDict(_resp))
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestKmiModule1.ListMarkets(
                api_config_override=rest_transport.api_config
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )
