from typing import Optional

from pydantic import BaseModel, Field


class PostalAddress(BaseModel):
    """
    PostalAddress model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    address: str = Field(validation_alias="address")

    city: str = Field(validation_alias="city")

    region: Optional[str] = Field(validation_alias="region", default=None)

    postalCode: Optional[str] = Field(validation_alias="postalCode", default=None)

    country: str = Field(validation_alias="country")
