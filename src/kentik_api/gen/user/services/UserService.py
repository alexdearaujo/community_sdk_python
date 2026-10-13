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

    return parse_response_model(
        ListUsersResponse,
        body,
        operation_name="ListUsers",
        method="get",
        path="/user/v202211/users",
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
        json_body=data.model_dump(by_alias=True, exclude_unset=True),
        header_params=header_params,
        expected_status=200,
        operation_name="CreateUser",
        error_cls=CreateUserError,
    )

    return parse_response_model(
        CreateUserResponse,
        body,
        operation_name="CreateUser",
        method="post",
        path="/user/v202211/users",
    )


def GetUser(
    api_config_override: Optional[APIConfig] = None, *, id: str
) -> GetUserResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path=f"/user/v202211/users/{path_segment(id)}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="GetUser",
        error_cls=GetUserError,
    )

    return parse_response_model(
        GetUserResponse,
        body,
        operation_name="GetUser",
        method="get",
        path="/user/v202211/users/{id}",
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
        path=f"/user/v202211/users/{path_segment(id)}",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(by_alias=True, exclude_unset=True),
        header_params=header_params,
        expected_status=200,
        operation_name="UpdateUser",
        error_cls=UpdateUserError,
    )

    return parse_response_model(
        UpdateUserResponse,
        body,
        operation_name="UpdateUser",
        method="put",
        path="/user/v202211/users/{id}",
    )


def DeleteUser(
    api_config_override: Optional[APIConfig] = None, *, id: str
) -> DeleteUserResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="delete",
        path=f"/user/v202211/users/{path_segment(id)}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="DeleteUser",
        error_cls=DeleteUserError,
    )

    return parse_response_model(
        DeleteUserResponse,
        body,
        operation_name="DeleteUser",
        method="delete",
        path="/user/v202211/users/{id}",
    )


def ResetActiveSessions(
    api_config_override: Optional[APIConfig] = None, *, id: str
) -> ResetActiveSessionsResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="put",
        path=f"/user/v202211/users/{path_segment(id)}/reset_active_sessions",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="ResetActiveSessions",
        error_cls=ResetActiveSessionsError,
    )

    return parse_response_model(
        ResetActiveSessionsResponse,
        body,
        operation_name="ResetActiveSessions",
        method="put",
        path="/user/v202211/users/{id}/reset_active_sessions",
    )


def ResetApiToken(
    api_config_override: Optional[APIConfig] = None, *, id: str
) -> ResetApiTokenResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="put",
        path=f"/user/v202211/users/{path_segment(id)}/reset_api_token",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="ResetApiToken",
        error_cls=ResetApiTokenError,
    )

    return parse_response_model(
        ResetApiTokenResponse,
        body,
        operation_name="ResetApiToken",
        method="put",
        path="/user/v202211/users/{id}/reset_api_token",
    )
