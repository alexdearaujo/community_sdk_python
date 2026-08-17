from typing import List, Optional

from pydantic import BaseModel, Field

from .v202501NumericPredicateGroup import v202501NumericPredicateGroup


class v202501NumericFormula(BaseModel):
    """
    v202501NumericFormula model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    or_: Optional[List[Optional[v202501NumericPredicateGroup]]] = Field(
        validation_alias="or", default=None
    )
