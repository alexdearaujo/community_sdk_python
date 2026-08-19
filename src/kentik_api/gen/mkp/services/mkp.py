from typing import Union, cast

import kentik_api.gen.mkp.services.PackageService as RestMkpModule1
import kentik_api.gen.mkp.services.TenantService as RestMkpModule2
import kentik_api.gen.mkp.services.TenantUserService as RestMkpModule3
from kentik_api.gen.mkp import models as rest_models
from kentik_api.transports.grpc_client import GrpcTransport
from kentik_api.transports.rest_client import RestTransport


class MkpServiceWrapper:
    """Unified Service routing to either gRPC or REST."""

    def __init__(self, transport: Union[GrpcTransport, RestTransport]):
        self._transport = transport
        if isinstance(self._transport, GrpcTransport):
            try:
                __import__("kentik_api.gen.pb_companions")
                import kentik_api.gen.mkp.pb.mkp_pb2 as _pb2_1_mod
                import kentik_api.gen.mkp.pb.mkp_pb2_grpc as _pb2_grpc_1_mod

                self._grpc_pb2_1 = _pb2_1_mod
                self._grpc_stub_1 = _pb2_grpc_1_mod.PackageServiceStub(
                    self._transport.channel
                )
            except (ImportError, TypeError):
                self._grpc_pb2_1 = None
                self._grpc_stub_1 = None
            try:
                __import__("kentik_api.gen.pb_companions")
                import kentik_api.gen.mkp.pb.mkp_pb2 as _pb2_2_mod
                import kentik_api.gen.mkp.pb.mkp_pb2_grpc as _pb2_grpc_2_mod

                self._grpc_pb2_2 = _pb2_2_mod
                self._grpc_stub_2 = _pb2_grpc_2_mod.TenantServiceStub(
                    self._transport.channel
                )
            except (ImportError, TypeError):
                self._grpc_pb2_2 = None
                self._grpc_stub_2 = None
            try:
                __import__("kentik_api.gen.pb_companions")
                import kentik_api.gen.mkp.pb.mkp_pb2 as _pb2_3_mod
                import kentik_api.gen.mkp.pb.mkp_pb2_grpc as _pb2_grpc_3_mod

                self._grpc_pb2_3 = _pb2_3_mod
                self._grpc_stub_3 = _pb2_grpc_3_mod.TenantUserServiceStub(
                    self._transport.channel
                )
            except (ImportError, TypeError):
                self._grpc_pb2_3 = None
                self._grpc_stub_3 = None

    def package_list(
        self,
    ) -> rest_models.ListPackageResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for PackageList is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestMkpModule1.PackageList(
                api_config_override=rest_transport.api_config
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def package_create(
        self, *, data: rest_models.CreatePackageRequest
    ) -> rest_models.CreatePackageResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for PackageCreate is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestMkpModule1.PackageCreate(
                api_config_override=rest_transport.api_config, data=data
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def package_get(self, *, id: str) -> rest_models.GetPackageResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for PackageGet is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestMkpModule1.PackageGet(
                api_config_override=rest_transport.api_config, id=id
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def package_update(
        self,
        *,
        id: str,
        data: rest_models.PackageServiceUpdatePackageBody,
    ) -> rest_models.UpdatePackageResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for PackageUpdate is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestMkpModule1.PackageUpdate(
                api_config_override=rest_transport.api_config, id=id, data=data
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def package_delete(self, *, id: str) -> rest_models.DeletePackageResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for PackageDelete is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestMkpModule1.PackageDelete(
                api_config_override=rest_transport.api_config, id=id
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def tenant_list(
        self,
    ) -> rest_models.ListTenantResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for TenantList is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestMkpModule2.TenantList(
                api_config_override=rest_transport.api_config
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def tenant_create(
        self, *, data: rest_models.CreateTenantRequest
    ) -> rest_models.CreateTenantResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for TenantCreate is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestMkpModule2.TenantCreate(
                api_config_override=rest_transport.api_config, data=data
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def tenant_get(self, *, id: str) -> rest_models.GetTenantResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for TenantGet is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestMkpModule2.TenantGet(
                api_config_override=rest_transport.api_config, id=id
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def tenant_update(
        self,
        *,
        id: str,
        data: rest_models.TenantServiceUpdateTenantBody,
    ) -> rest_models.UpdateTenantResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for TenantUpdate is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestMkpModule2.TenantUpdate(
                api_config_override=rest_transport.api_config, id=id, data=data
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def tenant_delete(self, *, id: str) -> rest_models.DeleteTenantResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for TenantDelete is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestMkpModule2.TenantDelete(
                api_config_override=rest_transport.api_config, id=id
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def tenant_user_list(self, *, tenantId: str) -> rest_models.ListTenantUserResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for TenantUserList is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestMkpModule3.TenantUserList(
                api_config_override=rest_transport.api_config, tenantId=tenantId
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def tenant_user_create(
        self,
        *,
        tenantId: str,
        data: rest_models.TenantUserServiceCreateTenantUserBody,
    ) -> rest_models.CreateTenantUserResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for TenantUserCreate is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestMkpModule3.TenantUserCreate(
                api_config_override=rest_transport.api_config,
                tenantId=tenantId,
                data=data,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def tenant_user_update(
        self,
        *,
        tenantId: str,
        id: str,
        data: rest_models.TenantUserServiceUpdateTenantUserBody,
    ) -> rest_models.UpdateTenantUserResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for TenantUserUpdate is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestMkpModule3.TenantUserUpdate(
                api_config_override=rest_transport.api_config,
                tenantId=tenantId,
                id=id,
                data=data,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def tenant_user_delete(
        self, *, tenantId: str, id: str
    ) -> rest_models.DeleteTenantUserResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for TenantUserDelete is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestMkpModule3.TenantUserDelete(
                api_config_override=rest_transport.api_config, tenantId=tenantId, id=id
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )
