from pydantic import BaseModel, Field


class JiraCloudContext(BaseModel):
    """
    JiraCloudContext model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    issueKey: str = Field(validation_alias="issueKey")

    issueUrl: str = Field(validation_alias="issueUrl")
