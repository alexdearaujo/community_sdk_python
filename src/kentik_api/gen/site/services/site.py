from typing import Optional, Union, cast

from google.protobuf.json_format import MessageToDict

import kentik_api.gen.site.services.SiteService as RestSiteModule1
from kentik_api.core.api_config import APIConfig
from kentik_api.core.grpc_runtime import build_grpc_request, call_grpc
from kentik_api.core.rate_limit import attach_rate_limit
from kentik_api.gen.site import models as rest_models
from kentik_api.transports.grpc_client import GrpcTransport
from kentik_api.transports.rest_client import RestTransport


class SiteServiceWrapper:
    """AUTO-GENERATED: scripts/generation/wrapper_generation.py, _generate_service_wrappers().
    Rebuilt on every `make generate`. Do not edit by hand.
    Unified Service routing to either gRPC or REST.
    """

    def __init__(self, transport: Union[GrpcTransport, RestTransport]):
        self._transport = transport
        if isinstance(self._transport, GrpcTransport):
            try:
                __import__("kentik_api.gen.pb_companions")
                import kentik_api.gen.site.pb.site_pb2 as _pb2_1_mod
                import kentik_api.gen.site.pb.site_pb2_grpc as _pb2_grpc_1_mod

                self._grpc_pb2_1 = _pb2_1_mod
                self._grpc_stub_1 = _pb2_grpc_1_mod.SiteServiceStub(
                    self._transport.channel
                )
            except (ImportError, TypeError) as exc:
                self._grpc_pb2_1 = None
                self._grpc_stub_1 = None
                self._grpc_import_error_1 = exc

    def list_markets(
        self, *, api_config_override: Optional[APIConfig] = None
    ) -> rest_models.ListSiteMarketsResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_1 is None or self._grpc_stub_1 is None:
                raise NotImplementedError(
                    f"gRPC proto modules for site service failed to import: {self._grpc_import_error_1!r}"
                ) from self._grpc_import_error_1
            _req = build_grpc_request(self._grpc_pb2_1.ListSiteMarketsRequest, None, {})
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_1.ListSiteMarkets,
                _req,
                api_config=api_config_override,
                error_cls=RestSiteModule1.ListSiteMarketsError,
            )
            return attach_rate_limit(
                rest_models.ListSiteMarketsResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestSiteModule1.ListSiteMarkets(
                api_config_override=api_config_override or rest_transport.api_config
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def create_market(
        self,
        *,
        api_config_override: Optional[APIConfig] = None,
        data: rest_models.CreateSiteMarketRequest,
    ) -> rest_models.CreateSiteMarketResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_1 is None or self._grpc_stub_1 is None:
                raise NotImplementedError(
                    f"gRPC proto modules for site service failed to import: {self._grpc_import_error_1!r}"
                ) from self._grpc_import_error_1
            _req = build_grpc_request(
                self._grpc_pb2_1.CreateSiteMarketRequest,
                data.model_dump(by_alias=True, exclude_unset=True),
                {},
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_1.CreateSiteMarket,
                _req,
                api_config=api_config_override,
                error_cls=RestSiteModule1.CreateSiteMarketError,
            )
            return attach_rate_limit(
                rest_models.CreateSiteMarketResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestSiteModule1.CreateSiteMarket(
                api_config_override=api_config_override or rest_transport.api_config,
                data=data,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def get_market(
        self, *, api_config_override: Optional[APIConfig] = None, id: str
    ) -> rest_models.GetSiteMarketResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_1 is None or self._grpc_stub_1 is None:
                raise NotImplementedError(
                    f"gRPC proto modules for site service failed to import: {self._grpc_import_error_1!r}"
                ) from self._grpc_import_error_1
            _req = build_grpc_request(
                self._grpc_pb2_1.GetSiteMarketRequest, None, {"id": id}
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_1.GetSiteMarket,
                _req,
                api_config=api_config_override,
                error_cls=RestSiteModule1.GetSiteMarketError,
            )
            return attach_rate_limit(
                rest_models.GetSiteMarketResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestSiteModule1.GetSiteMarket(
                api_config_override=api_config_override or rest_transport.api_config,
                id=id,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def update_market(
        self,
        *,
        api_config_override: Optional[APIConfig] = None,
        id: str,
        data: rest_models.SiteServiceUpdateSiteMarketBody,
    ) -> rest_models.UpdateSiteMarketResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_1 is None or self._grpc_stub_1 is None:
                raise NotImplementedError(
                    f"gRPC proto modules for site service failed to import: {self._grpc_import_error_1!r}"
                ) from self._grpc_import_error_1
            _req = build_grpc_request(
                self._grpc_pb2_1.UpdateSiteMarketRequest,
                data.model_dump(by_alias=True, exclude_unset=True),
                {"site_market.id": id},
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_1.UpdateSiteMarket,
                _req,
                api_config=api_config_override,
                error_cls=RestSiteModule1.UpdateSiteMarketError,
            )
            return attach_rate_limit(
                rest_models.UpdateSiteMarketResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestSiteModule1.UpdateSiteMarket(
                api_config_override=api_config_override or rest_transport.api_config,
                id=id,
                data=data,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def delete_market(
        self, *, api_config_override: Optional[APIConfig] = None, id: str
    ) -> rest_models.DeleteSiteMarketResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_1 is None or self._grpc_stub_1 is None:
                raise NotImplementedError(
                    f"gRPC proto modules for site service failed to import: {self._grpc_import_error_1!r}"
                ) from self._grpc_import_error_1
            _req = build_grpc_request(
                self._grpc_pb2_1.DeleteSiteMarketRequest, None, {"id": id}
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_1.DeleteSiteMarket,
                _req,
                api_config=api_config_override,
                error_cls=RestSiteModule1.DeleteSiteMarketError,
            )
            return attach_rate_limit(
                rest_models.DeleteSiteMarketResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestSiteModule1.DeleteSiteMarket(
                api_config_override=api_config_override or rest_transport.api_config,
                id=id,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def list_sites(
        self, *, api_config_override: Optional[APIConfig] = None
    ) -> rest_models.ListSitesResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_1 is None or self._grpc_stub_1 is None:
                raise NotImplementedError(
                    f"gRPC proto modules for site service failed to import: {self._grpc_import_error_1!r}"
                ) from self._grpc_import_error_1
            _req = build_grpc_request(self._grpc_pb2_1.ListSitesRequest, None, {})
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_1.ListSites,
                _req,
                api_config=api_config_override,
                error_cls=RestSiteModule1.ListSitesError,
            )
            return attach_rate_limit(
                rest_models.ListSitesResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestSiteModule1.ListSites(
                api_config_override=api_config_override or rest_transport.api_config
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def create_site(
        self,
        *,
        api_config_override: Optional[APIConfig] = None,
        data: rest_models.CreateSiteRequest,
    ) -> rest_models.CreateSiteResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_1 is None or self._grpc_stub_1 is None:
                raise NotImplementedError(
                    f"gRPC proto modules for site service failed to import: {self._grpc_import_error_1!r}"
                ) from self._grpc_import_error_1
            _req = build_grpc_request(
                self._grpc_pb2_1.CreateSiteRequest,
                data.model_dump(by_alias=True, exclude_unset=True),
                {},
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_1.CreateSite,
                _req,
                api_config=api_config_override,
                error_cls=RestSiteModule1.CreateSiteError,
            )
            return attach_rate_limit(
                rest_models.CreateSiteResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestSiteModule1.CreateSite(
                api_config_override=api_config_override or rest_transport.api_config,
                data=data,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def get_site(
        self, *, api_config_override: Optional[APIConfig] = None, id: str
    ) -> rest_models.GetSiteResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_1 is None or self._grpc_stub_1 is None:
                raise NotImplementedError(
                    f"gRPC proto modules for site service failed to import: {self._grpc_import_error_1!r}"
                ) from self._grpc_import_error_1
            _req = build_grpc_request(self._grpc_pb2_1.GetSiteRequest, None, {"id": id})
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_1.GetSite,
                _req,
                api_config=api_config_override,
                error_cls=RestSiteModule1.GetSiteError,
            )
            return attach_rate_limit(
                rest_models.GetSiteResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestSiteModule1.GetSite(
                api_config_override=api_config_override or rest_transport.api_config,
                id=id,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def update_site(
        self,
        *,
        api_config_override: Optional[APIConfig] = None,
        id: str,
        data: rest_models.SiteServiceUpdateSiteBody,
    ) -> rest_models.UpdateSiteResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_1 is None or self._grpc_stub_1 is None:
                raise NotImplementedError(
                    f"gRPC proto modules for site service failed to import: {self._grpc_import_error_1!r}"
                ) from self._grpc_import_error_1
            _req = build_grpc_request(
                self._grpc_pb2_1.UpdateSiteRequest,
                data.model_dump(by_alias=True, exclude_unset=True),
                {"site.id": id},
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_1.UpdateSite,
                _req,
                api_config=api_config_override,
                error_cls=RestSiteModule1.UpdateSiteError,
            )
            return attach_rate_limit(
                rest_models.UpdateSiteResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestSiteModule1.UpdateSite(
                api_config_override=api_config_override or rest_transport.api_config,
                id=id,
                data=data,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def delete_site(
        self, *, api_config_override: Optional[APIConfig] = None, id: str
    ) -> rest_models.DeleteSiteResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_1 is None or self._grpc_stub_1 is None:
                raise NotImplementedError(
                    f"gRPC proto modules for site service failed to import: {self._grpc_import_error_1!r}"
                ) from self._grpc_import_error_1
            _req = build_grpc_request(
                self._grpc_pb2_1.DeleteSiteRequest, None, {"id": id}
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_1.DeleteSite,
                _req,
                api_config=api_config_override,
                error_cls=RestSiteModule1.DeleteSiteError,
            )
            return attach_rate_limit(
                rest_models.DeleteSiteResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestSiteModule1.DeleteSite(
                api_config_override=api_config_override or rest_transport.api_config,
                id=id,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )
