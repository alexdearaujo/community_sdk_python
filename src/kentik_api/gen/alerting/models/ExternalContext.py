from pydantic import BaseModel, Field

from .JiraCloudContext import JiraCloudContext
from .ServiceNowContext import ServiceNowContext


class ExternalContext(BaseModel):
    """
    ExternalContext model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    servicenow: ServiceNowContext = Field(validation_alias="servicenow")

    jiraCloud: JiraCloudContext = Field(validation_alias="jiraCloud")
