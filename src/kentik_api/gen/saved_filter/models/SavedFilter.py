from typing import Optional

from pydantic import BaseModel, Field

from .FilterLevel import FilterLevel
from .SavedFilterFilters import SavedFilterFilters


class SavedFilter(BaseModel):
    """
    SavedFilter model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    id: Optional[str] = Field(validation_alias="id", default=None)

    filterName: str = Field(validation_alias="filterName")

    filterDescription: Optional[str] = Field(
        validation_alias="filterDescription", default=None
    )

    filters: Optional[SavedFilterFilters] = Field(
        validation_alias="filters", default=None
    )

    filterLevel: Optional[FilterLevel] = Field(
        validation_alias="filterLevel", default=None
    )

    createdDate: Optional[str] = Field(validation_alias="createdDate", default=None)

    updatedDate: Optional[str] = Field(validation_alias="updatedDate", default=None)
