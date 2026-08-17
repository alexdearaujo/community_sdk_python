from typing import Any, Dict, Optional

from kentik_api.core.api_config import APIConfig
from kentik_api.core.rest_runtime import request_json

from ..error import DisableError, EnableError, GetError, ListError
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
    v202506MitigationTarget,
)


def List(
    api_config_override: Optional[APIConfig] = None, *, data: PolicyServiceListRequest
) -> PolicyServiceListResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="post",
        path="/v202505/policies/list",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(),
        header_params=header_params,
        expected_status=200,
        operation_name="List",
        error_cls=ListError,
    )

    return (
        PolicyServiceListResponse(**body)
        if body is not None
        else PolicyServiceListResponse.model_construct()
    )


def Get(
    api_config_override: Optional[APIConfig] = None, *, policyType: str, id: str
) -> PolicyServiceGetResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="get",
        path=f"/v202505/policies/{policyType}/{id}",
        api_config_override=api_config_override,
        query_params=query_params,
        header_params=header_params,
        expected_status=200,
        operation_name="Get",
        error_cls=GetError,
    )

    return (
        PolicyServiceGetResponse(**body)
        if body is not None
        else PolicyServiceGetResponse.model_construct()
    )


def Disable(
    api_config_override: Optional[APIConfig] = None,
    *,
    policyType: str,
    id: str,
    data: PolicyServiceDisableBody,
) -> PolicyServiceDisableResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="post",
        path=f"/v202505/policies/{policyType}/{id}/disable",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(),
        header_params=header_params,
        expected_status=200,
        operation_name="Disable",
        error_cls=DisableError,
    )

    return (
        PolicyServiceDisableResponse(**body)
        if body is not None
        else PolicyServiceDisableResponse.model_construct()
    )


def Enable(
    api_config_override: Optional[APIConfig] = None,
    *,
    policyType: str,
    id: str,
    data: PolicyServiceEnableBody,
) -> PolicyServiceEnableResponse:
    query_params: Dict[str, Any] = {}

    header_params: Dict[str, Any] = {}

    body = request_json(
        method="post",
        path=f"/v202505/policies/{policyType}/{id}/enable",
        api_config_override=api_config_override,
        query_params=query_params,
        json_body=data.model_dump(),
        header_params=header_params,
        expected_status=200,
        operation_name="Enable",
        error_cls=EnableError,
    )

    return (
        PolicyServiceEnableResponse(**body)
        if body is not None
        else PolicyServiceEnableResponse.model_construct()
    )
