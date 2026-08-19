# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Optional

from pydantic import BaseModel, Field


class ScheduleSettings(BaseModel):
    """
    ScheduleSettings model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    enabled: Optional[bool] = Field(validation_alias="enabled", default=None)

    start: Optional[int] = Field(validation_alias="start", default=None)

    end: Optional[int] = Field(validation_alias="end", default=None)
