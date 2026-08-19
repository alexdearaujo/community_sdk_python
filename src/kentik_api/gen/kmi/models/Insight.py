# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Optional

from pydantic import BaseModel, Field


class Insight(BaseModel):
    """
    Insight model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    asn: Optional[int] = Field(validation_alias="asn", default=None)

    name: Optional[str] = Field(validation_alias="name", default=None)

    type: Optional[int] = Field(validation_alias="type", default=None)

    message: Optional[str] = Field(validation_alias="message", default=None)

    createdAt: Optional[str] = Field(validation_alias="createdAt", default=None)
