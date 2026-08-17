from typing import Optional

from pydantic import BaseModel, Field

from .Populator import Populator


class UpdatePopulatorResponse(BaseModel):
    """
    UpdatePopulatorResponse model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    populator: Optional[Populator] = Field(validation_alias="populator", default=None)
