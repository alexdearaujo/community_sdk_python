from typing import List, Optional

from pydantic import BaseModel, Field

from .PolicyDataSourcesDeviceTag import PolicyDataSourcesDeviceTag


class PolicyDataSources(BaseModel):
    """
    PolicyDataSources model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    allDevices: Optional[bool] = Field(validation_alias="allDevices", default=None)

    deviceIds: Optional[List[str]] = Field(validation_alias="deviceIds", default=None)

    labelIds: Optional[List[str]] = Field(validation_alias="labelIds", default=None)

    siteIds: Optional[List[str]] = Field(validation_alias="siteIds", default=None)

    types: Optional[List[str]] = Field(validation_alias="types", default=None)

    deviceTags: Optional[List[Optional[PolicyDataSourcesDeviceTag]]] = Field(
        validation_alias="deviceTags", default=None
    )
