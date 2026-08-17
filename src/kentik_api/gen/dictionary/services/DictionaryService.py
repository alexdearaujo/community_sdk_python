from typing import Any, Dict, Optional

from kentik_api.core.api_config import APIConfig
from kentik_api.core.rest_runtime import request_json

from ..error import GetDictionaryError
from ..models import (  # noqa: F401
    BaseUnit,
    DimensionField,
    FieldDataType,
    FieldDirection,
    GetDictionaryResponse,
    MeasurementDetail,
    MeasurementFamily,
    MetricFamilyDef,
    MetricField,
    MetricQuantity,
    Operator,
    OperatorSet,
    OperatorSetKey,
    protobufAny,
    rpcStatus,
)


def GetDictionary(
    api_config_override: Optional[APIConfig] = None,
) -> GetDictionaryResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path="/dictionary/v20260604alpha1",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="GetDictionary",
        error_cls=GetDictionaryError,
    )

    return (
        GetDictionaryResponse(**body)
        if body is not None
        else GetDictionaryResponse.model_construct()
    )
