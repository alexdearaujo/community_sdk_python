from typing import Any, Dict, Optional

from kentik_api.core.api_config import APIConfig
from kentik_api.core.rest_runtime import request_json

from ..error import CreateChatSessionError, GetChatSessionError, UpdateChatSessionError
from ..models import (  # noqa: F401
    ChatMessage,
    CreateChatSessionRequest,
    CreateChatSessionResponse,
    GetChatSessionResponse,
    SessionStatus,
    UpdateChatSessionRequest,
    UpdateChatSessionResponse,
    protobufAny,
    rpcStatus,
)


def CreateChatSession(
    api_config_override: Optional[APIConfig] = None, *, data: CreateChatSessionRequest
) -> CreateChatSessionResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="post",
        path="/ai_advisor/v202511/chat",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(),
        header_params=header_params,
        expected_status=200,
        operation_name="CreateChatSession",
        error_cls=CreateChatSessionError,
    )

    return (
        CreateChatSessionResponse(**body)
        if body is not None
        else CreateChatSessionResponse.model_construct()
    )


def UpdateChatSession(
    api_config_override: Optional[APIConfig] = None, *, data: UpdateChatSessionRequest
) -> UpdateChatSessionResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="put",
        path="/ai_advisor/v202511/chat",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(),
        header_params=header_params,
        expected_status=200,
        operation_name="UpdateChatSession",
        error_cls=UpdateChatSessionError,
    )

    return (
        UpdateChatSessionResponse(**body)
        if body is not None
        else UpdateChatSessionResponse.model_construct()
    )


def GetChatSession(
    api_config_override: Optional[APIConfig] = None, *, id: str
) -> GetChatSessionResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path=f"/ai_advisor/v202511/chat/{id}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="GetChatSession",
        error_cls=GetChatSessionError,
    )

    return (
        GetChatSessionResponse(**body)
        if body is not None
        else GetChatSessionResponse.model_construct()
    )
