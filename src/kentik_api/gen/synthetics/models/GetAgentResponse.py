from typing import Optional

from pydantic import BaseModel, Field

from .Agent import Agent


class GetAgentResponse(BaseModel):
    """
    GetAgentResponse model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    agent: Optional[Agent] = Field(validation_alias="agent", default=None)
