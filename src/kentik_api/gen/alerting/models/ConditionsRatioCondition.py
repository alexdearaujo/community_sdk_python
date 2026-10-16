# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from pydantic import BaseModel, Field

from .RatioConditionDirection import RatioConditionDirection


class ConditionsRatioCondition(BaseModel):
    """
    ConditionsRatioCondition model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    lhsMetric: str = Field(validation_alias="lhsMetric")

    rhsMetric: str = Field(validation_alias="rhsMetric")

    lhsProportion: int = Field(validation_alias="lhsProportion")

    rhsProportion: int = Field(validation_alias="rhsProportion")

    margin: float = Field(validation_alias="margin")

    direction: RatioConditionDirection = Field(validation_alias="direction")
