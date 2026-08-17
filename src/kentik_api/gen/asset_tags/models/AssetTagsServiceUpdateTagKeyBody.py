from typing import Optional

from pydantic import BaseModel, Field


class AssetTagsServiceUpdateTagKeyBody(BaseModel):
    """
    UpdateTagKeyRequest model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    displayName: Optional[str] = Field(validation_alias="displayName", default=None)

    color: Optional[str] = Field(validation_alias="color", default=None)

    description: Optional[str] = Field(validation_alias="description", default=None)
