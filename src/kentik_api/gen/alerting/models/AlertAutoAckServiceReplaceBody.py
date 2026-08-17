from typing import Any, Dict

from pydantic import BaseModel, Field


class AlertAutoAckServiceReplaceBody(BaseModel):
    """
    AlertAutoAckServiceReplaceBody model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    autoAck: Dict[str, Any] = Field(validation_alias="autoAck")
