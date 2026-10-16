# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from pydantic import BaseModel, Field

from .PolicyDimensionFilters import PolicyDimensionFilters


class EventPolicyLevelSettings(BaseModel):
    """
    EventPolicyLevelSettings model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    filters: PolicyDimensionFilters = Field(validation_alias="filters")
