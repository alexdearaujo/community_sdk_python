# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import List, Optional

from pydantic import BaseModel, Field

from .v202501BitwiseOp import v202501BitwiseOp
from .v202501TCPFlag import v202501TCPFlag


class v202501TCPFlagsPredicate(BaseModel):
    """
    v202501TCPFlagsPredicate model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    operator: Optional[v202501BitwiseOp] = Field(
        validation_alias="operator", default=None
    )

    values: Optional[List[Optional[v202501TCPFlag]]] = Field(
        validation_alias="values", default=None
    )
