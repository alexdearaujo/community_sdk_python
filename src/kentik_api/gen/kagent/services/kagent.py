from typing import Any, Dict, List, Optional, Union, cast

from google.protobuf.json_format import MessageToDict

import kentik_api.gen.kagent.services.AgentCapabilityService as RestKagentModule1
import kentik_api.gen.kagent.services.AgentService as RestKagentModule2
import kentik_api.gen.kagent.services.CapabilityAdminService as RestKagentModule3
import kentik_api.gen.kagent.services.CapabilityReleaseService as RestKagentModule4
import kentik_api.gen.kagent.services.ConfigService as RestKagentModule5
import kentik_api.gen.kagent.services.ProvisioningTokenService as RestKagentModule6
from kentik_api.core.api_config import APIConfig
from kentik_api.core.grpc_runtime import build_grpc_request, call_grpc
from kentik_api.core.rate_limit import attach_rate_limit
from kentik_api.gen.kagent import models as rest_models
from kentik_api.transports.grpc_client import GrpcTransport
from kentik_api.transports.rest_client import RestTransport


class KagentServiceWrapper:
    """AUTO-GENERATED: scripts/generation/wrapper_generation.py, _generate_service_wrappers().
    Rebuilt on every `make generate`. Do not edit by hand.
    Unified Service routing to either gRPC or REST.
    """

    def __init__(self, transport: Union[GrpcTransport, RestTransport]):
        self._transport = transport
        if isinstance(self._transport, GrpcTransport):
            try:
                __import__("kentik_api.gen.pb_companions")
                import kentik_api.gen.kagent.pb.agent_capabilities_pb2 as _pb2_1_mod
                import kentik_api.gen.kagent.pb.agent_capabilities_pb2_grpc as _pb2_grpc_1_mod

                self._grpc_pb2_1 = _pb2_1_mod
                self._grpc_stub_1 = _pb2_grpc_1_mod.AgentCapabilityServiceStub(
                    self._transport.channel
                )
            except (ImportError, TypeError):
                self._grpc_pb2_1 = None
                self._grpc_stub_1 = None
            try:
                __import__("kentik_api.gen.pb_companions")
                import kentik_api.gen.kagent.pb.agent_pb2 as _pb2_2_mod
                import kentik_api.gen.kagent.pb.agent_pb2_grpc as _pb2_grpc_2_mod

                self._grpc_pb2_2 = _pb2_2_mod
                self._grpc_stub_2 = _pb2_grpc_2_mod.AgentServiceStub(
                    self._transport.channel
                )
            except (ImportError, TypeError):
                self._grpc_pb2_2 = None
                self._grpc_stub_2 = None
            try:
                __import__("kentik_api.gen.pb_companions")
                import kentik_api.gen.kagent.pb.capability_pb2 as _pb2_3_mod
                import kentik_api.gen.kagent.pb.capability_pb2_grpc as _pb2_grpc_3_mod

                self._grpc_pb2_3 = _pb2_3_mod
                self._grpc_stub_3 = _pb2_grpc_3_mod.CapabilityReleaseServiceStub(
                    self._transport.channel
                )
            except (ImportError, TypeError):
                self._grpc_pb2_3 = None
                self._grpc_stub_3 = None
            try:
                __import__("kentik_api.gen.pb_companions")
                import kentik_api.gen.kagent.pb.capability_pb2 as _pb2_4_mod
                import kentik_api.gen.kagent.pb.capability_pb2_grpc as _pb2_grpc_4_mod

                self._grpc_pb2_4 = _pb2_4_mod
                self._grpc_stub_4 = _pb2_grpc_4_mod.CapabilityAdminServiceStub(
                    self._transport.channel
                )
            except (ImportError, TypeError):
                self._grpc_pb2_4 = None
                self._grpc_stub_4 = None
            try:
                __import__("kentik_api.gen.pb_companions")
                import kentik_api.gen.kagent.pb.config_pb2 as _pb2_5_mod
                import kentik_api.gen.kagent.pb.config_pb2_grpc as _pb2_grpc_5_mod

                self._grpc_pb2_5 = _pb2_5_mod
                self._grpc_stub_5 = _pb2_grpc_5_mod.ConfigServiceStub(
                    self._transport.channel
                )
            except (ImportError, TypeError):
                self._grpc_pb2_5 = None
                self._grpc_stub_5 = None
            try:
                __import__("kentik_api.gen.pb_companions")
                import kentik_api.gen.kagent.pb.provisioning_token_pb2 as _pb2_6_mod
                import kentik_api.gen.kagent.pb.provisioning_token_pb2_grpc as _pb2_grpc_6_mod

                self._grpc_pb2_6 = _pb2_6_mod
                self._grpc_stub_6 = _pb2_grpc_6_mod.ProvisioningTokenServiceStub(
                    self._transport.channel
                )
            except (ImportError, TypeError):
                self._grpc_pb2_6 = None
                self._grpc_stub_6 = None

    def list_agent_capabilities(
        self, *, api_config_override: Optional[APIConfig] = None, agentId: str
    ) -> rest_models.ListAgentCapabilitiesResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_1 is None or self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for kagent service"
                )
            _req = build_grpc_request(
                self._grpc_pb2_1.ListAgentCapabilitiesRequest,
                None,
                {"agent_id": agentId},
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_1.ListAgentCapabilities,
                _req,
                api_config=api_config_override,
                error_cls=RestKagentModule1.ListAgentCapabilitiesError,
            )
            return attach_rate_limit(
                rest_models.ListAgentCapabilitiesResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestKagentModule1.ListAgentCapabilities(
                api_config_override=api_config_override or rest_transport.api_config,
                agentId=agentId,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def get_agent_capability(
        self,
        *,
        api_config_override: Optional[APIConfig] = None,
        agentId: str,
        capabilityname: str,
    ) -> rest_models.GetAgentCapabilityResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_1 is None or self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for kagent service"
                )
            _req = build_grpc_request(
                self._grpc_pb2_1.GetAgentCapabilityRequest,
                None,
                {"agent_id": agentId, "capability": capabilityname},
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_1.GetAgentCapability,
                _req,
                api_config=api_config_override,
                error_cls=RestKagentModule1.GetAgentCapabilityError,
            )
            return attach_rate_limit(
                rest_models.GetAgentCapabilityResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestKagentModule1.GetAgentCapability(
                api_config_override=api_config_override or rest_transport.api_config,
                agentId=agentId,
                capabilityname=capabilityname,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def delete_agent_capability(
        self,
        *,
        api_config_override: Optional[APIConfig] = None,
        agentId: str,
        capabilityname: str,
    ) -> rest_models.DeleteAgentCapabilityResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_1 is None or self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for kagent service"
                )
            _req = build_grpc_request(
                self._grpc_pb2_1.DeleteAgentCapabilityRequest,
                None,
                {"agent_id": agentId, "capability": capabilityname},
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_1.DeleteAgentCapability,
                _req,
                api_config=api_config_override,
                error_cls=RestKagentModule1.DeleteAgentCapabilityError,
            )
            return attach_rate_limit(
                rest_models.DeleteAgentCapabilityResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestKagentModule1.DeleteAgentCapability(
                api_config_override=api_config_override or rest_transport.api_config,
                agentId=agentId,
                capabilityname=capabilityname,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def upsert_agent_capability(
        self,
        *,
        api_config_override: Optional[APIConfig] = None,
        agentId: str,
        capabilityname: str,
        data: Dict[str, Any],
        mask: Optional[str] = None,
    ) -> rest_models.UpsertAgentCapabilityResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_1 is None or self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for kagent service"
                )
            _req = build_grpc_request(
                self._grpc_pb2_1.UpsertAgentCapabilityRequest,
                {"capability": dict(data)},
                {"agent_id": agentId, "capability.name": capabilityname, "mask": mask},
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_1.UpsertAgentCapability,
                _req,
                api_config=api_config_override,
                error_cls=RestKagentModule1.UpsertAgentCapabilityError,
            )
            return attach_rate_limit(
                rest_models.UpsertAgentCapabilityResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestKagentModule1.UpsertAgentCapability(
                api_config_override=api_config_override or rest_transport.api_config,
                agentId=agentId,
                capabilityname=capabilityname,
                data=data,
                mask=mask,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def list_agents(
        self,
        *,
        api_config_override: Optional[APIConfig] = None,
        unregistered: Optional[bool] = None,
        ids: Optional[List[str]] = None,
        capabilities: Optional[List[str]] = None,
        includeDesiredState: Optional[bool] = None,
    ) -> rest_models.ListAgentsResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_2 is None or self._grpc_stub_2 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for kagent service"
                )
            _req = build_grpc_request(
                self._grpc_pb2_2.ListAgentsRequest,
                None,
                {
                    "unregistered": unregistered,
                    "ids": ids,
                    "capabilities": capabilities,
                    "includeDesiredState": includeDesiredState,
                },
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_2.ListAgents,
                _req,
                api_config=api_config_override,
                error_cls=RestKagentModule2.ListAgentsError,
            )
            return attach_rate_limit(
                rest_models.ListAgentsResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestKagentModule2.ListAgents(
                api_config_override=api_config_override or rest_transport.api_config,
                unregistered=unregistered,
                ids=ids,
                capabilities=capabilities,
                includeDesiredState=includeDesiredState,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def create_agent(
        self,
        *,
        api_config_override: Optional[APIConfig] = None,
        data: rest_models.CreateAgentRequest,
    ) -> rest_models.CreateAgentResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_2 is None or self._grpc_stub_2 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for kagent service"
                )
            _req = build_grpc_request(
                self._grpc_pb2_2.CreateAgentRequest,
                data.model_dump(by_alias=True, exclude_none=True),
                {},
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_2.CreateAgent,
                _req,
                api_config=api_config_override,
                error_cls=RestKagentModule2.CreateAgentError,
            )
            return attach_rate_limit(
                rest_models.CreateAgentResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestKagentModule2.CreateAgent(
                api_config_override=api_config_override or rest_transport.api_config,
                data=data,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def authorize(
        self, *, api_config_override: Optional[APIConfig] = None, installId: str
    ) -> rest_models.AuthorizeResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_2 is None or self._grpc_stub_2 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for kagent service"
                )
            _req = build_grpc_request(
                self._grpc_pb2_2.AuthorizeRequest, None, {"install_id": installId}
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_2.Authorize,
                _req,
                api_config=api_config_override,
                error_cls=RestKagentModule2.AuthorizeError,
            )
            return attach_rate_limit(
                rest_models.AuthorizeResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestKagentModule2.Authorize(
                api_config_override=api_config_override or rest_transport.api_config,
                installId=installId,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def generate_install_commands(
        self,
        *,
        api_config_override: Optional[APIConfig] = None,
        data: rest_models.GenerateInstallCommandsRequest,
    ) -> rest_models.GenerateInstallCommandsResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_2 is None or self._grpc_stub_2 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for kagent service"
                )
            _req = build_grpc_request(
                self._grpc_pb2_2.GenerateInstallCommandsRequest,
                data.model_dump(by_alias=True, exclude_none=True),
                {},
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_2.GenerateInstallCommands,
                _req,
                api_config=api_config_override,
                error_cls=RestKagentModule2.GenerateInstallCommandsError,
            )
            return attach_rate_limit(
                rest_models.GenerateInstallCommandsResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestKagentModule2.GenerateInstallCommands(
                api_config_override=api_config_override or rest_transport.api_config,
                data=data,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def get_agent(
        self,
        *,
        api_config_override: Optional[APIConfig] = None,
        agentid: str,
        unregistered: Optional[bool] = None,
    ) -> rest_models.GetAgentResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_2 is None or self._grpc_stub_2 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for kagent service"
                )
            _req = build_grpc_request(
                self._grpc_pb2_2.GetAgentRequest,
                None,
                {"id": agentid, "unregistered": unregistered},
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_2.GetAgent,
                _req,
                api_config=api_config_override,
                error_cls=RestKagentModule2.GetAgentError,
            )
            return attach_rate_limit(
                rest_models.GetAgentResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestKagentModule2.GetAgent(
                api_config_override=api_config_override or rest_transport.api_config,
                agentid=agentid,
                unregistered=unregistered,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def delete_agent(
        self,
        *,
        api_config_override: Optional[APIConfig] = None,
        agentid: str,
        unregistered: Optional[bool] = None,
    ) -> rest_models.DeleteAgentResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_2 is None or self._grpc_stub_2 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for kagent service"
                )
            _req = build_grpc_request(
                self._grpc_pb2_2.DeleteAgentRequest,
                None,
                {"id": agentid, "unregistered": unregistered},
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_2.DeleteAgent,
                _req,
                api_config=api_config_override,
                error_cls=RestKagentModule2.DeleteAgentError,
            )
            return attach_rate_limit(
                rest_models.DeleteAgentResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestKagentModule2.DeleteAgent(
                api_config_override=api_config_override or rest_transport.api_config,
                agentid=agentid,
                unregistered=unregistered,
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
        data: Dict[str, Any],
        mask: Optional[str] = None,
    ) -> rest_models.UpdateAgentResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_2 is None or self._grpc_stub_2 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for kagent service"
                )
            _req = build_grpc_request(
                self._grpc_pb2_2.UpdateAgentRequest,
                {"agent": dict(data)},
                {"agent.id": agentid, "mask": mask},
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_2.UpdateAgent,
                _req,
                api_config=api_config_override,
                error_cls=RestKagentModule2.UpdateAgentError,
            )
            return attach_rate_limit(
                rest_models.UpdateAgentResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestKagentModule2.UpdateAgent(
                api_config_override=api_config_override or rest_transport.api_config,
                agentid=agentid,
                data=data,
                mask=mask,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def capability_admin_service__list_capabilities(
        self, *, api_config_override: Optional[APIConfig] = None
    ) -> rest_models.ListCapabilitiesResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_4 is None or self._grpc_stub_4 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for kagent service"
                )
            _req = build_grpc_request(
                self._grpc_pb2_4.ListCapabilitiesRequest, None, {}
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_4.ListCapabilities,
                _req,
                api_config=api_config_override,
                error_cls=RestKagentModule3.CapabilityAdminService_ListCapabilitiesError,
            )
            return attach_rate_limit(
                rest_models.ListCapabilitiesResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestKagentModule3.CapabilityAdminService_ListCapabilities(
                api_config_override=api_config_override or rest_transport.api_config
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def capability_admin_service__create_capability(
        self,
        *,
        api_config_override: Optional[APIConfig] = None,
        data: rest_models.Capability,
    ) -> rest_models.CreateCapabilityResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_4 is None or self._grpc_stub_4 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for kagent service"
                )
            _req = build_grpc_request(
                self._grpc_pb2_4.CreateCapabilityRequest,
                {"capability": data.model_dump(by_alias=True, exclude_none=True)},
                {},
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_4.CreateCapability,
                _req,
                api_config=api_config_override,
                error_cls=RestKagentModule3.CapabilityAdminService_CreateCapabilityError,
            )
            return attach_rate_limit(
                rest_models.CreateCapabilityResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestKagentModule3.CapabilityAdminService_CreateCapability(
                api_config_override=api_config_override or rest_transport.api_config,
                data=data,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def capability_admin_service__get_capability(
        self, *, api_config_override: Optional[APIConfig] = None, capabilityname: str
    ) -> rest_models.GetCapabilityResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_4 is None or self._grpc_stub_4 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for kagent service"
                )
            _req = build_grpc_request(
                self._grpc_pb2_4.GetCapabilityRequest, None, {"name": capabilityname}
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_4.GetCapability,
                _req,
                api_config=api_config_override,
                error_cls=RestKagentModule3.CapabilityAdminService_GetCapabilityError,
            )
            return attach_rate_limit(
                rest_models.GetCapabilityResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestKagentModule3.CapabilityAdminService_GetCapability(
                api_config_override=api_config_override or rest_transport.api_config,
                capabilityname=capabilityname,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def capability_admin_service__delete_capability(
        self, *, api_config_override: Optional[APIConfig] = None, capabilityname: str
    ) -> rest_models.DeleteCapabilityResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_4 is None or self._grpc_stub_4 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for kagent service"
                )
            _req = build_grpc_request(
                self._grpc_pb2_4.DeleteCapabilityRequest, None, {"name": capabilityname}
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_4.DeleteCapability,
                _req,
                api_config=api_config_override,
                error_cls=RestKagentModule3.CapabilityAdminService_DeleteCapabilityError,
            )
            return attach_rate_limit(
                rest_models.DeleteCapabilityResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestKagentModule3.CapabilityAdminService_DeleteCapability(
                api_config_override=api_config_override or rest_transport.api_config,
                capabilityname=capabilityname,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def capability_admin_service__update_capability(
        self,
        *,
        api_config_override: Optional[APIConfig] = None,
        capabilityname: str,
        data: Dict[str, Any],
    ) -> rest_models.UpdateCapabilityResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_4 is None or self._grpc_stub_4 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for kagent service"
                )
            _req = build_grpc_request(
                self._grpc_pb2_4.UpdateCapabilityRequest,
                {"capability": dict(data)},
                {"capability.name": capabilityname},
                update_mask_from="capability",
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_4.UpdateCapability,
                _req,
                api_config=api_config_override,
                error_cls=RestKagentModule3.CapabilityAdminService_UpdateCapabilityError,
            )
            return attach_rate_limit(
                rest_models.UpdateCapabilityResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestKagentModule3.CapabilityAdminService_UpdateCapability(
                api_config_override=api_config_override or rest_transport.api_config,
                capabilityname=capabilityname,
                data=data,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def capability_release_service__get_capability_release(
        self,
        *,
        api_config_override: Optional[APIConfig] = None,
        os: Optional[str] = None,
        arch: Optional[str] = None,
        channel: Optional[str] = None,
        capability: Optional[str] = None,
        semver: Optional[str] = None,
        distro: Optional[str] = None,
    ) -> rest_models.GetCapabilityReleaseResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_3 is None or self._grpc_stub_3 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for kagent service"
                )
            _req = build_grpc_request(
                self._grpc_pb2_3.GetCapabilityReleaseRequest,
                None,
                {
                    "os": os,
                    "arch": arch,
                    "channel": channel,
                    "capability": capability,
                    "semver": semver,
                    "distro": distro,
                },
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_3.GetCapabilityRelease,
                _req,
                api_config=api_config_override,
                error_cls=RestKagentModule4.CapabilityReleaseService_GetCapabilityReleaseError,
            )
            return attach_rate_limit(
                rest_models.GetCapabilityReleaseResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestKagentModule4.CapabilityReleaseService_GetCapabilityRelease(
                api_config_override=api_config_override or rest_transport.api_config,
                os=os,
                arch=arch,
                channel=channel,
                capability=capability,
                semver=semver,
                distro=distro,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def capability_release_service__get_capability_latest_releases(
        self,
        *,
        api_config_override: Optional[APIConfig] = None,
        os: Optional[str] = None,
        arch: Optional[str] = None,
        channel: Optional[str] = None,
        installId: Optional[str] = None,
        capabilities: Optional[List[str]] = None,
        distro: Optional[str] = None,
    ) -> rest_models.GetCapabilityLatestReleasesResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_3 is None or self._grpc_stub_3 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for kagent service"
                )
            _req = build_grpc_request(
                self._grpc_pb2_3.GetCapabilityLatestReleasesRequest,
                None,
                {
                    "os": os,
                    "arch": arch,
                    "channel": channel,
                    "installId": installId,
                    "capabilities": capabilities,
                    "distro": distro,
                },
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_3.GetCapabilityLatestReleases,
                _req,
                api_config=api_config_override,
                error_cls=RestKagentModule4.CapabilityReleaseService_GetCapabilityLatestReleasesError,
            )
            return attach_rate_limit(
                rest_models.GetCapabilityLatestReleasesResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return (
                RestKagentModule4.CapabilityReleaseService_GetCapabilityLatestReleases(
                    api_config_override=api_config_override
                    or rest_transport.api_config,
                    os=os,
                    arch=arch,
                    channel=channel,
                    installId=installId,
                    capabilities=capabilities,
                    distro=distro,
                )
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def capability_release_service__get_capability_supported_distros(
        self,
        *,
        api_config_override: Optional[APIConfig] = None,
        capabilities: Optional[List[str]] = None,
    ) -> rest_models.GetCapabilitySupportedDistrosResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_3 is None or self._grpc_stub_3 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for kagent service"
                )
            _req = build_grpc_request(
                self._grpc_pb2_3.GetCapabilitySupportedDistrosRequest,
                None,
                {"capabilities": capabilities},
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_3.GetCapabilitySupportedDistros,
                _req,
                api_config=api_config_override,
                error_cls=RestKagentModule4.CapabilityReleaseService_GetCapabilitySupportedDistrosError,
            )
            return attach_rate_limit(
                rest_models.GetCapabilitySupportedDistrosResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestKagentModule4.CapabilityReleaseService_GetCapabilitySupportedDistros(
                api_config_override=api_config_override or rest_transport.api_config,
                capabilities=capabilities,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def create_config(
        self,
        *,
        api_config_override: Optional[APIConfig] = None,
        data: rest_models.Config,
    ) -> rest_models.CreateConfigResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_5 is None or self._grpc_stub_5 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for kagent service"
                )
            _req = build_grpc_request(
                self._grpc_pb2_5.CreateConfigRequest,
                {"config": data.model_dump(by_alias=True, exclude_none=True)},
                {},
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_5.CreateConfig,
                _req,
                api_config=api_config_override,
                error_cls=RestKagentModule5.CreateConfigError,
            )
            return attach_rate_limit(
                rest_models.CreateConfigResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestKagentModule5.CreateConfig(
                api_config_override=api_config_override or rest_transport.api_config,
                data=data,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def get_config(
        self, *, api_config_override: Optional[APIConfig] = None, configname: str
    ) -> rest_models.GetConfigResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_5 is None or self._grpc_stub_5 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for kagent service"
                )
            _req = build_grpc_request(
                self._grpc_pb2_5.GetConfigRequest, None, {"name": configname}
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_5.GetConfig,
                _req,
                api_config=api_config_override,
                error_cls=RestKagentModule5.GetConfigError,
            )
            return attach_rate_limit(
                rest_models.GetConfigResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestKagentModule5.GetConfig(
                api_config_override=api_config_override or rest_transport.api_config,
                configname=configname,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def delete_config(
        self, *, api_config_override: Optional[APIConfig] = None, configname: str
    ) -> rest_models.DeleteConfigResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_5 is None or self._grpc_stub_5 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for kagent service"
                )
            _req = build_grpc_request(
                self._grpc_pb2_5.DeleteConfigRequest, None, {"name": configname}
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_5.DeleteConfig,
                _req,
                api_config=api_config_override,
                error_cls=RestKagentModule5.DeleteConfigError,
            )
            return attach_rate_limit(
                rest_models.DeleteConfigResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestKagentModule5.DeleteConfig(
                api_config_override=api_config_override or rest_transport.api_config,
                configname=configname,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def update_config(
        self,
        *,
        api_config_override: Optional[APIConfig] = None,
        configname: str,
        data: rest_models.ConfigServiceUpdateConfigBody,
    ) -> rest_models.UpdateConfigResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_5 is None or self._grpc_stub_5 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for kagent service"
                )
            _req = build_grpc_request(
                self._grpc_pb2_5.UpdateConfigRequest,
                data.model_dump(by_alias=True, exclude_none=True),
                {"config.name": configname},
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_5.UpdateConfig,
                _req,
                api_config=api_config_override,
                error_cls=RestKagentModule5.UpdateConfigError,
            )
            return attach_rate_limit(
                rest_models.UpdateConfigResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestKagentModule5.UpdateConfig(
                api_config_override=api_config_override or rest_transport.api_config,
                configname=configname,
                data=data,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def list_provisioning_tokens(
        self, *, api_config_override: Optional[APIConfig] = None
    ) -> rest_models.ListProvisioningTokensResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_6 is None or self._grpc_stub_6 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for kagent service"
                )
            _req = build_grpc_request(
                self._grpc_pb2_6.ListProvisioningTokensRequest, None, {}
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_6.ListProvisioningTokens,
                _req,
                api_config=api_config_override,
                error_cls=RestKagentModule6.ListProvisioningTokensError,
            )
            return attach_rate_limit(
                rest_models.ListProvisioningTokensResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestKagentModule6.ListProvisioningTokens(
                api_config_override=api_config_override or rest_transport.api_config
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def create_provisioning_token(
        self,
        *,
        api_config_override: Optional[APIConfig] = None,
        data: rest_models.ProvisioningToken,
    ) -> rest_models.CreateProvisioningTokenResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_6 is None or self._grpc_stub_6 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for kagent service"
                )
            _req = build_grpc_request(
                self._grpc_pb2_6.CreateProvisioningTokenRequest,
                {"token": data.model_dump(by_alias=True, exclude_none=True)},
                {},
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_6.CreateProvisioningToken,
                _req,
                api_config=api_config_override,
                error_cls=RestKagentModule6.CreateProvisioningTokenError,
            )
            return attach_rate_limit(
                rest_models.CreateProvisioningTokenResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestKagentModule6.CreateProvisioningToken(
                api_config_override=api_config_override or rest_transport.api_config,
                data=data,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def get_provisioning_token(
        self, *, api_config_override: Optional[APIConfig] = None, token: str
    ) -> rest_models.GetProvisioningTokenResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_6 is None or self._grpc_stub_6 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for kagent service"
                )
            _req = build_grpc_request(
                self._grpc_pb2_6.GetProvisioningTokenRequest, None, {"token": token}
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_6.GetProvisioningToken,
                _req,
                api_config=api_config_override,
                error_cls=RestKagentModule6.GetProvisioningTokenError,
            )
            return attach_rate_limit(
                rest_models.GetProvisioningTokenResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestKagentModule6.GetProvisioningToken(
                api_config_override=api_config_override or rest_transport.api_config,
                token=token,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def list_agents_by_provisioning_token(
        self, *, api_config_override: Optional[APIConfig] = None, token: str
    ) -> rest_models.ListAgentsByProvisioningTokenResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_6 is None or self._grpc_stub_6 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for kagent service"
                )
            _req = build_grpc_request(
                self._grpc_pb2_6.ListAgentsByProvisioningTokenRequest,
                None,
                {"token": token},
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_6.ListAgentsByProvisioningToken,
                _req,
                api_config=api_config_override,
                error_cls=RestKagentModule6.ListAgentsByProvisioningTokenError,
            )
            return attach_rate_limit(
                rest_models.ListAgentsByProvisioningTokenResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestKagentModule6.ListAgentsByProvisioningToken(
                api_config_override=api_config_override or rest_transport.api_config,
                token=token,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def revoke_provisioning_token(
        self,
        *,
        api_config_override: Optional[APIConfig] = None,
        token: str,
        data: rest_models.ProvisioningTokenServiceRevokeProvisioningTokenBody,
    ) -> rest_models.RevokeProvisioningTokenResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_6 is None or self._grpc_stub_6 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for kagent service"
                )
            _req = build_grpc_request(
                self._grpc_pb2_6.RevokeProvisioningTokenRequest,
                data.model_dump(by_alias=True, exclude_none=True),
                {"token": token},
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_6.RevokeProvisioningToken,
                _req,
                api_config=api_config_override,
                error_cls=RestKagentModule6.RevokeProvisioningTokenError,
            )
            return attach_rate_limit(
                rest_models.RevokeProvisioningTokenResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestKagentModule6.RevokeProvisioningToken(
                api_config_override=api_config_override or rest_transport.api_config,
                token=token,
                data=data,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )
