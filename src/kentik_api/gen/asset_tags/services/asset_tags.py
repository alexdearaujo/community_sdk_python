from typing import Optional, Union, cast

from google.protobuf.json_format import MessageToDict

import kentik_api.gen.asset_tags.services.AssetTagsService as RestAssetTagsModule1
from kentik_api.core.api_config import APIConfig
from kentik_api.core.grpc_runtime import build_grpc_request, call_grpc
from kentik_api.core.rate_limit import attach_rate_limit
from kentik_api.gen.asset_tags import models as rest_models
from kentik_api.transports.grpc_client import GrpcTransport
from kentik_api.transports.rest_client import RestTransport


class AssetTagsServiceWrapper:
    """AUTO-GENERATED: scripts/generation/wrapper_generation.py, _generate_service_wrappers().
    Rebuilt on every `make generate`. Do not edit by hand.
    Unified Service routing to either gRPC or REST.
    """

    def __init__(self, transport: Union[GrpcTransport, RestTransport]):
        self._transport = transport
        if isinstance(self._transport, GrpcTransport):
            try:
                __import__("kentik_api.gen.pb_companions")
                import kentik_api.gen.asset_tags.pb.asset_tags_pb2 as _pb2_1_mod
                import kentik_api.gen.asset_tags.pb.asset_tags_pb2_grpc as _pb2_grpc_1_mod

                self._grpc_pb2_1 = _pb2_1_mod
                self._grpc_stub_1 = _pb2_grpc_1_mod.AssetTagsServiceStub(
                    self._transport.channel
                )
            except (ImportError, TypeError):
                self._grpc_pb2_1 = None
                self._grpc_stub_1 = None

    def get_tag_values(
        self,
        *,
        api_config_override: Optional[APIConfig] = None,
        assetType: str,
        assetId: str,
    ) -> rest_models.GetTagValuesResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_1 is None or self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for asset_tags service"
                )
            _req = build_grpc_request(
                self._grpc_pb2_1.GetTagValuesRequest,
                None,
                {"asset_type": assetType, "asset_id": assetId},
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_1.GetTagValues,
                _req,
                api_config=api_config_override,
                error_cls=RestAssetTagsModule1.GetTagValuesError,
            )
            return attach_rate_limit(
                rest_models.GetTagValuesResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestAssetTagsModule1.GetTagValues(
                api_config_override=api_config_override or rest_transport.api_config,
                assetType=assetType,
                assetId=assetId,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def list_tag_keys(
        self, *, api_config_override: Optional[APIConfig] = None
    ) -> rest_models.ListTagKeysResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_1 is None or self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for asset_tags service"
                )
            _req = build_grpc_request(self._grpc_pb2_1.ListTagKeysRequest, None, {})
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_1.ListTagKeys,
                _req,
                api_config=api_config_override,
                error_cls=RestAssetTagsModule1.ListTagKeysError,
            )
            return attach_rate_limit(
                rest_models.ListTagKeysResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestAssetTagsModule1.ListTagKeys(
                api_config_override=api_config_override or rest_transport.api_config
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def create_tag_key(
        self,
        *,
        api_config_override: Optional[APIConfig] = None,
        data: rest_models.CreateTagKeyRequest,
    ) -> rest_models.CreateTagKeyResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_1 is None or self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for asset_tags service"
                )
            _req = build_grpc_request(
                self._grpc_pb2_1.CreateTagKeyRequest,
                data.model_dump(by_alias=True, exclude_none=True),
                {},
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_1.CreateTagKey,
                _req,
                api_config=api_config_override,
                error_cls=RestAssetTagsModule1.CreateTagKeyError,
            )
            return attach_rate_limit(
                rest_models.CreateTagKeyResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestAssetTagsModule1.CreateTagKey(
                api_config_override=api_config_override or rest_transport.api_config,
                data=data,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def get_tag_key(
        self, *, api_config_override: Optional[APIConfig] = None, id: str
    ) -> rest_models.GetTagKeyResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_1 is None or self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for asset_tags service"
                )
            _req = build_grpc_request(
                self._grpc_pb2_1.GetTagKeyRequest, None, {"id": id}
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_1.GetTagKey,
                _req,
                api_config=api_config_override,
                error_cls=RestAssetTagsModule1.GetTagKeyError,
            )
            return attach_rate_limit(
                rest_models.GetTagKeyResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestAssetTagsModule1.GetTagKey(
                api_config_override=api_config_override or rest_transport.api_config,
                id=id,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def update_tag_key(
        self,
        *,
        api_config_override: Optional[APIConfig] = None,
        id: str,
        data: rest_models.AssetTagsServiceUpdateTagKeyBody,
    ) -> rest_models.UpdateTagKeyResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_1 is None or self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for asset_tags service"
                )
            _req = build_grpc_request(
                self._grpc_pb2_1.UpdateTagKeyRequest,
                data.model_dump(by_alias=True, exclude_none=True),
                {"id": id},
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_1.UpdateTagKey,
                _req,
                api_config=api_config_override,
                error_cls=RestAssetTagsModule1.UpdateTagKeyError,
            )
            return attach_rate_limit(
                rest_models.UpdateTagKeyResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestAssetTagsModule1.UpdateTagKey(
                api_config_override=api_config_override or rest_transport.api_config,
                id=id,
                data=data,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def delete_tag_key(
        self, *, api_config_override: Optional[APIConfig] = None, id: str
    ) -> rest_models.DeleteTagKeyResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_1 is None or self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for asset_tags service"
                )
            _req = build_grpc_request(
                self._grpc_pb2_1.DeleteTagKeyRequest, None, {"id": id}
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_1.DeleteTagKey,
                _req,
                api_config=api_config_override,
                error_cls=RestAssetTagsModule1.DeleteTagKeyError,
            )
            return attach_rate_limit(
                rest_models.DeleteTagKeyResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestAssetTagsModule1.DeleteTagKey(
                api_config_override=api_config_override or rest_transport.api_config,
                id=id,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def list_tag_values(
        self,
        *,
        api_config_override: Optional[APIConfig] = None,
        tagId: str,
        assetType: str,
    ) -> rest_models.ListTagValuesResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_1 is None or self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for asset_tags service"
                )
            _req = build_grpc_request(
                self._grpc_pb2_1.ListTagValuesRequest,
                None,
                {"tag_id": tagId, "asset_type": assetType},
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_1.ListTagValues,
                _req,
                api_config=api_config_override,
                error_cls=RestAssetTagsModule1.ListTagValuesError,
            )
            return attach_rate_limit(
                rest_models.ListTagValuesResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestAssetTagsModule1.ListTagValues(
                api_config_override=api_config_override or rest_transport.api_config,
                tagId=tagId,
                assetType=assetType,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def set_tag_values(
        self,
        *,
        api_config_override: Optional[APIConfig] = None,
        data: rest_models.SetTagValuesRequest,
    ) -> rest_models.SetTagValuesResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_1 is None or self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for asset_tags service"
                )
            _req = build_grpc_request(
                self._grpc_pb2_1.SetTagValuesRequest,
                data.model_dump(by_alias=True, exclude_none=True),
                {},
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_1.SetTagValues,
                _req,
                api_config=api_config_override,
                error_cls=RestAssetTagsModule1.SetTagValuesError,
            )
            return attach_rate_limit(
                rest_models.SetTagValuesResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestAssetTagsModule1.SetTagValues(
                api_config_override=api_config_override or rest_transport.api_config,
                data=data,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def delete_tag_values(
        self,
        *,
        api_config_override: Optional[APIConfig] = None,
        data: rest_models.DeleteTagValuesRequest,
    ) -> rest_models.DeleteTagValuesResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_1 is None or self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for asset_tags service"
                )
            _req = build_grpc_request(
                self._grpc_pb2_1.DeleteTagValuesRequest,
                data.model_dump(by_alias=True, exclude_none=True),
                {},
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_1.DeleteTagValues,
                _req,
                api_config=api_config_override,
                error_cls=RestAssetTagsModule1.DeleteTagValuesError,
            )
            return attach_rate_limit(
                rest_models.DeleteTagValuesResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestAssetTagsModule1.DeleteTagValues(
                api_config_override=api_config_override or rest_transport.api_config,
                data=data,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )
