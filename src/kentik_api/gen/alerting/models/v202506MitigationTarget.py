from typing import Optional

from pydantic import BaseModel, Field

from .v202303KeyValue import v202303KeyValue
from .v202501FlowspecMatch import v202501FlowspecMatch


class v202506MitigationTarget(BaseModel):
    """
    v202506MitigationTarget model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    ipCidr: Optional[str] = Field(validation_alias="ipCidr", default=None)

    flowspec: Optional[v202501FlowspecMatch] = Field(
        validation_alias="flowspec", default=None
    )

    adaptiveFlowspec: Optional[v202303KeyValue] = Field(
        validation_alias="adaptiveFlowspec", default=None
    )
