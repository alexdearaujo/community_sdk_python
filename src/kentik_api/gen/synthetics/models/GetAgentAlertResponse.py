from typing import Optional

from pydantic import BaseModel, Field

from .AgentAlert import AgentAlert


class GetAgentAlertResponse(BaseModel):
    """
    GetAgentAlertResponse model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    agentAlert: Optional[AgentAlert] = Field(
        validation_alias="agentAlert", default=None
    )
