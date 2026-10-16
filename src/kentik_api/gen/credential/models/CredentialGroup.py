# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import List, Optional

from pydantic import BaseModel, Field

from .Secret import Secret
from .SecretType import SecretType
from .User import User


class CredentialGroup(BaseModel):
    """
    CredentialGroup model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    id: Optional[str] = Field(validation_alias="id", default=None)

    name: Optional[str] = Field(validation_alias="name", default=None)

    version: int = Field(validation_alias="version", description="The secret's version")

    description: Optional[str] = Field(
        validation_alias="description",
        default=None,
        description="Purpose of this secret",
    )

    type: Optional[SecretType] = Field(validation_alias="type", default=None)

    cdate: Optional[str] = Field(validation_alias="cdate", default=None)

    edate: Optional[str] = Field(validation_alias="edate", default=None)

    createdBy: Optional[User] = Field(validation_alias="createdBy", default=None)

    credentials: Optional[List[Optional[Secret]]] = Field(
        validation_alias="credentials", default=None
    )

    labels: Optional[List[str]] = Field(validation_alias="labels", default=None)
