from typing import List, Optional

from pydantic import BaseModel, Field

from .labelv202210Label import labelv202210Label


class ListLabelsResponse(BaseModel):
    """
    ListLabelsResponse model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    labels: Optional[List[Optional[labelv202210Label]]] = Field(
        validation_alias="labels", default=None
    )

    invalidCount: Optional[int] = Field(validation_alias="invalidCount", default=None)
