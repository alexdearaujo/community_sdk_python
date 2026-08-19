# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import List, Optional

from pydantic import BaseModel, Field

from .CloudSubnet import CloudSubnet


class NetworkClass(BaseModel):
    """
    NetworkClass model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    internalAsns: Optional[List[str]] = Field(
        validation_alias="internalAsns", default=None
    )

    internalIps: Optional[List[str]] = Field(
        validation_alias="internalIps", default=None
    )

    usePrivateAsns: Optional[bool] = Field(
        validation_alias="usePrivateAsns", default=None
    )

    usePrivateSubnets: Optional[bool] = Field(
        validation_alias="usePrivateSubnets", default=None
    )

    cloudSubnets: Optional[List[Optional[CloudSubnet]]] = Field(
        validation_alias="cloudSubnets", default=None
    )
