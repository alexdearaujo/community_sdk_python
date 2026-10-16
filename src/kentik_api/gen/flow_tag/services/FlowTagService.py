# AUTO-GENERATED: scripts/openapi_templates/service.jinja2 via openapi-python-generator
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Any, Dict, List, Optional

from kentik_api.core.api_config import APIConfig
from kentik_api.core.rest_runtime import request_json

from ..error import (
    CreateFlowTagError,
    DeleteFlowTagError,
    GetFlowTagError,
    SearchFlowTagError,
    UpdateFlowTagError,
)
from ..models import (  # noqa: F401
    AddressInfo,
    CreateFlowTagRequest,
    CreateFlowTagResponse,
    DeleteFlowTagResponse,
    FlowTag,
    FlowTagSearch,
    FlowTagServiceUpdateFlowTagBody,
    GetFlowTagResponse,
    LookupField,
    OrderDirection,
    OrderField,
    SearchFlowTagResponse,
    UpdateFlowTagResponse,
    protobufAny,
    rpcStatus,
)


def SearchFlowTag(
    api_config_override: Optional[APIConfig] = None,
    *,
    searchlimit: Optional[int] = None,
    searchoffset: Optional[int] = None,
    searchlookupFields: Optional[List[str]] = None,
    searchlookupValues: Optional[List[str]] = None,
    searchfieldLimit: Optional[int] = None,
) -> SearchFlowTagResponse:
    query_params: Dict[str, Any] = {
        "search.limit": searchlimit,
        "search.offset": searchoffset,
        "search.lookupFields": searchlookupFields,
        "search.lookupValues": searchlookupValues,
        "search.fieldLimit": searchfieldLimit,
    }

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path="/flow_tag/v202404alpha1/tag",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="SearchFlowTag",
        error_cls=SearchFlowTagError,
    )

    return (
        SearchFlowTagResponse(**body)
        if body is not None
        else SearchFlowTagResponse.model_construct()
    )


def CreateFlowTag(
    api_config_override: Optional[APIConfig] = None, *, data: CreateFlowTagRequest
) -> CreateFlowTagResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="post",
        path="/flow_tag/v202404alpha1/tag",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(),
        header_params=header_params,
        expected_status=200,
        operation_name="CreateFlowTag",
        error_cls=CreateFlowTagError,
    )

    return (
        CreateFlowTagResponse(**body)
        if body is not None
        else CreateFlowTagResponse.model_construct()
    )


def GetFlowTag(
    api_config_override: Optional[APIConfig] = None, *, flowTagid: str
) -> GetFlowTagResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path=f"/flow_tag/v202404alpha1/tag/{flowTagid}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="GetFlowTag",
        error_cls=GetFlowTagError,
    )

    return (
        GetFlowTagResponse(**body)
        if body is not None
        else GetFlowTagResponse.model_construct()
    )


def UpdateFlowTag(
    api_config_override: Optional[APIConfig] = None,
    *,
    flowTagid: str,
    data: FlowTagServiceUpdateFlowTagBody,
) -> UpdateFlowTagResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="put",
        path=f"/flow_tag/v202404alpha1/tag/{flowTagid}",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(),
        header_params=header_params,
        expected_status=200,
        operation_name="UpdateFlowTag",
        error_cls=UpdateFlowTagError,
    )

    return (
        UpdateFlowTagResponse(**body)
        if body is not None
        else UpdateFlowTagResponse.model_construct()
    )


def DeleteFlowTag(
    api_config_override: Optional[APIConfig] = None, *, flowTagid: str
) -> DeleteFlowTagResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="delete",
        path=f"/flow_tag/v202404alpha1/tag/{flowTagid}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="DeleteFlowTag",
        error_cls=DeleteFlowTagError,
    )

    return (
        DeleteFlowTagResponse(**body)
        if body is not None
        else DeleteFlowTagResponse.model_construct()
    )
