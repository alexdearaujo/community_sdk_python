# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import List, Optional

from pydantic import BaseModel, Field

from .TaskResults import TaskResults


class AgentResults(BaseModel):
    """
    AgentResults model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    agentId: Optional[str] = Field(validation_alias="agentId", default=None)

    health: Optional[str] = Field(validation_alias="health", default=None)

    tasks: Optional[List[Optional[TaskResults]]] = Field(
        validation_alias="tasks", default=None
    )
