from typing import Optional

from pydantic import BaseModel, Field


class TenantLink(BaseModel):
    """
    TenantLink model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    id: Optional[str] = Field(validation_alias="id", default=None)

    pivotTemplateId: Optional[str] = Field(
        validation_alias="pivotTemplateId", default=None
    )

    pivotUserGroupId: Optional[str] = Field(
        validation_alias="pivotUserGroupId", default=None
    )
