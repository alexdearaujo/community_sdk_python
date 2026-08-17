from typing import List, Optional

from pydantic import BaseModel, Field

from .FragmentPredicateGroup import FragmentPredicateGroup


class FragmentFormula(BaseModel):
    """
    FragmentFormula model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    or_: Optional[List[Optional[FragmentPredicateGroup]]] = Field(
        validation_alias="or", default=None
    )
