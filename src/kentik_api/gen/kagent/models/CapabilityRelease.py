# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import List, Optional

from pydantic import BaseModel, Field

from .CompatibilityInfo import CompatibilityInfo


class CapabilityRelease(BaseModel):
    """
    CapabilityRelease model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    capability: Optional[str] = Field(validation_alias="capability", default=None)

    semver: Optional[str] = Field(validation_alias="semver", default=None)

    downloadUrls: Optional[List[str]] = Field(
        validation_alias="downloadUrls", default=None
    )

    checksum: Optional[str] = Field(validation_alias="checksum", default=None)

    checksumAlgorithm: Optional[str] = Field(
        validation_alias="checksumAlgorithm", default=None
    )

    provenance: Optional[str] = Field(validation_alias="provenance", default=None)

    supportedDistros: Optional[List[str]] = Field(
        validation_alias="supportedDistros", default=None
    )

    compatibility: Optional[CompatibilityInfo] = Field(
        validation_alias="compatibility", default=None
    )
