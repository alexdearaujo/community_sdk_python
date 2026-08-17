from typing import Optional

from pydantic import BaseModel, Field

from .Policy import Policy


class PolicyServiceGetResponse(BaseModel):
    """
    PolicyServiceGetResponse model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    policy: Optional[Policy] = Field(validation_alias="policy", default=None)
