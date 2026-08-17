from typing import List, Optional

from pydantic import BaseModel, Field

from .v202501TCPFlagsPredicate import v202501TCPFlagsPredicate


class v202501TCPFlagsPredicateGroup(BaseModel):
    """
    v202501TCPFlagsPredicateGroup model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    and_: Optional[List[Optional[v202501TCPFlagsPredicate]]] = Field(
        validation_alias="and", default=None
    )
