from typing import List, Optional

from pydantic import BaseModel, Field

from .Market import Market


class ListMarketsResponse(BaseModel):
    """
    ListMarketsResponse model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    markets: Optional[List[Optional[Market]]] = Field(
        validation_alias="markets", default=None
    )
