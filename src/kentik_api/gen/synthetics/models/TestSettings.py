# AUTO-GENERATED: openapi-python-generator, model generation
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import List, Optional

from pydantic import BaseModel, Field

from .AgentTest import AgentTest
from .AlertingSettings import AlertingSettings
from .DnsTest import DnsTest
from .FlowTest import FlowTest
from .HealthSettings import HealthSettings
from .HostnameTest import HostnameTest
from .IPFamily import IPFamily
from .IpTest import IpTest
from .NetworkMeshTest import NetworkMeshTest
from .PageLoadTest import PageLoadTest
from .ScheduleSettings import ScheduleSettings
from .TestPingSettings import TestPingSettings
from .TestThroughputSettings import TestThroughputSettings
from .TestTraceSettings import TestTraceSettings
from .UrlTest import UrlTest


class TestSettings(BaseModel):
    """
    TestSettings model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    hostname: Optional[HostnameTest] = Field(validation_alias="hostname", default=None)

    ip: Optional[IpTest] = Field(validation_alias="ip", default=None)

    agent: Optional[AgentTest] = Field(validation_alias="agent", default=None)

    flow: Optional[FlowTest] = Field(validation_alias="flow", default=None)

    dns: Optional[DnsTest] = Field(validation_alias="dns", default=None)

    url: Optional[UrlTest] = Field(validation_alias="url", default=None)

    networkGrid: Optional[IpTest] = Field(validation_alias="networkGrid", default=None)

    pageLoad: Optional[PageLoadTest] = Field(validation_alias="pageLoad", default=None)

    dnsGrid: Optional[DnsTest] = Field(validation_alias="dnsGrid", default=None)

    networkMesh: Optional[NetworkMeshTest] = Field(
        validation_alias="networkMesh", default=None
    )

    agentIds: Optional[List[str]] = Field(validation_alias="agentIds", default=None)

    tasks: Optional[List[str]] = Field(validation_alias="tasks", default=None)

    healthSettings: Optional[HealthSettings] = Field(
        validation_alias="healthSettings", default=None
    )

    ping: Optional[TestPingSettings] = Field(validation_alias="ping", default=None)

    trace: Optional[TestTraceSettings] = Field(validation_alias="trace", default=None)

    period: Optional[int] = Field(validation_alias="period", default=None)

    family: Optional[IPFamily] = Field(validation_alias="family", default=None)

    notificationChannels: Optional[List[str]] = Field(
        validation_alias="notificationChannels", default=None
    )

    notes: Optional[str] = Field(validation_alias="notes", default=None)

    throughput: Optional[TestThroughputSettings] = Field(
        validation_alias="throughput", default=None
    )

    schedule: Optional[ScheduleSettings] = Field(
        validation_alias="schedule", default=None
    )

    alerting: Optional[AlertingSettings] = Field(
        validation_alias="alerting", default=None
    )
