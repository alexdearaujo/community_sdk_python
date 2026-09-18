from typing import Union, cast

from google.protobuf.json_format import MessageToDict, ParseDict

import kentik_api.gen.kmeta.services.KmetaService as RestKmetaModule1
from kentik_api.core.grpc_runtime import call_grpc
from kentik_api.gen.kmeta import models as rest_models
from kentik_api.transports.grpc_client import GrpcTransport
from kentik_api.transports.rest_client import RestTransport


class KmetaServiceWrapper:
    """AUTO-GENERATED: scripts/generation/wrapper_generation.py, _generate_service_wrappers().
    Rebuilt on every `make generate`. Do not edit by hand.
    Unified Service routing to either gRPC or REST.
    """

    def __init__(self, transport: Union[GrpcTransport, RestTransport]):
        self._transport = transport
        if isinstance(self._transport, GrpcTransport):
            try:
                __import__("kentik_api.gen.pb_companions")
                import kentik_api.gen.kmeta.pb.kmeta_pb2 as _pb2_1_mod
                import kentik_api.gen.kmeta.pb.kmeta_pb2_grpc as _pb2_grpc_1_mod

                self._grpc_pb2_1 = _pb2_1_mod
                self._grpc_stub_1 = _pb2_grpc_1_mod.KmetaServiceStub(
                    self._transport.channel
                )
            except (ImportError, TypeError):
                self._grpc_pb2_1 = None
                self._grpc_stub_1 = None

    def list_service_now_configs(
        self, *, cid: str
    ) -> rest_models.ListServiceNowConfigsResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for kmeta service"
                )
            _req = ParseDict(
                {k: v for k, v in {"cid": cid}.items() if v is not None},
                self._grpc_pb2_1.ListServiceNowConfigsRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_1.ListServiceNowConfigs, _req)
            return rest_models.ListServiceNowConfigsResponse.model_validate(
                MessageToDict(_resp, always_print_fields_with_no_presence=True)
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestKmetaModule1.ListServiceNowConfigs(
                api_config_override=rest_transport.api_config, cid=cid
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def create_service_now_config(
        self, *, cid: str, data: rest_models.ServiceNowConfig
    ) -> rest_models.CreateServiceNowConfigResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for kmeta service"
                )
            _req_dict = data.model_dump(by_alias=True, exclude_none=True)
            _req_dict.update({k: v for k, v in {"cid": cid}.items() if v is not None})
            _req = ParseDict(
                _req_dict,
                self._grpc_pb2_1.CreateServiceNowConfigRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_1.CreateServiceNowConfig, _req)
            return rest_models.CreateServiceNowConfigResponse.model_validate(
                MessageToDict(_resp, always_print_fields_with_no_presence=True)
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestKmetaModule1.CreateServiceNowConfig(
                api_config_override=rest_transport.api_config, cid=cid, data=data
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def get_service_now_config(
        self, *, cid: str, id: str
    ) -> rest_models.GetServiceNowConfigResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for kmeta service"
                )
            _req = ParseDict(
                {k: v for k, v in {"cid": cid, "id": id}.items() if v is not None},
                self._grpc_pb2_1.GetServiceNowConfigRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_1.GetServiceNowConfig, _req)
            return rest_models.GetServiceNowConfigResponse.model_validate(
                MessageToDict(_resp, always_print_fields_with_no_presence=True)
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestKmetaModule1.GetServiceNowConfig(
                api_config_override=rest_transport.api_config, cid=cid, id=id
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def update_service_now_config(
        self, *, cid: str, id: str, data: rest_models.ServiceNowConfig
    ) -> rest_models.UpdateServiceNowConfigResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for kmeta service"
                )
            _req_dict = data.model_dump(by_alias=True, exclude_none=True)
            _req_dict.update(
                {k: v for k, v in {"cid": cid, "id": id}.items() if v is not None}
            )
            _req = ParseDict(
                _req_dict,
                self._grpc_pb2_1.UpdateServiceNowConfigRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_1.UpdateServiceNowConfig, _req)
            return rest_models.UpdateServiceNowConfigResponse.model_validate(
                MessageToDict(_resp, always_print_fields_with_no_presence=True)
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestKmetaModule1.UpdateServiceNowConfig(
                api_config_override=rest_transport.api_config, cid=cid, id=id, data=data
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def delete_service_now_config(
        self, *, cid: str, id: str
    ) -> rest_models.DeleteServiceNowConfigResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for kmeta service"
                )
            _req = ParseDict(
                {k: v for k, v in {"cid": cid, "id": id}.items() if v is not None},
                self._grpc_pb2_1.DeleteServiceNowConfigRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_1.DeleteServiceNowConfig, _req)
            return rest_models.DeleteServiceNowConfigResponse.model_validate(
                MessageToDict(_resp, always_print_fields_with_no_presence=True)
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestKmetaModule1.DeleteServiceNowConfig(
                api_config_override=rest_transport.api_config, cid=cid, id=id
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )
