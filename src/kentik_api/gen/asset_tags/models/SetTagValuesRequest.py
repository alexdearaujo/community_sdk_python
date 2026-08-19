# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import List

from pydantic import BaseModel, Field

from .AssetType import AssetType


class SetTagValuesRequest(BaseModel):
    """
    SetTagValuesRequest model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    tagId: str = Field(validation_alias="tagId")

    assetType: AssetType = Field(validation_alias="assetType")

    assetIds: List[str] = Field(validation_alias="assetIds")

    value: str = Field(validation_alias="value")
