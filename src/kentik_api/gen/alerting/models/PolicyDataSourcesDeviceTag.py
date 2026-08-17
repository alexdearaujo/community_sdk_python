from typing import List, Optional

from pydantic import BaseModel, Field


class PolicyDataSourcesDeviceTag(BaseModel):
    """
    PolicyDataSourcesDeviceTag model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    id: Optional[str] = Field(validation_alias="id", default=None)

    values: Optional[List[str]] = Field(validation_alias="values", default=None)
