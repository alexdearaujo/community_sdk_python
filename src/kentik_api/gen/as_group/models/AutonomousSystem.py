from typing import Optional

from pydantic import BaseModel, Field


class AutonomousSystem(BaseModel):
    """
    AutonomousSystem model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    asn: Optional[int] = Field(validation_alias="asn", default=None)

    name: Optional[str] = Field(validation_alias="name", default=None)
