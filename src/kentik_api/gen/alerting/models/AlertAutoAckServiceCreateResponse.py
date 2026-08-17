from typing import Optional

from pydantic import BaseModel, Field

from .AlertAutoAck import AlertAutoAck


class AlertAutoAckServiceCreateResponse(BaseModel):
    """
    AlertAutoAckServiceCreateResponse model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    autoAck: Optional[AlertAutoAck] = Field(validation_alias="autoAck", default=None)
