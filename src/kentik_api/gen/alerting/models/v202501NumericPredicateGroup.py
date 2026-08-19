# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import List, Optional

from pydantic import BaseModel, Field

from .v202501NumericPredicate import v202501NumericPredicate


class v202501NumericPredicateGroup(BaseModel):
    """
    v202501NumericPredicateGroup model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    and_: Optional[List[Optional[v202501NumericPredicate]]] = Field(
        validation_alias="and", default=None
    )
