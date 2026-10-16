# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Optional

from pydantic import BaseModel, Field

from .HostMetadata import HostMetadata
from .InstallerType import InstallerType


class InstallConfig(BaseModel):
    """
    InstallConfig
    Describes an individual agent install configuration model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    id: Optional[str] = Field(validation_alias="id", default=None)

    type: Optional[InstallerType] = Field(validation_alias="type", default=None)

    hostMetadata: Optional[HostMetadata] = Field(
        validation_alias="hostMetadata", default=None
    )
