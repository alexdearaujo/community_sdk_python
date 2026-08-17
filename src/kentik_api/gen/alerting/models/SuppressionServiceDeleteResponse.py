from pydantic import BaseModel


class SuppressionServiceDeleteResponse(BaseModel):
    """
    SuppressionServiceDeleteResponse model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}
