# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Optional

from pydantic import BaseModel, Field


class TenantUser(BaseModel):
    """
    TenantUser model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    id: Optional[str] = Field(validation_alias="id", default=None)

    tenantId: str = Field(validation_alias="tenantId")

    userFullName: str = Field(validation_alias="userFullName")

    userEmail: str = Field(validation_alias="userEmail")
