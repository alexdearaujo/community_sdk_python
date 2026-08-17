from typing import List, Optional

from pydantic import BaseModel, Field

from .Alert import Alert
from .Asset import Asset
from .TenantLink import TenantLink


class Package(BaseModel):
    """
    Package model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    id: Optional[str] = Field(validation_alias="id", default=None)

    companyId: Optional[str] = Field(validation_alias="companyId", default=None)

    name: Optional[str] = Field(validation_alias="name", default=None)

    description: Optional[str] = Field(validation_alias="description", default=None)

    icon: Optional[str] = Field(validation_alias="icon", default=None)

    color: Optional[str] = Field(validation_alias="color", default=None)

    alerts: Optional[List[Optional[Alert]]] = Field(
        validation_alias="alerts", default=None
    )

    assets: Optional[Asset] = Field(validation_alias="assets", default=None)

    isDefault: Optional[bool] = Field(validation_alias="isDefault", default=None)

    tenants: Optional[List[Optional[TenantLink]]] = Field(
        validation_alias="tenants", default=None
    )
