from pydantic import BaseModel


class AlertAutoAckServiceDeleteResponse(BaseModel):
    """
    AlertAutoAckServiceDeleteResponse model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}
