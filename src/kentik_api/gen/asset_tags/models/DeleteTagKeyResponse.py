from pydantic import BaseModel


class DeleteTagKeyResponse(BaseModel):
    """
    {.Name} model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}
