from typing import List, Optional

from pydantic import BaseModel, Field

from .PathTrace import PathTrace
from .Stats import Stats


class Path(BaseModel):
    """
    Path model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    agentId: Optional[str] = Field(validation_alias="agentId", default=None)

    targetIp: Optional[str] = Field(validation_alias="targetIp", default=None)

    hopCount: Optional[Stats] = Field(validation_alias="hopCount", default=None)

    maxAsPathLength: Optional[int] = Field(
        validation_alias="maxAsPathLength", default=None
    )

    traces: Optional[List[Optional[PathTrace]]] = Field(
        validation_alias="traces", default=None
    )

    time: Optional[str] = Field(validation_alias="time", default=None)
