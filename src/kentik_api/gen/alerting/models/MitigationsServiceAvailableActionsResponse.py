from typing import List, Optional

from pydantic import BaseModel, Field

from .MitigationsServiceAvailableActionsResponseMitigationAvailableTransitions import (
    MitigationsServiceAvailableActionsResponseMitigationAvailableTransitions,
)


class MitigationsServiceAvailableActionsResponse(BaseModel):
    """
    MitigationsServiceAvailableActionsResponse model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    transitions: Optional[
        List[
            Optional[
                MitigationsServiceAvailableActionsResponseMitigationAvailableTransitions
            ]
        ]
    ] = Field(validation_alias="transitions", default=None)
