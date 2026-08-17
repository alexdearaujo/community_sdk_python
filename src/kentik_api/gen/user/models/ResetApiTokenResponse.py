from pydantic import BaseModel


class ResetApiTokenResponse(BaseModel):
    """
    ResetApiTokenResponse model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}
