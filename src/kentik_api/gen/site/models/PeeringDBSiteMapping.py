# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Optional

from pydantic import BaseModel, Field


class PeeringDBSiteMapping(BaseModel):
    """
    PeeringDBSiteMapping model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    id: str = Field(validation_alias="id")

    siteId: str = Field(validation_alias="siteId")

    peeringdbFacId: str = Field(validation_alias="peeringdbFacId")

    edate: Optional[str] = Field(validation_alias="edate", default=None)

    cdate: Optional[str] = Field(validation_alias="cdate", default=None)

    companyId: Optional[str] = Field(validation_alias="companyId", default=None)
