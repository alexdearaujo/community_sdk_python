from pydantic import BaseModel


class DeleteSiteMarketResponse(BaseModel):
    """
    DeleteSiteMarketResponse model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}
