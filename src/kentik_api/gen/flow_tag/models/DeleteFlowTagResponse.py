from pydantic import BaseModel


class DeleteFlowTagResponse(BaseModel):
    """
    DeleteFlowTagResponse model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}
