# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import List, Optional

from pydantic import BaseModel, Field


class AssetTagSelector(BaseModel):
    """
    AssetTagSelector model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    tagId: str = Field(validation_alias="tagId")

    values: Optional[List[str]] = Field(validation_alias="values", default=None)
