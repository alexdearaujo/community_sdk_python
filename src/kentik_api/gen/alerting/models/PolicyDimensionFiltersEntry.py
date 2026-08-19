# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Optional

from pydantic import BaseModel, Field

from .PolicyDimensionFiltersEntryStringArray import (
    PolicyDimensionFiltersEntryStringArray,
)


class PolicyDimensionFiltersEntry(BaseModel):
    """
    PolicyDimensionFiltersEntry model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    not_: Optional[bool] = Field(validation_alias="not", default=None)

    dimension: Optional[str] = Field(validation_alias="dimension", default=None)

    equalsAny: Optional[PolicyDimensionFiltersEntryStringArray] = Field(
        validation_alias="equalsAny", default=None
    )

    matchesAny: Optional[PolicyDimensionFiltersEntryStringArray] = Field(
        validation_alias="matchesAny", default=None
    )
