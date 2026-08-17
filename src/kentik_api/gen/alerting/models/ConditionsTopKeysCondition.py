from pydantic import BaseModel, Field

from .TopKeysConditionTopKeysEvent import TopKeysConditionTopKeysEvent


class ConditionsTopKeysCondition(BaseModel):
    """
    ConditionsTopKeysCondition model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    event: TopKeysConditionTopKeysEvent = Field(validation_alias="event")

    count: str = Field(validation_alias="count")
