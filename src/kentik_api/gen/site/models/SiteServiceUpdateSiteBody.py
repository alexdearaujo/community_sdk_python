from typing import Any, Dict

from pydantic import BaseModel, Field


class SiteServiceUpdateSiteBody(BaseModel):
    """
    UpdateSiteRequest model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    site: Dict[str, Any] = Field(validation_alias="site")
