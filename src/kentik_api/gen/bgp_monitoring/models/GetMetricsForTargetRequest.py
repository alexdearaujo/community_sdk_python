from typing import List, Optional

from pydantic import BaseModel, Field

from .BgpMetricType import BgpMetricType
from .Nlri import Nlri


class GetMetricsForTargetRequest(BaseModel):
    """
    GetMetricsForTargetRequest model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    startTime: str = Field(validation_alias="startTime")

    endTime: str = Field(validation_alias="endTime")

    target: Nlri = Field(validation_alias="target")

    includeCovered: Optional[bool] = Field(
        validation_alias="includeCovered", default=None
    )

    metrics: List[BgpMetricType] = Field(validation_alias="metrics")
