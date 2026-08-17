from pydantic import BaseModel


class PolicyServiceEnableBody(BaseModel):
    """
    PolicyServiceEnableBody model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}
