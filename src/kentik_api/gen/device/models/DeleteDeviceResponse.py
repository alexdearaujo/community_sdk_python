from pydantic import BaseModel


class DeleteDeviceResponse(BaseModel):
    """
    DeleteDeviceResponse model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}
