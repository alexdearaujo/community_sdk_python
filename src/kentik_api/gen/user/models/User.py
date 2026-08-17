from typing import List, Optional

from pydantic import BaseModel, Field

from .LandingType import LandingType
from .PermissionEntry import PermissionEntry
from .Role import Role


class User(BaseModel):
    """
    User model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    id: Optional[str] = Field(validation_alias="id", default=None)

    userEmail: str = Field(validation_alias="userEmail")

    userFullName: str = Field(validation_alias="userFullName")

    role: Role = Field(validation_alias="role")

    permissions: Optional[List[Optional[PermissionEntry]]] = Field(
        validation_alias="permissions", default=None
    )

    filter: Optional[str] = Field(validation_alias="filter", default=None)

    lastLogin: Optional[str] = Field(validation_alias="lastLogin", default=None)

    cdate: Optional[str] = Field(validation_alias="cdate", default=None)

    edate: Optional[str] = Field(validation_alias="edate", default=None)

    defaultLandingPageType: Optional[LandingType] = Field(
        validation_alias="defaultLandingPageType", default=None
    )

    defaultLandingPageValue: Optional[str] = Field(
        validation_alias="defaultLandingPageValue", default=None
    )

    roles: Optional[List[str]] = Field(validation_alias="roles", default=None)

    roleSets: Optional[List[str]] = Field(validation_alias="roleSets", default=None)
