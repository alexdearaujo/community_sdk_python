from typing import Optional, Union, cast

from google.protobuf.json_format import MessageToDict, ParseDict

import kentik_api.gen.custom_dimension.services.CustomDimensionService as RestCustomDimensionModule1
from kentik_api.core.grpc_runtime import call_grpc
from kentik_api.gen.custom_dimension import models as rest_models
from kentik_api.transports.grpc_client import GrpcTransport
from kentik_api.transports.rest_client import RestTransport


class CustomDimensionServiceWrapper:
    """Unified Service routing to either gRPC or REST."""

    def __init__(self, transport: Union[GrpcTransport, RestTransport]):
        self._transport = transport
        if isinstance(self._transport, GrpcTransport):
            try:
                import kentik_api.gen.custom_dimension.pb.custom_dimension_pb2 as _pb2_1_mod
                import kentik_api.gen.custom_dimension.pb.custom_dimension_pb2_grpc as _pb2_grpc_1_mod

                self._grpc_pb2_1 = _pb2_1_mod
                self._grpc_stub_1 = _pb2_grpc_1_mod.CustomDimensionServiceStub(
                    self._transport.channel
                )
            except (ImportError, TypeError):
                self._grpc_pb2_1 = None
                self._grpc_stub_1 = None

    def list_custom_dimensions(
        self,
    ) -> rest_models.ListCustomDimensionsResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for custom_dimension service"
                )
            _req = self._grpc_pb2_1.ListCustomDimensionsRequest()
            _resp = call_grpc(self._grpc_stub_1.ListCustomDimensions, _req)
            return rest_models.ListCustomDimensionsResponse.model_validate(
                MessageToDict(_resp)
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
            if self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for custom_dimension service"
                )
            _req = ParseDict(
                {
                    k: v
                    for k, v in {"customDimensionId": customDimensionId}.items()
                    if v is not None
                },
                self._grpc_pb2_1.GetCustomDimensionInfoRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_1.GetCustomDimensionInfo, _req)
            return rest_models.GetCustomDimensionInfoResponse.model_validate(
                MessageToDict(_resp)
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
            if self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for custom_dimension service"
                )
            _req = ParseDict(
                {
                    k: v
                    for k, v in {"customDimensionId": customDimensionId}.items()
                    if v is not None
                },
                self._grpc_pb2_1.UpdateCustomDimensionRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_1.UpdateCustomDimension, _req)
            return rest_models.UpdateCustomDimensionResponse.model_validate(
                MessageToDict(_resp)
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
            if self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for custom_dimension service"
                )
            _req = ParseDict(
                {
                    k: v
                    for k, v in {"customDimensionId": customDimensionId}.items()
                    if v is not None
                },
                self._grpc_pb2_1.DeleteCustomDimensionRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_1.DeleteCustomDimension, _req)
            return rest_models.DeleteCustomDimensionResponse.model_validate(
                MessageToDict(_resp)
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
            if self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for custom_dimension service"
                )
            _req = ParseDict(
                {
                    k: v
                    for k, v in {"customDimensionId": customDimensionId}.items()
                    if v is not None
                },
                self._grpc_pb2_1.CreatePopulatorRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_1.CreatePopulator, _req)
            return rest_models.CreatePopulatorResponse.model_validate(
                MessageToDict(_resp)
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
            if self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for custom_dimension service"
                )
            _req = ParseDict(
                {
                    k: v
                    for k, v in {
                        "customDimensionId": customDimensionId,
                        "populatorId": populatorId,
                        "fieldLimit": fieldLimit,
                    }.items()
                    if v is not None
                },
                self._grpc_pb2_1.GetPopulatorRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_1.GetPopulator, _req)
            return rest_models.GetPopulatorResponse.model_validate(MessageToDict(_resp))
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
            if self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for custom_dimension service"
                )
            _req = ParseDict(
                {
                    k: v
                    for k, v in {
                        "customDimensionId": customDimensionId,
                        "populatorId": populatorId,
                    }.items()
                    if v is not None
                },
                self._grpc_pb2_1.UpdatePopulatorRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_1.UpdatePopulator, _req)
            return rest_models.UpdatePopulatorResponse.model_validate(
                MessageToDict(_resp)
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
            if self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for custom_dimension service"
                )
            _req = ParseDict(
                {
                    k: v
                    for k, v in {
                        "customDimensionId": customDimensionId,
                        "populatorId": populatorId,
                    }.items()
                    if v is not None
                },
                self._grpc_pb2_1.DeletePopulatorRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_1.DeletePopulator, _req)
            return rest_models.DeletePopulatorResponse.model_validate(
                MessageToDict(_resp)
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
            if self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for custom_dimension service"
                )
            _req = ParseDict(
                {
                    k: v
                    for k, v in {
                        "customDimensionId": customDimensionId,
                        "populatorId": populatorId,
                        "fieldName": fieldName,
                        "offset": offset,
                        "limit": limit,
                    }.items()
                    if v is not None
                },
                self._grpc_pb2_1.GetPopulatorFieldRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_1.GetPopulatorField, _req)
            return rest_models.GetPopulatorFieldResponse.model_validate(
                MessageToDict(_resp)
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
            if self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for custom_dimension service"
                )
            _req = self._grpc_pb2_1.CreateCustomDimensionRequest()
            _resp = call_grpc(self._grpc_stub_1.CreateCustomDimension, _req)
            return rest_models.CreateCustomDimensionResponse.model_validate(
                MessageToDict(_resp)
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
