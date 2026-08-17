from typing import List, Optional

from pydantic import BaseModel, Field

from .Alert import Alert
from .Asset import Asset
from .CustomDimension import CustomDimension
from .Devices import Devices
from .Filter import Filter
from .Package import Package
from .v202211User import v202211User


class Tenant(BaseModel):
    """
    Tenant model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    id: Optional[str] = Field(validation_alias="id", default=None)

    companyId: Optional[str] = Field(validation_alias="companyId", default=None)

    name: Optional[str] = Field(validation_alias="name", default=None)

    description: Optional[str] = Field(validation_alias="description", default=None)

    type: Optional[str] = Field(validation_alias="type", default=None)

    enabled: Optional[bool] = Field(validation_alias="enabled", default=None)

    alerts: Optional[List[Optional[Alert]]] = Field(
        validation_alias="alerts", default=None
    )

    assets: Optional[Asset] = Field(validation_alias="assets", default=None)

    asn: Optional[str] = Field(validation_alias="asn", default=None)

    cidr: Optional[str] = Field(validation_alias="cidr", default=None)

    customDimensions: Optional[List[Optional[CustomDimension]]] = Field(
        validation_alias="customDimensions", default=None
    )

    devices: Optional[Devices] = Field(validation_alias="devices", default=None)

    filters: Optional[Filter] = Field(validation_alias="filters", default=None)

    interfaceName: Optional[str] = Field(validation_alias="interfaceName", default=None)

    snmpAlias: Optional[str] = Field(validation_alias="snmpAlias", default=None)

    packages: Optional[List[Optional[Package]]] = Field(
        validation_alias="packages", default=None
    )

    users: Optional[List[Optional[v202211User]]] = Field(
        validation_alias="users", default=None
    )

    templateId: Optional[str] = Field(validation_alias="templateId", default=None)
