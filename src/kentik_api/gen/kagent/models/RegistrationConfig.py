# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import List, Optional

from pydantic import BaseModel, Field


class RegistrationConfig(BaseModel):
    """
    RegistrationConfig model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    expiresAt: Optional[str] = Field(validation_alias="expiresAt", default=None)

    allowedPrivateCidrs: Optional[List[str]] = Field(
        validation_alias="allowedPrivateCidrs", default=None
    )

    allowedPublicCidrs: Optional[List[str]] = Field(
        validation_alias="allowedPublicCidrs", default=None
    )
