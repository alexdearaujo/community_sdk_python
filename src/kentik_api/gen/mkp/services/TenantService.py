from typing import Any, Dict, Optional

from kentik_api.core.api_config import APIConfig
from kentik_api.core.rest_runtime import request_json

from ..error import (
    TenantCreateError,
    TenantDeleteError,
    TenantGetError,
    TenantListError,
    TenantUpdateError,
)
from ..models import (  # noqa: F401
    Activate,
    Alert,
    Asset,
    AssetReport,
    Condition,
    CreatePackageRequest,
    CreatePackageResponse,
    CreateTenantRequest,
    CreateTenantResponse,
    CreateTenantUserResponse,
    CustomDimension,
    DeletePackageResponse,
    DeleteTenantResponse,
    DeleteTenantUserResponse,
    Devices,
    Filter,
    FilterField,
    GetPackageResponse,
    GetTenantResponse,
    ListPackageResponse,
    ListTenantResponse,
    ListTenantUserResponse,
    Mitigation,
    NotificationChannel,
    Package,
    PackageServiceUpdatePackageBody,
    Tenant,
    TenantLink,
    TenantServiceUpdateTenantBody,
    TenantUser,
    TenantUserServiceCreateTenantUserBody,
    TenantUserServiceUpdateTenantUserBody,
    Threshold,
    UpdatePackageResponse,
    UpdateTenantResponse,
    UpdateTenantUserResponse,
    protobufAny,
    rpcStatus,
    v202211LandingType,
    v202211PermissionEntry,
    v202211Role,
    v202211User,
)


def TenantList(api_config_override: Optional[APIConfig] = None) -> ListTenantResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path="/mkp/v202407/tenants",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="TenantList",
        error_cls=TenantListError,
    )

    return (
        ListTenantResponse(**body)
        if body is not None
        else ListTenantResponse.model_construct()
    )


def TenantCreate(
    api_config_override: Optional[APIConfig] = None, *, data: CreateTenantRequest
) -> CreateTenantResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="post",
        path="/mkp/v202407/tenants",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(),
        header_params=header_params,
        expected_status=200,
        operation_name="TenantCreate",
        error_cls=TenantCreateError,
    )

    return (
        CreateTenantResponse(**body)
        if body is not None
        else CreateTenantResponse.model_construct()
    )


def TenantGet(
    api_config_override: Optional[APIConfig] = None, *, id: str
) -> GetTenantResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path=f"/mkp/v202407/tenants/{id}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="TenantGet",
        error_cls=TenantGetError,
    )

    return (
        GetTenantResponse(**body)
        if body is not None
        else GetTenantResponse.model_construct()
    )


def TenantUpdate(
    api_config_override: Optional[APIConfig] = None,
    *,
    id: str,
    data: TenantServiceUpdateTenantBody,
) -> UpdateTenantResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="put",
        path=f"/mkp/v202407/tenants/{id}",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(),
        header_params=header_params,
        expected_status=200,
        operation_name="TenantUpdate",
        error_cls=TenantUpdateError,
    )

    return (
        UpdateTenantResponse(**body)
        if body is not None
        else UpdateTenantResponse.model_construct()
    )


def TenantDelete(
    api_config_override: Optional[APIConfig] = None, *, id: str
) -> DeleteTenantResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="delete",
        path=f"/mkp/v202407/tenants/{id}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="TenantDelete",
        error_cls=TenantDeleteError,
    )

    return (
        DeleteTenantResponse(**body)
        if body is not None
        else DeleteTenantResponse.model_construct()
    )
