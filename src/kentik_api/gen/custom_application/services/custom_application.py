from typing import Union, cast
from kentik_api.gen.custom_application import models as rest_models
import kentik_api.gen.custom_application.services.CustomApplicationService as RestCustomApplicationModule1
from kentik_api.transports.grpc_client import GrpcTransport
from kentik_api.transports.rest_client import RestTransport
from google.protobuf.json_format import MessageToDict, ParseDict
from kentik_api.core.grpc_runtime import call_grpc


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
        self,
    ) -> rest_models.ListCustomApplicationsResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for custom_application service"
                )
            _req = self._grpc_pb2_1.ListCustomApplicationsRequest()
            _resp = call_grpc(self._grpc_stub_1.ListCustomApplications, _req)
            return rest_models.ListCustomApplicationsResponse.model_validate(
                MessageToDict(_resp)
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestCustomApplicationModule1.ListCustomApplications(
                api_config_override=rest_transport.api_config
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def create_custom_application(
        self, *, data: rest_models.CustomApplication
    ) -> rest_models.CreateCustomApplicationResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for custom_application service"
                )
            _req = ParseDict(
                data.model_dump(by_alias=True, exclude_none=True),
                self._grpc_pb2_1.CreateCustomApplicationRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_1.CreateCustomApplication, _req)
            return rest_models.CreateCustomApplicationResponse.model_validate(
                MessageToDict(_resp)
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestCustomApplicationModule1.CreateCustomApplication(
                api_config_override=rest_transport.api_config, data=data
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def get_custom_application(
        self, *, customApplicationId: str
    ) -> rest_models.GetCustomApplicationResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for custom_application service"
                )
            _req = ParseDict(
                {
                    k: v
                    for k, v in {"customApplicationId": customApplicationId}.items()
                    if v is not None
                },
                self._grpc_pb2_1.GetCustomApplicationRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_1.GetCustomApplication, _req)
            return rest_models.GetCustomApplicationResponse.model_validate(
                MessageToDict(_resp)
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestCustomApplicationModule1.GetCustomApplication(
                api_config_override=rest_transport.api_config,
                customApplicationId=customApplicationId,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def update_custom_application(
        self, *, customApplicationId: str, data: rest_models.CustomApplication
    ) -> rest_models.UpdateCustomApplicationResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for custom_application service"
                )
            _req_dict = data.model_dump(by_alias=True, exclude_none=True)
            _req_dict.update(
                {
                    k: v
                    for k, v in {"customApplicationId": customApplicationId}.items()
                    if v is not None
                }
            )
            _req = ParseDict(
                _req_dict,
                self._grpc_pb2_1.UpdateCustomApplicationRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_1.UpdateCustomApplication, _req)
            return rest_models.UpdateCustomApplicationResponse.model_validate(
                MessageToDict(_resp)
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestCustomApplicationModule1.UpdateCustomApplication(
                api_config_override=rest_transport.api_config,
                customApplicationId=customApplicationId,
                data=data,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def delete_custom_application(
        self, *, customApplicationId: str
    ) -> rest_models.DeleteCustomApplicationResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for custom_application service"
                )
            _req = ParseDict(
                {
                    k: v
                    for k, v in {"customApplicationId": customApplicationId}.items()
                    if v is not None
                },
                self._grpc_pb2_1.DeleteCustomApplicationRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_1.DeleteCustomApplication, _req)
            return rest_models.DeleteCustomApplicationResponse.model_validate(
                MessageToDict(_resp)
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestCustomApplicationModule1.DeleteCustomApplication(
                api_config_override=rest_transport.api_config,
                customApplicationId=customApplicationId,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )
