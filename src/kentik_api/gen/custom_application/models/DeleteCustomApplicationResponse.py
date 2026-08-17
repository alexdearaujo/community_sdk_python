from pydantic import BaseModel


class DeleteCustomApplicationResponse(BaseModel):
    """
    DeleteCustomApplicationResponse model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}
