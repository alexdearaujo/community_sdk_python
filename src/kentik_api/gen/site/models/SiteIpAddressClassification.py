from typing import List, Optional

from pydantic import BaseModel, Field


class SiteIpAddressClassification(BaseModel):
    """
    SiteIpAddressClassification model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    infrastructureNetworks: Optional[List[str]] = Field(
        validation_alias="infrastructureNetworks", default=None
    )

    userAccessNetworks: Optional[List[str]] = Field(
        validation_alias="userAccessNetworks", default=None
    )

    otherNetworks: Optional[List[str]] = Field(
        validation_alias="otherNetworks", default=None
    )
