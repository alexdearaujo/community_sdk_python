from typing import Optional

from pydantic import BaseModel, Field


class RTBHMatch(BaseModel):
    """
    RTBHMatch model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    srcPrefix: Optional[str] = Field(validation_alias="srcPrefix", default=None)
