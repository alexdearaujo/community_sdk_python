# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import List, Optional

from pydantic import BaseModel, Field

from .PolicyDataSources import PolicyDataSources
from .PolicyFilters import PolicyFilters


class FlowPolicySettingsDatasetConfig(BaseModel):
    """
    FlowPolicySettingsDatasetConfig model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    sources: Optional[PolicyDataSources] = Field(
        validation_alias="sources", default=None
    )

    filters: Optional[PolicyFilters] = Field(validation_alias="filters", default=None)

    dimensions: List[str] = Field(validation_alias="dimensions")

    metrics: List[str] = Field(validation_alias="metrics")
