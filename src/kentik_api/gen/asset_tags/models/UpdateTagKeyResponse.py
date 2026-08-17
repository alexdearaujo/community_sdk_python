from typing import Optional

from pydantic import BaseModel, Field

from .TagKey import TagKey


class UpdateTagKeyResponse(BaseModel):
    """
    UpdateTagKeyResponse model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    tagKey: Optional[TagKey] = Field(validation_alias="tagKey", default=None)
