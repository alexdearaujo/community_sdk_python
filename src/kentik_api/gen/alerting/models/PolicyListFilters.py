from typing import List, Optional

from pydantic import BaseModel, Field

from .Source import Source
from .v202303TimeRange import v202303TimeRange


class PolicyListFilters(BaseModel):
    """
    PolicyListFilters model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    sources: Optional[List[Optional[Source]]] = Field(
        validation_alias="sources", default=None
    )

    userIds: Optional[List[str]] = Field(validation_alias="userIds", default=None)

    createdAt: Optional[v202303TimeRange] = Field(
        validation_alias="createdAt", default=None
    )

    modifiedAt: Optional[v202303TimeRange] = Field(
        validation_alias="modifiedAt", default=None
    )
