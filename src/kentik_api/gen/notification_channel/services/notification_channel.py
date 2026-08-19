from typing import Union, cast

from google.protobuf.json_format import MessageToDict, ParseDict

import kentik_api.gen.notification_channel.services.NotificationChannelService as RestNotificationChannelModule1
from kentik_api.core.grpc_runtime import call_grpc
from kentik_api.gen.notification_channel import models as rest_models
from kentik_api.transports.grpc_client import GrpcTransport
from kentik_api.transports.rest_client import RestTransport


class NotificationChannelServiceWrapper:
    """Unified Service routing to either gRPC or REST."""

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
        self,
    ) -> rest_models.ListNotificationChannelsResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for notification_channel service"
                )
            _req = self._grpc_pb2_1.ListNotificationChannelsRequest()
            _resp = call_grpc(self._grpc_stub_1.ListNotificationChannels, _req)
            return rest_models.ListNotificationChannelsResponse.model_validate(
                MessageToDict(_resp)
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestNotificationChannelModule1.ListNotificationChannels(
                api_config_override=rest_transport.api_config
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def search_notification_channels(
        self,
        *,
        data: rest_models.SearchNotificationChannelsRequest,
    ) -> rest_models.SearchNotificationChannelsResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for notification_channel service"
                )
            _req = ParseDict(
                data.model_dump(by_alias=True, exclude_none=True),
                self._grpc_pb2_1.SearchNotificationChannelsRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_1.SearchNotificationChannels, _req)
            return rest_models.SearchNotificationChannelsResponse.model_validate(
                MessageToDict(_resp)
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestNotificationChannelModule1.SearchNotificationChannels(
                api_config_override=rest_transport.api_config, data=data
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def get_notification_channel(
        self, *, id: str
    ) -> rest_models.GetNotificationChannelResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for notification_channel service"
                )
            _req = ParseDict(
                {k: v for k, v in {"id": id}.items() if v is not None},
                self._grpc_pb2_1.GetNotificationChannelRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_1.GetNotificationChannel, _req)
            return rest_models.GetNotificationChannelResponse.model_validate(
                MessageToDict(_resp)
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestNotificationChannelModule1.GetNotificationChannel(
                api_config_override=rest_transport.api_config, id=id
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )
