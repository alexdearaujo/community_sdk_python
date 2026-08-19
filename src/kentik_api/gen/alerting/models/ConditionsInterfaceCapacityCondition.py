# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Optional

from pydantic import BaseModel, Field


class ConditionsInterfaceCapacityCondition(BaseModel):
    """
    ConditionsInterfaceCapacityCondition model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    absolute: Optional[float] = Field(validation_alias="absolute", default=None)

    percentage: Optional[str] = Field(validation_alias="percentage", default=None)
