from typing import Optional

from pydantic import BaseModel, Field

from .Mitigation import Mitigation


class MitigationsServiceGetResponse(BaseModel):
    """
    MitigationsServiceGetResponse model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    mitigation: Optional[Mitigation] = Field(
        validation_alias="mitigation", default=None
    )
