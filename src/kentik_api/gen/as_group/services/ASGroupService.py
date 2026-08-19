# AUTO-GENERATED: scripts/openapi_templates/service.jinja2 via openapi-python-generator
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Any, Dict, Optional

from kentik_api.core.api_config import APIConfig
from kentik_api.core.rest_runtime import request_json

from ..error import (
    CreateASGroupError,
    DeleteASGroupError,
    GetASGroupError,
    ListASGroupsError,
    UpdateASGroupError,
)
from ..models import (  # noqa: F401
    ASGroupConcise,
    ASGroupDetailed,
    ASGroupServiceUpdateASGroupBody,
    AutonomousSystem,
    CreateASGroupRequest,
    CreateASGroupResponse,
    DeleteASGroupResponse,
    GetASGroupResponse,
    ListASGroupsResponse,
    UpdateASGroupResponse,
    protobufAny,
    rpcStatus,
)


def ListASGroups(
    api_config_override: Optional[APIConfig] = None,
) -> ListASGroupsResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path="/as_group/v202212/as_group",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="ListASGroups",
        error_cls=ListASGroupsError,
    )

    return (
        ListASGroupsResponse(**body)
        if body is not None
        else ListASGroupsResponse.model_construct()
    )


def CreateASGroup(
    api_config_override: Optional[APIConfig] = None, *, data: CreateASGroupRequest
) -> CreateASGroupResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="post",
        path="/as_group/v202212/as_group",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(),
        header_params=header_params,
        expected_status=200,
        operation_name="CreateASGroup",
        error_cls=CreateASGroupError,
    )

    return (
        CreateASGroupResponse(**body)
        if body is not None
        else CreateASGroupResponse.model_construct()
    )


def GetASGroup(
    api_config_override: Optional[APIConfig] = None, *, asGroupid: str
) -> GetASGroupResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path=f"/as_group/v202212/as_group/{asGroupid}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="GetASGroup",
        error_cls=GetASGroupError,
    )

    return (
        GetASGroupResponse(**body)
        if body is not None
        else GetASGroupResponse.model_construct()
    )


def UpdateASGroup(
    api_config_override: Optional[APIConfig] = None,
    *,
    asGroupid: str,
    data: ASGroupServiceUpdateASGroupBody,
) -> UpdateASGroupResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="put",
        path=f"/as_group/v202212/as_group/{asGroupid}",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(),
        header_params=header_params,
        expected_status=200,
        operation_name="UpdateASGroup",
        error_cls=UpdateASGroupError,
    )

    return (
        UpdateASGroupResponse(**body)
        if body is not None
        else UpdateASGroupResponse.model_construct()
    )


def DeleteASGroup(
    api_config_override: Optional[APIConfig] = None, *, asGroupid: str
) -> DeleteASGroupResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="delete",
        path=f"/as_group/v202212/as_group/{asGroupid}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="DeleteASGroup",
        error_cls=DeleteASGroupError,
    )

    return (
        DeleteASGroupResponse(**body)
        if body is not None
        else DeleteASGroupResponse.model_construct()
    )
