from typing import List, Optional, Union, cast

from google.protobuf.json_format import MessageToDict

import kentik_api.gen.flow_tag.services.FlowTagService as RestFlowTagModule1
from kentik_api.core.api_config import APIConfig
from kentik_api.core.grpc_runtime import build_grpc_request, call_grpc
from kentik_api.core.rate_limit import attach_rate_limit
from kentik_api.gen.flow_tag import models as rest_models
from kentik_api.transports.grpc_client import GrpcTransport
from kentik_api.transports.rest_client import RestTransport


class FlowTagServiceWrapper:
    """AUTO-GENERATED: scripts/generation/wrapper_generation.py, _generate_service_wrappers().
    Rebuilt on every `make generate`. Do not edit by hand.
    Unified Service routing to either gRPC or REST.
    """

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
        api_config_override: Optional[APIConfig] = None,
        searchlimit: Optional[int] = None,
        searchoffset: Optional[int] = None,
        searchlookupFields: Optional[List[str]] = None,
        searchlookupValues: Optional[List[str]] = None,
        searchfieldLimit: Optional[int] = None,
    ) -> rest_models.SearchFlowTagResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_1 is None or self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for flow_tag service"
                )
            _req = build_grpc_request(
                self._grpc_pb2_1.SearchFlowTagRequest,
                None,
                {
                    "search.limit": searchlimit,
                    "search.offset": searchoffset,
                    "search.lookupFields": searchlookupFields,
                    "search.lookupValues": searchlookupValues,
                    "search.fieldLimit": searchfieldLimit,
                },
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_1.SearchFlowTag,
                _req,
                api_config=api_config_override,
                error_cls=RestFlowTagModule1.SearchFlowTagError,
            )
            return attach_rate_limit(
                rest_models.SearchFlowTagResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestFlowTagModule1.SearchFlowTag(
                api_config_override=api_config_override or rest_transport.api_config,
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
        self,
        *,
        api_config_override: Optional[APIConfig] = None,
        data: rest_models.CreateFlowTagRequest,
    ) -> rest_models.CreateFlowTagResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_1 is None or self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for flow_tag service"
                )
            _req = build_grpc_request(
                self._grpc_pb2_1.CreateFlowTagRequest,
                data.model_dump(by_alias=True, exclude_none=True),
                {},
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_1.CreateFlowTag,
                _req,
                api_config=api_config_override,
                error_cls=RestFlowTagModule1.CreateFlowTagError,
            )
            return attach_rate_limit(
                rest_models.CreateFlowTagResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestFlowTagModule1.CreateFlowTag(
                api_config_override=api_config_override or rest_transport.api_config,
                data=data,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def get_flow_tag(
        self, *, api_config_override: Optional[APIConfig] = None, flowTagid: str
    ) -> rest_models.GetFlowTagResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_1 is None or self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for flow_tag service"
                )
            _req = build_grpc_request(
                self._grpc_pb2_1.GetFlowTagRequest, None, {"id": flowTagid}
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_1.GetFlowTag,
                _req,
                api_config=api_config_override,
                error_cls=RestFlowTagModule1.GetFlowTagError,
            )
            return attach_rate_limit(
                rest_models.GetFlowTagResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestFlowTagModule1.GetFlowTag(
                api_config_override=api_config_override or rest_transport.api_config,
                flowTagid=flowTagid,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def update_flow_tag(
        self,
        *,
        api_config_override: Optional[APIConfig] = None,
        flowTagid: str,
        data: rest_models.FlowTagServiceUpdateFlowTagBody,
    ) -> rest_models.UpdateFlowTagResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_1 is None or self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for flow_tag service"
                )
            _req = build_grpc_request(
                self._grpc_pb2_1.UpdateFlowTagRequest,
                data.model_dump(by_alias=True, exclude_none=True),
                {"flow_tag.id": flowTagid},
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_1.UpdateFlowTag,
                _req,
                api_config=api_config_override,
                error_cls=RestFlowTagModule1.UpdateFlowTagError,
            )
            return attach_rate_limit(
                rest_models.UpdateFlowTagResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestFlowTagModule1.UpdateFlowTag(
                api_config_override=api_config_override or rest_transport.api_config,
                flowTagid=flowTagid,
                data=data,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def delete_flow_tag(
        self, *, api_config_override: Optional[APIConfig] = None, flowTagid: str
    ) -> rest_models.DeleteFlowTagResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_1 is None or self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for flow_tag service"
                )
            _req = build_grpc_request(
                self._grpc_pb2_1.DeleteFlowTagRequest, None, {"id": flowTagid}
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_1.DeleteFlowTag,
                _req,
                api_config=api_config_override,
                error_cls=RestFlowTagModule1.DeleteFlowTagError,
            )
            return attach_rate_limit(
                rest_models.DeleteFlowTagResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestFlowTagModule1.DeleteFlowTag(
                api_config_override=api_config_override or rest_transport.api_config,
                flowTagid=flowTagid,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )
