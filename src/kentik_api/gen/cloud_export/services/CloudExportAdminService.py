# AUTO-GENERATED: scripts/openapi_templates/service.jinja2 via openapi-python-generator
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Any, Dict, Optional

from kentik_api.core.api_config import APIConfig
from kentik_api.core.rate_limit import attach_rate_limit, rate_limit_of
from kentik_api.core.rest_runtime import path_segment, request_json

from ..error import (
    CreateCloudExportError,
    DeleteCloudExportError,
    GetCloudExportError,
    ListCloudExportsError,
    UpdateCloudExportError,
)
from ..models import (  # noqa: F401
    AwsProperties,
    AzureProperties,
    CloudExport,
    CloudExportAdminServiceUpdateCloudExportBody,
    CloudExportSamplingProperties,
    CloudExportSamplingType,
    CloudExportStatus,
    CloudExportType,
    CloudProvider,
    CreateCloudExportRequest,
    CreateCloudExportResponse,
    DeleteCloudExportResponse,
    GceProperties,
    GetCloudExportResponse,
    ListCloudExportsResponse,
    OciProperties,
    UpdateCloudExportResponse,
    protobufAny,
    rpcStatus,
)


def ListCloudExports(
    api_config_override: Optional[APIConfig] = None,
) -> ListCloudExportsResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path="/cloud_export/v202506/exports",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="ListCloudExports",
        error_cls=ListCloudExportsError,
    )

    return (
        attach_rate_limit(ListCloudExportsResponse(**body), rate_limit_of(body))
        if body is not None
        else ListCloudExportsResponse.model_construct()
    )


def CreateCloudExport(
    api_config_override: Optional[APIConfig] = None, *, data: CreateCloudExportRequest
) -> CreateCloudExportResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="post",
        path="/cloud_export/v202506/exports",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(by_alias=True),
        header_params=header_params,
        expected_status=200,
        operation_name="CreateCloudExport",
        error_cls=CreateCloudExportError,
    )

    return (
        attach_rate_limit(CreateCloudExportResponse(**body), rate_limit_of(body))
        if body is not None
        else CreateCloudExportResponse.model_construct()
    )


def GetCloudExport(
    api_config_override: Optional[APIConfig] = None, *, exportid: str
) -> GetCloudExportResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path=f"/cloud_export/v202506/exports/{path_segment(exportid)}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="GetCloudExport",
        error_cls=GetCloudExportError,
    )

    return (
        attach_rate_limit(GetCloudExportResponse(**body), rate_limit_of(body))
        if body is not None
        else GetCloudExportResponse.model_construct()
    )


def UpdateCloudExport(
    api_config_override: Optional[APIConfig] = None,
    *,
    exportid: str,
    data: CloudExportAdminServiceUpdateCloudExportBody,
) -> UpdateCloudExportResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="put",
        path=f"/cloud_export/v202506/exports/{path_segment(exportid)}",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(by_alias=True),
        header_params=header_params,
        expected_status=200,
        operation_name="UpdateCloudExport",
        error_cls=UpdateCloudExportError,
    )

    return (
        attach_rate_limit(UpdateCloudExportResponse(**body), rate_limit_of(body))
        if body is not None
        else UpdateCloudExportResponse.model_construct()
    )


def DeleteCloudExport(
    api_config_override: Optional[APIConfig] = None, *, exportid: str
) -> DeleteCloudExportResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="delete",
        path=f"/cloud_export/v202506/exports/{path_segment(exportid)}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="DeleteCloudExport",
        error_cls=DeleteCloudExportError,
    )

    return (
        attach_rate_limit(DeleteCloudExportResponse(**body), rate_limit_of(body))
        if body is not None
        else DeleteCloudExportResponse.model_construct()
    )
