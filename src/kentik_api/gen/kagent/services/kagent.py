from typing import Any, Dict, List, Optional, Union, cast

from google.protobuf.json_format import MessageToDict, ParseDict

import kentik_api.gen.kagent.services.AgentCapabilityService as RestKagentModule1
import kentik_api.gen.kagent.services.AgentService as RestKagentModule2
import kentik_api.gen.kagent.services.CapabilityAdminService as RestKagentModule3
import kentik_api.gen.kagent.services.CapabilityReleaseService as RestKagentModule4
import kentik_api.gen.kagent.services.ConfigService as RestKagentModule5
import kentik_api.gen.kagent.services.ProvisioningTokenService as RestKagentModule6
from kentik_api.core.grpc_runtime import call_grpc
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
        self, *, agentId: str
    ) -> rest_models.ListAgentCapabilitiesResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for kagent service"
                )
            _req = ParseDict(
                {k: v for k, v in {"agentId": agentId}.items() if v is not None},
                self._grpc_pb2_1.ListAgentCapabilitiesRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_1.ListAgentCapabilities, _req)
            return rest_models.ListAgentCapabilitiesResponse.model_validate(
                MessageToDict(_resp)
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestKagentModule1.ListAgentCapabilities(
                api_config_override=rest_transport.api_config, agentId=agentId
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def get_agent_capability(
        self, *, agentId: str, capabilityname: str
    ) -> rest_models.GetAgentCapabilityResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for kagent service"
                )
            _req = ParseDict(
                {
                    k: v
                    for k, v in {
                        "agentId": agentId,
                        "capabilityname": capabilityname,
                    }.items()
                    if v is not None
                },
                self._grpc_pb2_1.GetAgentCapabilityRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_1.GetAgentCapability, _req)
            return rest_models.GetAgentCapabilityResponse.model_validate(
                MessageToDict(_resp)
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestKagentModule1.GetAgentCapability(
                api_config_override=rest_transport.api_config,
                agentId=agentId,
                capabilityname=capabilityname,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def delete_agent_capability(
        self, *, agentId: str, capabilityname: str
    ) -> rest_models.DeleteAgentCapabilityResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for kagent service"
                )
            _req = ParseDict(
                {
                    k: v
                    for k, v in {
                        "agentId": agentId,
                        "capabilityname": capabilityname,
                    }.items()
                    if v is not None
                },
                self._grpc_pb2_1.DeleteAgentCapabilityRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_1.DeleteAgentCapability, _req)
            return rest_models.DeleteAgentCapabilityResponse.model_validate(
                MessageToDict(_resp)
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestKagentModule1.DeleteAgentCapability(
                api_config_override=rest_transport.api_config,
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
        agentId: str,
        capabilityname: str,
        data: Dict[str, Any],
        mask: Optional[str] = None,
    ) -> rest_models.UpsertAgentCapabilityResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_1 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for kagent service"
                )
            _req_dict = data.model_dump(by_alias=True, exclude_none=True)
            _req_dict.update(
                {
                    k: v
                    for k, v in {
                        "agentId": agentId,
                        "capabilityname": capabilityname,
                        "mask": mask,
                    }.items()
                    if v is not None
                }
            )
            _req = ParseDict(
                _req_dict,
                self._grpc_pb2_1.UpsertAgentCapabilityRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_1.UpsertAgentCapability, _req)
            return rest_models.UpsertAgentCapabilityResponse.model_validate(
                MessageToDict(_resp)
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestKagentModule1.UpsertAgentCapability(
                api_config_override=rest_transport.api_config,
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
        unregistered: Optional[bool] = None,
        ids: Optional[List[str]] = None,
        capabilities: Optional[List[str]] = None,
        includeDesiredState: Optional[bool] = None,
    ) -> rest_models.ListAgentsResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_2 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for kagent service"
                )
            _req = ParseDict(
                {
                    k: v
                    for k, v in {
                        "unregistered": unregistered,
                        "ids": ids,
                        "capabilities": capabilities,
                        "includeDesiredState": includeDesiredState,
                    }.items()
                    if v is not None
                },
                self._grpc_pb2_2.ListAgentsRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_2.ListAgents, _req)
            return rest_models.ListAgentsResponse.model_validate(MessageToDict(_resp))
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestKagentModule2.ListAgents(
                api_config_override=rest_transport.api_config,
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
        self, *, data: rest_models.CreateAgentRequest
    ) -> rest_models.CreateAgentResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_2 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for kagent service"
                )
            _req = ParseDict(
                data.model_dump(by_alias=True, exclude_none=True),
                self._grpc_pb2_2.CreateAgentRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_2.CreateAgent, _req)
            return rest_models.CreateAgentResponse.model_validate(MessageToDict(_resp))
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestKagentModule2.CreateAgent(
                api_config_override=rest_transport.api_config, data=data
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def authorize(self, *, installId: str) -> rest_models.AuthorizeResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_2 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for kagent service"
                )
            _req = ParseDict(
                {k: v for k, v in {"installId": installId}.items() if v is not None},
                self._grpc_pb2_2.AuthorizeRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_2.Authorize, _req)
            return rest_models.AuthorizeResponse.model_validate(MessageToDict(_resp))
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestKagentModule2.Authorize(
                api_config_override=rest_transport.api_config, installId=installId
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def generate_install_commands(
        self, *, data: rest_models.GenerateInstallCommandsRequest
    ) -> rest_models.GenerateInstallCommandsResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_2 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for kagent service"
                )
            _req = ParseDict(
                data.model_dump(by_alias=True, exclude_none=True),
                self._grpc_pb2_2.GenerateInstallCommandsRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_2.GenerateInstallCommands, _req)
            return rest_models.GenerateInstallCommandsResponse.model_validate(
                MessageToDict(_resp)
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestKagentModule2.GenerateInstallCommands(
                api_config_override=rest_transport.api_config, data=data
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def get_agent(
        self, *, agentid: str, unregistered: Optional[bool] = None
    ) -> rest_models.GetAgentResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_2 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for kagent service"
                )
            _req = ParseDict(
                {
                    k: v
                    for k, v in {
                        "agentid": agentid,
                        "unregistered": unregistered,
                    }.items()
                    if v is not None
                },
                self._grpc_pb2_2.GetAgentRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_2.GetAgent, _req)
            return rest_models.GetAgentResponse.model_validate(MessageToDict(_resp))
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestKagentModule2.GetAgent(
                api_config_override=rest_transport.api_config,
                agentid=agentid,
                unregistered=unregistered,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def delete_agent(
        self, *, agentid: str, unregistered: Optional[bool] = None
    ) -> rest_models.DeleteAgentResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_2 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for kagent service"
                )
            _req = ParseDict(
                {
                    k: v
                    for k, v in {
                        "agentid": agentid,
                        "unregistered": unregistered,
                    }.items()
                    if v is not None
                },
                self._grpc_pb2_2.DeleteAgentRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_2.DeleteAgent, _req)
            return rest_models.DeleteAgentResponse.model_validate(MessageToDict(_resp))
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestKagentModule2.DeleteAgent(
                api_config_override=rest_transport.api_config,
                agentid=agentid,
                unregistered=unregistered,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def update_agent(
        self, *, agentid: str, data: Dict[str, Any], mask: Optional[str] = None
    ) -> rest_models.UpdateAgentResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_2 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for kagent service"
                )
            _req_dict = data.model_dump(by_alias=True, exclude_none=True)
            _req_dict.update(
                {
                    k: v
                    for k, v in {"agentid": agentid, "mask": mask}.items()
                    if v is not None
                }
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
            return RestKagentModule2.UpdateAgent(
                api_config_override=rest_transport.api_config,
                agentid=agentid,
                data=data,
                mask=mask,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def capability_admin_service__list_capabilities(
        self,
    ) -> rest_models.ListCapabilitiesResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for CapabilityAdminService_ListCapabilities is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestKagentModule3.CapabilityAdminService_ListCapabilities(
                api_config_override=rest_transport.api_config
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def capability_admin_service__create_capability(
        self, *, data: rest_models.Capability
    ) -> rest_models.CreateCapabilityResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for CapabilityAdminService_CreateCapability is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestKagentModule3.CapabilityAdminService_CreateCapability(
                api_config_override=rest_transport.api_config, data=data
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def capability_admin_service__get_capability(
        self, *, capabilityname: str
    ) -> rest_models.GetCapabilityResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for CapabilityAdminService_GetCapability is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestKagentModule3.CapabilityAdminService_GetCapability(
                api_config_override=rest_transport.api_config,
                capabilityname=capabilityname,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def capability_admin_service__delete_capability(
        self, *, capabilityname: str
    ) -> rest_models.DeleteCapabilityResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for CapabilityAdminService_DeleteCapability is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestKagentModule3.CapabilityAdminService_DeleteCapability(
                api_config_override=rest_transport.api_config,
                capabilityname=capabilityname,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def capability_admin_service__update_capability(
        self, *, capabilityname: str, data: Dict[str, Any]
    ) -> rest_models.UpdateCapabilityResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for CapabilityAdminService_UpdateCapability is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestKagentModule3.CapabilityAdminService_UpdateCapability(
                api_config_override=rest_transport.api_config,
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
        os: Optional[str] = None,
        arch: Optional[str] = None,
        channel: Optional[str] = None,
        capability: Optional[str] = None,
        semver: Optional[str] = None,
        distro: Optional[str] = None,
    ) -> rest_models.GetCapabilityReleaseResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for CapabilityReleaseService_GetCapabilityRelease is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestKagentModule4.CapabilityReleaseService_GetCapabilityRelease(
                api_config_override=rest_transport.api_config,
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
        os: Optional[str] = None,
        arch: Optional[str] = None,
        channel: Optional[str] = None,
        installId: Optional[str] = None,
        capabilities: Optional[List[str]] = None,
        distro: Optional[str] = None,
    ) -> rest_models.GetCapabilityLatestReleasesResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for CapabilityReleaseService_GetCapabilityLatestReleases is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return (
                RestKagentModule4.CapabilityReleaseService_GetCapabilityLatestReleases(
                    api_config_override=rest_transport.api_config,
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
        self, *, capabilities: Optional[List[str]] = None
    ) -> rest_models.GetCapabilitySupportedDistrosResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for CapabilityReleaseService_GetCapabilitySupportedDistros is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestKagentModule4.CapabilityReleaseService_GetCapabilitySupportedDistros(
                api_config_override=rest_transport.api_config, capabilities=capabilities
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def create_config(
        self, *, data: rest_models.Config
    ) -> rest_models.CreateConfigResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_5 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for kagent service"
                )
            _req = ParseDict(
                data.model_dump(by_alias=True, exclude_none=True),
                self._grpc_pb2_5.CreateConfigRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_5.CreateConfig, _req)
            return rest_models.CreateConfigResponse.model_validate(MessageToDict(_resp))
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestKagentModule5.CreateConfig(
                api_config_override=rest_transport.api_config, data=data
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def get_config(self, *, configname: str) -> rest_models.GetConfigResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_5 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for kagent service"
                )
            _req = ParseDict(
                {k: v for k, v in {"configname": configname}.items() if v is not None},
                self._grpc_pb2_5.GetConfigRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_5.GetConfig, _req)
            return rest_models.GetConfigResponse.model_validate(MessageToDict(_resp))
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestKagentModule5.GetConfig(
                api_config_override=rest_transport.api_config, configname=configname
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def delete_config(self, *, configname: str) -> rest_models.DeleteConfigResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_5 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for kagent service"
                )
            _req = ParseDict(
                {k: v for k, v in {"configname": configname}.items() if v is not None},
                self._grpc_pb2_5.DeleteConfigRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_5.DeleteConfig, _req)
            return rest_models.DeleteConfigResponse.model_validate(MessageToDict(_resp))
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestKagentModule5.DeleteConfig(
                api_config_override=rest_transport.api_config, configname=configname
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def update_config(
        self, *, configname: str, data: rest_models.ConfigServiceUpdateConfigBody
    ) -> rest_models.UpdateConfigResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_5 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for kagent service"
                )
            _req_dict = data.model_dump(by_alias=True, exclude_none=True)
            _req_dict.update(
                {k: v for k, v in {"configname": configname}.items() if v is not None}
            )
            _req = ParseDict(
                _req_dict,
                self._grpc_pb2_5.UpdateConfigRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_5.UpdateConfig, _req)
            return rest_models.UpdateConfigResponse.model_validate(MessageToDict(_resp))
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestKagentModule5.UpdateConfig(
                api_config_override=rest_transport.api_config,
                configname=configname,
                data=data,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def list_provisioning_tokens(
        self,
    ) -> rest_models.ListProvisioningTokensResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_6 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for kagent service"
                )
            _req = self._grpc_pb2_6.ListProvisioningTokensRequest()
            _resp = call_grpc(self._grpc_stub_6.ListProvisioningTokens, _req)
            return rest_models.ListProvisioningTokensResponse.model_validate(
                MessageToDict(_resp)
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestKagentModule6.ListProvisioningTokens(
                api_config_override=rest_transport.api_config
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def create_provisioning_token(
        self, *, data: rest_models.ProvisioningToken
    ) -> rest_models.CreateProvisioningTokenResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_6 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for kagent service"
                )
            _req = ParseDict(
                data.model_dump(by_alias=True, exclude_none=True),
                self._grpc_pb2_6.CreateProvisioningTokenRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_6.CreateProvisioningToken, _req)
            return rest_models.CreateProvisioningTokenResponse.model_validate(
                MessageToDict(_resp)
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestKagentModule6.CreateProvisioningToken(
                api_config_override=rest_transport.api_config, data=data
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def get_provisioning_token(
        self, *, token: str
    ) -> rest_models.GetProvisioningTokenResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_6 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for kagent service"
                )
            _req = ParseDict(
                {k: v for k, v in {"token": token}.items() if v is not None},
                self._grpc_pb2_6.GetProvisioningTokenRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_6.GetProvisioningToken, _req)
            return rest_models.GetProvisioningTokenResponse.model_validate(
                MessageToDict(_resp)
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestKagentModule6.GetProvisioningToken(
                api_config_override=rest_transport.api_config, token=token
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def list_agents_by_provisioning_token(
        self, *, token: str
    ) -> rest_models.ListAgentsByProvisioningTokenResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_6 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for kagent service"
                )
            _req = ParseDict(
                {k: v for k, v in {"token": token}.items() if v is not None},
                self._grpc_pb2_6.ListAgentsByProvisioningTokenRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_6.ListAgentsByProvisioningToken, _req)
            return rest_models.ListAgentsByProvisioningTokenResponse.model_validate(
                MessageToDict(_resp)
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestKagentModule6.ListAgentsByProvisioningToken(
                api_config_override=rest_transport.api_config, token=token
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def revoke_provisioning_token(
        self,
        *,
        token: str,
        data: rest_models.ProvisioningTokenServiceRevokeProvisioningTokenBody,
    ) -> rest_models.RevokeProvisioningTokenResponse:
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_stub_6 is None:
                raise NotImplementedError(
                    "gRPC proto dependencies not installed for kagent service"
                )
            _req_dict = data.model_dump(by_alias=True, exclude_none=True)
            _req_dict.update(
                {k: v for k, v in {"token": token}.items() if v is not None}
            )
            _req = ParseDict(
                _req_dict,
                self._grpc_pb2_6.RevokeProvisioningTokenRequest(),
                ignore_unknown_fields=True,
            )
            _resp = call_grpc(self._grpc_stub_6.RevokeProvisioningToken, _req)
            return rest_models.RevokeProvisioningTokenResponse.model_validate(
                MessageToDict(_resp)
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestKagentModule6.RevokeProvisioningToken(
                api_config_override=rest_transport.api_config, token=token, data=data
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )
