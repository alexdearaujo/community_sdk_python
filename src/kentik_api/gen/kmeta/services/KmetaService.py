# AUTO-GENERATED: scripts/openapi_templates/service.jinja2 via openapi-python-generator
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Any, Dict, Optional

from kentik_api.core.api_config import APIConfig
from kentik_api.core.rate_limit import attach_rate_limit, rate_limit_of
from kentik_api.core.rest_runtime import request_json

from ..error import (
    CreateServiceNowConfigError,
    DeleteServiceNowConfigError,
    GetServiceNowConfigError,
    ListServiceNowConfigsError,
    UpdateServiceNowConfigError,
)
from ..models import (  # noqa: F401
    CreateServiceNowConfigResponse,
    DeleteServiceNowConfigResponse,
    GetServiceNowConfigResponse,
    ListServiceNowConfigsResponse,
    ServiceNowConfig,
    UpdateServiceNowConfigResponse,
    protobufAny,
    rpcStatus,
)


def ListServiceNowConfigs(
    api_config_override: Optional[APIConfig] = None, *, cid: str
) -> ListServiceNowConfigsResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path=f"/kmeta/v202607alpha1/{cid}/servicenow/config",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="ListServiceNowConfigs",
        error_cls=ListServiceNowConfigsError,
    )

    return (
        attach_rate_limit(ListServiceNowConfigsResponse(**body), rate_limit_of(body))
        if body is not None
        else ListServiceNowConfigsResponse.model_construct()
    )


def CreateServiceNowConfig(
    api_config_override: Optional[APIConfig] = None, *, cid: str, data: ServiceNowConfig
) -> CreateServiceNowConfigResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="post",
        path=f"/kmeta/v202607alpha1/{cid}/servicenow/config",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(),
        header_params=header_params,
        expected_status=200,
        operation_name="CreateServiceNowConfig",
        error_cls=CreateServiceNowConfigError,
    )

    return (
        attach_rate_limit(CreateServiceNowConfigResponse(**body), rate_limit_of(body))
        if body is not None
        else CreateServiceNowConfigResponse.model_construct()
    )


def GetServiceNowConfig(
    api_config_override: Optional[APIConfig] = None, *, cid: str, id: str
) -> GetServiceNowConfigResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path=f"/kmeta/v202607alpha1/{cid}/servicenow/config/{id}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="GetServiceNowConfig",
        error_cls=GetServiceNowConfigError,
    )

    return (
        attach_rate_limit(GetServiceNowConfigResponse(**body), rate_limit_of(body))
        if body is not None
        else GetServiceNowConfigResponse.model_construct()
    )


def UpdateServiceNowConfig(
    api_config_override: Optional[APIConfig] = None,
    *,
    cid: str,
    id: str,
    data: ServiceNowConfig,
) -> UpdateServiceNowConfigResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="put",
        path=f"/kmeta/v202607alpha1/{cid}/servicenow/config/{id}",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(),
        header_params=header_params,
        expected_status=200,
        operation_name="UpdateServiceNowConfig",
        error_cls=UpdateServiceNowConfigError,
    )

    return (
        attach_rate_limit(UpdateServiceNowConfigResponse(**body), rate_limit_of(body))
        if body is not None
        else UpdateServiceNowConfigResponse.model_construct()
    )


def DeleteServiceNowConfig(
    api_config_override: Optional[APIConfig] = None, *, cid: str, id: str
) -> DeleteServiceNowConfigResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="delete",
        path=f"/kmeta/v202607alpha1/{cid}/servicenow/config/{id}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="DeleteServiceNowConfig",
        error_cls=DeleteServiceNowConfigError,
    )

    return (
        attach_rate_limit(DeleteServiceNowConfigResponse(**body), rate_limit_of(body))
        if body is not None
        else DeleteServiceNowConfigResponse.model_construct()
    )
