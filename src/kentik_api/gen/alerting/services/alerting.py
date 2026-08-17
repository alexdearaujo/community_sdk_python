from typing import List, Optional, Union, cast

import kentik_api.gen.alerting.services.AlertAutoAckService as RestAlertingModule1
import kentik_api.gen.alerting.services.AlertService as RestAlertingModule2
import kentik_api.gen.alerting.services.AlertSilenceNotificationsService as RestAlertingModule3
import kentik_api.gen.alerting.services.MitigationMethodsService as RestAlertingModule4
import kentik_api.gen.alerting.services.MitigationPlatformsService as RestAlertingModule5
import kentik_api.gen.alerting.services.MitigationsService as RestAlertingModule6
import kentik_api.gen.alerting.services.PolicyService as RestAlertingModule7
import kentik_api.gen.alerting.services.SuppressionService as RestAlertingModule8
from kentik_api.gen.alerting import models as rest_models
from kentik_api.transports.grpc_client import GrpcTransport
from kentik_api.transports.rest_client import RestTransport


class AlertingServiceWrapper:
    """Unified Service routing to either gRPC or REST."""

    def __init__(self, transport: Union[GrpcTransport, RestTransport]):
        self._transport = transport
        if isinstance(self._transport, GrpcTransport):
            pass  # TODO: Initialize gRPC stub here

    def create(
        self,
        *,
        data: rest_models.AlertAutoAckServiceCreateRequest,
    ) -> rest_models.AlertAutoAckServiceCreateResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for Create is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestAlertingModule1.Create(
                api_config_override=rest_transport.api_config, data=data
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def list(
        self,
        *,
        data: rest_models.AlertAutoAckServiceListRequest,
    ) -> rest_models.AlertAutoAckServiceListResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for List is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestAlertingModule1.List(
                api_config_override=rest_transport.api_config, data=data
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def get(self, *, autoAckid: str) -> rest_models.AlertAutoAckServiceGetResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for Get is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestAlertingModule1.Get(
                api_config_override=rest_transport.api_config, autoAckid=autoAckid
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def delete(
        self, *, autoAckid: str
    ) -> rest_models.AlertAutoAckServiceDeleteResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for Delete is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestAlertingModule1.Delete(
                api_config_override=rest_transport.api_config, autoAckid=autoAckid
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def replace(
        self,
        *,
        autoAckid: str,
        data: rest_models.AlertAutoAckServiceReplaceBody,
    ) -> rest_models.AlertAutoAckServiceReplaceResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for Replace is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestAlertingModule1.Replace(
                api_config_override=rest_transport.api_config,
                autoAckid=autoAckid,
                data=data,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def alert_list(
        self, *, data: rest_models.AlertServiceListRequest
    ) -> rest_models.AlertServiceListResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for List is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestAlertingModule2.List(
                api_config_override=rest_transport.api_config, data=data
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def clear(
        self, *, data: rest_models.AlertServiceClearRequest
    ) -> rest_models.AlertServiceClearResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for Clear is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestAlertingModule2.Clear(
                api_config_override=rest_transport.api_config, data=data
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def list_comments(
        self, *, alertId: str
    ) -> rest_models.AlertServiceListCommentsResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for ListComments is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestAlertingModule2.ListComments(
                api_config_override=rest_transport.api_config, alertId=alertId
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def add_comment(
        self,
        *,
        alertId: str,
        data: rest_models.AlertServiceAddCommentBody,
    ) -> rest_models.AlertServiceAddCommentResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for AddComment is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestAlertingModule2.AddComment(
                api_config_override=rest_transport.api_config,
                alertId=alertId,
                data=data,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def set_external_context(
        self,
        *,
        alertId: str,
        data: rest_models.AlertServiceSetExternalContextBody,
    ) -> rest_models.AlertServiceSetExternalContextResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for SetExternalContext is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestAlertingModule2.SetExternalContext(
                api_config_override=rest_transport.api_config,
                alertId=alertId,
                data=data,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def alert_get(self, *, id: str) -> rest_models.AlertServiceGetResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for Get is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestAlertingModule2.Get(
                api_config_override=rest_transport.api_config, id=id
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def ack(
        self,
        *,
        id: str,
        data: rest_models.AlertServiceAckBody,
    ) -> rest_models.AlertServiceAckResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for Ack is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestAlertingModule2.Ack(
                api_config_override=rest_transport.api_config, id=id, data=data
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def un_ack(
        self,
        *,
        id: str,
        data: rest_models.AlertServiceUnAckBody,
    ) -> rest_models.AlertServiceUnAckResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for UnAck is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestAlertingModule2.UnAck(
                api_config_override=rest_transport.api_config, id=id, data=data
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def alert_silence_notifications_create(
        self,
        *,
        data: rest_models.AlertSilenceNotificationsServiceCreateRequest,
    ) -> rest_models.AlertSilenceNotificationsServiceCreateResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for Create is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestAlertingModule3.Create(
                api_config_override=rest_transport.api_config, data=data
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def alert_silence_notifications_list(
        self,
        *,
        data: rest_models.AlertSilenceNotificationsServiceListRequest,
    ) -> rest_models.AlertSilenceNotificationsServiceListResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for List is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestAlertingModule3.List(
                api_config_override=rest_transport.api_config, data=data
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def alert_silence_notifications_get(
        self, *, id: str
    ) -> rest_models.AlertSilenceNotificationsServiceGetResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for Get is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestAlertingModule3.Get(
                api_config_override=rest_transport.api_config, id=id
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def alert_silence_notifications_delete(
        self, *, id: str
    ) -> rest_models.AlertSilenceNotificationsServiceDeleteResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for Delete is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestAlertingModule3.Delete(
                api_config_override=rest_transport.api_config, id=id
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def alert_silence_notifications_replace(
        self,
        *,
        id: str,
        data: rest_models.AlertSilenceNotificationsServiceReplaceBody,
    ) -> rest_models.AlertSilenceNotificationsServiceReplaceResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for Replace is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestAlertingModule3.Replace(
                api_config_override=rest_transport.api_config, id=id, data=data
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def mitigation_methods_list(
        self,
        *,
        paginationlimit: Optional[str] = None,
        paginationoffset: Optional[str] = None,
        paginationincludeTotalCount: Optional[bool] = None,
        filtersmethodIds: Optional[List[str]] = None,
        filtersplatformTypes: Optional[List[str]] = None,
        filterscreatedAtstart: Optional[str] = None,
        filterscreatedAtend: Optional[str] = None,
        filtersmodifiedAtstart: Optional[str] = None,
        filtersmodifiedAtend: Optional[str] = None,
    ) -> rest_models.MitigationMethodsServiceListResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for List is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestAlertingModule4.List(
                api_config_override=rest_transport.api_config,
                paginationlimit=paginationlimit,
                paginationoffset=paginationoffset,
                paginationincludeTotalCount=paginationincludeTotalCount,
                filtersmethodIds=filtersmethodIds,
                filtersplatformTypes=filtersplatformTypes,
                filterscreatedAtstart=filterscreatedAtstart,
                filterscreatedAtend=filterscreatedAtend,
                filtersmodifiedAtstart=filtersmodifiedAtstart,
                filtersmodifiedAtend=filtersmodifiedAtend,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def mitigation_methods_get(
        self, *, id: str
    ) -> rest_models.MitigationMethodsServiceGetResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for Get is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestAlertingModule4.Get(
                api_config_override=rest_transport.api_config, id=id
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def mitigation_platforms_list(
        self,
        *,
        paginationlimit: Optional[str] = None,
        paginationoffset: Optional[str] = None,
        paginationincludeTotalCount: Optional[bool] = None,
        filtersplatformIds: Optional[List[str]] = None,
        filtersplatformTypes: Optional[List[str]] = None,
        filterscreatedAtstart: Optional[str] = None,
        filterscreatedAtend: Optional[str] = None,
        filtersmodifiedAtstart: Optional[str] = None,
        filtersmodifiedAtend: Optional[str] = None,
    ) -> rest_models.MitigationPlatformsServiceListResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for List is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestAlertingModule5.List(
                api_config_override=rest_transport.api_config,
                paginationlimit=paginationlimit,
                paginationoffset=paginationoffset,
                paginationincludeTotalCount=paginationincludeTotalCount,
                filtersplatformIds=filtersplatformIds,
                filtersplatformTypes=filtersplatformTypes,
                filterscreatedAtstart=filterscreatedAtstart,
                filterscreatedAtend=filterscreatedAtend,
                filtersmodifiedAtstart=filtersmodifiedAtstart,
                filtersmodifiedAtend=filtersmodifiedAtend,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def mitigation_platforms_get(
        self, *, id: str
    ) -> rest_models.MitigationPlatformsServiceGetResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for Get is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestAlertingModule5.Get(
                api_config_override=rest_transport.api_config, id=id
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def mitigations_list(
        self,
        *,
        paginationlimit: Optional[str] = None,
        paginationoffset: Optional[str] = None,
        paginationincludeTotalCount: Optional[bool] = None,
        filterscreatedAtstart: Optional[str] = None,
        filterscreatedAtend: Optional[str] = None,
        filtersmitigationIds: Optional[List[str]] = None,
        filtersalarmIds: Optional[List[str]] = None,
        filtersstates: Optional[List[str]] = None,
        filtersplatformIds: Optional[List[str]] = None,
        filtersmethodIds: Optional[List[str]] = None,
        filtersipCidrs: Optional[List[str]] = None,
        filtersipCidrPattern: Optional[str] = None,
        filterstypes: Optional[List[str]] = None,
    ) -> rest_models.MitigationsServiceListResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for List is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestAlertingModule6.List(
                api_config_override=rest_transport.api_config,
                paginationlimit=paginationlimit,
                paginationoffset=paginationoffset,
                paginationincludeTotalCount=paginationincludeTotalCount,
                filterscreatedAtstart=filterscreatedAtstart,
                filterscreatedAtend=filterscreatedAtend,
                filtersmitigationIds=filtersmitigationIds,
                filtersalarmIds=filtersalarmIds,
                filtersstates=filtersstates,
                filtersplatformIds=filtersplatformIds,
                filtersmethodIds=filtersmethodIds,
                filtersipCidrs=filtersipCidrs,
                filtersipCidrPattern=filtersipCidrPattern,
                filterstypes=filterstypes,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def mitigations_create(
        self,
        *,
        data: rest_models.MitigationsServiceCreateRequest,
    ) -> rest_models.MitigationsServiceCreateResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for Create is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestAlertingModule6.Create(
                api_config_override=rest_transport.api_config, data=data
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def available_actions(
        self,
    ) -> rest_models.MitigationsServiceAvailableActionsResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for AvailableActions is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestAlertingModule6.AvailableActions(
                api_config_override=rest_transport.api_config
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def mitigations_get(
        self, *, action: str
    ) -> rest_models.MitigationsServiceGetResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for Get is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestAlertingModule6.Get(
                api_config_override=rest_transport.api_config, action=action
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def act(
        self,
        *,
        action: str,
        data: rest_models.MitigationsServiceActBody,
    ) -> rest_models.MitigationsServiceActResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for Act is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestAlertingModule6.Act(
                api_config_override=rest_transport.api_config, action=action, data=data
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def available_actions_for_mitigation(
        self, *, id: str
    ) -> rest_models.MitigationsServiceAvailableActionsForMitigationResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for AvailableActionsForMitigation is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestAlertingModule6.AvailableActionsForMitigation(
                api_config_override=rest_transport.api_config, id=id
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def policy_list(
        self, *, data: rest_models.PolicyServiceListRequest
    ) -> rest_models.PolicyServiceListResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for List is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestAlertingModule7.List(
                api_config_override=rest_transport.api_config, data=data
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def policy_get(
        self, *, policyType: str, id: str
    ) -> rest_models.PolicyServiceGetResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for Get is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestAlertingModule7.Get(
                api_config_override=rest_transport.api_config,
                policyType=policyType,
                id=id,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def disable(
        self,
        *,
        policyType: str,
        id: str,
        data: rest_models.PolicyServiceDisableBody,
    ) -> rest_models.PolicyServiceDisableResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for Disable is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestAlertingModule7.Disable(
                api_config_override=rest_transport.api_config,
                policyType=policyType,
                id=id,
                data=data,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def enable(
        self,
        *,
        policyType: str,
        id: str,
        data: rest_models.PolicyServiceEnableBody,
    ) -> rest_models.PolicyServiceEnableResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for Enable is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestAlertingModule7.Enable(
                api_config_override=rest_transport.api_config,
                policyType=policyType,
                id=id,
                data=data,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def suppression_create(
        self,
        *,
        data: rest_models.SuppressionServiceCreateRequest,
    ) -> rest_models.SuppressionServiceCreateResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for Create is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestAlertingModule8.Create(
                api_config_override=rest_transport.api_config, data=data
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def suppression_list(
        self,
        *,
        data: rest_models.SuppressionServiceListRequest,
    ) -> rest_models.SuppressionServiceListResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for List is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestAlertingModule8.List(
                api_config_override=rest_transport.api_config, data=data
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def suppression_get(self, *, id: str) -> rest_models.SuppressionServiceGetResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for Get is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestAlertingModule8.Get(
                api_config_override=rest_transport.api_config, id=id
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def suppression_delete(
        self, *, id: str
    ) -> rest_models.SuppressionServiceDeleteResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for Delete is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestAlertingModule8.Delete(
                api_config_override=rest_transport.api_config, id=id
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def suppression_replace(
        self,
        *,
        id: str,
        data: rest_models.SuppressionServiceReplaceBody,
    ) -> rest_models.SuppressionServiceReplaceResponse:
        if isinstance(self._transport, GrpcTransport):
            raise NotImplementedError(
                "gRPC translation for Replace is not yet implemented."
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestAlertingModule8.Replace(
                api_config_override=rest_transport.api_config, id=id, data=data
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )
