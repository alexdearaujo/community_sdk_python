from typing import List, Optional

from pydantic import BaseModel, Field

from .NumericPredicate import NumericPredicate


class NumericPredicateGroup(BaseModel):
    """
    NumericPredicateGroup model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    and_: Optional[List[Optional[NumericPredicate]]] = Field(
        validation_alias="and", default=None
    )
