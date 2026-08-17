from typing import Optional

from pydantic import BaseModel, Field


class EchoResponse(BaseModel):
    """
    EchoResponse model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    message: Optional[str] = Field(validation_alias="message", default=None)
