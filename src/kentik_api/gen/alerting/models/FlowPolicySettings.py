# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from pydantic import BaseModel, Field

from .FlowPolicySettingsBaselineConfig import FlowPolicySettingsBaselineConfig
from .FlowPolicySettingsDatasetConfig import FlowPolicySettingsDatasetConfig
from .FlowPolicySettingsEvaluationConfig import FlowPolicySettingsEvaluationConfig


class FlowPolicySettings(BaseModel):
    """
    FlowPolicySettings model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    dataset: FlowPolicySettingsDatasetConfig = Field(validation_alias="dataset")

    evaluation: FlowPolicySettingsEvaluationConfig = Field(
        validation_alias="evaluation"
    )

    baseline: FlowPolicySettingsBaselineConfig = Field(validation_alias="baseline")
