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
        path_template="/custom_application/v202501alpha1",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="ListCustomApplications",
        error_cls=ListCustomApplicationsError,
    )

    return parse_response_model(
        ListCustomApplicationsResponse,
        body,
        operation_name="ListCustomApplications",
        method="get",
        path="/custom_application/v202501alpha1",
    )


def CreateCustomApplication(
    api_config_override: Optional[APIConfig] = None, *, data: CustomApplication
) -> CreateCustomApplicationResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="post",
        path="/custom_application/v202501alpha1",
        path_template="/custom_application/v202501alpha1",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(by_alias=True, exclude_unset=True),
        header_params=header_params,
        expected_status=200,
        operation_name="CreateCustomApplication",
        error_cls=CreateCustomApplicationError,
    )

    return parse_response_model(
        CreateCustomApplicationResponse,
        body,
        operation_name="CreateCustomApplication",
        method="post",
        path="/custom_application/v202501alpha1",
    )


def GetCustomApplication(
    api_config_override: Optional[APIConfig] = None, *, customApplicationId: str
) -> GetCustomApplicationResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path=f"/custom_application/v202501alpha1/{path_segment(customApplicationId)}",
        path_template="/custom_application/v202501alpha1/{customApplicationId}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="GetCustomApplication",
        error_cls=GetCustomApplicationError,
    )

    return parse_response_model(
        GetCustomApplicationResponse,
        body,
        operation_name="GetCustomApplication",
        method="get",
        path="/custom_application/v202501alpha1/{customApplicationId}",
    )


def UpdateCustomApplication(
    api_config_override: Optional[APIConfig] = None,
    *,
    customApplicationId: str,
    data: CustomApplication,
) -> UpdateCustomApplicationResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="put",
        path=f"/custom_application/v202501alpha1/{path_segment(customApplicationId)}",
        path_template="/custom_application/v202501alpha1/{customApplicationId}",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(by_alias=True, exclude_unset=True),
        header_params=header_params,
        expected_status=200,
        operation_name="UpdateCustomApplication",
        error_cls=UpdateCustomApplicationError,
    )

    return parse_response_model(
        UpdateCustomApplicationResponse,
        body,
        operation_name="UpdateCustomApplication",
        method="put",
        path="/custom_application/v202501alpha1/{customApplicationId}",
    )


def DeleteCustomApplication(
    api_config_override: Optional[APIConfig] = None, *, customApplicationId: str
) -> DeleteCustomApplicationResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="delete",
        path=f"/custom_application/v202501alpha1/{path_segment(customApplicationId)}",
        path_template="/custom_application/v202501alpha1/{customApplicationId}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="DeleteCustomApplication",
        error_cls=DeleteCustomApplicationError,
    )

    return parse_response_model(
        DeleteCustomApplicationResponse,
        body,
        operation_name="DeleteCustomApplication",
        method="delete",
        path="/custom_application/v202501alpha1/{customApplicationId}",
    )
