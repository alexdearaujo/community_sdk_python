from pydantic import BaseModel


class DeleteCloudExportResponse(BaseModel):
    """
    DeleteCloudExportResponse model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}
