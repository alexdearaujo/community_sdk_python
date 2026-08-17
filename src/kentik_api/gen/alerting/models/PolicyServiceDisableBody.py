from pydantic import BaseModel


class PolicyServiceDisableBody(BaseModel):
    """
    PolicyServiceDisableBody model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}
