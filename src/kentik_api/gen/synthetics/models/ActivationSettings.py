from typing import Optional

from pydantic import BaseModel, Field


class ActivationSettings(BaseModel):
    """
    ActivationSettings model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    gracePeriod: Optional[str] = Field(validation_alias="gracePeriod", default=None)

    timeUnit: Optional[str] = Field(validation_alias="timeUnit", default=None)

    timeWindow: Optional[str] = Field(validation_alias="timeWindow", default=None)

    times: Optional[str] = Field(validation_alias="times", default=None)
