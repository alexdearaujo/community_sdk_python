from typing import List, Optional, Union, cast

from google.protobuf.json_format import MessageToDict

import kentik_api.gen.synthetics.services.SyntheticsAdminService as RestSyntheticsModule1
import kentik_api.gen.synthetics.services.SyntheticsDataService as RestSyntheticsModule2
from kentik_api.core.api_config import APIConfig
from kentik_api.core.grpc_runtime import build_grpc_request, call_grpc
from kentik_api.core.rate_limit import attach_rate_limit
from kentik_api.gen.synthetics import models as rest_models
from kentik_api.transports.grpc_client import GrpcTransport
from kentik_api.transports.rest_client import RestTransport


class SyntheticsServiceWrapper:
    """AUTO-GENERATED: scripts/generation/wrapper_generation.py, _generate_service_wrappers().
    Rebuilt on every `make generate`. Do not edit by hand.
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
            return attach_rate_limit(
                rest_models.ListAgentAlertsResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
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
            return attach_rate_limit(
                rest_models.CreateAgentAlertResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
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
            return attach_rate_limit(
                rest_models.GetAgentAlertResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
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
            return attach_rate_limit(
                rest_models.UpdateAgentAlertResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
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
            return attach_rate_limit(
                rest_models.DeleteAgentAlertResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
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
            return attach_rate_limit(
                rest_models.ListAgentsResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
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
            return attach_rate_limit(
                rest_models.GetAgentResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
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
            return attach_rate_limit(
                rest_models.UpdateAgentResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
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
            return attach_rate_limit(
                rest_models.DeleteAgentResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
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
            return attach_rate_limit(
                rest_models.ListTestsResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
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
            return attach_rate_limit(
                rest_models.CreateTestResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
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
            return attach_rate_limit(
                rest_models.GetTestResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
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
            return attach_rate_limit(
                rest_models.UpdateTestResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
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
            return attach_rate_limit(
                rest_models.DeleteTestResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
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
            return attach_rate_limit(
                rest_models.SetTestStatusResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
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
            return attach_rate_limit(
                rest_models.GetResultsForTestsResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
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
            return attach_rate_limit(
                rest_models.GetResultsForTestsCsvResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
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
            return attach_rate_limit(
                rest_models.GetTraceForTestResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
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
