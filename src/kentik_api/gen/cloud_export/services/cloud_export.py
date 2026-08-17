from typing import Union, cast

import kentik_api.gen.cloud_export.services.CloudExportAdminService as RestCloudExportModule1
from kentik_api.gen.cloud_export import models as rest_models
from kentik_api.transports.grpc_client import GrpcTransport
from kentik_api.transports.rest_client import RestTransport


class CloudExportServiceWrapper:
    """Unified Service routing to either gRPC or REST."""

    def __init__(self, transport: Union[GrpcTransport, RestTransport]):
        self._transport = transport
        if isinstance(self._transport, GrpcTransport):
            pass  # TODO: Initialize gRPC stub here

    def list_cloud_exports(
        self,
    ) -> rest_models.ListCloudExportsResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for ListCloudExports is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestCloudExportModule1.ListCloudExports(
                api_config_override=rest_transport.api_config
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def create_cloud_export(
        self, *, data: rest_models.CreateCloudExportRequest
    ) -> rest_models.CreateCloudExportResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for CreateCloudExport is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestCloudExportModule1.CreateCloudExport(
                api_config_override=rest_transport.api_config, data=data
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def get_cloud_export(self, *, exportid: str) -> rest_models.GetCloudExportResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for GetCloudExport is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestCloudExportModule1.GetCloudExport(
                api_config_override=rest_transport.api_config, exportid=exportid
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def update_cloud_export(
        self,
        *,
        exportid: str,
        data: rest_models.CloudExportAdminServiceUpdateCloudExportBody,
    ) -> rest_models.UpdateCloudExportResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for UpdateCloudExport is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestCloudExportModule1.UpdateCloudExport(
                api_config_override=rest_transport.api_config,
                exportid=exportid,
                data=data,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def delete_cloud_export(
        self, *, exportid: str
    ) -> rest_models.DeleteCloudExportResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for DeleteCloudExport is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestCloudExportModule1.DeleteCloudExport(
                api_config_override=rest_transport.api_config, exportid=exportid
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )
