from pydantic import BaseModel


class UpdateAddressNamesResponse(BaseModel):
    """
    UpdateAddressNamesResponse model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}
