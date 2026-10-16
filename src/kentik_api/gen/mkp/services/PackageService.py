# AUTO-GENERATED: scripts/openapi_templates/service.jinja2 via openapi-python-generator
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Any, Dict, Optional

from kentik_api.core.api_config import APIConfig
from kentik_api.core.rate_limit import attach_rate_limit, rate_limit_of
from kentik_api.core.rest_runtime import path_segment, request_json

from ..error import (
    PackageCreateError,
    PackageDeleteError,
    PackageGetError,
    PackageListError,
    PackageUpdateError,
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


def PackageList(api_config_override: Optional[APIConfig] = None) -> ListPackageResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path="/mkp/v202407/packages",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="PackageList",
        error_cls=PackageListError,
    )

    return (
        attach_rate_limit(ListPackageResponse(**body), rate_limit_of(body))
        if body is not None
        else ListPackageResponse.model_construct()
    )


def PackageCreate(
    api_config_override: Optional[APIConfig] = None, *, data: CreatePackageRequest
) -> CreatePackageResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="post",
        path="/mkp/v202407/packages",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(by_alias=True),
        header_params=header_params,
        expected_status=200,
        operation_name="PackageCreate",
        error_cls=PackageCreateError,
    )

    return (
        attach_rate_limit(CreatePackageResponse(**body), rate_limit_of(body))
        if body is not None
        else CreatePackageResponse.model_construct()
    )


def PackageGet(
    api_config_override: Optional[APIConfig] = None, *, id: str
) -> GetPackageResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path=f"/mkp/v202407/packages/{path_segment(id)}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="PackageGet",
        error_cls=PackageGetError,
    )

    return (
        attach_rate_limit(GetPackageResponse(**body), rate_limit_of(body))
        if body is not None
        else GetPackageResponse.model_construct()
    )


def PackageUpdate(
    api_config_override: Optional[APIConfig] = None,
    *,
    id: str,
    data: PackageServiceUpdatePackageBody,
) -> UpdatePackageResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="put",
        path=f"/mkp/v202407/packages/{path_segment(id)}",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(by_alias=True),
        header_params=header_params,
        expected_status=200,
        operation_name="PackageUpdate",
        error_cls=PackageUpdateError,
    )

    return (
        attach_rate_limit(UpdatePackageResponse(**body), rate_limit_of(body))
        if body is not None
        else UpdatePackageResponse.model_construct()
    )


def PackageDelete(
    api_config_override: Optional[APIConfig] = None, *, id: str
) -> DeletePackageResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="delete",
        path=f"/mkp/v202407/packages/{path_segment(id)}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="PackageDelete",
        error_cls=PackageDeleteError,
    )

    return (
        attach_rate_limit(DeletePackageResponse(**body), rate_limit_of(body))
        if body is not None
        else DeletePackageResponse.model_construct()
    )
