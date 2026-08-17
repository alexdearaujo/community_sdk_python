from pydantic import BaseModel, Field

from .AggregationType import AggregationType
from .BaselineConfigCompareMode import BaselineConfigCompareMode


class FlowPolicySettingsBaselineConfig(BaseModel):
    """
    FlowPolicySettingsBaselineConfig model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    storedKeyCount: str = Field(validation_alias="storedKeyCount")

    windowLength: str = Field(validation_alias="windowLength")

    windowStartOffset: str = Field(validation_alias="windowStartOffset")

    rollupAggregation: AggregationType = Field(validation_alias="rollupAggregation")

    compareMode: BaselineConfigCompareMode = Field(validation_alias="compareMode")

    neighbourhoodRadius: str = Field(validation_alias="neighbourhoodRadius")

    neighbourhoodAggregation: AggregationType = Field(
        validation_alias="neighbourhoodAggregation"
    )

    finalAggregation: AggregationType = Field(validation_alias="finalAggregation")
