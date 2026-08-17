from pydantic import BaseModel


class DeleteTenantResponse(BaseModel):
    """
    DeleteTenantResponse model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}
