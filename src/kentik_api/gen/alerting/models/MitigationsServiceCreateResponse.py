from typing import Optional

from pydantic import BaseModel, Field


class MitigationsServiceCreateResponse(BaseModel):
    """
    MitigationsServiceCreateResponse model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    id: Optional[str] = Field(validation_alias="id", default=None)
