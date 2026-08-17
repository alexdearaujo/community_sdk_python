from pydantic import BaseModel


class DeleteUserResponse(BaseModel):
    """
    DeleteUserResponse model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}
