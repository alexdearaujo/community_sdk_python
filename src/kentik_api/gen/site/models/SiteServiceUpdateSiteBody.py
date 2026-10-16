# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Any, Dict

from pydantic import BaseModel, Field


class SiteServiceUpdateSiteBody(BaseModel):
    """
    UpdateSiteRequest model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    site: Dict[str, Any] = Field(validation_alias="site")
