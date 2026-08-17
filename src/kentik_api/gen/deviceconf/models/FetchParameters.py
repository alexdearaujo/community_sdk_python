from typing import Optional

from pydantic import BaseModel, Field


class FetchParameters(BaseModel):
    """
    FetchParameters model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    fetchInterval: Optional[str] = Field(validation_alias="fetchInterval", default=None)

    fetchTimeout: Optional[str] = Field(validation_alias="fetchTimeout", default=None)
