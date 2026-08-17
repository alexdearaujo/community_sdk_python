from typing import Optional

from pydantic import BaseModel, Field

from .FlowspecMatch import FlowspecMatch
from .RTBHMatch import RTBHMatch


class ktbgpv202501Withdraw(BaseModel):
    """
    ktbgpv202501Withdraw model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    flowspec: Optional[FlowspecMatch] = Field(validation_alias="flowspec", default=None)

    rtbh: Optional[RTBHMatch] = Field(validation_alias="rtbh", default=None)
