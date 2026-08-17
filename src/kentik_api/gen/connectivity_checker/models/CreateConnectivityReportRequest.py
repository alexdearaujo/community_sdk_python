from typing import Optional

from pydantic import BaseModel, Field

from .CloudProvider import CloudProvider
from .EntityType import EntityType


class CreateConnectivityReportRequest(BaseModel):
    """
    CreateConnectivityReportRequest model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    cloudProvider: CloudProvider = Field(validation_alias="cloudProvider")

    src: str = Field(validation_alias="src")

    dst: str = Field(validation_alias="dst")

    dstPort: str = Field(validation_alias="dstPort")

    protocol: str = Field(validation_alias="protocol")

    srcType: Optional[EntityType] = Field(validation_alias="srcType", default=None)

    dstType: Optional[EntityType] = Field(validation_alias="dstType", default=None)

    startTime: str = Field(validation_alias="startTime")

    endTime: str = Field(validation_alias="endTime")

    name: Optional[str] = Field(validation_alias="name", default=None)
