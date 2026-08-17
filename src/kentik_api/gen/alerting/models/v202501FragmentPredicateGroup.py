from typing import List, Optional

from pydantic import BaseModel, Field

from .v202501FragmentPredicate import v202501FragmentPredicate


class v202501FragmentPredicateGroup(BaseModel):
    """
    v202501FragmentPredicateGroup model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    and_: Optional[List[Optional[v202501FragmentPredicate]]] = Field(
        validation_alias="and", default=None
    )
