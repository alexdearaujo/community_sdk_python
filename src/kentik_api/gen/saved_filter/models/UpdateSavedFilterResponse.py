from typing import Optional

from pydantic import BaseModel, Field

from .SavedFilter import SavedFilter


class UpdateSavedFilterResponse(BaseModel):
    """
    UpdateSavedFilterResponse model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    filter: Optional[SavedFilter] = Field(validation_alias="filter", default=None)
