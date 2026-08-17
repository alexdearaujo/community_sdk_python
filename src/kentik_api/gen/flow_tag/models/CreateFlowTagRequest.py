from typing import Optional

from pydantic import BaseModel, Field

from .FlowTag import FlowTag


class CreateFlowTagRequest(BaseModel):
    """
    CreateFlowTagRequest model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    flowTag: Optional[FlowTag] = Field(validation_alias="flowTag", default=None)
