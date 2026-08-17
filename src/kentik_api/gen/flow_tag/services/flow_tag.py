from typing import List, Optional, Union, cast

import kentik_api.gen.flow_tag.services.FlowTagService as RestFlowTagModule1
from kentik_api.gen.flow_tag import models as rest_models
from kentik_api.transports.grpc_client import GrpcTransport
from kentik_api.transports.rest_client import RestTransport


class FlowTagServiceWrapper:
    """Unified Service routing to either gRPC or REST."""

    def __init__(self, transport: Union[GrpcTransport, RestTransport]):
        self._transport = transport
        if isinstance(self._transport, GrpcTransport):
            pass  # TODO: Initialize gRPC stub here

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
            raise NotImplementedError(
                "gRPC translation for SearchFlowTag is not yet implemented."
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
            raise NotImplementedError(
                "gRPC translation for CreateFlowTag is not yet implemented."
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
            raise NotImplementedError(
                "gRPC translation for GetFlowTag is not yet implemented."
            )
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
            raise NotImplementedError(
                "gRPC translation for UpdateFlowTag is not yet implemented."
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
            raise NotImplementedError(
                "gRPC translation for DeleteFlowTag is not yet implemented."
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
