<!-- AUTO-GENERATED: scripts/generation/endpoint_docs.py, render_endpoint_docs() -->
<!-- Rebuilt on every `make generate`. Do not edit by hand. -->

# Saved Filter Service

## Overview

```mermaid
flowchart LR
    subgraph sdk["kentik_api"]
        KA["KentikAPI"]
        W["Saved FilterServiceWrapper\nclient.saved_filter"]
        REST["REST functions\ngen/saved_filter/services/"]
        RJ["request_json()\ncore/rest_runtime"]
        M["Models\ngen/saved_filter/models/"]
        E["Error classes\ngen/saved_filter/error/"]
    end
    API["Kentik API"]

    KA --> W
    W --> REST
    REST --> RJ
    REST --> M
    REST --> E
    RJ --> API
```

## Endpoints

### `POST` `/saved-filter/v202501alpha1`

Create Saved Filter

Creates and returns a saved filter object containing information about an individual saved filter.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.saved_filter
    participant API as Kentik REST API

    C->>W: create_saved_filter(data=SavedFilter(...))
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

**gRPC transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.saved_filter
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: create_saved_filter(data=SavedFilter(...))
    W->>R: build_grpc_request(CreateSavedFilterRequest, arguments)
    R->>API: SavedFilterService/CreateSavedFilter (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: MessageToDict(response)
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

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.saved_filter.create_saved_filter(
    data=SavedFilter(...),
)
```

---

### `GET` `/saved-filter/v202501alpha1/{id}`

Custom Saved Filter Info

Returns a saved filter object containing information about an individual saved filter.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.saved_filter
    participant API as Kentik REST API

    C->>W: get_saved_filter(id="id-example")
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

**gRPC transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.saved_filter
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: get_saved_filter(id="id-example")
    W->>R: build_grpc_request(GetSavedFilterRequest, arguments)
    R->>API: SavedFilterService/GetSavedFilter (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: MessageToDict(response)
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
response = client.saved_filter.get_saved_filter(
    id="id-example",
)
```

---

### `PUT` `/saved-filter/v202501alpha1/{id}`

Update Saved Filter

Updates and returns a saved filter object containing information about an individual saved filter.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.saved_filter
    participant API as Kentik REST API

    C->>W: update_saved_filter(id="id-example", data=SavedFilter(...))
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

**gRPC transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.saved_filter
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: update_saved_filter(id="id-example", data=SavedFilter(...))
    W->>R: build_grpc_request(UpdateSavedFilterRequest, arguments)
    R->>API: SavedFilterService/UpdateSavedFilter (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: MessageToDict(response)
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

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.saved_filter.update_saved_filter(
    id="id-example",
    data=SavedFilter(...),
)
```

---

### `DELETE` `/saved-filter/v202501alpha1/{id}`

Delete Saved Filter

Deletes a saved filter.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.saved_filter
    participant API as Kentik REST API

    C->>W: delete_saved_filter(id="id-example")
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

**gRPC transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.saved_filter
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: delete_saved_filter(id="id-example")
    W->>R: build_grpc_request(DeleteSavedFilterRequest, arguments)
    R->>API: SavedFilterService/DeleteSavedFilter (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: MessageToDict(response)
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
response = client.saved_filter.delete_saved_filter(
    id="id-example",
)
```

---

### `GET` `/saved-filters/v202501alpha1`

List Saved Filters

Returns all custom saved filters created by the user's company.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.saved_filter
    participant API as Kentik REST API

    C->>W: list_saved_filters()
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

**gRPC transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.saved_filter
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: list_saved_filters()
    W->>R: build_grpc_request(ListSavedFiltersRequest, arguments)
    R->>API: SavedFilterService/ListSavedFilters (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: MessageToDict(response)
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
response = client.saved_filter.list_saved_filters()
```

---

### `GET` `/saved-filters/v202501alpha1/all`

List All Saved Filters

Returns all saved filters, including system default filters.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.saved_filter
    participant API as Kentik REST API

    C->>W: list_saved_filters_all()
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

**gRPC transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.saved_filter
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: list_saved_filters_all()
    W->>R: build_grpc_request(ListSavedFiltersAllRequest, arguments)
    R->>API: SavedFilterService/ListSavedFiltersAll (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: MessageToDict(response)
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
response = client.saved_filter.list_saved_filters_all()
```

## Data Models

<details>
<summary>Model relationships (11 of 16 models)</summary>

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
    CreateSavedFilterResponse --> SavedFilter
    GetSavedFilterResponse --> SavedFilter
    ListSavedFiltersAllResponse --> SavedFilter
    ListSavedFiltersResponse --> SavedFilter
    SavedFilter --> FilterLevel
    SavedFilter --> SavedFilterFilters
    UpdateSavedFilterResponse --> SavedFilter
    rpcStatus --> protobufAny
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
