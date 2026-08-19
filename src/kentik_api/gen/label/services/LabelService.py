# AUTO-GENERATED: scripts/openapi_templates/service.jinja2 via openapi-python-generator
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Any, Dict, Optional

from kentik_api.core.api_config import APIConfig
from kentik_api.core.rest_runtime import request_json

from ..error import (
    CreateLabelError,
    DeleteLabelError,
    ListLabelsError,
    UpdateLabelError,
)
from ..models import (  # noqa: F401
    CreateLabelRequest,
    CreateLabelResponse,
    DeleteLabelResponse,
    LabelServiceUpdateLabelBody,
    ListLabelsResponse,
    UpdateLabelResponse,
    labelv202210Label,
    protobufAny,
    rpcStatus,
)


def ListLabels(api_config_override: Optional[APIConfig] = None) -> ListLabelsResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path="/label/v202210/labels",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="ListLabels",
        error_cls=ListLabelsError,
    )

    return (
        ListLabelsResponse(**body)
        if body is not None
        else ListLabelsResponse.model_construct()
    )


def CreateLabel(
    api_config_override: Optional[APIConfig] = None, *, data: CreateLabelRequest
) -> CreateLabelResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="post",
        path="/label/v202210/labels",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(),
        header_params=header_params,
        expected_status=200,
        operation_name="CreateLabel",
        error_cls=CreateLabelError,
    )

    return (
        CreateLabelResponse(**body)
        if body is not None
        else CreateLabelResponse.model_construct()
    )


def UpdateLabel(
    api_config_override: Optional[APIConfig] = None,
    *,
    id: str,
    data: LabelServiceUpdateLabelBody,
) -> UpdateLabelResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="post",
        path=f"/label/v202210/labels/{id}",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(),
        header_params=header_params,
        expected_status=200,
        operation_name="UpdateLabel",
        error_cls=UpdateLabelError,
    )

    return (
        UpdateLabelResponse(**body)
        if body is not None
        else UpdateLabelResponse.model_construct()
    )


def DeleteLabel(
    api_config_override: Optional[APIConfig] = None, *, id: str
) -> DeleteLabelResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="delete",
        path=f"/label/v202210/labels/{id}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="DeleteLabel",
        error_cls=DeleteLabelError,
    )

    return (
        DeleteLabelResponse(**body)
        if body is not None
        else DeleteLabelResponse.model_construct()
    )
