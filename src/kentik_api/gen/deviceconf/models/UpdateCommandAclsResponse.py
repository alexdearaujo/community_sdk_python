from pydantic import BaseModel


class UpdateCommandAclsResponse(BaseModel):
    """
    UpdateCommandAclsResponse model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}
