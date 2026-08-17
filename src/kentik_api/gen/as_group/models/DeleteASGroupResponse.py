from pydantic import BaseModel


class DeleteASGroupResponse(BaseModel):
    """
    DeleteASGroupResponse model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}
