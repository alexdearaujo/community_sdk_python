# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from pydantic import BaseModel, Field


class ServiceNowContext(BaseModel):
    """
    ServiceNowContext model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    incidentId: str = Field(validation_alias="incidentId")

    incidentUrl: str = Field(validation_alias="incidentUrl")
