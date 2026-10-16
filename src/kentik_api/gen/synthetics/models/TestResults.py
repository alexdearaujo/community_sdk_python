# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import List, Optional

from pydantic import BaseModel, Field

from .AgentResults import AgentResults


class TestResults(BaseModel):
    """
    TestResults model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    testId: Optional[str] = Field(validation_alias="testId", default=None)

    time: Optional[str] = Field(validation_alias="time", default=None)

    health: Optional[str] = Field(validation_alias="health", default=None)

    agents: Optional[List[Optional[AgentResults]]] = Field(
        validation_alias="agents", default=None
    )
