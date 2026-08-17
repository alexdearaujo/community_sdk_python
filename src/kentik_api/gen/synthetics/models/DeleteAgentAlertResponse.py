from pydantic import BaseModel


class DeleteAgentAlertResponse(BaseModel):
    """
    DeleteAgentAlertResponse model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}
