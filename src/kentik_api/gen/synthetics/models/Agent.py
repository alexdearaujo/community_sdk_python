from typing import List, Optional

from pydantic import BaseModel, Field

from .AgentMetadata import AgentMetadata
from .AgentStatus import AgentStatus
from .ImplementType import ImplementType
from .IPFamily import IPFamily


class Agent(BaseModel):
    """
    Agent model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    id: Optional[str] = Field(validation_alias="id", default=None)

    siteName: Optional[str] = Field(validation_alias="siteName", default=None)

    status: Optional[AgentStatus] = Field(validation_alias="status", default=None)

    alias: Optional[str] = Field(validation_alias="alias", default=None)

    type: Optional[str] = Field(validation_alias="type", default=None)

    os: Optional[str] = Field(validation_alias="os", default=None)

    ip: Optional[str] = Field(validation_alias="ip", default=None)

    lat: Optional[float] = Field(validation_alias="lat", default=None)

    long: Optional[float] = Field(validation_alias="long", default=None)

    lastAuthed: Optional[str] = Field(validation_alias="lastAuthed", default=None)

    family: Optional[IPFamily] = Field(validation_alias="family", default=None)

    asn: Optional[int] = Field(validation_alias="asn", default=None)

    siteId: Optional[str] = Field(validation_alias="siteId", default=None)

    version: Optional[str] = Field(validation_alias="version", default=None)

    city: Optional[str] = Field(validation_alias="city", default=None)

    region: Optional[str] = Field(validation_alias="region", default=None)

    country: Optional[str] = Field(validation_alias="country", default=None)

    testIds: Optional[List[str]] = Field(validation_alias="testIds", default=None)

    localIp: Optional[str] = Field(validation_alias="localIp", default=None)

    cloudRegion: Optional[str] = Field(validation_alias="cloudRegion", default=None)

    cloudProvider: Optional[str] = Field(validation_alias="cloudProvider", default=None)

    agentImpl: Optional[ImplementType] = Field(
        validation_alias="agentImpl", default=None
    )

    labels: Optional[List[str]] = Field(validation_alias="labels", default=None)

    metadata: Optional[AgentMetadata] = Field(validation_alias="metadata", default=None)
