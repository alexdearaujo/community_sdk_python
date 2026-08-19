# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Optional

from pydantic import BaseModel, Field


class devicev202504beta2Label(BaseModel):
    """
    Label model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    id: Optional[str] = Field(validation_alias="id", default=None)

    name: Optional[str] = Field(validation_alias="name", default=None)

    description: Optional[str] = Field(validation_alias="description", default=None)

    edate: Optional[str] = Field(validation_alias="edate", default=None)

    cdate: Optional[str] = Field(validation_alias="cdate", default=None)

    userId: Optional[str] = Field(validation_alias="userId", default=None)

    companyId: Optional[str] = Field(validation_alias="companyId", default=None)

    color: Optional[str] = Field(validation_alias="color", default=None)

    order: Optional[str] = Field(validation_alias="order", default=None)

    pivotDeviceId: Optional[str] = Field(validation_alias="pivotDeviceId", default=None)

    pivotLabelId: Optional[str] = Field(validation_alias="pivotLabelId", default=None)
