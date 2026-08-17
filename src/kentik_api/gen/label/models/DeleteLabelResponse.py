from pydantic import BaseModel


class DeleteLabelResponse(BaseModel):
    """
    DeleteLabelResponse model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}
