# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import List, Optional

from pydantic import BaseModel, Field

from .LayerSet import LayerSet
from .PeeringDBSiteMapping import PeeringDBSiteMapping
from .PostalAddress import PostalAddress
from .SiteIpAddressClassification import SiteIpAddressClassification
from .SiteMarket import SiteMarket
from .SiteType import SiteType


class Site(BaseModel):
    """
    Site model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    id: Optional[str] = Field(validation_alias="id", default=None)

    title: str = Field(validation_alias="title")

    lat: Optional[float] = Field(validation_alias="lat", default=None)

    lon: Optional[float] = Field(validation_alias="lon", default=None)

    postalAddress: Optional[PostalAddress] = Field(
        validation_alias="postalAddress", default=None
    )

    type: SiteType = Field(validation_alias="type")

    addressClassification: Optional[SiteIpAddressClassification] = Field(
        validation_alias="addressClassification", default=None
    )

    architecture: Optional[List[Optional[LayerSet]]] = Field(
        validation_alias="architecture", default=None
    )

    siteMarket: Optional[SiteMarket] = Field(
        validation_alias="siteMarket", default=None
    )

    peeringdbSiteMapping: Optional[List[Optional[PeeringDBSiteMapping]]] = Field(
        validation_alias="peeringdbSiteMapping", default=None
    )
