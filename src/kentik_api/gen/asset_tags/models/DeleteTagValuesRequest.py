from typing import List

from pydantic import BaseModel, Field

from .AssetType import AssetType


class DeleteTagValuesRequest(BaseModel):
    """
    DeleteTagValuesRequest model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    tagId: str = Field(validation_alias="tagId")

    assetType: AssetType = Field(validation_alias="assetType")

    assetIds: List[str] = Field(validation_alias="assetIds")
