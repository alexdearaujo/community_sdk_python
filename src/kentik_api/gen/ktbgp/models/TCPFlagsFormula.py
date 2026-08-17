from typing import List, Optional

from pydantic import BaseModel, Field

from .TCPFlagsPredicateGroup import TCPFlagsPredicateGroup


class TCPFlagsFormula(BaseModel):
    """
    TCPFlagsFormula model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    or_: Optional[List[Optional[TCPFlagsPredicateGroup]]] = Field(
        validation_alias="or", default=None
    )
