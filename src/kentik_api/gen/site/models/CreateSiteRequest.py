from pydantic import BaseModel, Field

from .Site import Site


class CreateSiteRequest(BaseModel):
    """
    CreateSiteRequest model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    site: Site = Field(validation_alias="site")
