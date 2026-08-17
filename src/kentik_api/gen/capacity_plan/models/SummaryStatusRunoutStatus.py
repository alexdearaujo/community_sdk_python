from typing import Optional

from pydantic import BaseModel, Field


class SummaryStatusRunoutStatus(BaseModel):
    """
    RunoutStatus model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    status: Optional[str] = Field(validation_alias="status", default=None)

    earliestDate: Optional[str] = Field(validation_alias="earliestDate", default=None)
