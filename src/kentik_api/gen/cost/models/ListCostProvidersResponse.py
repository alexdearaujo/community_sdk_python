from typing import List, Optional

from pydantic import BaseModel, Field

from .CostProviderConcise import CostProviderConcise


class ListCostProvidersResponse(BaseModel):
    """
    ListCostProvidersResponse model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    providers: Optional[List[Optional[CostProviderConcise]]] = Field(
        validation_alias="providers", default=None
    )

    invalidCount: Optional[int] = Field(validation_alias="invalidCount", default=None)
