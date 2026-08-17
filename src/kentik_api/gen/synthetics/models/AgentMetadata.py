from typing import List, Optional

from pydantic import BaseModel, Field

from .AgentMetadataIpValue import AgentMetadataIpValue


class AgentMetadata(BaseModel):
    """
    AgentMetadata model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    privateIpv4Addresses: Optional[List[Optional[AgentMetadataIpValue]]] = Field(
        validation_alias="privateIpv4Addresses", default=None
    )

    publicIpv4Addresses: Optional[List[Optional[AgentMetadataIpValue]]] = Field(
        validation_alias="publicIpv4Addresses", default=None
    )

    privateIpv6Addresses: Optional[List[Optional[AgentMetadataIpValue]]] = Field(
        validation_alias="privateIpv6Addresses", default=None
    )

    publicIpv6Addresses: Optional[List[Optional[AgentMetadataIpValue]]] = Field(
        validation_alias="publicIpv6Addresses", default=None
    )
