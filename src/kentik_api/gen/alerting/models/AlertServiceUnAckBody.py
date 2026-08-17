from pydantic import BaseModel


class AlertServiceUnAckBody(BaseModel):
    """
    AlertServiceUnAckBody model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}
