from typing import Optional, Union, cast

from google.protobuf.json_format import MessageToDict

import kentik_api.gen.label.services.LabelService as RestLabelModule1
from kentik_api.core.api_config import APIConfig
from kentik_api.core.grpc_runtime import build_grpc_request, call_grpc
from kentik_api.core.rate_limit import attach_rate_limit
from kentik_api.gen.label import models as rest_models
from kentik_api.transports.grpc_client import GrpcTransport
from kentik_api.transports.rest_client import RestTransport


class LabelServiceWrapper:
    """AUTO-GENERATED: scripts/generation/wrapper_generation.py, _generate_service_wrappers().
    Rebuilt on every `make generate`. Do not edit by hand.
    Unified Service routing to either gRPC or REST.
    """

    def __init__(self, transport: Union[GrpcTransport, RestTransport]):
        self._transport = transport
        if isinstance(self._transport, GrpcTransport):
            try:
                __import__("kentik_api.gen.pb_companions")
                import kentik_api.gen.label.pb.label_pb2 as _pb2_1_mod
                import kentik_api.gen.label.pb.label_pb2_grpc as _pb2_grpc_1_mod

                self._grpc_pb2_1 = _pb2_1_mod
                self._grpc_stub_1 = _pb2_grpc_1_mod.LabelServiceStub(
                    self._transport.channel
                )
            except (ImportError, TypeError) as exc:
                self._grpc_pb2_1 = None
                self._grpc_stub_1 = None
                self._grpc_import_error_1 = exc

    def list_labels(
        self, *, api_config_override: Optional[APIConfig] = None
    ) -> rest_models.ListLabelsResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_1 is None or self._grpc_stub_1 is None:
                raise NotImplementedError(
                    f"gRPC proto modules for label service failed to import: {self._grpc_import_error_1!r}"
                ) from self._grpc_import_error_1
            _req = build_grpc_request(self._grpc_pb2_1.ListLabelsRequest, None, {})
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_1.ListLabels,
                _req,
                api_config=api_config_override,
                error_cls=RestLabelModule1.ListLabelsError,
            )
            return attach_rate_limit(
                rest_models.ListLabelsResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestLabelModule1.ListLabels(
                api_config_override=api_config_override or rest_transport.api_config
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def create_label(
        self,
        *,
        api_config_override: Optional[APIConfig] = None,
        data: rest_models.CreateLabelRequest,
    ) -> rest_models.CreateLabelResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_1 is None or self._grpc_stub_1 is None:
                raise NotImplementedError(
                    f"gRPC proto modules for label service failed to import: {self._grpc_import_error_1!r}"
                ) from self._grpc_import_error_1
            _req = build_grpc_request(
                self._grpc_pb2_1.CreateLabelRequest,
                data.model_dump(by_alias=True, exclude_unset=True),
                {},
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_1.CreateLabel,
                _req,
                api_config=api_config_override,
                error_cls=RestLabelModule1.CreateLabelError,
            )
            return attach_rate_limit(
                rest_models.CreateLabelResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestLabelModule1.CreateLabel(
                api_config_override=api_config_override or rest_transport.api_config,
                data=data,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def update_label(
        self,
        *,
        api_config_override: Optional[APIConfig] = None,
        id: str,
        data: rest_models.LabelServiceUpdateLabelBody,
    ) -> rest_models.UpdateLabelResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_1 is None or self._grpc_stub_1 is None:
                raise NotImplementedError(
                    f"gRPC proto modules for label service failed to import: {self._grpc_import_error_1!r}"
                ) from self._grpc_import_error_1
            _req = build_grpc_request(
                self._grpc_pb2_1.UpdateLabelRequest,
                data.model_dump(by_alias=True, exclude_unset=True),
                {"label.id": id},
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_1.UpdateLabel,
                _req,
                api_config=api_config_override,
                error_cls=RestLabelModule1.UpdateLabelError,
            )
            return attach_rate_limit(
                rest_models.UpdateLabelResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestLabelModule1.UpdateLabel(
                api_config_override=api_config_override or rest_transport.api_config,
                id=id,
                data=data,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def delete_label(
        self, *, api_config_override: Optional[APIConfig] = None, id: str
    ) -> rest_models.DeleteLabelResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_1 is None or self._grpc_stub_1 is None:
                raise NotImplementedError(
                    f"gRPC proto modules for label service failed to import: {self._grpc_import_error_1!r}"
                ) from self._grpc_import_error_1
            _req = build_grpc_request(
                self._grpc_pb2_1.DeleteLabelRequest, None, {"id": id}
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_1.DeleteLabel,
                _req,
                api_config=api_config_override,
                error_cls=RestLabelModule1.DeleteLabelError,
            )
            return attach_rate_limit(
                rest_models.DeleteLabelResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestLabelModule1.DeleteLabel(
                api_config_override=api_config_override or rest_transport.api_config,
                id=id,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )
