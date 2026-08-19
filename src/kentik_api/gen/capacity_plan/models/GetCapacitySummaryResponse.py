# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Optional

from pydantic import BaseModel, Field

from .CapacitySummary import CapacitySummary


class GetCapacitySummaryResponse(BaseModel):
    """
    GetCapacitySummaryResponse model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    capacity: Optional[CapacitySummary] = Field(
        validation_alias="capacity", default=None
    )
