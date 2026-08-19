# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Optional

from pydantic import BaseModel, Field

from .v202501NumericOp import v202501NumericOp


class v202501NumericPredicate(BaseModel):
    """
    v202501NumericPredicate model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    operator: Optional[v202501NumericOp] = Field(
        validation_alias="operator", default=None
    )

    value: Optional[str] = Field(validation_alias="value", default=None)
