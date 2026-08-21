# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

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
