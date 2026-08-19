# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import List, Optional

from pydantic import BaseModel, Field

from .v202501TCPFlagsPredicateGroup import v202501TCPFlagsPredicateGroup


class v202501TCPFlagsFormula(BaseModel):
    """
    v202501TCPFlagsFormula model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    or_: Optional[List[Optional[v202501TCPFlagsPredicateGroup]]] = Field(
        validation_alias="or", default=None
    )
