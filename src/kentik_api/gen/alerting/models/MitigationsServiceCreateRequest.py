# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Optional

from pydantic import BaseModel, Field


class MitigationsServiceCreateRequest(BaseModel):
    """
    MitigationsServiceCreateRequest model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    platformId: str = Field(validation_alias="platformId")

    methodId: str = Field(validation_alias="methodId")

    ipCidr: str = Field(validation_alias="ipCidr")

    srcPort: Optional[str] = Field(validation_alias="srcPort", default=None)

    dstPort: Optional[str] = Field(validation_alias="dstPort", default=None)

    comment: Optional[str] = Field(validation_alias="comment", default=None)

    autoStopTtl: Optional[str] = Field(validation_alias="autoStopTtl", default=None)
