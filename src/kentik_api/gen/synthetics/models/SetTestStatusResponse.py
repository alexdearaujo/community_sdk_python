from pydantic import BaseModel


class SetTestStatusResponse(BaseModel):
    """
    SetTestStatusResponse model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}
