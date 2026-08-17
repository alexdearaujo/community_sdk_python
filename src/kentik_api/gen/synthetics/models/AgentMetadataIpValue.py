from typing import Optional

from pydantic import BaseModel, Field


class AgentMetadataIpValue(BaseModel):
    """
    AgentMetadataIpValue model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    value: Optional[str] = Field(validation_alias="value", default=None)
