from typing import Optional

from pydantic import BaseModel, Field


class Activate(BaseModel):
    """
    Activate model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    times: Optional[int] = Field(validation_alias="times", default=None)

    operator: Optional[str] = Field(validation_alias="operator", default=None)

    timeWindowSeconds: Optional[int] = Field(
        validation_alias="timeWindowSeconds", default=None
    )

    gracePeriodSeconds: Optional[int] = Field(
        validation_alias="gracePeriodSeconds", default=None
    )
