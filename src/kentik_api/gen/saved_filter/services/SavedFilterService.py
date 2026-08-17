from typing import Any, Dict, Optional

from kentik_api.core.api_config import APIConfig
from kentik_api.core.rest_runtime import request_json

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
    api_config_override: Optional[APIConfig] = None,
) -> CreateSavedFilterResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="post",
        path="/saved-filter/v202501alpha1",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="CreateSavedFilter",
        error_cls=CreateSavedFilterError,
    )

    return (
        CreateSavedFilterResponse(**body)
        if body is not None
        else CreateSavedFilterResponse.model_construct()
    )


def GetSavedFilter(
    api_config_override: Optional[APIConfig] = None, *, id: str
) -> GetSavedFilterResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path=f"/saved-filter/v202501alpha1/{id}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="GetSavedFilter",
        error_cls=GetSavedFilterError,
    )

    return (
        GetSavedFilterResponse(**body)
        if body is not None
        else GetSavedFilterResponse.model_construct()
    )


def UpdateSavedFilter(
    api_config_override: Optional[APIConfig] = None, *, id: str
) -> UpdateSavedFilterResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="put",
        path=f"/saved-filter/v202501alpha1/{id}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="UpdateSavedFilter",
        error_cls=UpdateSavedFilterError,
    )

    return (
        UpdateSavedFilterResponse(**body)
        if body is not None
        else UpdateSavedFilterResponse.model_construct()
    )


def DeleteSavedFilter(
    api_config_override: Optional[APIConfig] = None, *, id: str
) -> DeleteSavedFilterResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="delete",
        path=f"/saved-filter/v202501alpha1/{id}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="DeleteSavedFilter",
        error_cls=DeleteSavedFilterError,
    )

    return (
        DeleteSavedFilterResponse(**body)
        if body is not None
        else DeleteSavedFilterResponse.model_construct()
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

    return (
        ListSavedFiltersResponse(**body)
        if body is not None
        else ListSavedFiltersResponse.model_construct()
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

    return (
        ListSavedFiltersAllResponse(**body)
        if body is not None
        else ListSavedFiltersAllResponse.model_construct()
    )
