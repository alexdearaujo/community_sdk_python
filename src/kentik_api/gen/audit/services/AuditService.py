from typing import Any, Dict, Optional

from kentik_api.core.api_config import APIConfig
from kentik_api.core.rest_runtime import request_json

from ..error import GetAuditEventError, ListAuditEventsError
from ..models import (  # noqa: F401
    AuditEvent,
    GenericEvent,
    GetAuditEventResponse,
    ListAuditEventsResponse,
    protobufAny,
    rpcStatus,
)


def ListAuditEvents(
    api_config_override: Optional[APIConfig] = None,
    *,
    startTime: Optional[str] = None,
    endTime: Optional[str] = None,
    offset: Optional[str] = None,
    limit: Optional[str] = None,
) -> ListAuditEventsResponse:
    query_params: Dict[str, Any] = {
        "startTime": startTime,
        "endTime": endTime,
        "offset": offset,
        "limit": limit,
    }

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path="/audit/v202601/events",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="ListAuditEvents",
        error_cls=ListAuditEventsError,
    )

    return (
        ListAuditEventsResponse(**body)
        if body is not None
        else ListAuditEventsResponse.model_construct()
    )


def GetAuditEvent(
    api_config_override: Optional[APIConfig] = None,
    *,
    id: str,
    ctime: Optional[str] = None,
) -> GetAuditEventResponse:
    query_params: Dict[str, Any] = {"ctime": ctime}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path=f"/audit/v202601/events/{id}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="GetAuditEvent",
        error_cls=GetAuditEventError,
    )

    return (
        GetAuditEventResponse(**body)
        if body is not None
        else GetAuditEventResponse.model_construct()
    )


def GetAuditEvent_2(
    api_config_override: Optional[APIConfig] = None, *, id: str, ctime: str
) -> GetAuditEventResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path=f"/audit/v202601/events/{id}/{ctime}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="GetAuditEvent",
        error_cls=GetAuditEventError,
    )

    return (
        GetAuditEventResponse(**body)
        if body is not None
        else GetAuditEventResponse.model_construct()
    )
