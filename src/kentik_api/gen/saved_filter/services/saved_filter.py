from typing import Optional, Union, cast

from google.protobuf.json_format import MessageToDict

import kentik_api.gen.saved_filter.services.SavedFilterService as RestSavedFilterModule1
from kentik_api.core.api_config import APIConfig
from kentik_api.core.grpc_runtime import build_grpc_request, call_grpc
from kentik_api.core.rate_limit import attach_rate_limit
from kentik_api.gen.saved_filter import models as rest_models
from kentik_api.transports.grpc_client import GrpcTransport
from kentik_api.transports.rest_client import RestTransport


class SavedFilterServiceWrapper:
    """AUTO-GENERATED: scripts/generation/wrapper_generation.py, _generate_service_wrappers().
    Rebuilt on every `make generate`. Do not edit by hand.
    Unified Service routing to either gRPC or REST.
    """

    def __init__(self, transport: Union[GrpcTransport, RestTransport]):
        self._transport = transport
        if isinstance(self._transport, GrpcTransport):
            try:
                __import__("kentik_api.gen.pb_companions")
                import kentik_api.gen.saved_filter.pb.saved_filter_pb2 as _pb2_1_mod
                import kentik_api.gen.saved_filter.pb.saved_filter_pb2_grpc as _pb2_grpc_1_mod

                self._grpc_pb2_1 = _pb2_1_mod
                self._grpc_stub_1 = _pb2_grpc_1_mod.SavedFilterServiceStub(
                    self._transport.channel
                )
            except (ImportError, TypeError) as exc:
                self._grpc_pb2_1 = None
                self._grpc_stub_1 = None
                self._grpc_import_error_1 = exc

    def create_saved_filter(
        self,
        *,
        api_config_override: Optional[APIConfig] = None,
        data: rest_models.SavedFilter,
    ) -> rest_models.CreateSavedFilterResponse:
        """
        Create Saved Filter

        Creates and returns a saved filter object containing information about an individual saved filter.
        """
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_1 is None or self._grpc_stub_1 is None:
                raise NotImplementedError(
                    f"gRPC proto modules for saved_filter service failed to import: {self._grpc_import_error_1!r}"
                ) from self._grpc_import_error_1
            _req = build_grpc_request(
                self._grpc_pb2_1.CreateSavedFilterRequest,
                {"filter": data.model_dump(by_alias=True, exclude_unset=True)},
                {},
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_1.CreateSavedFilter,
                _req,
                api_config=api_config_override,
                error_cls=RestSavedFilterModule1.CreateSavedFilterError,
            )
            return attach_rate_limit(
                rest_models.CreateSavedFilterResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestSavedFilterModule1.CreateSavedFilter(
                api_config_override=api_config_override or rest_transport.api_config,
                data=data,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def get_saved_filter(
        self, *, api_config_override: Optional[APIConfig] = None, id: str
    ) -> rest_models.GetSavedFilterResponse:
        """
        Custom Saved Filter Info

        Returns a saved filter object containing information about an individual saved filter.
        """
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_1 is None or self._grpc_stub_1 is None:
                raise NotImplementedError(
                    f"gRPC proto modules for saved_filter service failed to import: {self._grpc_import_error_1!r}"
                ) from self._grpc_import_error_1
            _req = build_grpc_request(
                self._grpc_pb2_1.GetSavedFilterRequest, None, {"id": id}
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_1.GetSavedFilter,
                _req,
                api_config=api_config_override,
                error_cls=RestSavedFilterModule1.GetSavedFilterError,
            )
            return attach_rate_limit(
                rest_models.GetSavedFilterResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestSavedFilterModule1.GetSavedFilter(
                api_config_override=api_config_override or rest_transport.api_config,
                id=id,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def update_saved_filter(
        self,
        *,
        api_config_override: Optional[APIConfig] = None,
        id: str,
        data: rest_models.SavedFilter,
    ) -> rest_models.UpdateSavedFilterResponse:
        """
        Update Saved Filter

        Updates and returns a saved filter object containing information about an individual saved filter.
        """
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_1 is None or self._grpc_stub_1 is None:
                raise NotImplementedError(
                    f"gRPC proto modules for saved_filter service failed to import: {self._grpc_import_error_1!r}"
                ) from self._grpc_import_error_1
            _req = build_grpc_request(
                self._grpc_pb2_1.UpdateSavedFilterRequest,
                {"filter": data.model_dump(by_alias=True, exclude_unset=True)},
                {"id": id},
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_1.UpdateSavedFilter,
                _req,
                api_config=api_config_override,
                error_cls=RestSavedFilterModule1.UpdateSavedFilterError,
            )
            return attach_rate_limit(
                rest_models.UpdateSavedFilterResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestSavedFilterModule1.UpdateSavedFilter(
                api_config_override=api_config_override or rest_transport.api_config,
                id=id,
                data=data,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def delete_saved_filter(
        self, *, api_config_override: Optional[APIConfig] = None, id: str
    ) -> rest_models.DeleteSavedFilterResponse:
        """
        Delete Saved Filter

        Deletes a saved filter.
        """
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_1 is None or self._grpc_stub_1 is None:
                raise NotImplementedError(
                    f"gRPC proto modules for saved_filter service failed to import: {self._grpc_import_error_1!r}"
                ) from self._grpc_import_error_1
            _req = build_grpc_request(
                self._grpc_pb2_1.DeleteSavedFilterRequest, None, {"id": id}
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_1.DeleteSavedFilter,
                _req,
                api_config=api_config_override,
                error_cls=RestSavedFilterModule1.DeleteSavedFilterError,
            )
            return attach_rate_limit(
                rest_models.DeleteSavedFilterResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestSavedFilterModule1.DeleteSavedFilter(
                api_config_override=api_config_override or rest_transport.api_config,
                id=id,
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def list_saved_filters(
        self, *, api_config_override: Optional[APIConfig] = None
    ) -> rest_models.ListSavedFiltersResponse:
        """
        List Saved Filters

        Returns all custom saved filters created by the user's company.
        """
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_1 is None or self._grpc_stub_1 is None:
                raise NotImplementedError(
                    f"gRPC proto modules for saved_filter service failed to import: {self._grpc_import_error_1!r}"
                ) from self._grpc_import_error_1
            _req = build_grpc_request(
                self._grpc_pb2_1.ListSavedFiltersRequest, None, {}
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_1.ListSavedFilters,
                _req,
                api_config=api_config_override,
                error_cls=RestSavedFilterModule1.ListSavedFiltersError,
            )
            return attach_rate_limit(
                rest_models.ListSavedFiltersResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestSavedFilterModule1.ListSavedFilters(
                api_config_override=api_config_override or rest_transport.api_config
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )

    def list_saved_filters_all(
        self, *, api_config_override: Optional[APIConfig] = None
    ) -> rest_models.ListSavedFiltersAllResponse:
        """
        List All Saved Filters

        Returns all saved filters, including system default filters.
        """
        if isinstance(self._transport, GrpcTransport):
            if self._grpc_pb2_1 is None or self._grpc_stub_1 is None:
                raise NotImplementedError(
                    f"gRPC proto modules for saved_filter service failed to import: {self._grpc_import_error_1!r}"
                ) from self._grpc_import_error_1
            _req = build_grpc_request(
                self._grpc_pb2_1.ListSavedFiltersAllRequest, None, {}
            )
            _resp, _rate_limit = call_grpc(
                self._grpc_stub_1.ListSavedFiltersAll,
                _req,
                api_config=api_config_override,
                error_cls=RestSavedFilterModule1.ListSavedFiltersAllError,
            )
            return attach_rate_limit(
                rest_models.ListSavedFiltersAllResponse.model_validate(
                    MessageToDict(_resp, always_print_fields_with_no_presence=True)
                ),
                _rate_limit,
            )
        elif isinstance(self._transport, RestTransport):
            rest_transport = cast(RestTransport, self._transport)
            return RestSavedFilterModule1.ListSavedFiltersAll(
                api_config_override=api_config_override or rest_transport.api_config
            )
        else:
            raise TypeError(
                f"Unsupported transport type: {self._transport.__class__.__name__}"
            )
