from pydantic import BaseModel, Field

from .v202303Afi import v202303Afi
from .v202303Safi import v202303Safi


class Nlri(BaseModel):
    """
    Nlri model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    afi: v202303Afi = Field(validation_alias="afi")

    safi: v202303Safi = Field(validation_alias="safi")

    prefix: str = Field(validation_alias="prefix")
