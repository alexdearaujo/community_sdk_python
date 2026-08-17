from typing import Optional

from pydantic import BaseModel, Field

from .Site import Site


class GetSiteResponse(BaseModel):
    """
    GetSiteResponse model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    site: Optional[Site] = Field(validation_alias="site", default=None)
