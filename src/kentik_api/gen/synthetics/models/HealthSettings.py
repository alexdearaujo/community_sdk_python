# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import List, Optional

from pydantic import BaseModel, Field

from .ActivationSettings import ActivationSettings
from .DisabledMetrics import DisabledMetrics


class HealthSettings(BaseModel):
    """
    HealthSettings model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    latencyCritical: Optional[float] = Field(
        validation_alias="latencyCritical", default=None
    )

    latencyWarning: Optional[float] = Field(
        validation_alias="latencyWarning", default=None
    )

    packetLossCritical: Optional[float] = Field(
        validation_alias="packetLossCritical", default=None
    )

    packetLossWarning: Optional[float] = Field(
        validation_alias="packetLossWarning", default=None
    )

    jitterCritical: Optional[float] = Field(
        validation_alias="jitterCritical", default=None
    )

    jitterWarning: Optional[float] = Field(
        validation_alias="jitterWarning", default=None
    )

    httpLatencyCritical: Optional[float] = Field(
        validation_alias="httpLatencyCritical", default=None
    )

    httpLatencyWarning: Optional[float] = Field(
        validation_alias="httpLatencyWarning", default=None
    )

    httpValidCodes: Optional[List[int]] = Field(
        validation_alias="httpValidCodes", default=None
    )

    dnsValidCodes: Optional[List[int]] = Field(
        validation_alias="dnsValidCodes", default=None
    )

    latencyCriticalStddev: Optional[float] = Field(
        validation_alias="latencyCriticalStddev", default=None
    )

    latencyWarningStddev: Optional[float] = Field(
        validation_alias="latencyWarningStddev", default=None
    )

    jitterCriticalStddev: Optional[float] = Field(
        validation_alias="jitterCriticalStddev", default=None
    )

    jitterWarningStddev: Optional[float] = Field(
        validation_alias="jitterWarningStddev", default=None
    )

    httpLatencyCriticalStddev: Optional[float] = Field(
        validation_alias="httpLatencyCriticalStddev", default=None
    )

    httpLatencyWarningStddev: Optional[float] = Field(
        validation_alias="httpLatencyWarningStddev", default=None
    )

    unhealthySubtestThreshold: Optional[int] = Field(
        validation_alias="unhealthySubtestThreshold", default=None
    )

    activation: Optional[ActivationSettings] = Field(
        validation_alias="activation", default=None
    )

    certExpiryWarning: Optional[int] = Field(
        validation_alias="certExpiryWarning", default=None
    )

    certExpiryCritical: Optional[int] = Field(
        validation_alias="certExpiryCritical", default=None
    )

    dnsValidIps: Optional[str] = Field(validation_alias="dnsValidIps", default=None)

    dnsLatencyCritical: Optional[float] = Field(
        validation_alias="dnsLatencyCritical", default=None
    )

    dnsLatencyWarning: Optional[float] = Field(
        validation_alias="dnsLatencyWarning", default=None
    )

    dnsLatencyCriticalStddev: Optional[float] = Field(
        validation_alias="dnsLatencyCriticalStddev", default=None
    )

    dnsLatencyWarningStddev: Optional[float] = Field(
        validation_alias="dnsLatencyWarningStddev", default=None
    )

    perAgentAlerting: Optional[bool] = Field(
        validation_alias="perAgentAlerting", default=None
    )

    disabledMetrics: Optional[DisabledMetrics] = Field(
        validation_alias="disabledMetrics", default=None
    )

    healthDisabled: Optional[bool] = Field(
        validation_alias="healthDisabled", default=None
    )

    throughputCritical: Optional[float] = Field(
        validation_alias="throughputCritical", default=None
    )

    throughputWarning: Optional[float] = Field(
        validation_alias="throughputWarning", default=None
    )

    throughputCriticalStddev: Optional[float] = Field(
        validation_alias="throughputCriticalStddev", default=None
    )

    throughputWarningStddev: Optional[float] = Field(
        validation_alias="throughputWarningStddev", default=None
    )

    disableAlerts: Optional[bool] = Field(
        validation_alias="disableAlerts", default=None
    )
