from pydantic import BaseModel


class RequestDeviceConfigurationFetchResponse(BaseModel):
    """
    RequestDeviceConfigurationFetchResponse model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}
