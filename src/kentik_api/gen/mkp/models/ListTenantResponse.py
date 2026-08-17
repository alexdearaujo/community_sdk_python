from typing import List, Optional

from pydantic import BaseModel, Field

from .Tenant import Tenant


class ListTenantResponse(BaseModel):
    """
    ListTenantResponse model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    tenants: Optional[List[Optional[Tenant]]] = Field(
        validation_alias="tenants", default=None
    )

    invalidCount: Optional[int] = Field(validation_alias="invalidCount", default=None)
