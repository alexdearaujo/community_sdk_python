# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import List, Optional

from pydantic import BaseModel, Field

from .Site import Site


class ListSitesResponse(BaseModel):
    """
    ListSitesResponse model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    sites: Optional[List[Optional[Site]]] = Field(
        validation_alias="sites", default=None
    )

    invalidCount: Optional[int] = Field(validation_alias="invalidCount", default=None)
