from pydantic import BaseModel, Field

from .Test import Test


class CreateTestRequest(BaseModel):
    """
    CreateTestRequest model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    test: Test = Field(validation_alias="test")
