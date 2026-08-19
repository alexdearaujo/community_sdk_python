# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Optional

from pydantic import BaseModel, Field

from .GenericEvent import GenericEvent


class AuditEvent(BaseModel):
    """
    AuditEvent model
    AuditEvent represents an audit event with request and enriched contextual information.
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    userId: Optional[str] = Field(validation_alias="userId", default=None)

    id: Optional[str] = Field(validation_alias="id", default=None)

    ctime: Optional[str] = Field(validation_alias="ctime", default=None)

    apiMethod: Optional[str] = Field(validation_alias="apiMethod", default=None)

    apiPath: Optional[str] = Field(validation_alias="apiPath", default=None)

    ipAddress: Optional[str] = Field(validation_alias="ipAddress", default=None)

    authority: Optional[str] = Field(validation_alias="authority", default=None)

    kentikUserId: Optional[str] = Field(validation_alias="kentikUserId", default=None)

    kentikUserEmail: Optional[str] = Field(
        validation_alias="kentikUserEmail", default=None
    )

    objectType: Optional[str] = Field(validation_alias="objectType", default=None)

    objectName: Optional[str] = Field(validation_alias="objectName", default=None)

    apiAction: Optional[str] = Field(validation_alias="apiAction", default=None)

    source: Optional[str] = Field(validation_alias="source", default=None)

    objectId: Optional[str] = Field(validation_alias="objectId", default=None)

    parentId: Optional[str] = Field(validation_alias="parentId", default=None)

    portalPath: Optional[str] = Field(validation_alias="portalPath", default=None)

    generic: Optional[GenericEvent] = Field(validation_alias="generic", default=None)

    titleField: Optional[str] = Field(validation_alias="titleField", default=None)

    eventPayload: Optional[str] = Field(validation_alias="eventPayload", default=None)

    userAgent: Optional[str] = Field(validation_alias="userAgent", default=None)
