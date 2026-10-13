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

    return parse_response_model(
        ListTenantUserResponse,
        body,
        operation_name="TenantUserList",
        method="get",
        path="/mkp/v202407/tenants/{tenantId}/users",
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
        json_body=data.model_dump(by_alias=True, exclude_unset=True),
        header_params=header_params,
        expected_status=200,
        operation_name="TenantUserCreate",
        error_cls=TenantUserCreateError,
    )

    return parse_response_model(
        CreateTenantUserResponse,
        body,
        operation_name="TenantUserCreate",
        method="post",
        path="/mkp/v202407/tenants/{tenantId}/users",
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
        json_body=data.model_dump(by_alias=True, exclude_unset=True),
        header_params=header_params,
        expected_status=200,
        operation_name="TenantUserUpdate",
        error_cls=TenantUserUpdateError,
    )

    return parse_response_model(
        UpdateTenantUserResponse,
        body,
        operation_name="TenantUserUpdate",
        method="put",
        path="/mkp/v202407/tenants/{tenantId}/users/{id}",
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

    return parse_response_model(
        DeleteTenantUserResponse,
        body,
        operation_name="TenantUserDelete",
        method="delete",
        path="/mkp/v202407/tenants/{tenantId}/users/{id}",
    )
