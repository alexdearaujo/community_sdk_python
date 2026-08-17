from typing import List, Optional

from pydantic import BaseModel, Field

from .PolicyDimensionFiltersConjunction import PolicyDimensionFiltersConjunction


class PolicyDimensionFilters(BaseModel):
    """
    PolicyDimensionFilters model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    conjunctions: Optional[List[Optional[PolicyDimensionFiltersConjunction]]] = Field(
        validation_alias="conjunctions", default=None
    )
