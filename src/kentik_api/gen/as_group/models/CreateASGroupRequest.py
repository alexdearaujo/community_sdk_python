from pydantic import BaseModel, Field

from .ASGroupConcise import ASGroupConcise


class CreateASGroupRequest(BaseModel):
    """
    CreateASGroupRequest model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    asGroup: ASGroupConcise = Field(validation_alias="asGroup")
