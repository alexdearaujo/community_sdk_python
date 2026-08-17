from pydantic import BaseModel


class DeleteTestResponse(BaseModel):
    """
    DeleteTestResponse model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}
