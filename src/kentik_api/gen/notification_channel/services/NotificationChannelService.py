# AUTO-GENERATED: scripts/openapi_templates/service.jinja2 via openapi-python-generator
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Any, Dict, Optional

from kentik_api.core.api_config import APIConfig
from kentik_api.core.rate_limit import attach_rate_limit, rate_limit_of
from kentik_api.core.rest_runtime import path_segment, request_json

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
        attach_rate_limit(ListNotificationChannelsResponse(**body), rate_limit_of(body))
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
        json_body=data.model_dump(by_alias=True),
        header_params=header_params,
        expected_status=200,
        operation_name="SearchNotificationChannels",
        error_cls=SearchNotificationChannelsError,
    )

    return (
        attach_rate_limit(
            SearchNotificationChannelsResponse(**body), rate_limit_of(body)
        )
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
        path=f"/notification_channel/v202210/notification_channels/{path_segment(id)}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="GetNotificationChannel",
        error_cls=GetNotificationChannelError,
    )

    return (
        attach_rate_limit(GetNotificationChannelResponse(**body), rate_limit_of(body))
        if body is not None
        else GetNotificationChannelResponse.model_construct()
    )
