# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import List, Optional

from pydantic import BaseModel, Field

from .v202211User import v202211User
from .v202312alpha1Secret import v202312alpha1Secret
from .v202312alpha1SecretType import v202312alpha1SecretType


class CredentialGroup(BaseModel):
    """
    CredentialGroup model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    id: Optional[str] = Field(validation_alias="id", default=None)

    name: Optional[str] = Field(validation_alias="name", default=None)

    version: int = Field(validation_alias="version")

    description: Optional[str] = Field(validation_alias="description", default=None)

    type: Optional[v202312alpha1SecretType] = Field(
        validation_alias="type", default=None
    )

    cdate: Optional[str] = Field(validation_alias="cdate", default=None)

    edate: Optional[str] = Field(validation_alias="edate", default=None)

    createdBy: Optional[v202211User] = Field(validation_alias="createdBy", default=None)

    credentials: Optional[List[Optional[v202312alpha1Secret]]] = Field(
        validation_alias="credentials", default=None
    )

    labels: Optional[List[str]] = Field(validation_alias="labels", default=None)
