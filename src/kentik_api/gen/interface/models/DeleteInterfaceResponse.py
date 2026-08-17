from pydantic import BaseModel


class DeleteInterfaceResponse(BaseModel):
    """
    DeleteInterfaceResponse model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}
