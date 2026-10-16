# AUTO-GENERATED: scripts/openapi_templates/service.jinja2 via openapi-python-generator
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Any, Dict, Optional

from kentik_api.core.api_config import APIConfig
from kentik_api.core.rest_runtime import request_json

from ..error import (
    CreateScopeError,
    DeleteScopeError,
    GetScopeError,
    ListScopesError,
    UpdateScopeError,
)
from ..models import (  # noqa: F401
    AssetTagSelector,
    CreateScopeResponse,
    DeleteScopeResponse,
    GetScopeResponse,
    ListScopesResponse,
    Scope,
    ScopeConfig,
    ScopeDimensions,
    UpdateScopeResponse,
    protobufAny,
    rpcStatus,
    v202501alpha1FilterField,
    v202501alpha1FilterOperator,
    v202501alpha1SavedFilterFilter,
    v202501alpha1SavedFilterFilterGroup,
    v202501alpha1SavedFilterFilterId,
    v202501alpha1SavedFilterFilters,
)


def ListScopes(api_config_override: Optional[APIConfig] = None) -> ListScopesResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path="/rbux/v202607alpha1/scopes",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="ListScopes",
        error_cls=ListScopesError,
    )

    return (
        ListScopesResponse(**body)
        if body is not None
        else ListScopesResponse.model_construct()
    )


def CreateScope(
    api_config_override: Optional[APIConfig] = None, *, data: Scope
) -> CreateScopeResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="post",
        path="/rbux/v202607alpha1/scopes",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(),
        header_params=header_params,
        expected_status=200,
        operation_name="CreateScope",
        error_cls=CreateScopeError,
    )

    return (
        CreateScopeResponse(**body)
        if body is not None
        else CreateScopeResponse.model_construct()
    )


def GetScope(
    api_config_override: Optional[APIConfig] = None, *, id: str
) -> GetScopeResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path=f"/rbux/v202607alpha1/scopes/{id}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="GetScope",
        error_cls=GetScopeError,
    )

    return (
        GetScopeResponse(**body)
        if body is not None
        else GetScopeResponse.model_construct()
    )


def UpdateScope(
    api_config_override: Optional[APIConfig] = None, *, id: str, data: Dict[str, Any]
) -> UpdateScopeResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="put",
        path=f"/rbux/v202607alpha1/scopes/{id}",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data,
        header_params=header_params,
        expected_status=200,
        operation_name="UpdateScope",
        error_cls=UpdateScopeError,
    )

    return (
        UpdateScopeResponse(**body)
        if body is not None
        else UpdateScopeResponse.model_construct()
    )


def DeleteScope(
    api_config_override: Optional[APIConfig] = None, *, id: str
) -> DeleteScopeResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="delete",
        path=f"/rbux/v202607alpha1/scopes/{id}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="DeleteScope",
        error_cls=DeleteScopeError,
    )

    return (
        DeleteScopeResponse(**body)
        if body is not None
        else DeleteScopeResponse.model_construct()
    )
