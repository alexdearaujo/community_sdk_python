from typing import Any, Dict, Optional

from pydantic import BaseModel, Field


class TenantServiceUpdateTenantBody(BaseModel):
    """
    UpdateTenantRequest model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    tenant: Optional[Dict[str, Any]] = Field(validation_alias="tenant", default=None)
