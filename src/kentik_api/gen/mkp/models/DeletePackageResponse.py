from pydantic import BaseModel


class DeletePackageResponse(BaseModel):
    """
    DeletePackageResponse model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}
