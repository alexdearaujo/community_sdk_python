from typing import List

from pydantic import BaseModel, Field

from .FlowPolicyLevelSettingsActivationSettings import (
    FlowPolicyLevelSettingsActivationSettings,
)
from .FlowPolicyLevelSettingsConditions import FlowPolicyLevelSettingsConditions
from .FlowPolicyLevelSettingsMitigationAssociation import (
    FlowPolicyLevelSettingsMitigationAssociation,
)


class FlowPolicyLevelSettings(BaseModel):
    """
    FlowPolicyLevelSettings model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    conditions: List[FlowPolicyLevelSettingsConditions] = Field(
        validation_alias="conditions"
    )

    activation: FlowPolicyLevelSettingsActivationSettings = Field(
        validation_alias="activation"
    )

    mitigationAssociations: List[FlowPolicyLevelSettingsMitigationAssociation] = Field(
        validation_alias="mitigationAssociations"
    )
