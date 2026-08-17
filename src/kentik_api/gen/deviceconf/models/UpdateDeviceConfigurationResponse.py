from pydantic import BaseModel


class UpdateDeviceConfigurationResponse(BaseModel):
    """
    UpdateDeviceConfigurationResponse model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}
