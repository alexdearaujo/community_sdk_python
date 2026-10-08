# AUTO-GENERATED: scripts/openapi_templates/service.jinja2 via openapi-python-generator
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Any, Dict, Optional

from kentik_api.core.api_config import APIConfig
from kentik_api.core.rate_limit import attach_rate_limit, rate_limit_of
from kentik_api.core.rest_runtime import path_segment, request_json

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
        path=f"/mkp/v202407/tenants/{path_segment(tenantId)}/users",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="TenantUserList",
        error_cls=TenantUserListError,
    )

    return (
        attach_rate_limit(ListTenantUserResponse(**body), rate_limit_of(body))
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
        path=f"/mkp/v202407/tenants/{path_segment(tenantId)}/users",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(),
        header_params=header_params,
        expected_status=200,
        operation_name="TenantUserCreate",
        error_cls=TenantUserCreateError,
    )

    return (
        attach_rate_limit(CreateTenantUserResponse(**body), rate_limit_of(body))
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
        path=f"/mkp/v202407/tenants/{path_segment(tenantId)}/users/{path_segment(id)}",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(),
        header_params=header_params,
        expected_status=200,
        operation_name="TenantUserUpdate",
        error_cls=TenantUserUpdateError,
    )

    return (
        attach_rate_limit(UpdateTenantUserResponse(**body), rate_limit_of(body))
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
        path=f"/mkp/v202407/tenants/{path_segment(tenantId)}/users/{path_segment(id)}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="TenantUserDelete",
        error_cls=TenantUserDeleteError,
    )

    return (
        attach_rate_limit(DeleteTenantUserResponse(**body), rate_limit_of(body))
        if body is not None
        else DeleteTenantUserResponse.model_construct()
    )
