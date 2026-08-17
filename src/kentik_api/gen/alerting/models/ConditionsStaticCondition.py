from pydantic import BaseModel, Field

from .FlowPolicyLevelSettingsConditionsOperator import (
    FlowPolicyLevelSettingsConditionsOperator,
)


class ConditionsStaticCondition(BaseModel):
    """
    ConditionsStaticCondition model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    metric: str = Field(validation_alias="metric")

    operator: FlowPolicyLevelSettingsConditionsOperator = Field(
        validation_alias="operator"
    )

    value: float = Field(validation_alias="value")
