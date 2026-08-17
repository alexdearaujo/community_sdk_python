from typing import Union, cast

import kentik_api.gen.custom_application.services.CustomApplicationService as RestCustomApplicationModule1
from kentik_api.gen.custom_application import models as rest_models
from kentik_api.transports.grpc_client import GrpcTransport
from kentik_api.transports.rest_client import RestTransport


class CustomApplicationServiceWrapper:
    """Unified Service routing to either gRPC or REST."""

    def __init__(self, transport: Union[GrpcTransport, RestTransport]):
        self._transport = transport
        if isinstance(self._transport, GrpcTransport):
            pass  # TODO: Initialize gRPC stub here

    def list_custom_applications(
        self,
    ) -> rest_models.ListCustomApplicationsResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for ListCustomApplications is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestCustomApplicationModule1.ListCustomApplications(
                api_config_override=rest_transport.api_config
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def create_custom_application(
        self,
    ) -> rest_models.CreateCustomApplicationResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for CreateCustomApplication is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestCustomApplicationModule1.CreateCustomApplication(
                api_config_override=rest_transport.api_config
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def get_custom_application(
        self, *, customApplicationId: str
    ) -> rest_models.GetCustomApplicationResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for GetCustomApplication is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestCustomApplicationModule1.GetCustomApplication(
                api_config_override=rest_transport.api_config,
                customApplicationId=customApplicationId,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def update_custom_application(
        self, *, customApplicationId: str
    ) -> rest_models.UpdateCustomApplicationResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for UpdateCustomApplication is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestCustomApplicationModule1.UpdateCustomApplication(
                api_config_override=rest_transport.api_config,
                customApplicationId=customApplicationId,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def delete_custom_application(
        self, *, customApplicationId: str
    ) -> rest_models.DeleteCustomApplicationResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for DeleteCustomApplication is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestCustomApplicationModule1.DeleteCustomApplication(
                api_config_override=rest_transport.api_config,
                customApplicationId=customApplicationId,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )
