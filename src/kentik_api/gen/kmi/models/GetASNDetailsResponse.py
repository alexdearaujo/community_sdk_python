from typing import Optional

from pydantic import BaseModel, Field

from .ASNDetails import ASNDetails


class GetASNDetailsResponse(BaseModel):
    """
    GetASNDetailsResponse model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    asnDetails: Optional[ASNDetails] = Field(
        validation_alias="asnDetails", default=None
    )
