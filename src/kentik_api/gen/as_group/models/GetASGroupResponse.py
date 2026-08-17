from typing import Optional

from pydantic import BaseModel, Field

from .ASGroupDetailed import ASGroupDetailed


class GetASGroupResponse(BaseModel):
    """
    GetASGroupResponse model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    asGroup: Optional[ASGroupDetailed] = Field(validation_alias="asGroup", default=None)
