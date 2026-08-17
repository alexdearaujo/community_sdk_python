from typing import List, Optional

from pydantic import BaseModel, Field

from .MeasurementDetail import MeasurementDetail
from .MetricFamilyDef import MetricFamilyDef
from .OperatorSet import OperatorSet


class GetDictionaryResponse(BaseModel):
    """
    GetDictionaryResponse model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    measurements: Optional[List[Optional[MeasurementDetail]]] = Field(
        validation_alias="measurements", default=None
    )

    operatorSets: Optional[List[Optional[OperatorSet]]] = Field(
        validation_alias="operatorSets", default=None
    )

    metricFamilies: Optional[List[Optional[MetricFamilyDef]]] = Field(
        validation_alias="metricFamilies", default=None
    )
