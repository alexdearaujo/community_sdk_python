# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import List, Optional

from pydantic import BaseModel, Field

from .Populator import Populator


class CustomDimension(BaseModel):
    """
    CustomDimension model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    id: Optional[str] = Field(validation_alias="id", default=None)

    name: str = Field(validation_alias="name")

    type: str = Field(validation_alias="type")

    description: str = Field(validation_alias="description")

    populators: Optional[List[Optional[Populator]]] = Field(
        validation_alias="populators", default=None
    )

    companyId: Optional[str] = Field(validation_alias="companyId", default=None)

    createdDate: Optional[str] = Field(validation_alias="createdDate", default=None)

    updatedDate: Optional[str] = Field(validation_alias="updatedDate", default=None)
