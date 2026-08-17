from typing import Optional

from pydantic import BaseModel, Field


class PolicyFiltersSavedFilter(BaseModel):
    """
    PolicyFiltersSavedFilter model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    id: Optional[str] = Field(validation_alias="id", default=None)

    not_: Optional[bool] = Field(validation_alias="not", default=None)
