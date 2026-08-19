from typing import Union, cast

from google.protobuf.json_format import MessageToDict, ParseDict

import kentik_api.gen.cloud_export.services.CloudExportAdminService as RestCloudExportModule1
from kentik_api.core.grpc_runtime import call_grpc
from kentik_api.gen.cloud_export import models as rest_models
from kentik_api.transports.grpc_client import GrpcTransport
from kentik_api.transports.rest_client import RestTransport


class CloudExportServiceWrapper:
    """Unified Service routing to either gRPC or REST."""

    def __init__(self, transport: Union[GrpcTransport, RestTransport]):
        self._transport = transport
        if isinstance(self._transport, GrpcTransport):
            try:
                __import__("kentik_api.gen.pb_companions")
                import kentik_api.gen.cloud_export.pb.cloud_export_pb2 as _pb2_1_mod
                import kentik_api.gen.cloud_export.pb.cloud_export_pb2_grpc as _pb2_grpc_1_mod

                self._grpc_pb2_1 = _pb2_1_mod
                self._grpc_stub_1 = _pb2_grpc_1_mod.CloudExportAdminServiceStub(
                    self._transport.channel
                )
            except (ImportError, TypeError):
                self._grpc_pb2_1 = None
                self._grpc_stub_1 = None

    def list_cloud_exports(
        self,
    ) -> rest_models.ListCloudExportsResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for cloud_export service"
                )
            _req = self._grpc_pb2_1.ListCloudExportsRequest()
            _resp = call_grpc(self._grpc_stub_1.ListCloudExports, _req)
            return rest_models.ListCloudExportsResponse.model_validate(
                MessageToDict(_resp)
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
            if self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for cloud_export service"
                )
            _req = ParseDict(
                data.model_dump(by_alias=True, exclude_none=True),
                self._grpc_pb2_1.CreateCloudExportRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_1.CreateCloudExport, _req)
            return rest_models.CreateCloudExportResponse.model_validate(
                MessageToDict(_resp)
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
            if self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for cloud_export service"
                )
            _req = ParseDict(
                {k: v for k, v in {"exportid": exportid}.items() if v is not None},
                self._grpc_pb2_1.GetCloudExportRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_1.GetCloudExport, _req)
            return rest_models.GetCloudExportResponse.model_validate(
                MessageToDict(_resp)
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
            if self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for cloud_export service"
                )
            _req_dict = data.model_dump(by_alias=True, exclude_none=True)
            _req_dict.update(
                {k: v for k, v in {"exportid": exportid}.items() if v is not None}
            )
            _req = ParseDict(
                _req_dict,
                self._grpc_pb2_1.UpdateCloudExportRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_1.UpdateCloudExport, _req)
            return rest_models.UpdateCloudExportResponse.model_validate(
                MessageToDict(_resp)
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
            if self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for cloud_export service"
                )
            _req = ParseDict(
                {k: v for k, v in {"exportid": exportid}.items() if v is not None},
                self._grpc_pb2_1.DeleteCloudExportRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_1.DeleteCloudExport, _req)
            return rest_models.DeleteCloudExportResponse.model_validate(
                MessageToDict(_resp)
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
