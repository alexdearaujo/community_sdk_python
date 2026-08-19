# AUTO-GENERATED: scripts/openapi_templates/service.jinja2 via openapi-python-generator
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Any, Dict, Optional

from kentik_api.core.api_config import APIConfig
from kentik_api.core.rest_runtime import request_json

from ..error import (
    CreateUserError,
    DeleteUserError,
    GetUserError,
    ListUsersError,
    ResetActiveSessionsError,
    ResetApiTokenError,
    UpdateUserError,
)
from ..models import (  # noqa: F401
    CreateUserRequest,
    CreateUserResponse,
    DeleteUserResponse,
    GetUserResponse,
    LandingType,
    ListUsersResponse,
    PermissionEntry,
    ResetActiveSessionsResponse,
    ResetApiTokenResponse,
    Role,
    UpdateUserResponse,
    User,
    UserServiceUpdateUserBody,
    protobufAny,
    rpcStatus,
)


def ListUsers(api_config_override: Optional[APIConfig] = None) -> ListUsersResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path="/user/v202211/users",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="ListUsers",
        error_cls=ListUsersError,
    )

    return (
        ListUsersResponse(**body)
        if body is not None
        else ListUsersResponse.model_construct()
    )


def CreateUser(
    api_config_override: Optional[APIConfig] = None, *, data: CreateUserRequest
) -> CreateUserResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="post",
        path="/user/v202211/users",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(),
        header_params=header_params,
        expected_status=200,
        operation_name="CreateUser",
        error_cls=CreateUserError,
    )

    return (
        CreateUserResponse(**body)
        if body is not None
        else CreateUserResponse.model_construct()
    )


def GetUser(
    api_config_override: Optional[APIConfig] = None, *, id: str
) -> GetUserResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path=f"/user/v202211/users/{id}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="GetUser",
        error_cls=GetUserError,
    )

    return (
        GetUserResponse(**body)
        if body is not None
        else GetUserResponse.model_construct()
    )


def UpdateUser(
    api_config_override: Optional[APIConfig] = None,
    *,
    id: str,
    data: UserServiceUpdateUserBody,
) -> UpdateUserResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="put",
        path=f"/user/v202211/users/{id}",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(),
        header_params=header_params,
        expected_status=200,
        operation_name="UpdateUser",
        error_cls=UpdateUserError,
    )

    return (
        UpdateUserResponse(**body)
        if body is not None
        else UpdateUserResponse.model_construct()
    )


def DeleteUser(
    api_config_override: Optional[APIConfig] = None, *, id: str
) -> DeleteUserResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="delete",
        path=f"/user/v202211/users/{id}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="DeleteUser",
        error_cls=DeleteUserError,
    )

    return (
        DeleteUserResponse(**body)
        if body is not None
        else DeleteUserResponse.model_construct()
    )


def ResetActiveSessions(
    api_config_override: Optional[APIConfig] = None, *, id: str
) -> ResetActiveSessionsResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="put",
        path=f"/user/v202211/users/{id}/reset_active_sessions",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="ResetActiveSessions",
        error_cls=ResetActiveSessionsError,
    )

    return (
        ResetActiveSessionsResponse(**body)
        if body is not None
        else ResetActiveSessionsResponse.model_construct()
    )


def ResetApiToken(
    api_config_override: Optional[APIConfig] = None, *, id: str
) -> ResetApiTokenResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="put",
        path=f"/user/v202211/users/{id}/reset_api_token",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="ResetApiToken",
        error_cls=ResetApiTokenError,
    )

    return (
        ResetApiTokenResponse(**body)
        if body is not None
        else ResetApiTokenResponse.model_construct()
    )
