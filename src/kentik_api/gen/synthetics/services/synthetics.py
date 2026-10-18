from typing import List, Optional, Union, cast

import kentik_api.gen.synthetics.services.SyntheticsAdminService as RestSyntheticsModule1
import kentik_api.gen.synthetics.services.SyntheticsDataService as RestSyntheticsModule2
from kentik_api.core.api_config import APIConfig
from kentik_api.core.grpc_runtime import (
    build_grpc_request,
    call_grpc,
    parse_grpc_response,
)
from kentik_api.gen.synthetics import models as rest_models
from kentik_api.transports.grpc_client import GrpcTransport
from kentik_api.transports.rest_client import RestTransport


class SyntheticsServiceWrapper:
    """AUTO-GENERATED: scripts/generation/wrapper_generation.py, _generate_service_wrappers().
    Rebuilt on every `uv run poe generate`. Do not edit by hand.
    Unified Service routing to either gRPC or REST.
    """

    def __init__(self, transport: Union[GrpcTransport, RestTransport]):
        self._transport = transport
        if isinstance(self._transport, GrpcTransport):
            try:
                __import__("kentik_api.gen.pb_companions")
                import kentik_api.gen.synthetics.pb.synthetics_pb2 as _pb2_1_mod
                import kentik_api.gen.synthetics.pb.synthetics_pb2_grpc as _pb2_grpc_1_mod

                self._grpc_pb2_1 = _pb2_1_mod
                self._grpc_stub_1 = _pb2_grpc_1_mod.SyntheticsDataServiceStub(
                    self._transport.channel
                )
            except (ImportError, TypeError) as exc:
                self._grpc_pb2_1 = None
                self._grpc_stub_1 = None
                self._grpc_import_error_1 = exc
            try:
                __import__("kentik_api.gen.pb_companions")
                import kentik_api.gen.synthetics.pb.synthetics_pb2 as _pb2_2_mod
                import kentik_api.gen.synthetics.pb.synthetics_pb2_grpc as _pb2_grpc_2_mod

                self._grpc_pb2_2 = _pb2_2_mod
                self._grpc_stub_2 = _pb2_grpc_2_mod.SyntheticsAdminServiceStub(
                    self._transport.channel
                )
            except (ImportError, TypeError) as exc:
                self._grpc_pb2_2 = None
                self._grpc_stub_2 = None
                self._grpc_import_error_2 = exc

    def list_agent_alerts(
        self,
        *,
        api_config_override: Optional[APIConfig] = None,
        agentIds: Optional[List[str]] = None,
    ) -> rest_models.ListAgentAlertsResponse:
        """
        List agent alert configurations

        Lists all agent alert configurations, optionally filtered by a list of agent ids.
        """
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_2 is None or self._grpc_stub_2 is None:
                raise NotImplementedError(
                    f"gRPC proto modules for synthetics service failed to import: {self._grpc_import_error_2!r}"
                ) from self._grpc_import_error_2
            _req = build_grpc_request(
                self._grpc_pb2_2.ListAgentAlertsRequest, None, {"agentIds": agentIds}
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_2.ListAgentAlerts,
                _req,
                api_config=api_config_override,
                error_cls=RestSyntheticsModule1.ListAgentAlertsError,
            )
            return parse_grpc_response(
                rest_models.ListAgentAlertsResponse,
                _resp,
                _rate_limit,
                stub_method=self._grpc_stub_2.ListAgentAlerts,
                operation_name="ListAgentAlerts",
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestSyntheticsModule1.ListAgentAlerts(
                api_config_override=api_config_override or rest_transport.api_config,
                agentIds=agentIds,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def create_agent_alert(
        self,
        *,
        api_config_override: Optional[APIConfig] = None,
        data: rest_models.CreateAgentAlertRequest,
    ) -> rest_models.CreateAgentAlertResponse:
        """
        Create an agent alert configuration

        Creates a new agent alert configuration.
        """
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_2 is None or self._grpc_stub_2 is None:
                raise NotImplementedError(
                    f"gRPC proto modules for synthetics service failed to import: {self._grpc_import_error_2!r}"
                ) from self._grpc_import_error_2
            _req = build_grpc_request(
                self._grpc_pb2_2.CreateAgentAlertRequest,
                data.model_dump(by_alias=True, exclude_unset=True),
                {},
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_2.CreateAgentAlert,
                _req,
                api_config=api_config_override,
                error_cls=RestSyntheticsModule1.CreateAgentAlertError,
            )
            return parse_grpc_response(
                rest_models.CreateAgentAlertResponse,
                _resp,
                _rate_limit,
                stub_method=self._grpc_stub_2.CreateAgentAlert,
                operation_name="CreateAgentAlert",
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestSyntheticsModule1.CreateAgentAlert(
                api_config_override=api_config_override or rest_transport.api_config,
                data=data,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def get_agent_alert(
        self, *, api_config_override: Optional[APIConfig] = None, id: str
    ) -> rest_models.GetAgentAlertResponse:
        """
        Get an agent alert configuration

        Retrieves an existing agent alert configuration.
        """
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_2 is None or self._grpc_stub_2 is None:
                raise NotImplementedError(
                    f"gRPC proto modules for synthetics service failed to import: {self._grpc_import_error_2!r}"
                ) from self._grpc_import_error_2
            _req = build_grpc_request(
                self._grpc_pb2_2.GetAgentAlertRequest, None, {"id": id}
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_2.GetAgentAlert,
                _req,
                api_config=api_config_override,
                error_cls=RestSyntheticsModule1.GetAgentAlertError,
            )
            return parse_grpc_response(
                rest_models.GetAgentAlertResponse,
                _resp,
                _rate_limit,
                stub_method=self._grpc_stub_2.GetAgentAlert,
                operation_name="GetAgentAlert",
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestSyntheticsModule1.GetAgentAlert(
                api_config_override=api_config_override or rest_transport.api_config,
                id=id,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def update_agent_alert(
        self,
        *,
        api_config_override: Optional[APIConfig] = None,
        id: str,
        data: rest_models.SyntheticsAdminServiceUpdateAgentAlertBody,
    ) -> rest_models.UpdateAgentAlertResponse:
        """
        Update an agent alert configuration

        Updates an existing agent alert configuration with the time threshold and notification channels provided.
        """
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_2 is None or self._grpc_stub_2 is None:
                raise NotImplementedError(
                    f"gRPC proto modules for synthetics service failed to import: {self._grpc_import_error_2!r}"
                ) from self._grpc_import_error_2
            _req = build_grpc_request(
                self._grpc_pb2_2.UpdateAgentAlertRequest,
                data.model_dump(by_alias=True, exclude_unset=True),
                {"id": id},
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_2.UpdateAgentAlert,
                _req,
                api_config=api_config_override,
                error_cls=RestSyntheticsModule1.UpdateAgentAlertError,
            )
            return parse_grpc_response(
                rest_models.UpdateAgentAlertResponse,
                _resp,
                _rate_limit,
                stub_method=self._grpc_stub_2.UpdateAgentAlert,
                operation_name="UpdateAgentAlert",
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestSyntheticsModule1.UpdateAgentAlert(
                api_config_override=api_config_override or rest_transport.api_config,
                id=id,
                data=data,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def delete_agent_alert(
        self, *, api_config_override: Optional[APIConfig] = None, id: str
    ) -> rest_models.DeleteAgentAlertResponse:
        """
        Delete an agent alert configuration

        Deletes an existing agent alert configuration.
        """
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_2 is None or self._grpc_stub_2 is None:
                raise NotImplementedError(
                    f"gRPC proto modules for synthetics service failed to import: {self._grpc_import_error_2!r}"
                ) from self._grpc_import_error_2
            _req = build_grpc_request(
                self._grpc_pb2_2.DeleteAgentAlertRequest, None, {"id": id}
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_2.DeleteAgentAlert,
                _req,
                api_config=api_config_override,
                error_cls=RestSyntheticsModule1.DeleteAgentAlertError,
            )
            return parse_grpc_response(
                rest_models.DeleteAgentAlertResponse,
                _resp,
                _rate_limit,
                stub_method=self._grpc_stub_2.DeleteAgentAlert,
                operation_name="DeleteAgentAlert",
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestSyntheticsModule1.DeleteAgentAlert(
                api_config_override=api_config_override or rest_transport.api_config,
                id=id,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def list_agents(
        self, *, api_config_override: Optional[APIConfig] = None
    ) -> rest_models.ListAgentsResponse:
        """
        List available agents

        Returns list of all synthetic agents available in the account.
        """
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_2 is None or self._grpc_stub_2 is None:
                raise NotImplementedError(
                    f"gRPC proto modules for synthetics service failed to import: {self._grpc_import_error_2!r}"
                ) from self._grpc_import_error_2
            _req = build_grpc_request(self._grpc_pb2_2.ListAgentsRequest, None, {})
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_2.ListAgents,
                _req,
                api_config=api_config_override,
                error_cls=RestSyntheticsModule1.ListAgentsError,
            )
            return parse_grpc_response(
                rest_models.ListAgentsResponse,
                _resp,
                _rate_limit,
                stub_method=self._grpc_stub_2.ListAgents,
                operation_name="ListAgents",
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestSyntheticsModule1.ListAgents(
                api_config_override=api_config_override or rest_transport.api_config
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def get_agent(
        self, *, api_config_override: Optional[APIConfig] = None, agentid: str
    ) -> rest_models.GetAgentResponse:
        """
        Get information about an agent

        Returns information about the requested synthetic agent.
        """
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_2 is None or self._grpc_stub_2 is None:
                raise NotImplementedError(
                    f"gRPC proto modules for synthetics service failed to import: {self._grpc_import_error_2!r}"
                ) from self._grpc_import_error_2
            _req = build_grpc_request(
                self._grpc_pb2_2.GetAgentRequest, None, {"id": agentid}
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_2.GetAgent,
                _req,
                api_config=api_config_override,
                error_cls=RestSyntheticsModule1.GetAgentError,
            )
            return parse_grpc_response(
                rest_models.GetAgentResponse,
                _resp,
                _rate_limit,
                stub_method=self._grpc_stub_2.GetAgent,
                operation_name="GetAgent",
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestSyntheticsModule1.GetAgent(
                api_config_override=api_config_override or rest_transport.api_config,
                agentid=agentid,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def update_agent(
        self,
        *,
        api_config_override: Optional[APIConfig] = None,
        agentid: str,
        data: rest_models.SyntheticsAdminServiceUpdateAgentBody,
    ) -> rest_models.UpdateAgentResponse:
        """
        Update configuration of an agent

        Update configuration of a synthetic agent.
        """
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_2 is None or self._grpc_stub_2 is None:
                raise NotImplementedError(
                    f"gRPC proto modules for synthetics service failed to import: {self._grpc_import_error_2!r}"
                ) from self._grpc_import_error_2
            _req = build_grpc_request(
                self._grpc_pb2_2.UpdateAgentRequest,
                data.model_dump(by_alias=True, exclude_unset=True),
                {"agent.id": agentid},
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_2.UpdateAgent,
                _req,
                api_config=api_config_override,
                error_cls=RestSyntheticsModule1.UpdateAgentError,
            )
            return parse_grpc_response(
                rest_models.UpdateAgentResponse,
                _resp,
                _rate_limit,
                stub_method=self._grpc_stub_2.UpdateAgent,
                operation_name="UpdateAgent",
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestSyntheticsModule1.UpdateAgent(
                api_config_override=api_config_override or rest_transport.api_config,
                agentid=agentid,
                data=data,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def delete_agent(
        self, *, api_config_override: Optional[APIConfig] = None, agentid: str
    ) -> rest_models.DeleteAgentResponse:
        """
        Delete an agent

        Deletes the requested agent. The deleted agent is removed from configuration of all tests.
        """
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_2 is None or self._grpc_stub_2 is None:
                raise NotImplementedError(
                    f"gRPC proto modules for synthetics service failed to import: {self._grpc_import_error_2!r}"
                ) from self._grpc_import_error_2
            _req = build_grpc_request(
                self._grpc_pb2_2.DeleteAgentRequest, None, {"id": agentid}
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_2.DeleteAgent,
                _req,
                api_config=api_config_override,
                error_cls=RestSyntheticsModule1.DeleteAgentError,
            )
            return parse_grpc_response(
                rest_models.DeleteAgentResponse,
                _resp,
                _rate_limit,
                stub_method=self._grpc_stub_2.DeleteAgent,
                operation_name="DeleteAgent",
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestSyntheticsModule1.DeleteAgent(
                api_config_override=api_config_override or rest_transport.api_config,
                agentid=agentid,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def list_tests(
        self, *, api_config_override: Optional[APIConfig] = None
    ) -> rest_models.ListTestsResponse:
        """
        List all tests

        Returns a list of all configured active and paused synthetic tests.
        """
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_2 is None or self._grpc_stub_2 is None:
                raise NotImplementedError(
                    f"gRPC proto modules for synthetics service failed to import: {self._grpc_import_error_2!r}"
                ) from self._grpc_import_error_2
            _req = build_grpc_request(self._grpc_pb2_2.ListTestsRequest, None, {})
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_2.ListTests,
                _req,
                api_config=api_config_override,
                error_cls=RestSyntheticsModule1.ListTestsError,
            )
            return parse_grpc_response(
                rest_models.ListTestsResponse,
                _resp,
                _rate_limit,
                stub_method=self._grpc_stub_2.ListTests,
                operation_name="ListTests",
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestSyntheticsModule1.ListTests(
                api_config_override=api_config_override or rest_transport.api_config
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def create_test(
        self,
        *,
        api_config_override: Optional[APIConfig] = None,
        data: rest_models.CreateTestRequest,
    ) -> rest_models.CreateTestResponse:
        """
        Create a test

        Create synthetic test based on configuration provided in the request.
        """
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_2 is None or self._grpc_stub_2 is None:
                raise NotImplementedError(
                    f"gRPC proto modules for synthetics service failed to import: {self._grpc_import_error_2!r}"
                ) from self._grpc_import_error_2
            _req = build_grpc_request(
                self._grpc_pb2_2.CreateTestRequest,
                data.model_dump(by_alias=True, exclude_unset=True),
                {},
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_2.CreateTest,
                _req,
                api_config=api_config_override,
                error_cls=RestSyntheticsModule1.CreateTestError,
            )
            return parse_grpc_response(
                rest_models.CreateTestResponse,
                _resp,
                _rate_limit,
                stub_method=self._grpc_stub_2.CreateTest,
                operation_name="CreateTest",
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestSyntheticsModule1.CreateTest(
                api_config_override=api_config_override or rest_transport.api_config,
                data=data,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def get_test(
        self, *, api_config_override: Optional[APIConfig] = None, id: str
    ) -> rest_models.GetTestResponse:
        """
        Get information about a test

        Returns configuration and status for the requested synthetic test.
        """
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_2 is None or self._grpc_stub_2 is None:
                raise NotImplementedError(
                    f"gRPC proto modules for synthetics service failed to import: {self._grpc_import_error_2!r}"
                ) from self._grpc_import_error_2
            _req = build_grpc_request(self._grpc_pb2_2.GetTestRequest, None, {"id": id})
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_2.GetTest,
                _req,
                api_config=api_config_override,
                error_cls=RestSyntheticsModule1.GetTestError,
            )
            return parse_grpc_response(
                rest_models.GetTestResponse,
                _resp,
                _rate_limit,
                stub_method=self._grpc_stub_2.GetTest,
                operation_name="GetTest",
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestSyntheticsModule1.GetTest(
                api_config_override=api_config_override or rest_transport.api_config,
                id=id,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def update_test(
        self,
        *,
        api_config_override: Optional[APIConfig] = None,
        id: str,
        data: rest_models.SyntheticsAdminServiceUpdateTestBody,
    ) -> rest_models.UpdateTestResponse:
        """
        Update configuration of a test

        Updates configuration of a synthetic test.
        """
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_2 is None or self._grpc_stub_2 is None:
                raise NotImplementedError(
                    f"gRPC proto modules for synthetics service failed to import: {self._grpc_import_error_2!r}"
                ) from self._grpc_import_error_2
            _req = build_grpc_request(
                self._grpc_pb2_2.UpdateTestRequest,
                data.model_dump(by_alias=True, exclude_unset=True),
                {"test.id": id},
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_2.UpdateTest,
                _req,
                api_config=api_config_override,
                error_cls=RestSyntheticsModule1.UpdateTestError,
            )
            return parse_grpc_response(
                rest_models.UpdateTestResponse,
                _resp,
                _rate_limit,
                stub_method=self._grpc_stub_2.UpdateTest,
                operation_name="UpdateTest",
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestSyntheticsModule1.UpdateTest(
                api_config_override=api_config_override or rest_transport.api_config,
                id=id,
                data=data,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def delete_test(
        self, *, api_config_override: Optional[APIConfig] = None, id: str
    ) -> rest_models.DeleteTestResponse:
        """
        Delete a synthetic test.

        Deletes the synthetics test. All accumulated results for the test cease to be accessible.
        """
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_2 is None or self._grpc_stub_2 is None:
                raise NotImplementedError(
                    f"gRPC proto modules for synthetics service failed to import: {self._grpc_import_error_2!r}"
                ) from self._grpc_import_error_2
            _req = build_grpc_request(
                self._grpc_pb2_2.DeleteTestRequest, None, {"id": id}
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_2.DeleteTest,
                _req,
                api_config=api_config_override,
                error_cls=RestSyntheticsModule1.DeleteTestError,
            )
            return parse_grpc_response(
                rest_models.DeleteTestResponse,
                _resp,
                _rate_limit,
                stub_method=self._grpc_stub_2.DeleteTest,
                operation_name="DeleteTest",
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestSyntheticsModule1.DeleteTest(
                api_config_override=api_config_override or rest_transport.api_config,
                id=id,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def set_test_status(
        self,
        *,
        api_config_override: Optional[APIConfig] = None,
        id: str,
        data: rest_models.SyntheticsAdminServiceSetTestStatusBody,
    ) -> rest_models.SetTestStatusResponse:
        """
        Update status of a synthetic test
        """
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_2 is None or self._grpc_stub_2 is None:
                raise NotImplementedError(
                    f"gRPC proto modules for synthetics service failed to import: {self._grpc_import_error_2!r}"
                ) from self._grpc_import_error_2
            _req = build_grpc_request(
                self._grpc_pb2_2.SetTestStatusRequest,
                data.model_dump(by_alias=True, exclude_unset=True),
                {"id": id},
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_2.SetTestStatus,
                _req,
                api_config=api_config_override,
                error_cls=RestSyntheticsModule1.SetTestStatusError,
            )
            return parse_grpc_response(
                rest_models.SetTestStatusResponse,
                _resp,
                _rate_limit,
                stub_method=self._grpc_stub_2.SetTestStatus,
                operation_name="SetTestStatus",
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestSyntheticsModule1.SetTestStatus(
                api_config_override=api_config_override or rest_transport.api_config,
                id=id,
                data=data,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def get_results_for_tests(
        self,
        *,
        api_config_override: Optional[APIConfig] = None,
        data: rest_models.GetResultsForTestsRequest,
    ) -> rest_models.GetResultsForTestsResponse:
        """
        Get results for tests

        Returns probe results for a set of tests for specified period of time.
        """
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_1 is None or self._grpc_stub_1 is None:
                raise NotImplementedError(
                    f"gRPC proto modules for synthetics service failed to import: {self._grpc_import_error_1!r}"
                ) from self._grpc_import_error_1
            _req = build_grpc_request(
                self._grpc_pb2_1.GetResultsForTestsRequest,
                data.model_dump(by_alias=True, exclude_unset=True),
                {},
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_1.GetResultsForTests,
                _req,
                api_config=api_config_override,
                error_cls=RestSyntheticsModule2.GetResultsForTestsError,
            )
            return parse_grpc_response(
                rest_models.GetResultsForTestsResponse,
                _resp,
                _rate_limit,
                stub_method=self._grpc_stub_1.GetResultsForTests,
                operation_name="GetResultsForTests",
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestSyntheticsModule2.GetResultsForTests(
                api_config_override=api_config_override or rest_transport.api_config,
                data=data,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def get_results_for_tests_csv(
        self,
        *,
        api_config_override: Optional[APIConfig] = None,
        data: rest_models.GetResultsForTestsCsvRequest,
    ) -> rest_models.GetResultsForTestsCsvResponse:
        """
        Get test results in CSV format

        Returns probe results for tests in CSV format.
        """
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_1 is None or self._grpc_stub_1 is None:
                raise NotImplementedError(
                    f"gRPC proto modules for synthetics service failed to import: {self._grpc_import_error_1!r}"
                ) from self._grpc_import_error_1
            _req = build_grpc_request(
                self._grpc_pb2_1.GetResultsForTestsCsvRequest,
                data.model_dump(by_alias=True, exclude_unset=True),
                {},
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_1.GetResultsForTestsCsv,
                _req,
                api_config=api_config_override,
                error_cls=RestSyntheticsModule2.GetResultsForTestsCsvError,
            )
            return parse_grpc_response(
                rest_models.GetResultsForTestsCsvResponse,
                _resp,
                _rate_limit,
                stub_method=self._grpc_stub_1.GetResultsForTestsCsv,
                operation_name="GetResultsForTestsCsv",
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestSyntheticsModule2.GetResultsForTestsCsv(
                api_config_override=api_config_override or rest_transport.api_config,
                data=data,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def get_trace_for_test(
        self,
        *,
        api_config_override: Optional[APIConfig] = None,
        data: rest_models.GetTraceForTestRequest,
    ) -> rest_models.GetTraceForTestResponse:
        """
        Get network trace data for a test

        Get network trace data for a specific synthetic test. The test must have traceroute task configured.
        """
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_1 is None or self._grpc_stub_1 is None:
                raise NotImplementedError(
                    f"gRPC proto modules for synthetics service failed to import: {self._grpc_import_error_1!r}"
                ) from self._grpc_import_error_1
            _req = build_grpc_request(
                self._grpc_pb2_1.GetTraceForTestRequest,
                data.model_dump(by_alias=True, exclude_unset=True),
                {},
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_1.GetTraceForTest,
                _req,
                api_config=api_config_override,
                error_cls=RestSyntheticsModule2.GetTraceForTestError,
            )
            return parse_grpc_response(
                rest_models.GetTraceForTestResponse,
                _resp,
                _rate_limit,
                stub_method=self._grpc_stub_1.GetTraceForTest,
                operation_name="GetTraceForTest",
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestSyntheticsModule2.GetTraceForTest(
                api_config_override=api_config_override or rest_transport.api_config,
                data=data,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )
