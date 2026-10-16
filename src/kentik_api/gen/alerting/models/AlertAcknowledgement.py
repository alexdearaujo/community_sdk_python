# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Optional

from pydantic import BaseModel, Field

from .v202505AlertAcknowledgement import v202505AlertAcknowledgement


class AlertAcknowledgement(BaseModel):
    """
    AlertAcknowledgement model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    state: Optional[v202505AlertAcknowledgement] = Field(
        validation_alias="state", default=None
    )

    ackedByUser: Optional[str] = Field(validation_alias="ackedByUser", default=None)

    autoAckId: Optional[str] = Field(validation_alias="autoAckId", default=None)

    ackedAt: Optional[str] = Field(validation_alias="ackedAt", default=None)
