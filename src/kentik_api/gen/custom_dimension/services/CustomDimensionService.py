# AUTO-GENERATED: scripts/openapi_templates/service.jinja2 via openapi-python-generator
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Any, Dict, Optional

from kentik_api.core.api_config import APIConfig
from kentik_api.core.rate_limit import attach_rate_limit, rate_limit_of
from kentik_api.core.rest_runtime import path_segment, request_json

from ..error import (
    CreateCustomDimensionError,
    CreatePopulatorError,
    DeleteCustomDimensionError,
    DeletePopulatorError,
    GetCustomDimensionInfoError,
    GetPopulatorError,
    GetPopulatorFieldError,
    ListCustomDimensionsError,
    UpdateCustomDimensionError,
    UpdatePopulatorError,
)
from ..models import (  # noqa: F401
    CreateCustomDimensionResponse,
    CreatePopulatorResponse,
    CustomDimension,
    DeleteCustomDimensionResponse,
    DeletePopulatorResponse,
    ExtendedField,
    GetCustomDimensionInfoResponse,
    GetPopulatorFieldResponse,
    GetPopulatorResponse,
    ListCustomDimensionsResponse,
    Populator,
    UpdateCustomDimensionResponse,
    UpdatePopulatorResponse,
    protobufAny,
    rpcStatus,
)


def ListCustomDimensions(
    api_config_override: Optional[APIConfig] = None,
) -> ListCustomDimensionsResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path="/custom_dimensions/v202411alpha1",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="ListCustomDimensions",
        error_cls=ListCustomDimensionsError,
    )

    return (
        attach_rate_limit(ListCustomDimensionsResponse(**body), rate_limit_of(body))
        if body is not None
        else ListCustomDimensionsResponse.model_construct()
    )


def GetCustomDimensionInfo(
    api_config_override: Optional[APIConfig] = None, *, customDimensionId: str
) -> GetCustomDimensionInfoResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path=f"/custom_dimensions/v202411alpha1/{path_segment(customDimensionId)}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="GetCustomDimensionInfo",
        error_cls=GetCustomDimensionInfoError,
    )

    return (
        attach_rate_limit(GetCustomDimensionInfoResponse(**body), rate_limit_of(body))
        if body is not None
        else GetCustomDimensionInfoResponse.model_construct()
    )


def UpdateCustomDimension(
    api_config_override: Optional[APIConfig] = None,
    *,
    customDimensionId: str,
    data: CustomDimension,
) -> UpdateCustomDimensionResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="put",
        path=f"/custom_dimensions/v202411alpha1/{path_segment(customDimensionId)}",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(by_alias=True),
        header_params=header_params,
        expected_status=200,
        operation_name="UpdateCustomDimension",
        error_cls=UpdateCustomDimensionError,
    )

    return (
        attach_rate_limit(UpdateCustomDimensionResponse(**body), rate_limit_of(body))
        if body is not None
        else UpdateCustomDimensionResponse.model_construct()
    )


def DeleteCustomDimension(
    api_config_override: Optional[APIConfig] = None, *, customDimensionId: str
) -> DeleteCustomDimensionResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="delete",
        path=f"/custom_dimensions/v202411alpha1/{path_segment(customDimensionId)}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="DeleteCustomDimension",
        error_cls=DeleteCustomDimensionError,
    )

    return (
        attach_rate_limit(DeleteCustomDimensionResponse(**body), rate_limit_of(body))
        if body is not None
        else DeleteCustomDimensionResponse.model_construct()
    )


def CreatePopulator(
    api_config_override: Optional[APIConfig] = None,
    *,
    customDimensionId: str,
    data: Populator,
) -> CreatePopulatorResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="post",
        path=f"/custom_dimensions/v202411alpha1/{path_segment(customDimensionId)}/populator",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(by_alias=True),
        header_params=header_params,
        expected_status=200,
        operation_name="CreatePopulator",
        error_cls=CreatePopulatorError,
    )

    return (
        attach_rate_limit(CreatePopulatorResponse(**body), rate_limit_of(body))
        if body is not None
        else CreatePopulatorResponse.model_construct()
    )


def GetPopulator(
    api_config_override: Optional[APIConfig] = None,
    *,
    customDimensionId: str,
    populatorId: str,
    fieldLimit: Optional[int] = None,
) -> GetPopulatorResponse:
    query_params: Dict[str, Any] = {"fieldLimit": fieldLimit}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path=f"/custom_dimensions/v202411alpha1/{path_segment(customDimensionId)}/populator/{path_segment(populatorId)}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="GetPopulator",
        error_cls=GetPopulatorError,
    )

    return (
        attach_rate_limit(GetPopulatorResponse(**body), rate_limit_of(body))
        if body is not None
        else GetPopulatorResponse.model_construct()
    )


def UpdatePopulator(
    api_config_override: Optional[APIConfig] = None,
    *,
    customDimensionId: str,
    populatorId: str,
    data: Populator,
) -> UpdatePopulatorResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="put",
        path=f"/custom_dimensions/v202411alpha1/{path_segment(customDimensionId)}/populator/{path_segment(populatorId)}",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(by_alias=True),
        header_params=header_params,
        expected_status=200,
        operation_name="UpdatePopulator",
        error_cls=UpdatePopulatorError,
    )

    return (
        attach_rate_limit(UpdatePopulatorResponse(**body), rate_limit_of(body))
        if body is not None
        else UpdatePopulatorResponse.model_construct()
    )


def DeletePopulator(
    api_config_override: Optional[APIConfig] = None,
    *,
    customDimensionId: str,
    populatorId: str,
) -> DeletePopulatorResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="delete",
        path=f"/custom_dimensions/v202411alpha1/{path_segment(customDimensionId)}/populator/{path_segment(populatorId)}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="DeletePopulator",
        error_cls=DeletePopulatorError,
    )

    return (
        attach_rate_limit(DeletePopulatorResponse(**body), rate_limit_of(body))
        if body is not None
        else DeletePopulatorResponse.model_construct()
    )


def GetPopulatorField(
    api_config_override: Optional[APIConfig] = None,
    *,
    customDimensionId: str,
    populatorId: str,
    fieldName: str,
    offset: Optional[int] = None,
    limit: Optional[int] = None,
) -> GetPopulatorFieldResponse:
    query_params: Dict[str, Any] = {"offset": offset, "limit": limit}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path=f"/custom_dimensions/v202411alpha1/{path_segment(customDimensionId)}/populator/{path_segment(populatorId)}/field/{path_segment(fieldName)}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="GetPopulatorField",
        error_cls=GetPopulatorFieldError,
    )

    return (
        attach_rate_limit(GetPopulatorFieldResponse(**body), rate_limit_of(body))
        if body is not None
        else GetPopulatorFieldResponse.model_construct()
    )


def CreateCustomDimension(
    api_config_override: Optional[APIConfig] = None, *, data: CustomDimension
) -> CreateCustomDimensionResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="post",
        path="/v1/customdimension",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(by_alias=True),
        header_params=header_params,
        expected_status=200,
        operation_name="CreateCustomDimension",
        error_cls=CreateCustomDimensionError,
    )

    return (
        attach_rate_limit(CreateCustomDimensionResponse(**body), rate_limit_of(body))
        if body is not None
        else CreateCustomDimensionResponse.model_construct()
    )
