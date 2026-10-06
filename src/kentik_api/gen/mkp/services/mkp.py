from typing import Optional, Union, cast

from google.protobuf.json_format import MessageToDict

import kentik_api.gen.mkp.services.PackageService as RestMkpModule1
import kentik_api.gen.mkp.services.TenantService as RestMkpModule2
import kentik_api.gen.mkp.services.TenantUserService as RestMkpModule3
from kentik_api.core.api_config import APIConfig
from kentik_api.core.grpc_runtime import build_grpc_request, call_grpc
from kentik_api.core.rate_limit import attach_rate_limit
from kentik_api.gen.mkp import models as rest_models
from kentik_api.transports.grpc_client import GrpcTransport
from kentik_api.transports.rest_client import RestTransport


class MkpServiceWrapper:
    """AUTO-GENERATED: scripts/generation/wrapper_generation.py, _generate_service_wrappers().
    Rebuilt on every `make generate`. Do not edit by hand.
    Unified Service routing to either gRPC or REST.
    """

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
        self, *, api_config_override: Optional[APIConfig] = None
    ) -> rest_models.ListPackageResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_1 is None or self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for mkp service"
                )
            _req = build_grpc_request(self._grpc_pb2_1.ListPackageRequest, None, {})
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_1.ListPackage, _req, api_config=api_config_override
            )
            return attach_rate_limit(
                rest_models.ListPackageResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestMkpModule1.PackageList(
                api_config_override=api_config_override or rest_transport.api_config
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def package_create(
        self,
        *,
        api_config_override: Optional[APIConfig] = None,
        data: rest_models.CreatePackageRequest,
    ) -> rest_models.CreatePackageResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_1 is None or self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for mkp service"
                )
            _req = build_grpc_request(
                self._grpc_pb2_1.CreatePackageRequest,
                data.model_dump(by_alias=True, exclude_none=True),
                {},
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_1.CreatePackage, _req, api_config=api_config_override
            )
            return attach_rate_limit(
                rest_models.CreatePackageResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestMkpModule1.PackageCreate(
                api_config_override=api_config_override or rest_transport.api_config,
                data=data,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def package_get(
        self, *, api_config_override: Optional[APIConfig] = None, id: str
    ) -> rest_models.GetPackageResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_1 is None or self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for mkp service"
                )
            _req = build_grpc_request(
                self._grpc_pb2_1.GetPackageRequest, None, {"id": id}
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_1.GetPackage, _req, api_config=api_config_override
            )
            return attach_rate_limit(
                rest_models.GetPackageResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestMkpModule1.PackageGet(
                api_config_override=api_config_override or rest_transport.api_config,
                id=id,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def package_update(
        self,
        *,
        api_config_override: Optional[APIConfig] = None,
        id: str,
        data: rest_models.PackageServiceUpdatePackageBody,
    ) -> rest_models.UpdatePackageResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_1 is None or self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for mkp service"
                )
            _req = build_grpc_request(
                self._grpc_pb2_1.UpdatePackageRequest,
                data.model_dump(by_alias=True, exclude_none=True),
                {"package.id": id},
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_1.UpdatePackage, _req, api_config=api_config_override
            )
            return attach_rate_limit(
                rest_models.UpdatePackageResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestMkpModule1.PackageUpdate(
                api_config_override=api_config_override or rest_transport.api_config,
                id=id,
                data=data,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def package_delete(
        self, *, api_config_override: Optional[APIConfig] = None, id: str
    ) -> rest_models.DeletePackageResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_1 is None or self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for mkp service"
                )
            _req = build_grpc_request(
                self._grpc_pb2_1.DeletePackageRequest, None, {"id": id}
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_1.DeletePackage, _req, api_config=api_config_override
            )
            return attach_rate_limit(
                rest_models.DeletePackageResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestMkpModule1.PackageDelete(
                api_config_override=api_config_override or rest_transport.api_config,
                id=id,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def tenant_list(
        self, *, api_config_override: Optional[APIConfig] = None
    ) -> rest_models.ListTenantResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_2 is None or self._grpc_stub_2 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for mkp service"
                )
            _req = build_grpc_request(self._grpc_pb2_2.ListTenantRequest, None, {})
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_2.ListTenant, _req, api_config=api_config_override
            )
            return attach_rate_limit(
                rest_models.ListTenantResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestMkpModule2.TenantList(
                api_config_override=api_config_override or rest_transport.api_config
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def tenant_create(
        self,
        *,
        api_config_override: Optional[APIConfig] = None,
        data: rest_models.CreateTenantRequest,
    ) -> rest_models.CreateTenantResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_2 is None or self._grpc_stub_2 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for mkp service"
                )
            _req = build_grpc_request(
                self._grpc_pb2_2.CreateTenantRequest,
                data.model_dump(by_alias=True, exclude_none=True),
                {},
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_2.CreateTenant, _req, api_config=api_config_override
            )
            return attach_rate_limit(
                rest_models.CreateTenantResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestMkpModule2.TenantCreate(
                api_config_override=api_config_override or rest_transport.api_config,
                data=data,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def tenant_get(
        self, *, api_config_override: Optional[APIConfig] = None, id: str
    ) -> rest_models.GetTenantResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_2 is None or self._grpc_stub_2 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for mkp service"
                )
            _req = build_grpc_request(
                self._grpc_pb2_2.GetTenantRequest, None, {"id": id}
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_2.GetTenant, _req, api_config=api_config_override
            )
            return attach_rate_limit(
                rest_models.GetTenantResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestMkpModule2.TenantGet(
                api_config_override=api_config_override or rest_transport.api_config,
                id=id,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def tenant_update(
        self,
        *,
        api_config_override: Optional[APIConfig] = None,
        id: str,
        data: rest_models.TenantServiceUpdateTenantBody,
    ) -> rest_models.UpdateTenantResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_2 is None or self._grpc_stub_2 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for mkp service"
                )
            _req = build_grpc_request(
                self._grpc_pb2_2.UpdateTenantRequest,
                data.model_dump(by_alias=True, exclude_none=True),
                {"tenant.id": id},
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_2.UpdateTenant, _req, api_config=api_config_override
            )
            return attach_rate_limit(
                rest_models.UpdateTenantResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestMkpModule2.TenantUpdate(
                api_config_override=api_config_override or rest_transport.api_config,
                id=id,
                data=data,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def tenant_delete(
        self, *, api_config_override: Optional[APIConfig] = None, id: str
    ) -> rest_models.DeleteTenantResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_2 is None or self._grpc_stub_2 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for mkp service"
                )
            _req = build_grpc_request(
                self._grpc_pb2_2.DeleteTenantRequest, None, {"id": id}
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_2.DeleteTenant, _req, api_config=api_config_override
            )
            return attach_rate_limit(
                rest_models.DeleteTenantResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestMkpModule2.TenantDelete(
                api_config_override=api_config_override or rest_transport.api_config,
                id=id,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def tenant_user_list(
        self, *, api_config_override: Optional[APIConfig] = None, tenantId: str
    ) -> rest_models.ListTenantUserResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_3 is None or self._grpc_stub_3 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for mkp service"
                )
            _req = build_grpc_request(
                self._grpc_pb2_3.ListTenantUserRequest, None, {"tenant_id": tenantId}
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_3.ListTenantUser, _req, api_config=api_config_override
            )
            return attach_rate_limit(
                rest_models.ListTenantUserResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestMkpModule3.TenantUserList(
                api_config_override=api_config_override or rest_transport.api_config,
                tenantId=tenantId,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def tenant_user_create(
        self,
        *,
        api_config_override: Optional[APIConfig] = None,
        tenantId: str,
        data: rest_models.TenantUserServiceCreateTenantUserBody,
    ) -> rest_models.CreateTenantUserResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_3 is None or self._grpc_stub_3 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for mkp service"
                )
            _req = build_grpc_request(
                self._grpc_pb2_3.CreateTenantUserRequest,
                data.model_dump(by_alias=True, exclude_none=True),
                {"user.tenant_id": tenantId},
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_3.CreateTenantUser, _req, api_config=api_config_override
            )
            return attach_rate_limit(
                rest_models.CreateTenantUserResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestMkpModule3.TenantUserCreate(
                api_config_override=api_config_override or rest_transport.api_config,
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
        api_config_override: Optional[APIConfig] = None,
        tenantId: str,
        id: str,
        data: rest_models.TenantUserServiceUpdateTenantUserBody,
    ) -> rest_models.UpdateTenantUserResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_3 is None or self._grpc_stub_3 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for mkp service"
                )
            _req = build_grpc_request(
                self._grpc_pb2_3.UpdateTenantUserRequest,
                data.model_dump(by_alias=True, exclude_none=True),
                {"user.tenant_id": tenantId, "user.id": id},
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_3.UpdateTenantUser, _req, api_config=api_config_override
            )
            return attach_rate_limit(
                rest_models.UpdateTenantUserResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestMkpModule3.TenantUserUpdate(
                api_config_override=api_config_override or rest_transport.api_config,
                tenantId=tenantId,
                id=id,
                data=data,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def tenant_user_delete(
        self, *, api_config_override: Optional[APIConfig] = None, tenantId: str, id: str
    ) -> rest_models.DeleteTenantUserResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_3 is None or self._grpc_stub_3 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for mkp service"
                )
            _req = build_grpc_request(
                self._grpc_pb2_3.DeleteTenantUserRequest,
                None,
                {"tenant_id": tenantId, "id": id},
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_3.DeleteTenantUser, _req, api_config=api_config_override
            )
            return attach_rate_limit(
                rest_models.DeleteTenantUserResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestMkpModule3.TenantUserDelete(
                api_config_override=api_config_override or rest_transport.api_config,
                tenantId=tenantId,
                id=id,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )
