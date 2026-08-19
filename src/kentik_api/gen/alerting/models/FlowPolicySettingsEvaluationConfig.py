# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from pydantic import BaseModel, Field


class FlowPolicySettingsEvaluationConfig(BaseModel):
    """
    FlowPolicySettingsEvaluationConfig model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    frequency: str = Field(validation_alias="frequency")

    keyCount: str = Field(validation_alias="keyCount")
