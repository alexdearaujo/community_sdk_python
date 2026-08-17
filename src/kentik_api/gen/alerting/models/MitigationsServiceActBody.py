from typing import List

from pydantic import BaseModel, Field


class MitigationsServiceActBody(BaseModel):
    """
    MitigationsServiceActBody model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    ids: List[str] = Field(validation_alias="ids")
