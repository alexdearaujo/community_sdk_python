from typing import List, Optional

from pydantic import BaseModel, Field

from .Agent import Agent


class ListAgentsResponse(BaseModel):
    """
    ListAgentsResponse model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    agents: Optional[List[Optional[Agent]]] = Field(
        validation_alias="agents", default=None
    )

    invalidCount: Optional[int] = Field(validation_alias="invalidCount", default=None)
