from typing import List, Optional

from pydantic import BaseModel, Field

from .ASGroupDetailed import ASGroupDetailed


class ListASGroupsResponse(BaseModel):
    """
    ListASGroupsResponse model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    asGroups: Optional[List[Optional[ASGroupDetailed]]] = Field(
        validation_alias="asGroups", default=None
    )

    invalidCount: Optional[int] = Field(validation_alias="invalidCount", default=None)
