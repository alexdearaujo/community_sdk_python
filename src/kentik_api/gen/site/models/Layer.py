from typing import List, Optional

from pydantic import BaseModel, Field


class Layer(BaseModel):
    """
    Layer model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    name: Optional[str] = Field(validation_alias="name", default=None)

    deviceIds: Optional[List[str]] = Field(validation_alias="deviceIds", default=None)
