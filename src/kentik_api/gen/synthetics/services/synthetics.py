from typing import List, Optional, Union, cast

from google.protobuf.json_format import MessageToDict, ParseDict

import kentik_api.gen.synthetics.services.SyntheticsAdminService as RestSyntheticsModule1
import kentik_api.gen.synthetics.services.SyntheticsDataService as RestSyntheticsModule2
from kentik_api.core.grpc_runtime import call_grpc
from kentik_api.gen.synthetics import models as rest_models
from kentik_api.transports.grpc_client import GrpcTransport
from kentik_api.transports.rest_client import RestTransport


class SyntheticsServiceWrapper:
    """Unified Service routing to either gRPC or REST."""

    def __init__(self, transport: Union[GrpcTransport, RestTransport]):
        self._transport = transport
        if isinstance(self._transport, GrpcTransport):
            try:
                import kentik_api.gen.synthetics.pb.synthetics_pb2 as _pb2_1_mod
                import kentik_api.gen.synthetics.pb.synthetics_pb2_grpc as _pb2_grpc_1_mod

                self._grpc_pb2_1 = _pb2_1_mod
                self._grpc_stub_1 = _pb2_grpc_1_mod.SyntheticsDataServiceStub(
                    self._transport.channel
                )
            except (ImportError, TypeError):
                self._grpc_pb2_1 = None
                self._grpc_stub_1 = None
            try:
                import kentik_api.gen.synthetics.pb.synthetics_pb2 as _pb2_2_mod
                import kentik_api.gen.synthetics.pb.synthetics_pb2_grpc as _pb2_grpc_2_mod

                self._grpc_pb2_2 = _pb2_2_mod
                self._grpc_stub_2 = _pb2_grpc_2_mod.SyntheticsAdminServiceStub(
                    self._transport.channel
                )
            except (ImportError, TypeError):
                self._grpc_pb2_2 = None
                self._grpc_stub_2 = None

    def list_agent_alerts(
        self,
        *,
        agentIds: Optional[List[str]] = None,
    ) -> rest_models.ListAgentAlertsResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_2 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for synthetics service"
                )
            _req = ParseDict(
                {k: v for k, v in {"agentIds": agentIds}.items() if v is not None},
                self._grpc_pb2_2.ListAgentAlertsRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_2.ListAgentAlerts, _req)
            return rest_models.ListAgentAlertsResponse.model_validate(
                MessageToDict(_resp)
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestSyntheticsModule1.ListAgentAlerts(
                api_config_override=rest_transport.api_config, agentIds=agentIds
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def create_agent_alert(
        self, *, data: rest_models.CreateAgentAlertRequest
    ) -> rest_models.CreateAgentAlertResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_2 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for synthetics service"
                )
            _req = ParseDict(
                data.model_dump(by_alias=True, exclude_none=True),
                self._grpc_pb2_2.CreateAgentAlertRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_2.CreateAgentAlert, _req)
            return rest_models.CreateAgentAlertResponse.model_validate(
                MessageToDict(_resp)
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestSyntheticsModule1.CreateAgentAlert(
                api_config_override=rest_transport.api_config, data=data
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def get_agent_alert(self, *, id: str) -> rest_models.GetAgentAlertResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_2 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for synthetics service"
                )
            _req = ParseDict(
                {k: v for k, v in {"id": id}.items() if v is not None},
                self._grpc_pb2_2.GetAgentAlertRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_2.GetAgentAlert, _req)
            return rest_models.GetAgentAlertResponse.model_validate(
                MessageToDict(_resp)
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestSyntheticsModule1.GetAgentAlert(
                api_config_override=rest_transport.api_config, id=id
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def update_agent_alert(
        self,
        *,
        id: str,
        data: rest_models.SyntheticsAdminServiceUpdateAgentAlertBody,
    ) -> rest_models.UpdateAgentAlertResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_2 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for synthetics service"
                )
            _req_dict = data.model_dump(by_alias=True, exclude_none=True)
            _req_dict.update({k: v for k, v in {"id": id}.items() if v is not None})
            _req = ParseDict(
                _req_dict,
                self._grpc_pb2_2.UpdateAgentAlertRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_2.UpdateAgentAlert, _req)
            return rest_models.UpdateAgentAlertResponse.model_validate(
                MessageToDict(_resp)
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestSyntheticsModule1.UpdateAgentAlert(
                api_config_override=rest_transport.api_config, id=id, data=data
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def delete_agent_alert(self, *, id: str) -> rest_models.DeleteAgentAlertResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_2 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for synthetics service"
                )
            _req = ParseDict(
                {k: v for k, v in {"id": id}.items() if v is not None},
                self._grpc_pb2_2.DeleteAgentAlertRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_2.DeleteAgentAlert, _req)
            return rest_models.DeleteAgentAlertResponse.model_validate(
                MessageToDict(_resp)
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestSyntheticsModule1.DeleteAgentAlert(
                api_config_override=rest_transport.api_config, id=id
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def list_agents(
        self,
    ) -> rest_models.ListAgentsResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_2 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for synthetics service"
                )
            _req = self._grpc_pb2_2.ListAgentsRequest()
            _resp = call_grpc(self._grpc_stub_2.ListAgents, _req)
            return rest_models.ListAgentsResponse.model_validate(MessageToDict(_resp))
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestSyntheticsModule1.ListAgents(
                api_config_override=rest_transport.api_config
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def get_agent(self, *, agentid: str) -> rest_models.GetAgentResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_2 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for synthetics service"
                )
            _req = ParseDict(
                {k: v for k, v in {"agentid": agentid}.items() if v is not None},
                self._grpc_pb2_2.GetAgentRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_2.GetAgent, _req)
            return rest_models.GetAgentResponse.model_validate(MessageToDict(_resp))
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestSyntheticsModule1.GetAgent(
                api_config_override=rest_transport.api_config, agentid=agentid
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def update_agent(
        self,
        *,
        agentid: str,
        data: rest_models.SyntheticsAdminServiceUpdateAgentBody,
    ) -> rest_models.UpdateAgentResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_2 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for synthetics service"
                )
            _req_dict = data.model_dump(by_alias=True, exclude_none=True)
            _req_dict.update(
                {k: v for k, v in {"agentid": agentid}.items() if v is not None}
            )
            _req = ParseDict(
                _req_dict,
                self._grpc_pb2_2.UpdateAgentRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_2.UpdateAgent, _req)
            return rest_models.UpdateAgentResponse.model_validate(MessageToDict(_resp))
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestSyntheticsModule1.UpdateAgent(
                api_config_override=rest_transport.api_config,
                agentid=agentid,
                data=data,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def delete_agent(self, *, agentid: str) -> rest_models.DeleteAgentResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_2 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for synthetics service"
                )
            _req = ParseDict(
                {k: v for k, v in {"agentid": agentid}.items() if v is not None},
                self._grpc_pb2_2.DeleteAgentRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_2.DeleteAgent, _req)
            return rest_models.DeleteAgentResponse.model_validate(MessageToDict(_resp))
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestSyntheticsModule1.DeleteAgent(
                api_config_override=rest_transport.api_config, agentid=agentid
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def list_tests(
        self,
    ) -> rest_models.ListTestsResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_2 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for synthetics service"
                )
            _req = self._grpc_pb2_2.ListTestsRequest()
            _resp = call_grpc(self._grpc_stub_2.ListTests, _req)
            return rest_models.ListTestsResponse.model_validate(MessageToDict(_resp))
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestSyntheticsModule1.ListTests(
                api_config_override=rest_transport.api_config
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def create_test(
        self, *, data: rest_models.CreateTestRequest
    ) -> rest_models.CreateTestResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_2 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for synthetics service"
                )
            _req = ParseDict(
                data.model_dump(by_alias=True, exclude_none=True),
                self._grpc_pb2_2.CreateTestRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_2.CreateTest, _req)
            return rest_models.CreateTestResponse.model_validate(MessageToDict(_resp))
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestSyntheticsModule1.CreateTest(
                api_config_override=rest_transport.api_config, data=data
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def get_test(self, *, id: str) -> rest_models.GetTestResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_2 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for synthetics service"
                )
            _req = ParseDict(
                {k: v for k, v in {"id": id}.items() if v is not None},
                self._grpc_pb2_2.GetTestRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_2.GetTest, _req)
            return rest_models.GetTestResponse.model_validate(MessageToDict(_resp))
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestSyntheticsModule1.GetTest(
                api_config_override=rest_transport.api_config, id=id
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def update_test(
        self,
        *,
        id: str,
        data: rest_models.SyntheticsAdminServiceUpdateTestBody,
    ) -> rest_models.UpdateTestResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_2 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for synthetics service"
                )
            _req_dict = data.model_dump(by_alias=True, exclude_none=True)
            _req_dict.update({k: v for k, v in {"id": id}.items() if v is not None})
            _req = ParseDict(
                _req_dict,
                self._grpc_pb2_2.UpdateTestRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_2.UpdateTest, _req)
            return rest_models.UpdateTestResponse.model_validate(MessageToDict(_resp))
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestSyntheticsModule1.UpdateTest(
                api_config_override=rest_transport.api_config, id=id, data=data
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def delete_test(self, *, id: str) -> rest_models.DeleteTestResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_2 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for synthetics service"
                )
            _req = ParseDict(
                {k: v for k, v in {"id": id}.items() if v is not None},
                self._grpc_pb2_2.DeleteTestRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_2.DeleteTest, _req)
            return rest_models.DeleteTestResponse.model_validate(MessageToDict(_resp))
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestSyntheticsModule1.DeleteTest(
                api_config_override=rest_transport.api_config, id=id
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def set_test_status(
        self,
        *,
        id: str,
        data: rest_models.SyntheticsAdminServiceSetTestStatusBody,
    ) -> rest_models.SetTestStatusResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_2 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for synthetics service"
                )
            _req_dict = data.model_dump(by_alias=True, exclude_none=True)
            _req_dict.update({k: v for k, v in {"id": id}.items() if v is not None})
            _req = ParseDict(
                _req_dict,
                self._grpc_pb2_2.SetTestStatusRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_2.SetTestStatus, _req)
            return rest_models.SetTestStatusResponse.model_validate(
                MessageToDict(_resp)
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestSyntheticsModule1.SetTestStatus(
                api_config_override=rest_transport.api_config, id=id, data=data
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def get_results_for_tests(
        self, *, data: rest_models.GetResultsForTestsRequest
    ) -> rest_models.GetResultsForTestsResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for synthetics service"
                )
            _req = ParseDict(
                data.model_dump(by_alias=True, exclude_none=True),
                self._grpc_pb2_1.GetResultsForTestsRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_1.GetResultsForTests, _req)
            return rest_models.GetResultsForTestsResponse.model_validate(
                MessageToDict(_resp)
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestSyntheticsModule2.GetResultsForTests(
                api_config_override=rest_transport.api_config, data=data
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def get_results_for_tests_csv(
        self,
        *,
        data: rest_models.GetResultsForTestsCsvRequest,
    ) -> rest_models.GetResultsForTestsCsvResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for synthetics service"
                )
            _req = ParseDict(
                data.model_dump(by_alias=True, exclude_none=True),
                self._grpc_pb2_1.GetResultsForTestsCsvRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_1.GetResultsForTestsCsv, _req)
            return rest_models.GetResultsForTestsCsvResponse.model_validate(
                MessageToDict(_resp)
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestSyntheticsModule2.GetResultsForTestsCsv(
                api_config_override=rest_transport.api_config, data=data
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def get_trace_for_test(
        self, *, data: rest_models.GetTraceForTestRequest
    ) -> rest_models.GetTraceForTestResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for synthetics service"
                )
            _req = ParseDict(
                data.model_dump(by_alias=True, exclude_none=True),
                self._grpc_pb2_1.GetTraceForTestRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_1.GetTraceForTest, _req)
            return rest_models.GetTraceForTestResponse.model_validate(
                MessageToDict(_resp)
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestSyntheticsModule2.GetTraceForTest(
                api_config_override=rest_transport.api_config, data=data
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )
