from typing import List, Optional

from pydantic import BaseModel, Field


class GetTraceForTestRequest(BaseModel):
    """
    GetTraceForTestRequest model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    id: Optional[str] = Field(validation_alias="id", default=None)

    startTime: str = Field(validation_alias="startTime")

    endTime: str = Field(validation_alias="endTime")

    agentIds: Optional[List[str]] = Field(validation_alias="agentIds", default=None)

    targetIps: Optional[List[str]] = Field(validation_alias="targetIps", default=None)
