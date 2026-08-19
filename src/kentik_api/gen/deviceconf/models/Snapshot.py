# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Optional

from pydantic import BaseModel, Field

from .CommitDetails import CommitDetails
from .ConfigEncoding import ConfigEncoding
from .DevicePlatform import DevicePlatform
from .Revision import Revision


class Snapshot(BaseModel):
    """
    Snapshot model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    agentId: Optional[str] = Field(validation_alias="agentId", default=None)

    deviceId: Optional[str] = Field(validation_alias="deviceId", default=None)

    revision: Optional[Revision] = Field(validation_alias="revision", default=None)

    fetchError: Optional[bool] = Field(validation_alias="fetchError", default=None)

    encoding: Optional[ConfigEncoding] = Field(
        validation_alias="encoding", default=None
    )

    configData: Optional[str] = Field(validation_alias="configData", default=None)

    digest: Optional[str] = Field(validation_alias="digest", default=None)

    diffData: Optional[str] = Field(validation_alias="diffData", default=None)

    diffRevision: Optional[Revision] = Field(
        validation_alias="diffRevision", default=None
    )

    firstFetched: Optional[str] = Field(validation_alias="firstFetched", default=None)

    commitDetails: Optional[CommitDetails] = Field(
        validation_alias="commitDetails", default=None
    )

    platform: Optional[DevicePlatform] = Field(
        validation_alias="platform", default=None
    )
