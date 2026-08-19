# AUTO-GENERATED: scripts/openapi_templates/service.jinja2 via openapi-python-generator
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Any, Dict, Optional

from kentik_api.core.api_config import APIConfig
from kentik_api.core.rest_runtime import request_json

from ..error import (
    CreateTagKeyError,
    DeleteTagKeyError,
    DeleteTagValuesError,
    GetTagKeyError,
    GetTagValuesError,
    ListTagKeysError,
    ListTagValuesError,
    SetTagValuesError,
    UpdateTagKeyError,
)
from ..models import (  # noqa: F401
    AssetTagsServiceUpdateTagKeyBody,
    AssetType,
    CreateTagKeyRequest,
    CreateTagKeyResponse,
    DeleteTagKeyResponse,
    DeleteTagValuesRequest,
    DeleteTagValuesResponse,
    GetTagKeyResponse,
    GetTagValuesResponse,
    ListTagKeysResponse,
    ListTagValuesResponse,
    SetTagValuesRequest,
    SetTagValuesResponse,
    TagKey,
    TagValue,
    UpdateTagKeyResponse,
    protobufAny,
    rpcStatus,
)


def GetTagValues(
    api_config_override: Optional[APIConfig] = None, *, assetType: str, assetId: str
) -> GetTagValuesResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path=f"/asset_tags/v20260515beta1/assets/{assetType}/{assetId}/values",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="GetTagValues",
        error_cls=GetTagValuesError,
    )

    return (
        GetTagValuesResponse(**body)
        if body is not None
        else GetTagValuesResponse.model_construct()
    )


def ListTagKeys(api_config_override: Optional[APIConfig] = None) -> ListTagKeysResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path="/asset_tags/v20260515beta1/keys",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="ListTagKeys",
        error_cls=ListTagKeysError,
    )

    return (
        ListTagKeysResponse(**body)
        if body is not None
        else ListTagKeysResponse.model_construct()
    )


def CreateTagKey(
    api_config_override: Optional[APIConfig] = None, *, data: CreateTagKeyRequest
) -> CreateTagKeyResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="post",
        path="/asset_tags/v20260515beta1/keys",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(),
        header_params=header_params,
        expected_status=200,
        operation_name="CreateTagKey",
        error_cls=CreateTagKeyError,
    )

    return (
        CreateTagKeyResponse(**body)
        if body is not None
        else CreateTagKeyResponse.model_construct()
    )


def GetTagKey(
    api_config_override: Optional[APIConfig] = None, *, id: str
) -> GetTagKeyResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path=f"/asset_tags/v20260515beta1/keys/{id}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="GetTagKey",
        error_cls=GetTagKeyError,
    )

    return (
        GetTagKeyResponse(**body)
        if body is not None
        else GetTagKeyResponse.model_construct()
    )


def UpdateTagKey(
    api_config_override: Optional[APIConfig] = None,
    *,
    id: str,
    data: AssetTagsServiceUpdateTagKeyBody,
) -> UpdateTagKeyResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="put",
        path=f"/asset_tags/v20260515beta1/keys/{id}",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(),
        header_params=header_params,
        expected_status=200,
        operation_name="UpdateTagKey",
        error_cls=UpdateTagKeyError,
    )

    return (
        UpdateTagKeyResponse(**body)
        if body is not None
        else UpdateTagKeyResponse.model_construct()
    )


def DeleteTagKey(
    api_config_override: Optional[APIConfig] = None, *, id: str
) -> DeleteTagKeyResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="delete",
        path=f"/asset_tags/v20260515beta1/keys/{id}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="DeleteTagKey",
        error_cls=DeleteTagKeyError,
    )

    return (
        DeleteTagKeyResponse(**body)
        if body is not None
        else DeleteTagKeyResponse.model_construct()
    )


def ListTagValues(
    api_config_override: Optional[APIConfig] = None, *, tagId: str, assetType: str
) -> ListTagValuesResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path=f"/asset_tags/v20260515beta1/keys/{tagId}/{assetType}/values",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="ListTagValues",
        error_cls=ListTagValuesError,
    )

    return (
        ListTagValuesResponse(**body)
        if body is not None
        else ListTagValuesResponse.model_construct()
    )


def SetTagValues(
    api_config_override: Optional[APIConfig] = None, *, data: SetTagValuesRequest
) -> SetTagValuesResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="put",
        path="/asset_tags/v20260515beta1/values",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(),
        header_params=header_params,
        expected_status=200,
        operation_name="SetTagValues",
        error_cls=SetTagValuesError,
    )

    return (
        SetTagValuesResponse(**body)
        if body is not None
        else SetTagValuesResponse.model_construct()
    )


def DeleteTagValues(
    api_config_override: Optional[APIConfig] = None, *, data: DeleteTagValuesRequest
) -> DeleteTagValuesResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="post",
        path="/asset_tags/v20260515beta1/values/delete",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(),
        header_params=header_params,
        expected_status=200,
        operation_name="DeleteTagValues",
        error_cls=DeleteTagValuesError,
    )

    return (
        DeleteTagValuesResponse(**body)
        if body is not None
        else DeleteTagValuesResponse.model_construct()
    )
