from typing import List

from pydantic import BaseModel, Field

from .PolicyDataSources import PolicyDataSources
from .PolicyFilters import PolicyFilters


class FlowPolicySettingsDatasetConfig(BaseModel):
    """
    FlowPolicySettingsDatasetConfig model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    sources: PolicyDataSources = Field(validation_alias="sources")

    filters: PolicyFilters = Field(validation_alias="filters")

    dimensions: List[str] = Field(validation_alias="dimensions")

    metrics: List[str] = Field(validation_alias="metrics")
