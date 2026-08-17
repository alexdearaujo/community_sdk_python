from typing import Any, Dict, Optional

from kentik_api.core.api_config import APIConfig
from kentik_api.core.rest_runtime import request_json

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
        ListPackageResponse(**body)
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
        json_body=data.model_dump(),
        header_params=header_params,
        expected_status=200,
        operation_name="PackageCreate",
        error_cls=PackageCreateError,
    )

    return (
        CreatePackageResponse(**body)
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
        path=f"/mkp/v202407/packages/{id}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="PackageGet",
        error_cls=PackageGetError,
    )

    return (
        GetPackageResponse(**body)
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
        path=f"/mkp/v202407/packages/{id}",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(),
        header_params=header_params,
        expected_status=200,
        operation_name="PackageUpdate",
        error_cls=PackageUpdateError,
    )

    return (
        UpdatePackageResponse(**body)
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
        path=f"/mkp/v202407/packages/{id}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="PackageDelete",
        error_cls=PackageDeleteError,
    )

    return (
        DeletePackageResponse(**body)
        if body is not None
        else DeletePackageResponse.model_construct()
    )
