from typing import Optional, Union, cast

import kentik_api.gen.custom_dimension.services.CustomDimensionService as RestCustomDimensionModule1
from kentik_api.gen.custom_dimension import models as rest_models
from kentik_api.transports.grpc_client import GrpcTransport
from kentik_api.transports.rest_client import RestTransport


class CustomDimensionServiceWrapper:
    """Unified Service routing to either gRPC or REST."""

    def __init__(self, transport: Union[GrpcTransport, RestTransport]):
        self._transport = transport
        if isinstance(self._transport, GrpcTransport):
            pass  # TODO: Initialize gRPC stub here

    def list_custom_dimensions(
        self,
    ) -> rest_models.ListCustomDimensionsResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for ListCustomDimensions is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestCustomDimensionModule1.ListCustomDimensions(
                api_config_override=rest_transport.api_config
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def get_custom_dimension_info(
        self, *, customDimensionId: str
    ) -> rest_models.GetCustomDimensionInfoResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for GetCustomDimensionInfo is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestCustomDimensionModule1.GetCustomDimensionInfo(
                api_config_override=rest_transport.api_config,
                customDimensionId=customDimensionId,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def update_custom_dimension(
        self, *, customDimensionId: str
    ) -> rest_models.UpdateCustomDimensionResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for UpdateCustomDimension is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestCustomDimensionModule1.UpdateCustomDimension(
                api_config_override=rest_transport.api_config,
                customDimensionId=customDimensionId,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def delete_custom_dimension(
        self, *, customDimensionId: str
    ) -> rest_models.DeleteCustomDimensionResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for DeleteCustomDimension is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestCustomDimensionModule1.DeleteCustomDimension(
                api_config_override=rest_transport.api_config,
                customDimensionId=customDimensionId,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def create_populator(
        self, *, customDimensionId: str
    ) -> rest_models.CreatePopulatorResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for CreatePopulator is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestCustomDimensionModule1.CreatePopulator(
                api_config_override=rest_transport.api_config,
                customDimensionId=customDimensionId,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def get_populator(
        self,
        *,
        customDimensionId: str,
        populatorId: str,
        fieldLimit: Optional[int] = None,
    ) -> rest_models.GetPopulatorResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for GetPopulator is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestCustomDimensionModule1.GetPopulator(
                api_config_override=rest_transport.api_config,
                customDimensionId=customDimensionId,
                populatorId=populatorId,
                fieldLimit=fieldLimit,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def update_populator(
        self,
        *,
        customDimensionId: str,
        populatorId: str,
    ) -> rest_models.UpdatePopulatorResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for UpdatePopulator is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestCustomDimensionModule1.UpdatePopulator(
                api_config_override=rest_transport.api_config,
                customDimensionId=customDimensionId,
                populatorId=populatorId,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def delete_populator(
        self,
        *,
        customDimensionId: str,
        populatorId: str,
    ) -> rest_models.DeletePopulatorResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for DeletePopulator is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestCustomDimensionModule1.DeletePopulator(
                api_config_override=rest_transport.api_config,
                customDimensionId=customDimensionId,
                populatorId=populatorId,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def get_populator_field(
        self,
        *,
        customDimensionId: str,
        populatorId: str,
        fieldName: str,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
    ) -> rest_models.GetPopulatorFieldResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for GetPopulatorField is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestCustomDimensionModule1.GetPopulatorField(
                api_config_override=rest_transport.api_config,
                customDimensionId=customDimensionId,
                populatorId=populatorId,
                fieldName=fieldName,
                offset=offset,
                limit=limit,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def create_custom_dimension(
        self,
    ) -> rest_models.CreateCustomDimensionResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for CreateCustomDimension is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestCustomDimensionModule1.CreateCustomDimension(
                api_config_override=rest_transport.api_config
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )
