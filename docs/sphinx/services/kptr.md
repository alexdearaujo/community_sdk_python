<!-- AUTO-GENERATED: scripts/generation/endpoint_docs.py, render_endpoint_docs() -->
<!-- Rebuilt on every `make generate`. Do not edit by hand. -->

# Kptr Service

## Endpoints

This service's schema defines shared types only -- no REST endpoints.

## Data Models

<details>
<summary>Model relationships (7 of 7 models)</summary>

```mermaid
classDiagram
    class GetNetworkRangeAssignmentsResponse
    class ListResolvedAddressesResponse
    class PtrResult
    class ResolveAddressesResponse
    class UpdateAddressNamesResponse
    class protobufAny
    class rpcStatus
    ListResolvedAddressesResponse --> PtrResult
    ResolveAddressesResponse --> PtrResult
    rpcStatus --> protobufAny
```

</details>

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.kptr.models.GetNetworkRangeAssignmentsResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.kptr.models.ListResolvedAddressesResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.kptr.models.PtrResult
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.kptr.models.ResolveAddressesResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.kptr.models.UpdateAddressNamesResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.kptr.models.protobufAny
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.kptr.models.rpcStatus
```
