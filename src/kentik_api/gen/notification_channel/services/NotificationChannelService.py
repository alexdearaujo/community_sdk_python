# AUTO-GENERATED: scripts/openapi_templates/service.jinja2 via openapi-python-generator
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Any, Dict, Optional

from kentik_api.core.api_config import APIConfig
from kentik_api.core.rest_runtime import (
    parse_response_model,
    path_segment,
    request_json,
)

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
        path_template="/notification_channel/v202210/notification_channels",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="ListNotificationChannels",
        error_cls=ListNotificationChannelsError,
    )

    return parse_response_model(
        ListNotificationChannelsResponse,
        body,
        operation_name="ListNotificationChannels",
        method="get",
        path="/notification_channel/v202210/notification_channels",
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
        path_template="/notification_channel/v202210/notification_channels/search",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(by_alias=True, exclude_unset=True),
        header_params=header_params,
        expected_status=200,
        operation_name="SearchNotificationChannels",
        error_cls=SearchNotificationChannelsError,
    )

    return parse_response_model(
        SearchNotificationChannelsResponse,
        body,
        operation_name="SearchNotificationChannels",
        method="post",
        path="/notification_channel/v202210/notification_channels/search",
    )


def GetNotificationChannel(
    api_config_override: Optional[APIConfig] = None, *, id: str
) -> GetNotificationChannelResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path=f"/notification_channel/v202210/notification_channels/{path_segment(id)}",
        path_template="/notification_channel/v202210/notification_channels/{id}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="GetNotificationChannel",
        error_cls=GetNotificationChannelError,
    )

    return parse_response_model(
        GetNotificationChannelResponse,
        body,
        operation_name="GetNotificationChannel",
        method="get",
        path="/notification_channel/v202210/notification_channels/{id}",
    )
