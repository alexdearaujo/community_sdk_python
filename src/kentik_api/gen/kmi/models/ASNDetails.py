from typing import List, Optional

from pydantic import BaseModel, Field

from .CustomerProvider import CustomerProvider
from .Peer import Peer


class ASNDetails(BaseModel):
    """
    ASNDetails model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    asn: Optional[int] = Field(validation_alias="asn", default=None)

    name: Optional[str] = Field(validation_alias="name", default=None)

    countryName: Optional[str] = Field(validation_alias="countryName", default=None)

    customers: Optional[List[Optional[CustomerProvider]]] = Field(
        validation_alias="customers", default=None
    )

    providers: Optional[List[Optional[CustomerProvider]]] = Field(
        validation_alias="providers", default=None
    )

    peers: Optional[List[Optional[Peer]]] = Field(
        validation_alias="peers", default=None
    )
