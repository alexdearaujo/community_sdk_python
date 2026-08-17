from pydantic import BaseModel


class DeleteCustomDimensionResponse(BaseModel):
    """
    DeleteCustomDimensionResponse model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}
