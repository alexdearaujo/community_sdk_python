# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import List, Optional

from pydantic import BaseModel, Field

from .AssetTagSelector import AssetTagSelector


class ScopeDimensions(BaseModel):
    """
    ScopeDimensions model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    sites: Optional[List[str]] = Field(validation_alias="sites", default=None)

    labels: Optional[List[str]] = Field(validation_alias="labels", default=None)

    assetTags: Optional[List[Optional[AssetTagSelector]]] = Field(
        validation_alias="assetTags", default=None
    )
