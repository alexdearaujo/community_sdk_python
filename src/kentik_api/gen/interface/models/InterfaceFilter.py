from typing import List, Optional

from pydantic import BaseModel, Field

from .ConnectivityType import ConnectivityType
from .IpFilter import IpFilter
from .NetworkBoundary import NetworkBoundary


class InterfaceFilter(BaseModel):
    """
    InterfaceFilter model
        Supports multiple search criteria. Fields are combined to AND statements to perform search.
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    text: Optional[str] = Field(validation_alias="text", default=None)

    deviceIds: Optional[List[str]] = Field(validation_alias="deviceIds", default=None)

    connectivityTypes: Optional[List[Optional[ConnectivityType]]] = Field(
        validation_alias="connectivityTypes", default=None
    )

    networkBoundaries: Optional[List[Optional[NetworkBoundary]]] = Field(
        validation_alias="networkBoundaries", default=None
    )

    providers: Optional[List[str]] = Field(validation_alias="providers", default=None)

    snmpSpeeds: Optional[List[int]] = Field(validation_alias="snmpSpeeds", default=None)

    ipTypes: Optional[List[Optional[IpFilter]]] = Field(
        validation_alias="ipTypes", default=None
    )
