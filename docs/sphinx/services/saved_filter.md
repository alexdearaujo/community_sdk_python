<!-- AUTO-GENERATED: scripts/generation/endpoint_docs.py, render_endpoint_docs() -->
<!-- Rebuilt on every `uv run poe generate`. Do not edit by hand. -->

# Saved Filter Service

## Overview

```mermaid
%%{init: {"fontFamily": "ui-monospace, SFMono-Regular, Menlo, monospace", "flowchart": {"curve": "step", "nodeSpacing": 30, "rankSpacing": 70, "wrappingWidth": 400}}}%%
flowchart LR
    code("Your code"):::greenSrc
    subgraph sdk["kentik_api"]
        wrap("SavedFilterServiceWrapper<br/>client.saved_filter<br/>6 operations"):::orange
        rest("REST functions<br/>gen/saved_filter/services/"):::blue
        rj("request_json()<br/>core/rest_runtime.py"):::blue
        cg("call_grpc()<br/>core/grpc_runtime.py"):::violet
    end
    grpcapi("Kentik gRPC API<br/>HTTP/2 + protobuf"):::violetSrc
    restapi("Kentik REST API<br/>HTTPS + JSON"):::blueSrc

    code -->|"method call"| wrap
    wrap -->|"Pydantic model from<br/>gen/saved_filter/models/"| code
    wrap -->|"arguments"| rest
    rest -->|"Pydantic model"| wrap
    rest -->|"method, path, body"| rj
    rj -->|"JSON dict"| rest
    rj -->|"HTTPS request"| restapi
    restapi -->|"JSON response"| rj
    wrap -->|"proto request"| cg
    cg -->|"proto response"| wrap
    cg -->|"gRPC call"| grpcapi
    grpcapi -->|"proto response"| cg

    classDef greenSrc fill:#b2f2bb,stroke:#2f9e44,color:#2b8a3e
    classDef orange fill:#fff4e6,stroke:#e8590c,color:#d9480f
    classDef blue fill:#e7f5ff,stroke:#1971c2,color:#1864ab
    classDef blueSrc fill:#a5d8ff,stroke:#1971c2,color:#1864ab
    classDef violet fill:#f3f0ff,stroke:#7048e8,color:#5f3dc4
    classDef violetSrc fill:#d0bfff,stroke:#7048e8,color:#5f3dc4
    classDef greenSrc,orange,blue,blueSrc,violet,violetSrc stroke-width:2px,rx:10px
    style sdk fill:none,stroke:#868e96,stroke-width:2px
    linkStyle default stroke-width:2px,stroke-linecap:round,stroke-linejoin:round
```

On an error status or a failed call, the SDK raises an error class from `gen/saved_filter/error/`, or a shared type from `kentik_api.errors`.

## Endpoints

### `POST` `/saved-filter/v202501alpha1`

Create Saved Filter

Creates and returns a saved filter object containing information about an individual saved filter.

#### REST call flow

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.saved_filter
    participant API as Kentik REST API

    C->>W: create(data=SavedFilter(...))
    W->>API: POST /saved-filter/v202501alpha1
    alt success
        API-->>W: CreateSavedFilterResponse (JSON)
        W-->>C: CreateSavedFilterResponse
    else error status
        API-->>W: error body
        W-->>C: raise AuthenticationError (401) or HTTPException
    else no response
        W-->>C: raise TransportError
    end
```

#### gRPC call flow

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.saved_filter
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: create(data=SavedFilter(...))
    W->>R: build_grpc_request(CreateSavedFilterRequest, arguments)
    R->>API: SavedFilterService/CreateSavedFilter (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: parse_grpc_response(response)
        W-->>C: CreateSavedFilterResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `data` | body | `SavedFilter` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `CreateSavedFilterResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI
from kentik_api.gen.saved_filter.models import SavedFilter

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.saved_filter.create(
    data=SavedFilter(...),
)
```

---

### `GET` `/saved-filter/v202501alpha1/{id}`

Custom Saved Filter Info

Returns a saved filter object containing information about an individual saved filter.

#### REST call flow

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.saved_filter
    participant API as Kentik REST API

    C->>W: get(id="id-example")
    W->>API: GET /saved-filter/v202501alpha1/{id}
    alt success
        API-->>W: GetSavedFilterResponse (JSON)
        W-->>C: GetSavedFilterResponse
    else error status
        API-->>W: error body
        W-->>C: raise AuthenticationError (401) or HTTPException
    else no response
        W-->>C: raise TransportError
    end
```

#### gRPC call flow

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.saved_filter
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: get(id="id-example")
    W->>R: build_grpc_request(GetSavedFilterRequest, arguments)
    R->>API: SavedFilterService/GetSavedFilter (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: parse_grpc_response(response)
        W-->>C: GetSavedFilterResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `id` | path | `string` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `GetSavedFilterResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.saved_filter.get(
    id="id-example",
)
```

---

### `PUT` `/saved-filter/v202501alpha1/{id}`

Update Saved Filter

Updates and returns a saved filter object containing information about an individual saved filter.

#### REST call flow

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.saved_filter
    participant API as Kentik REST API

    C->>W: update(id="id-example", data=SavedFilter(...))
    W->>API: PUT /saved-filter/v202501alpha1/{id}
    alt success
        API-->>W: UpdateSavedFilterResponse (JSON)
        W-->>C: UpdateSavedFilterResponse
    else error status
        API-->>W: error body
        W-->>C: raise AuthenticationError (401) or HTTPException
    else no response
        W-->>C: raise TransportError
    end
```

#### gRPC call flow

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.saved_filter
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: update(id="id-example", data=SavedFilter(...))
    W->>R: build_grpc_request(UpdateSavedFilterRequest, arguments)
    R->>API: SavedFilterService/UpdateSavedFilter (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: parse_grpc_response(response)
        W-->>C: UpdateSavedFilterResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `id` | path | `string` | Yes |
| `data` | body | `SavedFilter` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `UpdateSavedFilterResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI
from kentik_api.gen.saved_filter.models import SavedFilter

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.saved_filter.update(
    id="id-example",
    data=SavedFilter(...),
)
```

---

### `DELETE` `/saved-filter/v202501alpha1/{id}`

Delete Saved Filter

Deletes a saved filter.

#### REST call flow

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.saved_filter
    participant API as Kentik REST API

    C->>W: delete(id="id-example")
    W->>API: DELETE /saved-filter/v202501alpha1/{id}
    alt success
        API-->>W: DeleteSavedFilterResponse (JSON)
        W-->>C: DeleteSavedFilterResponse
    else error status
        API-->>W: error body
        W-->>C: raise AuthenticationError (401) or HTTPException
    else no response
        W-->>C: raise TransportError
    end
```

#### gRPC call flow

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.saved_filter
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: delete(id="id-example")
    W->>R: build_grpc_request(DeleteSavedFilterRequest, arguments)
    R->>API: SavedFilterService/DeleteSavedFilter (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: parse_grpc_response(response)
        W-->>C: DeleteSavedFilterResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `id` | path | `string` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `DeleteSavedFilterResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.saved_filter.delete(
    id="id-example",
)
```

---

### `GET` `/saved-filters/v202501alpha1`

List Saved Filters

Returns all custom saved filters created by the user's company.

#### REST call flow

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.saved_filter
    participant API as Kentik REST API

    C->>W: list()
    W->>API: GET /saved-filters/v202501alpha1
    alt success
        API-->>W: ListSavedFiltersResponse (JSON)
        W-->>C: ListSavedFiltersResponse
    else error status
        API-->>W: error body
        W-->>C: raise AuthenticationError (401) or HTTPException
    else no response
        W-->>C: raise TransportError
    end
```

#### gRPC call flow

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.saved_filter
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: list()
    W->>R: build_grpc_request(ListSavedFiltersRequest, arguments)
    R->>API: SavedFilterService/ListSavedFilters (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: parse_grpc_response(response)
        W-->>C: ListSavedFiltersResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `ListSavedFiltersResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.saved_filter.list()
```

---

### `GET` `/saved-filters/v202501alpha1/all`

List All Saved Filters

Returns all saved filters, including system default filters.

#### REST call flow

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.saved_filter
    participant API as Kentik REST API

    C->>W: list_all()
    W->>API: GET /saved-filters/v202501alpha1/all
    alt success
        API-->>W: ListSavedFiltersAllResponse (JSON)
        W-->>C: ListSavedFiltersAllResponse
    else error status
        API-->>W: error body
        W-->>C: raise AuthenticationError (401) or HTTPException
    else no response
        W-->>C: raise TransportError
    end
```

#### gRPC call flow

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.saved_filter
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: list_all()
    W->>R: build_grpc_request(ListSavedFiltersAllRequest, arguments)
    R->>API: SavedFilterService/ListSavedFiltersAll (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: parse_grpc_response(response)
        W-->>C: ListSavedFiltersAllResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `ListSavedFiltersAllResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.saved_filter.list_all()
```

## Data Models

<details>
<summary>Model relationships (11 of 16 models)</summary>

Each arrow points from a model to a model that one of its fields holds. The label names the field.

```mermaid
classDiagram
    class CreateSavedFilterResponse
    class DeleteSavedFilterResponse
    class FilterLevel
    class GetSavedFilterResponse
    class ListSavedFiltersAllResponse
    class ListSavedFiltersResponse
    class SavedFilter
    class SavedFilterFilters
    class UpdateSavedFilterResponse
    class protobufAny
    class rpcStatus
    CreateSavedFilterResponse --> SavedFilter : filter
    GetSavedFilterResponse --> SavedFilter : filter
    ListSavedFiltersAllResponse --> SavedFilter : filters
    ListSavedFiltersResponse --> SavedFilter : filters
    SavedFilter --> FilterLevel : filterLevel
    SavedFilter --> SavedFilterFilters : filters
    UpdateSavedFilterResponse --> SavedFilter : filter
    rpcStatus --> protobufAny : details
```

</details>

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.saved_filter.models.CreateSavedFilterResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.saved_filter.models.DeleteSavedFilterResponse
```

```{eval-rst}
.. autoclass:: kentik_api.gen.saved_filter.models.FilterField
   :members:
```

```{eval-rst}
.. autoclass:: kentik_api.gen.saved_filter.models.FilterLevel
   :members:
```

```{eval-rst}
.. autoclass:: kentik_api.gen.saved_filter.models.FilterOperator
   :members:
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.saved_filter.models.GetSavedFilterResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.saved_filter.models.ListSavedFiltersAllResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.saved_filter.models.ListSavedFiltersResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.saved_filter.models.SavedFilter
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.saved_filter.models.SavedFilterFilter
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.saved_filter.models.SavedFilterFilterGroup
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.saved_filter.models.SavedFilterFilterId
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.saved_filter.models.SavedFilterFilters
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.saved_filter.models.UpdateSavedFilterResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.saved_filter.models.protobufAny
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.saved_filter.models.rpcStatus
```
