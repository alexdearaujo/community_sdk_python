from typing import Any, Dict, Optional

from kentik_api.core.api_config import APIConfig
from kentik_api.core.rest_runtime import request_json

from ..error import (
    TenantUserCreateError,
    TenantUserDeleteError,
    TenantUserListError,
    TenantUserUpdateError,
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


def TenantUserList(
    api_config_override: Optional[APIConfig] = None, *, tenantId: str
) -> ListTenantUserResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path=f"/mkp/v202407/tenants/{tenantId}/users",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="TenantUserList",
        error_cls=TenantUserListError,
    )

    return (
        ListTenantUserResponse(**body)
        if body is not None
        else ListTenantUserResponse.model_construct()
    )


def TenantUserCreate(
    api_config_override: Optional[APIConfig] = None,
    *,
    tenantId: str,
    data: TenantUserServiceCreateTenantUserBody,
) -> CreateTenantUserResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="post",
        path=f"/mkp/v202407/tenants/{tenantId}/users",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(),
        header_params=header_params,
        expected_status=200,
        operation_name="TenantUserCreate",
        error_cls=TenantUserCreateError,
    )

    return (
        CreateTenantUserResponse(**body)
        if body is not None
        else CreateTenantUserResponse.model_construct()
    )


def TenantUserUpdate(
    api_config_override: Optional[APIConfig] = None,
    *,
    tenantId: str,
    id: str,
    data: TenantUserServiceUpdateTenantUserBody,
) -> UpdateTenantUserResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="put",
        path=f"/mkp/v202407/tenants/{tenantId}/users/{id}",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(),
        header_params=header_params,
        expected_status=200,
        operation_name="TenantUserUpdate",
        error_cls=TenantUserUpdateError,
    )

    return (
        UpdateTenantUserResponse(**body)
        if body is not None
        else UpdateTenantUserResponse.model_construct()
    )


def TenantUserDelete(
    api_config_override: Optional[APIConfig] = None, *, tenantId: str, id: str
) -> DeleteTenantUserResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="delete",
        path=f"/mkp/v202407/tenants/{tenantId}/users/{id}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="TenantUserDelete",
        error_cls=TenantUserDeleteError,
    )

    return (
        DeleteTenantUserResponse(**body)
        if body is not None
        else DeleteTenantUserResponse.model_construct()
    )
