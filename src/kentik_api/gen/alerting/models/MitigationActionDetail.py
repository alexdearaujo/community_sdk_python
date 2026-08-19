# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import List, Optional

from pydantic import BaseModel, Field

from .MitigationState import MitigationState
from .MitigationUserAction import MitigationUserAction


class MitigationActionDetail(BaseModel):
    """
    MitigationActionDetail model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    eventName: Optional[str] = Field(validation_alias="eventName", default=None)

    action: Optional[MitigationUserAction] = Field(
        validation_alias="action", default=None
    )

    actionDescription: Optional[str] = Field(
        validation_alias="actionDescription", default=None
    )

    fromState: Optional[MitigationState] = Field(
        validation_alias="fromState", default=None
    )

    toStates: Optional[List[Optional[MitigationState]]] = Field(
        validation_alias="toStates", default=None
    )
