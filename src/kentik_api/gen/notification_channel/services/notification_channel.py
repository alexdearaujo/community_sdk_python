from typing import Optional, Union, cast

from google.protobuf.json_format import MessageToDict

import kentik_api.gen.notification_channel.services.NotificationChannelService as RestNotificationChannelModule1
from kentik_api.core.api_config import APIConfig
from kentik_api.core.grpc_runtime import build_grpc_request, call_grpc
from kentik_api.core.rate_limit import attach_rate_limit
from kentik_api.gen.notification_channel import models as rest_models
from kentik_api.transports.grpc_client import GrpcTransport
from kentik_api.transports.rest_client import RestTransport


class NotificationChannelServiceWrapper:
    """AUTO-GENERATED: scripts/generation/wrapper_generation.py, _generate_service_wrappers().
    Rebuilt on every `make generate`. Do not edit by hand.
    Unified Service routing to either gRPC or REST.
    """

    def __init__(self, transport: Union[GrpcTransport, RestTransport]):
        self._transport = transport
        if isinstance(self._transport, GrpcTransport):
            try:
                __import__("kentik_api.gen.pb_companions")
                import kentik_api.gen.notification_channel.pb.notification_channel_pb2 as _pb2_1_mod
                import kentik_api.gen.notification_channel.pb.notification_channel_pb2_grpc as _pb2_grpc_1_mod

                self._grpc_pb2_1 = _pb2_1_mod
                self._grpc_stub_1 = _pb2_grpc_1_mod.NotificationChannelServiceStub(
                    self._transport.channel
                )
            except (ImportError, TypeError):
                self._grpc_pb2_1 = None
                self._grpc_stub_1 = None

    def list_notification_channels(
        self, *, api_config_override: Optional[APIConfig] = None
    ) -> rest_models.ListNotificationChannelsResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_1 is None or self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for notification_channel service"
                )
            _req = build_grpc_request(
                self._grpc_pb2_1.ListNotificationChannelsRequest, None, {}
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_1.ListNotificationChannels,
                _req,
                api_config=api_config_override,
                error_cls=RestNotificationChannelModule1.ListNotificationChannelsError,
            )
            return attach_rate_limit(
                rest_models.ListNotificationChannelsResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestNotificationChannelModule1.ListNotificationChannels(
                api_config_override=api_config_override or rest_transport.api_config
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def search_notification_channels(
        self,
        *,
        api_config_override: Optional[APIConfig] = None,
        data: rest_models.SearchNotificationChannelsRequest,
    ) -> rest_models.SearchNotificationChannelsResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_1 is None or self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for notification_channel service"
                )
            _req = build_grpc_request(
                self._grpc_pb2_1.SearchNotificationChannelsRequest,
                data.model_dump(by_alias=True, exclude_none=True),
                {},
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_1.SearchNotificationChannels,
                _req,
                api_config=api_config_override,
                error_cls=RestNotificationChannelModule1.SearchNotificationChannelsError,
            )
            return attach_rate_limit(
                rest_models.SearchNotificationChannelsResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestNotificationChannelModule1.SearchNotificationChannels(
                api_config_override=api_config_override or rest_transport.api_config,
                data=data,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def get_notification_channel(
        self, *, api_config_override: Optional[APIConfig] = None, id: str
    ) -> rest_models.GetNotificationChannelResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_1 is None or self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for notification_channel service"
                )
            _req = build_grpc_request(
                self._grpc_pb2_1.GetNotificationChannelRequest, None, {"id": id}
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_1.GetNotificationChannel,
                _req,
                api_config=api_config_override,
                error_cls=RestNotificationChannelModule1.GetNotificationChannelError,
            )
            return attach_rate_limit(
                rest_models.GetNotificationChannelResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestNotificationChannelModule1.GetNotificationChannel(
                api_config_override=api_config_override or rest_transport.api_config,
                id=id,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )
