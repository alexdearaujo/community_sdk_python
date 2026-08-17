from pydantic import BaseModel


class DeleteDeviceConfigurationResponse(BaseModel):
    """
    DeleteDeviceConfigurationResponse model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}
