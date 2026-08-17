from pydantic import BaseModel


class DeleteTenantUserResponse(BaseModel):
    """
    DeleteTenantUserResponse model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}
