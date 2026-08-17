from typing import Optional

from pydantic import BaseModel, Field


class LabelConcise(BaseModel):
    """
    LabelConcise model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    id: Optional[int] = Field(validation_alias="id", default=None)
