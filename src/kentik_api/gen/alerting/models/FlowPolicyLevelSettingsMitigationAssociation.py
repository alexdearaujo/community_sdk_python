# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from pydantic import BaseModel, Field


class FlowPolicyLevelSettingsMitigationAssociation(BaseModel):
    """
    FlowPolicyLevelSettingsMitigationAssociation model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    platformId: str = Field(validation_alias="platformId")

    methodId: str = Field(validation_alias="methodId")
