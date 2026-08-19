# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Optional

from pydantic import BaseModel, Field

from .BaselineConditionDeltaType import BaselineConditionDeltaType


class ConditionsBaselineCondition(BaseModel):
    """
    ConditionsBaselineCondition model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    absolute: Optional[float] = Field(validation_alias="absolute", default=None)

    percentage: Optional[str] = Field(validation_alias="percentage", default=None)

    delta: BaselineConditionDeltaType = Field(validation_alias="delta")

    useLowest: Optional[bool] = Field(validation_alias="useLowest", default=None)

    useHighest: Optional[bool] = Field(validation_alias="useHighest", default=None)

    useTrigger: Optional[bool] = Field(validation_alias="useTrigger", default=None)

    skip: Optional[bool] = Field(validation_alias="skip", default=None)

    useValue: Optional[str] = Field(validation_alias="useValue", default=None)
