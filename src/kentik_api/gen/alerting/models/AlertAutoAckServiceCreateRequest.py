from pydantic import BaseModel, Field

from .AlertAutoAck import AlertAutoAck


class AlertAutoAckServiceCreateRequest(BaseModel):
    """
    AlertAutoAckServiceCreateRequest model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    autoAck: AlertAutoAck = Field(validation_alias="autoAck")
