from typing import List, Optional

from pydantic import BaseModel, Field

from .SavedFilterFilterGroup import SavedFilterFilterGroup


class SavedFilterFilters(BaseModel):
    """
    SavedFilterFilters model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    any: Optional[bool] = Field(validation_alias="any", default=None)

    filterGroups: List[SavedFilterFilterGroup] = Field(validation_alias="filterGroups")
