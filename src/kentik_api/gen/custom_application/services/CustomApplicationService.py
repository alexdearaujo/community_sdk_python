# AUTO-GENERATED: scripts/openapi_templates/service.jinja2 via openapi-python-generator
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Any, Dict, Optional

from kentik_api.core.api_config import APIConfig
from kentik_api.core.rest_runtime import request_json

from ..error import (
    CreateCustomApplicationError,
    DeleteCustomApplicationError,
    GetCustomApplicationError,
    ListCustomApplicationsError,
    UpdateCustomApplicationError,
)
from ..models import (  # noqa: F401
    CreateCustomApplicationResponse,
    CustomApplication,
    DeleteCustomApplicationResponse,
    GetCustomApplicationResponse,
    ListCustomApplicationsResponse,
    UpdateCustomApplicationResponse,
    protobufAny,
    rpcStatus,
)


def ListCustomApplications(
    api_config_override: Optional[APIConfig] = None,
) -> ListCustomApplicationsResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path="/custom_application/v202501alpha1",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="ListCustomApplications",
        error_cls=ListCustomApplicationsError,
    )

    return (
        ListCustomApplicationsResponse(**body)
        if body is not None
        else ListCustomApplicationsResponse.model_construct()
    )


def CreateCustomApplication(
    api_config_override: Optional[APIConfig] = None,
) -> CreateCustomApplicationResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="post",
        path="/custom_application/v202501alpha1",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="CreateCustomApplication",
        error_cls=CreateCustomApplicationError,
    )

    return (
        CreateCustomApplicationResponse(**body)
        if body is not None
        else CreateCustomApplicationResponse.model_construct()
    )


def GetCustomApplication(
    api_config_override: Optional[APIConfig] = None, *, customApplicationId: str
) -> GetCustomApplicationResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path=f"/custom_application/v202501alpha1/{customApplicationId}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="GetCustomApplication",
        error_cls=GetCustomApplicationError,
    )

    return (
        GetCustomApplicationResponse(**body)
        if body is not None
        else GetCustomApplicationResponse.model_construct()
    )


def UpdateCustomApplication(
    api_config_override: Optional[APIConfig] = None, *, customApplicationId: str
) -> UpdateCustomApplicationResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="put",
        path=f"/custom_application/v202501alpha1/{customApplicationId}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="UpdateCustomApplication",
        error_cls=UpdateCustomApplicationError,
    )

    return (
        UpdateCustomApplicationResponse(**body)
        if body is not None
        else UpdateCustomApplicationResponse.model_construct()
    )


def DeleteCustomApplication(
    api_config_override: Optional[APIConfig] = None, *, customApplicationId: str
) -> DeleteCustomApplicationResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="delete",
        path=f"/custom_application/v202501alpha1/{customApplicationId}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="DeleteCustomApplication",
        error_cls=DeleteCustomApplicationError,
    )

    return (
        DeleteCustomApplicationResponse(**body)
        if body is not None
        else DeleteCustomApplicationResponse.model_construct()
    )
