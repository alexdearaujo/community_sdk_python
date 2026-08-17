from pydantic import BaseModel, Field


class UpdateChatSessionRequest(BaseModel):
    """
    UpdateChatSessionRequest model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    prompt: str = Field(validation_alias="prompt")

    id: str = Field(validation_alias="id")
