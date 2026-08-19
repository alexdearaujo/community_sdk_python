# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import List, Optional

from pydantic import BaseModel, Field


class CustomApplication(BaseModel):
    """
    CustomApplication model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    id: Optional[str] = Field(validation_alias="id", default=None)

    name: str = Field(validation_alias="name")

    description: Optional[str] = Field(validation_alias="description", default=None)

    ipRange: Optional[List[str]] = Field(validation_alias="ipRange", default=None)

    protocol: Optional[List[int]] = Field(validation_alias="protocol", default=None)

    port: Optional[List[int]] = Field(validation_alias="port", default=None)

    asn: Optional[List[int]] = Field(validation_alias="asn", default=None)

    createdDate: Optional[str] = Field(validation_alias="createdDate", default=None)

    updatedDate: Optional[str] = Field(validation_alias="updatedDate", default=None)

    userId: Optional[str] = Field(validation_alias="userId", default=None)
