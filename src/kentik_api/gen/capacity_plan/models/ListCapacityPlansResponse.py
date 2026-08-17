from typing import List, Optional

from pydantic import BaseModel, Field

from .CapacityPlan import CapacityPlan


class ListCapacityPlansResponse(BaseModel):
    """
    ListCapacityPlansResponse model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    capacity: Optional[List[Optional[CapacityPlan]]] = Field(
        validation_alias="capacity", default=None
    )

    invalidCount: Optional[int] = Field(validation_alias="invalidCount", default=None)
