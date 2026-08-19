# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from pydantic import BaseModel, Field


class FlowPolicyLevelSettingsActivationSettings(BaseModel):
    """
    FlowPolicyLevelSettingsActivationSettings model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    matchTimes: str = Field(validation_alias="matchTimes")

    matchWindow: str = Field(validation_alias="matchWindow")

    resetCountWindow: str = Field(validation_alias="resetCountWindow")
