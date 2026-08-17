from typing import List, Optional

from pydantic import BaseModel, Field

from .DimensionField import DimensionField
from .MeasurementFamily import MeasurementFamily
from .MetricField import MetricField


class MeasurementDetail(BaseModel):
    """
    MeasurementDetail model
        Full detail for a single measurement (e.g. a traffic flow table or NMS measurement).
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    name: Optional[str] = Field(validation_alias="name", default=None)

    displayName: Optional[str] = Field(validation_alias="displayName", default=None)

    family: Optional[MeasurementFamily] = Field(validation_alias="family", default=None)

    description: Optional[str] = Field(validation_alias="description", default=None)

    lastSeen: Optional[str] = Field(validation_alias="lastSeen", default=None)

    dimensions: Optional[List[Optional[DimensionField]]] = Field(
        validation_alias="dimensions", default=None
    )

    metrics: Optional[List[Optional[MetricField]]] = Field(
        validation_alias="metrics", default=None
    )
