from pydantic import BaseModel


class DeleteTagValuesResponse(BaseModel):
    """
    {.Name} model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}
