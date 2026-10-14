from typing import Optional, Union, cast

from google.protobuf.json_format import MessageToDict

import kentik_api.gen.network_class.services.NetworkClassService as RestNetworkClassModule1
from kentik_api.core.api_config import APIConfig
from kentik_api.core.grpc_runtime import build_grpc_request, call_grpc
from kentik_api.core.rate_limit import attach_rate_limit
from kentik_api.gen.network_class import models as rest_models
from kentik_api.transports.grpc_client import GrpcTransport
from kentik_api.transports.rest_client import RestTransport


class NetworkClassServiceWrapper:
    """AUTO-GENERATED: scripts/generation/wrapper_generation.py, _generate_service_wrappers().
    Rebuilt on every `make generate`. Do not edit by hand.
    Unified Service routing to either gRPC or REST.
    """

    def __init__(self, transport: Union[GrpcTransport, RestTransport]):
        self._transport = transport
        if isinstance(self._transport, GrpcTransport):
            try:
                __import__("kentik_api.gen.pb_companions")
                import kentik_api.gen.network_class.pb.network_class_pb2 as _pb2_1_mod
                import kentik_api.gen.network_class.pb.network_class_pb2_grpc as _pb2_grpc_1_mod

                self._grpc_pb2_1 = _pb2_1_mod
                self._grpc_stub_1 = _pb2_grpc_1_mod.NetworkClassServiceStub(
                    self._transport.channel
                )
            except (ImportError, TypeError) as exc:
                self._grpc_pb2_1 = None
                self._grpc_stub_1 = None
                self._grpc_import_error_1 = exc

    def network_class_get(
        self, *, api_config_override: Optional[APIConfig] = None
    ) -> rest_models.GetNetworkClassResponse:
        """
        Get a network classification.

        Returns information about a network classification for the company.
        """
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_1 is None or self._grpc_stub_1 is None:
                raise NotImplementedError(
                    f"gRPC proto modules for network_class service failed to import: {self._grpc_import_error_1!r}"
                ) from self._grpc_import_error_1
            _req = build_grpc_request(self._grpc_pb2_1.GetNetworkClassRequest, None, {})
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_1.GetNetworkClass,
                _req,
                api_config=api_config_override,
                error_cls=RestNetworkClassModule1.NetworkClassGetError,
            )
            return attach_rate_limit(
                rest_models.GetNetworkClassResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestNetworkClassModule1.NetworkClassGet(
                api_config_override=api_config_override or rest_transport.api_config
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def network_class_update(
        self,
        *,
        api_config_override: Optional[APIConfig] = None,
        data: rest_models.UpdateNetworkClassRequest,
    ) -> rest_models.UpdateNetworkClassResponse:
        """
        Update a network classification.

        Replaces the entire network classification attributes for the company.
        """
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_1 is None or self._grpc_stub_1 is None:
                raise NotImplementedError(
                    f"gRPC proto modules for network_class service failed to import: {self._grpc_import_error_1!r}"
                ) from self._grpc_import_error_1
            _req = build_grpc_request(
                self._grpc_pb2_1.UpdateNetworkClassRequest,
                data.model_dump(by_alias=True, exclude_unset=True),
                {},
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_1.UpdateNetworkClass,
                _req,
                api_config=api_config_override,
                error_cls=RestNetworkClassModule1.NetworkClassUpdateError,
            )
            return attach_rate_limit(
                rest_models.UpdateNetworkClassResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestNetworkClassModule1.NetworkClassUpdate(
                api_config_override=api_config_override or rest_transport.api_config,
                data=data,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )
