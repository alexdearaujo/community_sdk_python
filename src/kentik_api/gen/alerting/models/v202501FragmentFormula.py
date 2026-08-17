from typing import List, Optional

from pydantic import BaseModel, Field

from .v202501FragmentPredicateGroup import v202501FragmentPredicateGroup


class v202501FragmentFormula(BaseModel):
    """
    v202501FragmentFormula model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    or_: Optional[List[Optional[v202501FragmentPredicateGroup]]] = Field(
        validation_alias="or", default=None
    )
