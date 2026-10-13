from typing import Optional, Union, cast

from google.protobuf.json_format import MessageToDict

import kentik_api.gen.custom_application.services.CustomApplicationService as RestCustomApplicationModule1
from kentik_api.core.api_config import APIConfig
from kentik_api.core.grpc_runtime import build_grpc_request, call_grpc
from kentik_api.core.rate_limit import attach_rate_limit
from kentik_api.gen.custom_application import models as rest_models
from kentik_api.transports.grpc_client import GrpcTransport
from kentik_api.transports.rest_client import RestTransport


class CustomApplicationServiceWrapper:
    """AUTO-GENERATED: scripts/generation/wrapper_generation.py, _generate_service_wrappers().
    Rebuilt on every `make generate`. Do not edit by hand.
    Unified Service routing to either gRPC or REST.
    """

    def __init__(self, transport: Union[GrpcTransport, RestTransport]):
        self._transport = transport
        if isinstance(self._transport, GrpcTransport):
            try:
                __import__("kentik_api.gen.pb_companions")
                import kentik_api.gen.custom_application.pb.custom_application_pb2 as _pb2_1_mod
                import kentik_api.gen.custom_application.pb.custom_application_pb2_grpc as _pb2_grpc_1_mod

                self._grpc_pb2_1 = _pb2_1_mod
                self._grpc_stub_1 = _pb2_grpc_1_mod.CustomApplicationServiceStub(
                    self._transport.channel
                )
            except (ImportError, TypeError):
                self._grpc_pb2_1 = None
                self._grpc_stub_1 = None

    def list_custom_applications(
        self, *, api_config_override: Optional[APIConfig] = None
    ) -> rest_models.ListCustomApplicationsResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_1 is None or self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for custom_application service"
                )
            _req = build_grpc_request(
                self._grpc_pb2_1.ListCustomApplicationsRequest, None, {}
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_1.ListCustomApplications,
                _req,
                api_config=api_config_override,
                error_cls=RestCustomApplicationModule1.ListCustomApplicationsError,
            )
            return attach_rate_limit(
                rest_models.ListCustomApplicationsResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestCustomApplicationModule1.ListCustomApplications(
                api_config_override=api_config_override or rest_transport.api_config
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def create_custom_application(
        self,
        *,
        api_config_override: Optional[APIConfig] = None,
        data: rest_models.CustomApplication,
    ) -> rest_models.CreateCustomApplicationResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_1 is None or self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for custom_application service"
                )
            _req = build_grpc_request(
                self._grpc_pb2_1.CreateCustomApplicationRequest,
                {"application": data.model_dump(by_alias=True, exclude_unset=True)},
                {},
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_1.CreateCustomApplication,
                _req,
                api_config=api_config_override,
                error_cls=RestCustomApplicationModule1.CreateCustomApplicationError,
            )
            return attach_rate_limit(
                rest_models.CreateCustomApplicationResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestCustomApplicationModule1.CreateCustomApplication(
                api_config_override=api_config_override or rest_transport.api_config,
                data=data,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def get_custom_application(
        self,
        *,
        api_config_override: Optional[APIConfig] = None,
        customApplicationId: str,
    ) -> rest_models.GetCustomApplicationResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_1 is None or self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for custom_application service"
                )
            _req = build_grpc_request(
                self._grpc_pb2_1.GetCustomApplicationRequest,
                None,
                {"custom_application_id": customApplicationId},
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_1.GetCustomApplication,
                _req,
                api_config=api_config_override,
                error_cls=RestCustomApplicationModule1.GetCustomApplicationError,
            )
            return attach_rate_limit(
                rest_models.GetCustomApplicationResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestCustomApplicationModule1.GetCustomApplication(
                api_config_override=api_config_override or rest_transport.api_config,
                customApplicationId=customApplicationId,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def update_custom_application(
        self,
        *,
        api_config_override: Optional[APIConfig] = None,
        customApplicationId: str,
        data: rest_models.CustomApplication,
    ) -> rest_models.UpdateCustomApplicationResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_1 is None or self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for custom_application service"
                )
            _req = build_grpc_request(
                self._grpc_pb2_1.UpdateCustomApplicationRequest,
                {"application": data.model_dump(by_alias=True, exclude_unset=True)},
                {"custom_application_id": customApplicationId},
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_1.UpdateCustomApplication,
                _req,
                api_config=api_config_override,
                error_cls=RestCustomApplicationModule1.UpdateCustomApplicationError,
            )
            return attach_rate_limit(
                rest_models.UpdateCustomApplicationResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestCustomApplicationModule1.UpdateCustomApplication(
                api_config_override=api_config_override or rest_transport.api_config,
                customApplicationId=customApplicationId,
                data=data,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def delete_custom_application(
        self,
        *,
        api_config_override: Optional[APIConfig] = None,
        customApplicationId: str,
    ) -> rest_models.DeleteCustomApplicationResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_1 is None or self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for custom_application service"
                )
            _req = build_grpc_request(
                self._grpc_pb2_1.DeleteCustomApplicationRequest,
                None,
                {"custom_application_id": customApplicationId},
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_1.DeleteCustomApplication,
                _req,
                api_config=api_config_override,
                error_cls=RestCustomApplicationModule1.DeleteCustomApplicationError,
            )
            return attach_rate_limit(
                rest_models.DeleteCustomApplicationResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestCustomApplicationModule1.DeleteCustomApplication(
                api_config_override=api_config_override or rest_transport.api_config,
                customApplicationId=customApplicationId,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )
