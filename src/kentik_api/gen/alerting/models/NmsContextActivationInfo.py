from typing import Optional

from pydantic import BaseModel, Field

from .NmsActivateOrClearConditions import NmsActivateOrClearConditions
from .v202303Severity import v202303Severity


class NmsContextActivationInfo(BaseModel):
    """
    NmsContextActivationInfo model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    activate: Optional[NmsActivateOrClearConditions] = Field(
        validation_alias="activate", default=None
    )

    severity: Optional[v202303Severity] = Field(
        validation_alias="severity", default=None
    )

    clearManual: Optional[bool] = Field(validation_alias="clearManual", default=None)

    clearUnlessActivated: Optional[bool] = Field(
        validation_alias="clearUnlessActivated", default=None
    )
