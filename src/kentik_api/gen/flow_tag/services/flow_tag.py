from typing import List, Optional, Union, cast

from google.protobuf.json_format import MessageToDict, ParseDict

import kentik_api.gen.flow_tag.services.FlowTagService as RestFlowTagModule1
from kentik_api.core.grpc_runtime import call_grpc
from kentik_api.gen.flow_tag import models as rest_models
from kentik_api.transports.grpc_client import GrpcTransport
from kentik_api.transports.rest_client import RestTransport


class FlowTagServiceWrapper:
    """Unified Service routing to either gRPC or REST."""

    def __init__(self, transport: Union[GrpcTransport, RestTransport]):
        self._transport = transport
        if isinstance(self._transport, GrpcTransport):
            try:
                __import__("kentik_api.gen.pb_companions")
                import kentik_api.gen.flow_tag.pb.flow_tag_pb2 as _pb2_1_mod
                import kentik_api.gen.flow_tag.pb.flow_tag_pb2_grpc as _pb2_grpc_1_mod

                self._grpc_pb2_1 = _pb2_1_mod
                self._grpc_stub_1 = _pb2_grpc_1_mod.FlowTagServiceStub(
                    self._transport.channel
                )
            except (ImportError, TypeError):
                self._grpc_pb2_1 = None
                self._grpc_stub_1 = None

    def search_flow_tag(
        self,
        *,
        searchlimit: Optional[int] = None,
        searchoffset: Optional[int] = None,
        searchlookupFields: Optional[List[str]] = None,
        searchlookupValues: Optional[List[str]] = None,
        searchfieldLimit: Optional[int] = None,
    ) -> rest_models.SearchFlowTagResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for flow_tag service"
                )
            _req = ParseDict(
                {
                    k: v
                    for k, v in {
                        "searchlimit": searchlimit,
                        "searchoffset": searchoffset,
                        "searchlookupFields": searchlookupFields,
                        "searchlookupValues": searchlookupValues,
                        "searchfieldLimit": searchfieldLimit,
                    }.items()
                    if v is not None
                },
                self._grpc_pb2_1.SearchFlowTagRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_1.SearchFlowTag, _req)
            return rest_models.SearchFlowTagResponse.model_validate(
                MessageToDict(_resp)
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestFlowTagModule1.SearchFlowTag(
                api_config_override=rest_transport.api_config,
                searchlimit=searchlimit,
                searchoffset=searchoffset,
                searchlookupFields=searchlookupFields,
                searchlookupValues=searchlookupValues,
                searchfieldLimit=searchfieldLimit,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def create_flow_tag(
        self, *, data: rest_models.CreateFlowTagRequest
    ) -> rest_models.CreateFlowTagResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for flow_tag service"
                )
            _req = ParseDict(
                data.model_dump(by_alias=True, exclude_none=True),
                self._grpc_pb2_1.CreateFlowTagRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_1.CreateFlowTag, _req)
            return rest_models.CreateFlowTagResponse.model_validate(
                MessageToDict(_resp)
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestFlowTagModule1.CreateFlowTag(
                api_config_override=rest_transport.api_config, data=data
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def get_flow_tag(self, *, flowTagid: str) -> rest_models.GetFlowTagResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for flow_tag service"
                )
            _req = ParseDict(
                {k: v for k, v in {"flowTagid": flowTagid}.items() if v is not None},
                self._grpc_pb2_1.GetFlowTagRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_1.GetFlowTag, _req)
            return rest_models.GetFlowTagResponse.model_validate(MessageToDict(_resp))
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestFlowTagModule1.GetFlowTag(
                api_config_override=rest_transport.api_config, flowTagid=flowTagid
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def update_flow_tag(
        self,
        *,
        flowTagid: str,
        data: rest_models.FlowTagServiceUpdateFlowTagBody,
    ) -> rest_models.UpdateFlowTagResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for flow_tag service"
                )
            _req_dict = data.model_dump(by_alias=True, exclude_none=True)
            _req_dict.update(
                {k: v for k, v in {"flowTagid": flowTagid}.items() if v is not None}
            )
            _req = ParseDict(
                _req_dict,
                self._grpc_pb2_1.UpdateFlowTagRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_1.UpdateFlowTag, _req)
            return rest_models.UpdateFlowTagResponse.model_validate(
                MessageToDict(_resp)
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestFlowTagModule1.UpdateFlowTag(
                api_config_override=rest_transport.api_config,
                flowTagid=flowTagid,
                data=data,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def delete_flow_tag(self, *, flowTagid: str) -> rest_models.DeleteFlowTagResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for flow_tag service"
                )
            _req = ParseDict(
                {k: v for k, v in {"flowTagid": flowTagid}.items() if v is not None},
                self._grpc_pb2_1.DeleteFlowTagRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_1.DeleteFlowTag, _req)
            return rest_models.DeleteFlowTagResponse.model_validate(
                MessageToDict(_resp)
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestFlowTagModule1.DeleteFlowTag(
                api_config_override=rest_transport.api_config, flowTagid=flowTagid
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )
