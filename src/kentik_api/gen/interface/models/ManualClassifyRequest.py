from typing import List, Optional

from pydantic import BaseModel, Field

from .ConnectivityType import ConnectivityType
from .NetworkBoundary import NetworkBoundary


class ManualClassifyRequest(BaseModel):
    """
    ManualClassifyRequest model
        Set connection type, network boundary, and provider of interface id(s) specified.
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    interfaceIds: Optional[List[str]] = Field(
        validation_alias="interfaceIds", default=None
    )

    connectivityType: Optional[ConnectivityType] = Field(
        validation_alias="connectivityType", default=None
    )

    networkBoundary: Optional[NetworkBoundary] = Field(
        validation_alias="networkBoundary", default=None
    )

    provider: Optional[str] = Field(validation_alias="provider", default=None)
