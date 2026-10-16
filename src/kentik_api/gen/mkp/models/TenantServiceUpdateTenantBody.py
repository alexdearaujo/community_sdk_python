# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Any, Dict, Optional

from pydantic import BaseModel, Field


class TenantServiceUpdateTenantBody(BaseModel):
    """
    UpdateTenantRequest model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    tenant: Optional[Dict[str, Any]] = Field(validation_alias="tenant", default=None)
