from pydantic import BaseModel


class DeletePopulatorResponse(BaseModel):
    """
    DeletePopulatorResponse model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}
