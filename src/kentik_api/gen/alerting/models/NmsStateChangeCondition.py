from typing import Optional

from pydantic import BaseModel, Field

from .NmsStateSet import NmsStateSet


class NmsStateChangeCondition(BaseModel):
    """
    NmsStateChangeCondition model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    from_: Optional[NmsStateSet] = Field(validation_alias="from", default=None)

    to: Optional[NmsStateSet] = Field(validation_alias="to", default=None)
