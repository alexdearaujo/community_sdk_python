from typing import List, Optional

from pydantic import BaseModel, Field

from .SavedFilterFilter import SavedFilterFilter
from .SavedFilterFilterId import SavedFilterFilterId


class SavedFilterFilterGroup(BaseModel):
    """
    SavedFilterFilterGroup model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    any: Optional[bool] = Field(validation_alias="any", default=None)

    filters: Optional[List[Optional[SavedFilterFilter]]] = Field(
        validation_alias="filters", default=None
    )

    not_: Optional[bool] = Field(validation_alias="not", default=None)

    savedFilterIds: Optional[List[Optional[SavedFilterFilterId]]] = Field(
        validation_alias="savedFilterIds", default=None
    )

    nestedFilterGroups: Optional[List[Optional["SavedFilterFilterGroup"]]] = Field(
        validation_alias="nestedFilterGroups", default=None
    )
