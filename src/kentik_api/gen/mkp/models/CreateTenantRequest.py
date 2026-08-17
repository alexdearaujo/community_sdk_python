from typing import Optional

from pydantic import BaseModel, Field

from .Tenant import Tenant


class CreateTenantRequest(BaseModel):
    """
    CreateTenantRequest model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    tenant: Optional[Tenant] = Field(validation_alias="tenant", default=None)
