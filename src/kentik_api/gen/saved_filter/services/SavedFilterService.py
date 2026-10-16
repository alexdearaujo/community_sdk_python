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
    CreateSavedFilterError,
    DeleteSavedFilterError,
    GetSavedFilterError,
    ListSavedFiltersAllError,
    ListSavedFiltersError,
    UpdateSavedFilterError,
)
from ..models import (  # noqa: F401
    CreateSavedFilterResponse,
    DeleteSavedFilterResponse,
    FilterField,
    FilterLevel,
    FilterOperator,
    GetSavedFilterResponse,
    ListSavedFiltersAllResponse,
    ListSavedFiltersResponse,
    SavedFilter,
    SavedFilterFilter,
    SavedFilterFilterGroup,
    SavedFilterFilterId,
    SavedFilterFilters,
    UpdateSavedFilterResponse,
    protobufAny,
    rpcStatus,
)


def CreateSavedFilter(
    api_config_override: Optional[APIConfig] = None, *, data: SavedFilter
) -> CreateSavedFilterResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="post",
        path="/saved-filter/v202501alpha1",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(by_alias=True),
        header_params=header_params,
        expected_status=200,
        operation_name="CreateSavedFilter",
        error_cls=CreateSavedFilterError,
    )

    return parse_response_model(
        CreateSavedFilterResponse,
        body,
        operation_name="CreateSavedFilter",
        method="post",
        path="/saved-filter/v202501alpha1",
    )


def GetSavedFilter(
    api_config_override: Optional[APIConfig] = None, *, id: str
) -> GetSavedFilterResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path=f"/saved-filter/v202501alpha1/{path_segment(id)}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="GetSavedFilter",
        error_cls=GetSavedFilterError,
    )

    return parse_response_model(
        GetSavedFilterResponse,
        body,
        operation_name="GetSavedFilter",
        method="get",
        path="/saved-filter/v202501alpha1/{id}",
    )


def UpdateSavedFilter(
    api_config_override: Optional[APIConfig] = None, *, id: str, data: SavedFilter
) -> UpdateSavedFilterResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="put",
        path=f"/saved-filter/v202501alpha1/{path_segment(id)}",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(by_alias=True),
        header_params=header_params,
        expected_status=200,
        operation_name="UpdateSavedFilter",
        error_cls=UpdateSavedFilterError,
    )

    return parse_response_model(
        UpdateSavedFilterResponse,
        body,
        operation_name="UpdateSavedFilter",
        method="put",
        path="/saved-filter/v202501alpha1/{id}",
    )


def DeleteSavedFilter(
    api_config_override: Optional[APIConfig] = None, *, id: str
) -> DeleteSavedFilterResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="delete",
        path=f"/saved-filter/v202501alpha1/{path_segment(id)}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="DeleteSavedFilter",
        error_cls=DeleteSavedFilterError,
    )

    return parse_response_model(
        DeleteSavedFilterResponse,
        body,
        operation_name="DeleteSavedFilter",
        method="delete",
        path="/saved-filter/v202501alpha1/{id}",
    )


def ListSavedFilters(
    api_config_override: Optional[APIConfig] = None,
) -> ListSavedFiltersResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path="/saved-filters/v202501alpha1",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="ListSavedFilters",
        error_cls=ListSavedFiltersError,
    )

    return parse_response_model(
        ListSavedFiltersResponse,
        body,
        operation_name="ListSavedFilters",
        method="get",
        path="/saved-filters/v202501alpha1",
    )


def ListSavedFiltersAll(
    api_config_override: Optional[APIConfig] = None,
) -> ListSavedFiltersAllResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path="/saved-filters/v202501alpha1/all",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="ListSavedFiltersAll",
        error_cls=ListSavedFiltersAllError,
    )

    return parse_response_model(
        ListSavedFiltersAllResponse,
        body,
        operation_name="ListSavedFiltersAll",
        method="get",
        path="/saved-filters/v202501alpha1/all",
    )
