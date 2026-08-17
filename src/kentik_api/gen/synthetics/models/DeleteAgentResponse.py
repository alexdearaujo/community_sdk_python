from pydantic import BaseModel


class DeleteAgentResponse(BaseModel):
    """
    DeleteAgentResponse model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}
