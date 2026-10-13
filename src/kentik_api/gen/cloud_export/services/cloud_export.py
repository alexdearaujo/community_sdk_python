from typing import Optional, Union, cast

from google.protobuf.json_format import MessageToDict

import kentik_api.gen.cloud_export.services.CloudExportAdminService as RestCloudExportModule1
from kentik_api.core.api_config import APIConfig
from kentik_api.core.grpc_runtime import build_grpc_request, call_grpc
from kentik_api.core.rate_limit import attach_rate_limit
from kentik_api.gen.cloud_export import models as rest_models
from kentik_api.transports.grpc_client import GrpcTransport
from kentik_api.transports.rest_client import RestTransport


class CloudExportServiceWrapper:
    """AUTO-GENERATED: scripts/generation/wrapper_generation.py, _generate_service_wrappers().
    Rebuilt on every `make generate`. Do not edit by hand.
    Unified Service routing to either gRPC or REST.
    """

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
        self, *, api_config_override: Optional[APIConfig] = None
    ) -> rest_models.ListCloudExportsResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_1 is None or self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for cloud_export service"
                )
            _req = build_grpc_request(
                self._grpc_pb2_1.ListCloudExportsRequest, None, {}
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_1.ListCloudExports,
                _req,
                api_config=api_config_override,
                error_cls=RestCloudExportModule1.ListCloudExportsError,
            )
            return attach_rate_limit(
                rest_models.ListCloudExportsResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestCloudExportModule1.ListCloudExports(
                api_config_override=api_config_override or rest_transport.api_config
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def create_cloud_export(
        self,
        *,
        api_config_override: Optional[APIConfig] = None,
        data: rest_models.CreateCloudExportRequest,
    ) -> rest_models.CreateCloudExportResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_1 is None or self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for cloud_export service"
                )
            _req = build_grpc_request(
                self._grpc_pb2_1.CreateCloudExportRequest,
                data.model_dump(by_alias=True, exclude_unset=True),
                {},
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_1.CreateCloudExport,
                _req,
                api_config=api_config_override,
                error_cls=RestCloudExportModule1.CreateCloudExportError,
            )
            return attach_rate_limit(
                rest_models.CreateCloudExportResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestCloudExportModule1.CreateCloudExport(
                api_config_override=api_config_override or rest_transport.api_config,
                data=data,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def get_cloud_export(
        self, *, api_config_override: Optional[APIConfig] = None, exportid: str
    ) -> rest_models.GetCloudExportResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_1 is None or self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for cloud_export service"
                )
            _req = build_grpc_request(
                self._grpc_pb2_1.GetCloudExportRequest, None, {"id": exportid}
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_1.GetCloudExport,
                _req,
                api_config=api_config_override,
                error_cls=RestCloudExportModule1.GetCloudExportError,
            )
            return attach_rate_limit(
                rest_models.GetCloudExportResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestCloudExportModule1.GetCloudExport(
                api_config_override=api_config_override or rest_transport.api_config,
                exportid=exportid,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def update_cloud_export(
        self,
        *,
        api_config_override: Optional[APIConfig] = None,
        exportid: str,
        data: rest_models.CloudExportAdminServiceUpdateCloudExportBody,
    ) -> rest_models.UpdateCloudExportResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_1 is None or self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for cloud_export service"
                )
            _req = build_grpc_request(
                self._grpc_pb2_1.UpdateCloudExportRequest,
                data.model_dump(by_alias=True, exclude_unset=True),
                {"export.id": exportid},
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_1.UpdateCloudExport,
                _req,
                api_config=api_config_override,
                error_cls=RestCloudExportModule1.UpdateCloudExportError,
            )
            return attach_rate_limit(
                rest_models.UpdateCloudExportResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestCloudExportModule1.UpdateCloudExport(
                api_config_override=api_config_override or rest_transport.api_config,
                exportid=exportid,
                data=data,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def delete_cloud_export(
        self, *, api_config_override: Optional[APIConfig] = None, exportid: str
    ) -> rest_models.DeleteCloudExportResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_1 is None or self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for cloud_export service"
                )
            _req = build_grpc_request(
                self._grpc_pb2_1.DeleteCloudExportRequest, None, {"id": exportid}
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_1.DeleteCloudExport,
                _req,
                api_config=api_config_override,
                error_cls=RestCloudExportModule1.DeleteCloudExportError,
            )
            return attach_rate_limit(
                rest_models.DeleteCloudExportResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestCloudExportModule1.DeleteCloudExport(
                api_config_override=api_config_override or rest_transport.api_config,
                exportid=exportid,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )
