# AUTO-GENERATED: scripts/openapi_templates/service.jinja2 via openapi-python-generator
# Rebuilt on every `make generate`. Do not edit by hand.

from typing import Any, Dict, Optional

from kentik_api.core.api_config import APIConfig
from kentik_api.core.rest_runtime import (
    parse_response_model,
    path_segment,
    request_json,
)

from ..error import (
    AckError,
    AddCommentError,
    ClearError,
    GetError,
    ListCommentsError,
    ListError,
    SetExternalContextError,
    UnAckError,
)
from ..models import (  # noqa: F401
    AggregationType,
    Alert,
    AlertAcknowledgement,
    AlertAutoAck,
    AlertAutoAckFilters,
    AlertAutoAckServiceCreateRequest,
    AlertAutoAckServiceCreateResponse,
    AlertAutoAckServiceDeleteResponse,
    AlertAutoAckServiceGetResponse,
    AlertAutoAckServiceListRequest,
    AlertAutoAckServiceListResponse,
    AlertAutoAckServiceReplaceBody,
    AlertAutoAckServiceReplaceResponse,
    AlertFilters,
    AlertPhase,
    AlertServiceAckBody,
    AlertServiceAckResponse,
    AlertServiceAddCommentBody,
    AlertServiceAddCommentResponse,
    AlertServiceClearRequest,
    AlertServiceClearResponse,
    AlertServiceGetResponse,
    AlertServiceListCommentsResponse,
    AlertServiceListRequest,
    AlertServiceListResponse,
    AlertServiceSetExternalContextBody,
    AlertServiceSetExternalContextResponse,
    AlertServiceUnAckBody,
    AlertServiceUnAckResponse,
    AlertSilenceNotificationFilters,
    AlertSilenceNotificationsDefinition,
    AlertSilenceNotificationsServiceCreateRequest,
    AlertSilenceNotificationsServiceCreateResponse,
    AlertSilenceNotificationsServiceDeleteResponse,
    AlertSilenceNotificationsServiceGetResponse,
    AlertSilenceNotificationsServiceListRequest,
    AlertSilenceNotificationsServiceListResponse,
    AlertSilenceNotificationsServiceReplaceBody,
    AlertSilenceNotificationsServiceReplaceResponse,
    AlertState,
    BaselineConditionDeltaType,
    BaselineConfigCompareMode,
    Comment,
    ConditionsBaselineCondition,
    ConditionsForecastCondition,
    ConditionsInterfaceCapacityCondition,
    ConditionsRatioCondition,
    ConditionsStaticCondition,
    ConditionsTopKeysCondition,
    EventPolicyLevelSettings,
    EventPolicySettings,
    EventPolicySettingsEventType,
    ExternalContext,
    FieldBy,
    FlowContext,
    FlowContextActivationStatus,
    FlowContextAlertKeyDetails,
    FlowContextDeviceDetails,
    FlowContextInterfaceDetails,
    FlowContextMetricValue,
    FlowContextSiteDetails,
    FlowPolicyLevelSettings,
    FlowPolicyLevelSettingsActivationSettings,
    FlowPolicyLevelSettingsConditions,
    FlowPolicyLevelSettingsConditionsOperator,
    FlowPolicyLevelSettingsMitigationAssociation,
    FlowPolicySettings,
    FlowPolicySettingsBaselineConfig,
    FlowPolicySettingsDatasetConfig,
    FlowPolicySettingsEvaluationConfig,
    JiraCloudContext,
    Mitigation,
    MitigationActionDetail,
    MitigationEvent,
    MitigationFilters,
    MitigationMethod,
    MitigationMethodsFilters,
    MitigationMethodsServiceGetResponse,
    MitigationMethodsServiceListResponse,
    MitigationPlatform,
    MitigationPlatformsFilters,
    MitigationPlatformsServiceGetResponse,
    MitigationPlatformsServiceListResponse,
    MitigationPlatformType,
    MitigationsActResult,
    MitigationsServiceActBody,
    MitigationsServiceActResponse,
    MitigationsServiceAvailableActionsForMitigationResponse,
    MitigationsServiceAvailableActionsResponse,
    MitigationsServiceAvailableActionsResponseMitigationAvailableTransitions,
    MitigationsServiceCreateRequest,
    MitigationsServiceCreateResponse,
    MitigationsServiceGetResponse,
    MitigationsServiceListResponse,
    MitigationState,
    MitigationStateEntry,
    MitigationType,
    MitigationUserAction,
    NmsActivateOrClearConditions,
    NmsCondition,
    NmsConditionConnector,
    NmsConditionGroup,
    NmsConditionOperator,
    NmsContext,
    NmsContextActivationInfo,
    NmsContextAlarmMetricMap,
    NmsContextAlarmTarget,
    NmsContextDatasetInfo,
    NmsPolicyLevelSettings,
    NmsPolicyLevelSettingsClearType,
    NmsPolicySettings,
    NmsPolicySettingsDatasetConfig,
    NmsPolicySettingsEvaluationConfig,
    NmsStateChangeCondition,
    NmsStateSet,
    NmsThresholdCondition,
    NotificationChannelAssociation,
    Policy,
    PolicyDataSources,
    PolicyDataSourcesDeviceTag,
    PolicyDimensionFilters,
    PolicyDimensionFiltersConjunction,
    PolicyDimensionFiltersEntry,
    PolicyDimensionFiltersEntryStringArray,
    PolicyFilters,
    PolicyFiltersFieldFilter,
    PolicyFiltersFilterConnector,
    PolicyFiltersOperator,
    PolicyFiltersSavedFilter,
    PolicyListFilters,
    PolicyPolicyErrorInfo,
    PolicyPolicyLevel,
    PolicyServiceDisableBody,
    PolicyServiceDisableResponse,
    PolicyServiceEnableBody,
    PolicyServiceEnableResponse,
    PolicyServiceGetResponse,
    PolicyServiceListRequest,
    PolicyServiceListResponse,
    PolicyType,
    RatioConditionDirection,
    ServiceNowContext,
    SortingConfigField,
    SortingConfigOrder,
    Source,
    Suppression,
    SuppressionFilters,
    SuppressionServiceCreateRequest,
    SuppressionServiceCreateResponse,
    SuppressionServiceDeleteResponse,
    SuppressionServiceGetResponse,
    SuppressionServiceListRequest,
    SuppressionServiceListResponse,
    SuppressionServiceReplaceBody,
    SuppressionServiceReplaceResponse,
    TopKeysConditionTopKeysEvent,
    protobufAny,
    rpcStatus,
    typesv202506PaginationConfig,
    typesv202506PaginationInfo,
    typesv202506SortingConfig,
    v202303AttributeFilter,
    v202303AttributeFilterStringArray,
    v202303KeyValue,
    v202303KeyValueFilter,
    v202303MultiAttributeFilter,
    v202303Severity,
    v202303SimpleAttributeFilter,
    v202303SimpleAttributeFilterStringArray,
    v202303TimeRange,
    v202501BitwiseOp,
    v202501FlowspecMatch,
    v202501Fragment,
    v202501FragmentFormula,
    v202501FragmentPredicate,
    v202501FragmentPredicateGroup,
    v202501NumericFormula,
    v202501NumericOp,
    v202501NumericPredicate,
    v202501NumericPredicateGroup,
    v202501TCPFlag,
    v202501TCPFlagsFormula,
    v202501TCPFlagsPredicate,
    v202501TCPFlagsPredicateGroup,
    v202505AlertAcknowledgement,
    v202506MitigationTarget,
)


def List(
    api_config_override: Optional[APIConfig] = None, *, data: AlertServiceListRequest
) -> AlertServiceListResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="post",
        path="/v202505/alerts",
        path_template="/v202505/alerts",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(by_alias=True, exclude_unset=True),
        header_params=header_params,
        expected_status=200,
        operation_name="List",
        error_cls=ListError,
    )

    return parse_response_model(
        AlertServiceListResponse,
        body,
        operation_name="List",
        method="post",
        path="/v202505/alerts",
    )


def Clear(
    api_config_override: Optional[APIConfig] = None, *, data: AlertServiceClearRequest
) -> AlertServiceClearResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="post",
        path="/v202505/alerts/clear",
        path_template="/v202505/alerts/clear",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(by_alias=True, exclude_unset=True),
        header_params=header_params,
        expected_status=200,
        operation_name="Clear",
        error_cls=ClearError,
    )

    return parse_response_model(
        AlertServiceClearResponse,
        body,
        operation_name="Clear",
        method="post",
        path="/v202505/alerts/clear",
    )


def ListComments(
    api_config_override: Optional[APIConfig] = None, *, alertId: str
) -> AlertServiceListCommentsResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path=f"/v202505/alerts/{path_segment(alertId)}/comments",
        path_template="/v202505/alerts/{alertId}/comments",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="ListComments",
        error_cls=ListCommentsError,
    )

    return parse_response_model(
        AlertServiceListCommentsResponse,
        body,
        operation_name="ListComments",
        method="get",
        path="/v202505/alerts/{alertId}/comments",
    )


def AddComment(
    api_config_override: Optional[APIConfig] = None,
    *,
    alertId: str,
    data: AlertServiceAddCommentBody,
) -> AlertServiceAddCommentResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="post",
        path=f"/v202505/alerts/{path_segment(alertId)}/comments",
        path_template="/v202505/alerts/{alertId}/comments",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(by_alias=True, exclude_unset=True),
        header_params=header_params,
        expected_status=200,
        operation_name="AddComment",
        error_cls=AddCommentError,
    )

    return parse_response_model(
        AlertServiceAddCommentResponse,
        body,
        operation_name="AddComment",
        method="post",
        path="/v202505/alerts/{alertId}/comments",
    )


def SetExternalContext(
    api_config_override: Optional[APIConfig] = None,
    *,
    alertId: str,
    data: AlertServiceSetExternalContextBody,
) -> AlertServiceSetExternalContextResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="put",
        path=f"/v202505/alerts/{path_segment(alertId)}/external-context",
        path_template="/v202505/alerts/{alertId}/external-context",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(by_alias=True, exclude_unset=True),
        header_params=header_params,
        expected_status=200,
        operation_name="SetExternalContext",
        error_cls=SetExternalContextError,
    )

    return parse_response_model(
        AlertServiceSetExternalContextResponse,
        body,
        operation_name="SetExternalContext",
        method="put",
        path="/v202505/alerts/{alertId}/external-context",
    )


def Get(
    api_config_override: Optional[APIConfig] = None, *, id: str
) -> AlertServiceGetResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path=f"/v202505/alerts/{path_segment(id)}",
        path_template="/v202505/alerts/{id}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="Get",
        error_cls=GetError,
    )

    return parse_response_model(
        AlertServiceGetResponse,
        body,
        operation_name="Get",
        method="get",
        path="/v202505/alerts/{id}",
    )


def Ack(
    api_config_override: Optional[APIConfig] = None,
    *,
    id: str,
    data: AlertServiceAckBody,
) -> AlertServiceAckResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="post",
        path=f"/v202505/alerts/{path_segment(id)}/ack",
        path_template="/v202505/alerts/{id}/ack",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(by_alias=True, exclude_unset=True),
        header_params=header_params,
        expected_status=200,
        operation_name="Ack",
        error_cls=AckError,
    )

    return parse_response_model(
        AlertServiceAckResponse,
        body,
        operation_name="Ack",
        method="post",
        path="/v202505/alerts/{id}/ack",
    )


def UnAck(
    api_config_override: Optional[APIConfig] = None,
    *,
    id: str,
    data: AlertServiceUnAckBody,
) -> AlertServiceUnAckResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="post",
        path=f"/v202505/alerts/{path_segment(id)}/unack",
        path_template="/v202505/alerts/{id}/unack",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(by_alias=True, exclude_unset=True),
        header_params=header_params,
        expected_status=200,
        operation_name="UnAck",
        error_cls=UnAckError,
    )

    return parse_response_model(
        AlertServiceUnAckResponse,
        body,
        operation_name="UnAck",
        method="post",
        path="/v202505/alerts/{id}/unack",
    )
