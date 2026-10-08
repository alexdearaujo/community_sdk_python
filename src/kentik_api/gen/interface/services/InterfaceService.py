# AUTO-GENERATED: scripts/openapi_templates/service.jinja2 via openapi-python-generator
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Any, Dict, List, Optional

from kentik_api.core.api_config import APIConfig
from kentik_api.core.rate_limit import attach_rate_limit, rate_limit_of
from kentik_api.core.rest_runtime import path_segment, request_json

from ..error import (
    InterfaceCreateError,
    InterfaceDeleteError,
    InterfaceGetError,
    InterfaceUpdateError,
    ListInterfaceError,
    ManualClassifyError,
)
from ..models import (  # noqa: F401
    ConnectivityType,
    CreateInterfaceRequest,
    CreateInterfaceResponse,
    DeleteInterfaceResponse,
    GetInterfaceResponse,
    Interface,
    InterfaceFilter,
    InterfaceServiceUpdateInterfaceBody,
    InterfaceVrf,
    IpFilter,
    ListInterfaceResponse,
    ManualClassifyRequest,
    ManualClassifyResponse,
    NetworkBoundary,
    UpdateInterfaceResponse,
    protobufAny,
    rpcStatus,
)


def ListInterface(
    api_config_override: Optional[APIConfig] = None,
    *,
    filterstext: Optional[str] = None,
    filtersdeviceIds: Optional[List[str]] = None,
    filtersconnectivityTypes: Optional[List[str]] = None,
    filtersnetworkBoundaries: Optional[List[str]] = None,
    filtersproviders: Optional[List[str]] = None,
    filterssnmpSpeeds: Optional[List[int]] = None,
    filtersipTypes: Optional[List[str]] = None,
) -> ListInterfaceResponse:
    query_params: Dict[str, Any] = {
        "filters.text": filterstext,
        "filters.deviceIds": filtersdeviceIds,
        "filters.connectivityTypes": filtersconnectivityTypes,
        "filters.networkBoundaries": filtersnetworkBoundaries,
        "filters.providers": filtersproviders,
        "filters.snmpSpeeds": filterssnmpSpeeds,
        "filters.ipTypes": filtersipTypes,
    }

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path="/interface/v202108alpha1/interfaces",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="ListInterface",
        error_cls=ListInterfaceError,
    )

    return (
        attach_rate_limit(ListInterfaceResponse(**body), rate_limit_of(body))
        if body is not None
        else ListInterfaceResponse.model_construct()
    )


def InterfaceCreate(
    api_config_override: Optional[APIConfig] = None, *, data: CreateInterfaceRequest
) -> CreateInterfaceResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="post",
        path="/interface/v202108alpha1/interfaces",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(),
        header_params=header_params,
        expected_status=200,
        operation_name="InterfaceCreate",
        error_cls=InterfaceCreateError,
    )

    return (
        attach_rate_limit(CreateInterfaceResponse(**body), rate_limit_of(body))
        if body is not None
        else CreateInterfaceResponse.model_construct()
    )


def InterfaceGet(
    api_config_override: Optional[APIConfig] = None, *, id: str
) -> GetInterfaceResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path=f"/interface/v202108alpha1/interfaces/{path_segment(id)}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="InterfaceGet",
        error_cls=InterfaceGetError,
    )

    return (
        attach_rate_limit(GetInterfaceResponse(**body), rate_limit_of(body))
        if body is not None
        else GetInterfaceResponse.model_construct()
    )


def InterfaceUpdate(
    api_config_override: Optional[APIConfig] = None,
    *,
    id: str,
    data: InterfaceServiceUpdateInterfaceBody,
) -> UpdateInterfaceResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="put",
        path=f"/interface/v202108alpha1/interfaces/{path_segment(id)}",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(),
        header_params=header_params,
        expected_status=200,
        operation_name="InterfaceUpdate",
        error_cls=InterfaceUpdateError,
    )

    return (
        attach_rate_limit(UpdateInterfaceResponse(**body), rate_limit_of(body))
        if body is not None
        else UpdateInterfaceResponse.model_construct()
    )


def InterfaceDelete(
    api_config_override: Optional[APIConfig] = None, *, id: str
) -> DeleteInterfaceResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="delete",
        path=f"/interface/v202108alpha1/interfaces/{path_segment(id)}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="InterfaceDelete",
        error_cls=InterfaceDeleteError,
    )

    return (
        attach_rate_limit(DeleteInterfaceResponse(**body), rate_limit_of(body))
        if body is not None
        else DeleteInterfaceResponse.model_construct()
    )


def ManualClassify(
    api_config_override: Optional[APIConfig] = None, *, data: ManualClassifyRequest
) -> ManualClassifyResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="post",
        path="/interface/v202108alpha1/manual_classify",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(),
        header_params=header_params,
        expected_status=200,
        operation_name="ManualClassify",
        error_cls=ManualClassifyError,
    )

    return (
        attach_rate_limit(ManualClassifyResponse(**body), rate_limit_of(body))
        if body is not None
        else ManualClassifyResponse.model_construct()
    )
