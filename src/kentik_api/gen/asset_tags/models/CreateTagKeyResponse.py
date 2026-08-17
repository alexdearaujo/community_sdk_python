from typing import Optional

from pydantic import BaseModel, Field

from .TagKey import TagKey


class CreateTagKeyResponse(BaseModel):
    """
    CreateTagKeyResponse model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    tagKey: Optional[TagKey] = Field(validation_alias="tagKey", default=None)
