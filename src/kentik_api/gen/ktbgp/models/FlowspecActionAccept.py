from pydantic import BaseModel


class FlowspecActionAccept(BaseModel):
    """
        FlowspecActionAccept specifies that the traffic should be accepted.
    https://datatracker.ietf.org/doc/html/rfc8955 model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}
