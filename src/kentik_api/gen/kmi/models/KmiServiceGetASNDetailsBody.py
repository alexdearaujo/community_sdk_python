from typing import Optional

from pydantic import BaseModel, Field


class KmiServiceGetASNDetailsBody(BaseModel):
    """
    GetASNDetailsRequest model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    ip: Optional[str] = Field(validation_alias="ip", default=None)

    mutualProvider: Optional[str] = Field(
        validation_alias="mutualProvider", default=None
    )

    mutualCustomer: Optional[str] = Field(
        validation_alias="mutualCustomer", default=None
    )

    singlehomedCustomer: Optional[str] = Field(
        validation_alias="singlehomedCustomer", default=None
    )
