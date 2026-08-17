from typing import List, Optional

from pydantic import BaseModel, Field

from .CostProviderSummary import CostProviderSummary


class ListCostProviderSummariesResponse(BaseModel):
    """
    ListCostProviderSummariesResponse model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    providers: Optional[List[Optional[CostProviderSummary]]] = Field(
        validation_alias="providers", default=None
    )

    invalidCount: Optional[int] = Field(validation_alias="invalidCount", default=None)
