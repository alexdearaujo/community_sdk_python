from typing import Optional

from pydantic import BaseModel, Field


class FlowContextMetricValue(BaseModel):
    """
    FlowContextMetricValue model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    name: Optional[str] = Field(validation_alias="name", default=None)

    value: Optional[float] = Field(validation_alias="value", default=None)
