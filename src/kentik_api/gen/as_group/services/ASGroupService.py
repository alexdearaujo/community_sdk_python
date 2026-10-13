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

    return parse_response_model(
        ListASGroupsResponse,
        body,
        operation_name="ListASGroups",
        method="get",
        path="/as_group/v202212/as_group",
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
        json_body=data.model_dump(by_alias=True, exclude_unset=True),
        header_params=header_params,
        expected_status=200,
        operation_name="CreateASGroup",
        error_cls=CreateASGroupError,
    )

    return parse_response_model(
        CreateASGroupResponse,
        body,
        operation_name="CreateASGroup",
        method="post",
        path="/as_group/v202212/as_group",
    )


def GetASGroup(
    api_config_override: Optional[APIConfig] = None, *, asGroupid: str
) -> GetASGroupResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path=f"/as_group/v202212/as_group/{path_segment(asGroupid)}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="GetASGroup",
        error_cls=GetASGroupError,
    )

    return parse_response_model(
        GetASGroupResponse,
        body,
        operation_name="GetASGroup",
        method="get",
        path="/as_group/v202212/as_group/{asGroup.id}",
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
        path=f"/as_group/v202212/as_group/{path_segment(asGroupid)}",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(by_alias=True, exclude_unset=True),
        header_params=header_params,
        expected_status=200,
        operation_name="UpdateASGroup",
        error_cls=UpdateASGroupError,
    )

    return parse_response_model(
        UpdateASGroupResponse,
        body,
        operation_name="UpdateASGroup",
        method="put",
        path="/as_group/v202212/as_group/{asGroup.id}",
    )


def DeleteASGroup(
    api_config_override: Optional[APIConfig] = None, *, asGroupid: str
) -> DeleteASGroupResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="delete",
        path=f"/as_group/v202212/as_group/{path_segment(asGroupid)}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="DeleteASGroup",
        error_cls=DeleteASGroupError,
    )

    return parse_response_model(
        DeleteASGroupResponse,
        body,
        operation_name="DeleteASGroup",
        method="delete",
        path="/as_group/v202212/as_group/{asGroup.id}",
    )
