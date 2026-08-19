# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Optional

from pydantic import BaseModel, Field


class MetricData(BaseModel):
    """
    MetricData model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    current: Optional[int] = Field(validation_alias="current", default=None)

    rollingAvg: Optional[int] = Field(validation_alias="rollingAvg", default=None)

    rollingStddev: Optional[int] = Field(validation_alias="rollingStddev", default=None)

    health: Optional[str] = Field(validation_alias="health", default=None)
