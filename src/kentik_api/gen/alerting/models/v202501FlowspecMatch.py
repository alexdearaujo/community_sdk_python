from typing import Optional

from pydantic import BaseModel, Field

from .v202501FragmentFormula import v202501FragmentFormula
from .v202501NumericFormula import v202501NumericFormula
from .v202501TCPFlagsFormula import v202501TCPFlagsFormula


class v202501FlowspecMatch(BaseModel):
    """
    v202501FlowspecMatch model
    FlowspecMatch represents the traffic filtering criteria encoded
    as Flow Specification NLRI as per RFC 8955:
    https://datatracker.ietf.org/doc/html/rfc8955#name-dissemination-of-ipv4-flow-
    and other related documents.
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    dstPrefix: Optional[str] = Field(validation_alias="dstPrefix", default=None)

    srcPrefix: Optional[str] = Field(validation_alias="srcPrefix", default=None)

    ipProtocol: Optional[v202501NumericFormula] = Field(
        validation_alias="ipProtocol", default=None
    )

    dstPort: Optional[v202501NumericFormula] = Field(
        validation_alias="dstPort", default=None
    )

    srcPort: Optional[v202501NumericFormula] = Field(
        validation_alias="srcPort", default=None
    )

    icmpType: Optional[v202501NumericFormula] = Field(
        validation_alias="icmpType", default=None
    )

    icmpCode: Optional[v202501NumericFormula] = Field(
        validation_alias="icmpCode", default=None
    )

    tcpFlags: Optional[v202501TCPFlagsFormula] = Field(
        validation_alias="tcpFlags", default=None
    )

    packetLength: Optional[v202501NumericFormula] = Field(
        validation_alias="packetLength", default=None
    )

    dscp: Optional[v202501NumericFormula] = Field(validation_alias="dscp", default=None)

    fragments: Optional[v202501FragmentFormula] = Field(
        validation_alias="fragments", default=None
    )
