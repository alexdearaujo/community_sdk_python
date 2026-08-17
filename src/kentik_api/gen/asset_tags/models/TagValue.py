from typing import Optional

from pydantic import BaseModel, Field

from .AssetType import AssetType


class TagValue(BaseModel):
    """
    TagValue model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    tagId: Optional[str] = Field(validation_alias="tagId", default=None)

    assetType: Optional[AssetType] = Field(validation_alias="assetType", default=None)

    assetId: Optional[str] = Field(validation_alias="assetId", default=None)

    value: Optional[str] = Field(validation_alias="value", default=None)
