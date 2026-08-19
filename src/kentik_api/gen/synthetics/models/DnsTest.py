# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import List, Optional

from pydantic import BaseModel, Field

from .DNSRecord import DNSRecord


class DnsTest(BaseModel):
    """
    DnsTest model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    target: Optional[str] = Field(validation_alias="target", default=None)

    timeout: Optional[int] = Field(validation_alias="timeout", default=None)

    recordType: Optional[DNSRecord] = Field(validation_alias="recordType", default=None)

    servers: Optional[List[str]] = Field(validation_alias="servers", default=None)

    port: Optional[int] = Field(validation_alias="port", default=None)
