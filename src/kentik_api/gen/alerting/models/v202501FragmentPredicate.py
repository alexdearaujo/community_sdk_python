# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import List, Optional

from pydantic import BaseModel, Field

from .v202501BitwiseOp import v202501BitwiseOp
from .v202501Fragment import v202501Fragment


class v202501FragmentPredicate(BaseModel):
    """
    v202501FragmentPredicate model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    operator: Optional[v202501BitwiseOp] = Field(
        validation_alias="operator", default=None
    )

    values: Optional[List[Optional[v202501Fragment]]] = Field(
        validation_alias="values", default=None
    )
