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

    C->>W: create_saved_filter()
    W->>API: POST /saved-filter/v202501alpha1
    alt success
        API-->>W: CreateSavedFilterResponse (JSON)
        W-->>C: CreateSavedFilterResponse
    else error
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

**gRPC transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.saved_filter
    participant B as proto bridge
    participant API as Kentik gRPC API

    C->>W: create_saved_filter()
    W->>B: ParseDict(params, CreateSavedFilterRequest)
    B->>API: create_saved_filter (gRPC/TLS)
    alt success
        API-->>B: CreateSavedFilterResponse proto
        B-->>W: MessageToDict(response)
        W-->>C: CreateSavedFilterResponse
    else gRPC error
        API-->>B: gRPC status + details
        B-->>W: raise HTTPException
        W-->>C: raise HTTPException
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `data` | body | `-` | No |

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
response = client.saved_filter.create_saved_filter()
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
    else error
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

**gRPC transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.saved_filter
    participant B as proto bridge
    participant API as Kentik gRPC API

    C->>W: get_saved_filter(id="id-example")
    W->>B: ParseDict(params, GetSavedFilterRequest)
    B->>API: get_saved_filter (gRPC/TLS)
    alt success
        API-->>B: GetSavedFilterResponse proto
        B-->>W: MessageToDict(response)
        W-->>C: GetSavedFilterResponse
    else gRPC error
        API-->>B: gRPC status + details
        B-->>W: raise HTTPException
        W-->>C: raise HTTPException
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

    C->>W: update_saved_filter(id="id-example")
    W->>API: PUT /saved-filter/v202501alpha1/{id}
    alt success
        API-->>W: UpdateSavedFilterResponse (JSON)
        W-->>C: UpdateSavedFilterResponse
    else error
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

**gRPC transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.saved_filter
    participant B as proto bridge
    participant API as Kentik gRPC API

    C->>W: update_saved_filter(id="id-example")
    W->>B: ParseDict(params, UpdateSavedFilterRequest)
    B->>API: update_saved_filter (gRPC/TLS)
    alt success
        API-->>B: UpdateSavedFilterResponse proto
        B-->>W: MessageToDict(response)
        W-->>C: UpdateSavedFilterResponse
    else gRPC error
        API-->>B: gRPC status + details
        B-->>W: raise HTTPException
        W-->>C: raise HTTPException
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `id` | path | `string` | Yes |
| `data` | body | `-` | No |

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
    else error
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

**gRPC transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.saved_filter
    participant B as proto bridge
    participant API as Kentik gRPC API

    C->>W: delete_saved_filter(id="id-example")
    W->>B: ParseDict(params, DeleteSavedFilterRequest)
    B->>API: delete_saved_filter (gRPC/TLS)
    alt success
        API-->>B: DeleteSavedFilterResponse proto
        B-->>W: MessageToDict(response)
        W-->>C: DeleteSavedFilterResponse
    else gRPC error
        API-->>B: gRPC status + details
        B-->>W: raise HTTPException
        W-->>C: raise HTTPException
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
    else error
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

**gRPC transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.saved_filter
    participant B as proto bridge
    participant API as Kentik gRPC API

    C->>W: list_saved_filters()
    W->>B: ParseDict(params, ListSavedFiltersRequest)
    B->>API: list_saved_filters (gRPC/TLS)
    alt success
        API-->>B: ListSavedFiltersResponse proto
        B-->>W: MessageToDict(response)
        W-->>C: ListSavedFiltersResponse
    else gRPC error
        API-->>B: gRPC status + details
        B-->>W: raise HTTPException
        W-->>C: raise HTTPException
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
    else error
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

**gRPC transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.saved_filter
    participant B as proto bridge
    participant API as Kentik gRPC API

    C->>W: list_saved_filters_all()
    W->>B: ParseDict(params, ListSavedFiltersAllRequest)
    B->>API: list_saved_filters_all (gRPC/TLS)
    alt success
        API-->>B: ListSavedFiltersAllResponse proto
        B-->>W: MessageToDict(response)
        W-->>C: ListSavedFiltersAllResponse
    else gRPC error
        API-->>B: gRPC status + details
        B-->>W: raise HTTPException
        W-->>C: raise HTTPException
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
<summary>Model relationships (9 of 16 models)</summary>

```mermaid
classDiagram
    class CreateSavedFilterResponse
    class DeleteSavedFilterResponse
    class GetSavedFilterResponse
    class ListSavedFiltersAllResponse
    class ListSavedFiltersResponse
    class SavedFilter
    class UpdateSavedFilterResponse
    class protobufAny
    class rpcStatus
    CreateSavedFilterResponse --> SavedFilter
    GetSavedFilterResponse --> SavedFilter
    ListSavedFiltersAllResponse --> SavedFilter
    ListSavedFiltersResponse --> SavedFilter
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
