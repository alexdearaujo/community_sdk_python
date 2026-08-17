from typing import Any, Dict, List, Optional

from kentik_api.core.api_config import APIConfig
from kentik_api.core.rest_runtime import request_json

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

    return (
        ListAgentAlertsResponse(**body)
        if body is not None
        else ListAgentAlertsResponse.model_construct()
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
        json_body=data.model_dump(),
        header_params=header_params,
        expected_status=200,
        operation_name="CreateAgentAlert",
        error_cls=CreateAgentAlertError,
    )

    return (
        CreateAgentAlertResponse(**body)
        if body is not None
        else CreateAgentAlertResponse.model_construct()
    )


def GetAgentAlert(
    api_config_override: Optional[APIConfig] = None, *, id: str
) -> GetAgentAlertResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path=f"/synthetics/v202309/agentAlerts/{id}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="GetAgentAlert",
        error_cls=GetAgentAlertError,
    )

    return (
        GetAgentAlertResponse(**body)
        if body is not None
        else GetAgentAlertResponse.model_construct()
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
        path=f"/synthetics/v202309/agentAlerts/{id}",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(),
        header_params=header_params,
        expected_status=200,
        operation_name="UpdateAgentAlert",
        error_cls=UpdateAgentAlertError,
    )

    return (
        UpdateAgentAlertResponse(**body)
        if body is not None
        else UpdateAgentAlertResponse.model_construct()
    )


def DeleteAgentAlert(
    api_config_override: Optional[APIConfig] = None, *, id: str
) -> DeleteAgentAlertResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="delete",
        path=f"/synthetics/v202309/agentAlerts/{id}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="DeleteAgentAlert",
        error_cls=DeleteAgentAlertError,
    )

    return (
        DeleteAgentAlertResponse(**body)
        if body is not None
        else DeleteAgentAlertResponse.model_construct()
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

    return (
        ListAgentsResponse(**body)
        if body is not None
        else ListAgentsResponse.model_construct()
    )


def GetAgent(
    api_config_override: Optional[APIConfig] = None, *, agentid: str
) -> GetAgentResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path=f"/synthetics/v202309/agents/{agentid}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="GetAgent",
        error_cls=GetAgentError,
    )

    return (
        GetAgentResponse(**body)
        if body is not None
        else GetAgentResponse.model_construct()
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
        path=f"/synthetics/v202309/agents/{agentid}",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(),
        header_params=header_params,
        expected_status=200,
        operation_name="UpdateAgent",
        error_cls=UpdateAgentError,
    )

    return (
        UpdateAgentResponse(**body)
        if body is not None
        else UpdateAgentResponse.model_construct()
    )


def DeleteAgent(
    api_config_override: Optional[APIConfig] = None, *, agentid: str
) -> DeleteAgentResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="delete",
        path=f"/synthetics/v202309/agents/{agentid}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="DeleteAgent",
        error_cls=DeleteAgentError,
    )

    return (
        DeleteAgentResponse(**body)
        if body is not None
        else DeleteAgentResponse.model_construct()
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

    return (
        ListTestsResponse(**body)
        if body is not None
        else ListTestsResponse.model_construct()
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
        json_body=data.model_dump(),
        header_params=header_params,
        expected_status=200,
        operation_name="CreateTest",
        error_cls=CreateTestError,
    )

    return (
        CreateTestResponse(**body)
        if body is not None
        else CreateTestResponse.model_construct()
    )


def GetTest(
    api_config_override: Optional[APIConfig] = None, *, id: str
) -> GetTestResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path=f"/synthetics/v202309/tests/{id}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="GetTest",
        error_cls=GetTestError,
    )

    return (
        GetTestResponse(**body)
        if body is not None
        else GetTestResponse.model_construct()
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
        path=f"/synthetics/v202309/tests/{id}",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(),
        header_params=header_params,
        expected_status=200,
        operation_name="UpdateTest",
        error_cls=UpdateTestError,
    )

    return (
        UpdateTestResponse(**body)
        if body is not None
        else UpdateTestResponse.model_construct()
    )


def DeleteTest(
    api_config_override: Optional[APIConfig] = None, *, id: str
) -> DeleteTestResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="delete",
        path=f"/synthetics/v202309/tests/{id}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="DeleteTest",
        error_cls=DeleteTestError,
    )

    return (
        DeleteTestResponse(**body)
        if body is not None
        else DeleteTestResponse.model_construct()
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
        path=f"/synthetics/v202309/tests/{id}/status",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(),
        header_params=header_params,
        expected_status=200,
        operation_name="SetTestStatus",
        error_cls=SetTestStatusError,
    )

    return (
        SetTestStatusResponse(**body)
        if body is not None
        else SetTestStatusResponse.model_construct()
    )
