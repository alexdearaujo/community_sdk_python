from pydantic import BaseModel, Field


class CreateChatSessionRequest(BaseModel):
    """
    CreateChatSessionRequest model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    prompt: str = Field(validation_alias="prompt")
