from pydantic import BaseModel


class DeleteSavedFilterResponse(BaseModel):
    """
    DeleteSavedFilterResponse model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}
