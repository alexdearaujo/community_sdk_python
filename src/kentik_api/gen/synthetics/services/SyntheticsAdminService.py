# AUTO-GENERATED: scripts/openapi_templates/service.jinja2 via openapi-python-generator
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Any, Dict, List, Optional

from kentik_api.core.api_config import APIConfig
from kentik_api.core.rest_runtime import (
    parse_response_model,
    path_segment,
    request_json,
)

from ..error import (
    CreateAgentAlertError,
    CreateTestError,
    DeleteAgentAlertError,
    DeleteAgentError,
    DeleteTestError,
    GetAgentAlertError,
    GetAgentError,
    GetTestError,
    ListAgentAlertsError,
    ListAgentsError,
    ListTestsError,
    SetTestStatusError,
    UpdateAgentAlertError,
    UpdateAgentError,
    UpdateTestError,
)
from ..models import (  # noqa: F401
    ActivationSettings,
    Agent,
    AgentAlert,
    AgentMetadata,
    AgentMetadataIpValue,
    AgentResults,
    AgentStatus,
    AgentTest,
    AlertingSettings,
    AlertingType,
    CreateAgentAlertRequest,
    CreateAgentAlertResponse,
    CreateTestRequest,
    CreateTestResponse,
    DeleteAgentAlertResponse,
    DeleteAgentResponse,
    DeleteTestResponse,
    DisabledMetrics,
    DNSRecord,
    DNSResponseData,
    DNSResults,
    DnsTest,
    FlowTest,
    GetAgentAlertResponse,
    GetAgentResponse,
    GetResultsForTestsCsvRequest,
    GetResultsForTestsCsvResponse,
    GetResultsForTestsRequest,
    GetResultsForTestsResponse,
    GetTestResponse,
    GetTraceForTestRequest,
    GetTraceForTestResponse,
    GroupedAlertSetting,
    GroupedAlertSettings,
    HealthSettings,
    HostnameTest,
    HTTPResponseData,
    HTTPResults,
    ImplementType,
    IPFamily,
    IpTest,
    ListAgentAlertsResponse,
    ListAgentsResponse,
    ListTestsResponse,
    MetricData,
    NetNode,
    NetworkMeshTest,
    PacketLossData,
    PageLoadTest,
    Path,
    PathTrace,
    PingResults,
    ScheduleSettings,
    SetTestStatusResponse,
    SrcGroupBy,
    Stats,
    SyntheticsAdminServiceSetTestStatusBody,
    SyntheticsAdminServiceUpdateAgentAlertBody,
    SyntheticsAdminServiceUpdateAgentBody,
    SyntheticsAdminServiceUpdateTestBody,
    TaskResults,
    Test,
    TestPingSettings,
    TestResults,
    TestSettings,
    TestStatus,
    TestThroughputSettings,
    TestTraceSettings,
    TraceHop,
    UpdateAgentAlertResponse,
    UpdateAgentResponse,
    UpdateTestResponse,
    UrlTest,
    protobufAny,
    rpcStatus,
    syntheticsv202309Location,
    v202303UserInfo,
)


def ListAgentAlerts(
    api_config_override: Optional[APIConfig] = None,
    *,
    agentIds: Optional[List[str]] = None,
) -> ListAgentAlertsResponse:
    query_params: Dict[str, Any] = {"agentIds": agentIds}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path="/synthetics/v202309/agentAlerts",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="ListAgentAlerts",
        error_cls=ListAgentAlertsError,
    )

    return parse_response_model(
        ListAgentAlertsResponse,
        body,
        operation_name="ListAgentAlerts",
        method="get",
        path="/synthetics/v202309/agentAlerts",
    )


def CreateAgentAlert(
    api_config_override: Optional[APIConfig] = None, *, data: CreateAgentAlertRequest
) -> CreateAgentAlertResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="post",
        path="/synthetics/v202309/agentAlerts",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(by_alias=True),
        header_params=header_params,
        expected_status=200,
        operation_name="CreateAgentAlert",
        error_cls=CreateAgentAlertError,
    )

    return parse_response_model(
        CreateAgentAlertResponse,
        body,
        operation_name="CreateAgentAlert",
        method="post",
        path="/synthetics/v202309/agentAlerts",
    )


def GetAgentAlert(
    api_config_override: Optional[APIConfig] = None, *, id: str
) -> GetAgentAlertResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path=f"/synthetics/v202309/agentAlerts/{path_segment(id)}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="GetAgentAlert",
        error_cls=GetAgentAlertError,
    )

    return parse_response_model(
        GetAgentAlertResponse,
        body,
        operation_name="GetAgentAlert",
        method="get",
        path="/synthetics/v202309/agentAlerts/{id}",
    )


def UpdateAgentAlert(
    api_config_override: Optional[APIConfig] = None,
    *,
    id: str,
    data: SyntheticsAdminServiceUpdateAgentAlertBody,
) -> UpdateAgentAlertResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="put",
        path=f"/synthetics/v202309/agentAlerts/{path_segment(id)}",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(by_alias=True),
        header_params=header_params,
        expected_status=200,
        operation_name="UpdateAgentAlert",
        error_cls=UpdateAgentAlertError,
    )

    return parse_response_model(
        UpdateAgentAlertResponse,
        body,
        operation_name="UpdateAgentAlert",
        method="put",
        path="/synthetics/v202309/agentAlerts/{id}",
    )


def DeleteAgentAlert(
    api_config_override: Optional[APIConfig] = None, *, id: str
) -> DeleteAgentAlertResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="delete",
        path=f"/synthetics/v202309/agentAlerts/{path_segment(id)}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="DeleteAgentAlert",
        error_cls=DeleteAgentAlertError,
    )

    return parse_response_model(
        DeleteAgentAlertResponse,
        body,
        operation_name="DeleteAgentAlert",
        method="delete",
        path="/synthetics/v202309/agentAlerts/{id}",
    )


def ListAgents(api_config_override: Optional[APIConfig] = None) -> ListAgentsResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path="/synthetics/v202309/agents",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="ListAgents",
        error_cls=ListAgentsError,
    )

    return parse_response_model(
        ListAgentsResponse,
        body,
        operation_name="ListAgents",
        method="get",
        path="/synthetics/v202309/agents",
    )


def GetAgent(
    api_config_override: Optional[APIConfig] = None, *, agentid: str
) -> GetAgentResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path=f"/synthetics/v202309/agents/{path_segment(agentid)}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="GetAgent",
        error_cls=GetAgentError,
    )

    return parse_response_model(
        GetAgentResponse,
        body,
        operation_name="GetAgent",
        method="get",
        path="/synthetics/v202309/agents/{agent.id}",
    )


def UpdateAgent(
    api_config_override: Optional[APIConfig] = None,
    *,
    agentid: str,
    data: SyntheticsAdminServiceUpdateAgentBody,
) -> UpdateAgentResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="put",
        path=f"/synthetics/v202309/agents/{path_segment(agentid)}",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(by_alias=True),
        header_params=header_params,
        expected_status=200,
        operation_name="UpdateAgent",
        error_cls=UpdateAgentError,
    )

    return parse_response_model(
        UpdateAgentResponse,
        body,
        operation_name="UpdateAgent",
        method="put",
        path="/synthetics/v202309/agents/{agent.id}",
    )


def DeleteAgent(
    api_config_override: Optional[APIConfig] = None, *, agentid: str
) -> DeleteAgentResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="delete",
        path=f"/synthetics/v202309/agents/{path_segment(agentid)}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="DeleteAgent",
        error_cls=DeleteAgentError,
    )

    return parse_response_model(
        DeleteAgentResponse,
        body,
        operation_name="DeleteAgent",
        method="delete",
        path="/synthetics/v202309/agents/{agent.id}",
    )


def ListTests(api_config_override: Optional[APIConfig] = None) -> ListTestsResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path="/synthetics/v202309/tests",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="ListTests",
        error_cls=ListTestsError,
    )

    return parse_response_model(
        ListTestsResponse,
        body,
        operation_name="ListTests",
        method="get",
        path="/synthetics/v202309/tests",
    )


def CreateTest(
    api_config_override: Optional[APIConfig] = None, *, data: CreateTestRequest
) -> CreateTestResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="post",
        path="/synthetics/v202309/tests",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(by_alias=True),
        header_params=header_params,
        expected_status=200,
        operation_name="CreateTest",
        error_cls=CreateTestError,
    )

    return parse_response_model(
        CreateTestResponse,
        body,
        operation_name="CreateTest",
        method="post",
        path="/synthetics/v202309/tests",
    )


def GetTest(
    api_config_override: Optional[APIConfig] = None, *, id: str
) -> GetTestResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path=f"/synthetics/v202309/tests/{path_segment(id)}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="GetTest",
        error_cls=GetTestError,
    )

    return parse_response_model(
        GetTestResponse,
        body,
        operation_name="GetTest",
        method="get",
        path="/synthetics/v202309/tests/{id}",
    )


def UpdateTest(
    api_config_override: Optional[APIConfig] = None,
    *,
    id: str,
    data: SyntheticsAdminServiceUpdateTestBody,
) -> UpdateTestResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="put",
        path=f"/synthetics/v202309/tests/{path_segment(id)}",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(by_alias=True),
        header_params=header_params,
        expected_status=200,
        operation_name="UpdateTest",
        error_cls=UpdateTestError,
    )

    return parse_response_model(
        UpdateTestResponse,
        body,
        operation_name="UpdateTest",
        method="put",
        path="/synthetics/v202309/tests/{id}",
    )


def DeleteTest(
    api_config_override: Optional[APIConfig] = None, *, id: str
) -> DeleteTestResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="delete",
        path=f"/synthetics/v202309/tests/{path_segment(id)}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="DeleteTest",
        error_cls=DeleteTestError,
    )

    return parse_response_model(
        DeleteTestResponse,
        body,
        operation_name="DeleteTest",
        method="delete",
        path="/synthetics/v202309/tests/{id}",
    )


def SetTestStatus(
    api_config_override: Optional[APIConfig] = None,
    *,
    id: str,
    data: SyntheticsAdminServiceSetTestStatusBody,
) -> SetTestStatusResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="put",
        path=f"/synthetics/v202309/tests/{path_segment(id)}/status",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(by_alias=True),
        header_params=header_params,
        expected_status=200,
        operation_name="SetTestStatus",
        error_cls=SetTestStatusError,
    )

    return parse_response_model(
        SetTestStatusResponse,
        body,
        operation_name="SetTestStatus",
        method="put",
        path="/synthetics/v202309/tests/{id}/status",
    )
