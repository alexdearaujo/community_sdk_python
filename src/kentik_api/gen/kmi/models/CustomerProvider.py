from typing import Optional

from pydantic import BaseModel, Field


class CustomerProvider(BaseModel):
    """
    CustomerProvider model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    asn: Optional[int] = Field(validation_alias="asn", default=None)

    name: Optional[str] = Field(validation_alias="name", default=None)

    score: Optional[int] = Field(validation_alias="score", default=None)

    singlehomedCustomer: Optional[bool] = Field(
        validation_alias="singlehomedCustomer", default=None
    )

    mutualCustomer: Optional[bool] = Field(
        validation_alias="mutualCustomer", default=None
    )

    mutualProvider: Optional[bool] = Field(
        validation_alias="mutualProvider", default=None
    )
