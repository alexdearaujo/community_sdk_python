from typing import List, Optional

from pydantic import BaseModel, Field

from .BgpMetric import BgpMetric


class GetMetricsForTargetResponse(BaseModel):
    """
    GetMetricsForTargetResponse model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    metrics: Optional[List[Optional[BgpMetric]]] = Field(
        validation_alias="metrics", default=None
    )
