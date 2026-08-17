from pydantic import BaseModel


class ResetActiveSessionsResponse(BaseModel):
    """
    ResetActiveSessionsResponse model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}
