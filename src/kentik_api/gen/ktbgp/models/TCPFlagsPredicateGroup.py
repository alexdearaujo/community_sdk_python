from typing import List, Optional

from pydantic import BaseModel, Field

from .TCPFlagsPredicate import TCPFlagsPredicate


class TCPFlagsPredicateGroup(BaseModel):
    """
    TCPFlagsPredicateGroup model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    and_: Optional[List[Optional[TCPFlagsPredicate]]] = Field(
        validation_alias="and", default=None
    )
