# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import List, Optional

from pydantic import BaseModel, Field

from .CapacitySummary import CapacitySummary


class ListCapacitySummariesResponse(BaseModel):
    """
    ListCapacitySummariesResponse model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    capacity: Optional[List[Optional[CapacitySummary]]] = Field(
        validation_alias="capacity", default=None
    )

    invalidCount: Optional[int] = Field(validation_alias="invalidCount", default=None)
