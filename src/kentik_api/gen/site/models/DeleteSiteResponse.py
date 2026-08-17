from pydantic import BaseModel


class DeleteSiteResponse(BaseModel):
    """
    DeleteSiteResponse model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}
