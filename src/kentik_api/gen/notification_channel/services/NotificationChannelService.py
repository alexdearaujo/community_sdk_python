from typing import Any, Dict, Optional

from kentik_api.core.api_config import APIConfig
from kentik_api.core.rest_runtime import request_json

from ..error import (
    GetNotificationChannelError,
    ListNotificationChannelsError,
    SearchNotificationChannelsError,
)
from ..models import (  # noqa: F401
    ChannelType,
    GetNotificationChannelResponse,
    ListNotificationChannelsResponse,
    NotificationChannel,
    SearchNotificationChannelsRequest,
    SearchNotificationChannelsResponse,
    protobufAny,
    rpcStatus,
)


def ListNotificationChannels(
    api_config_override: Optional[APIConfig] = None,
) -> ListNotificationChannelsResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path="/notification_channel/v202210/notification_channels",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="ListNotificationChannels",
        error_cls=ListNotificationChannelsError,
    )

    return (
        ListNotificationChannelsResponse(**body)
        if body is not None
        else ListNotificationChannelsResponse.model_construct()
    )


def SearchNotificationChannels(
    api_config_override: Optional[APIConfig] = None,
    *,
    data: SearchNotificationChannelsRequest,
) -> SearchNotificationChannelsResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="post",
        path="/notification_channel/v202210/notification_channels/search",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(),
        header_params=header_params,
        expected_status=200,
        operation_name="SearchNotificationChannels",
        error_cls=SearchNotificationChannelsError,
    )

    return (
        SearchNotificationChannelsResponse(**body)
        if body is not None
        else SearchNotificationChannelsResponse.model_construct()
    )


def GetNotificationChannel(
    api_config_override: Optional[APIConfig] = None, *, id: str
) -> GetNotificationChannelResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path=f"/notification_channel/v202210/notification_channels/{id}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="GetNotificationChannel",
        error_cls=GetNotificationChannelError,
    )

    return (
        GetNotificationChannelResponse(**body)
        if body is not None
        else GetNotificationChannelResponse.model_construct()
    )
