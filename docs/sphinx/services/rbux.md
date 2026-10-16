<!-- AUTO-GENERATED: scripts/generation/endpoint_docs.py, render_endpoint_docs() -->
<!-- Rebuilt on every `make generate`. Do not edit by hand. -->

# Rbux Service

## Overview

```mermaid
flowchart LR
    subgraph sdk["kentik_api"]
        KA["KentikAPI"]
        W["RbuxServiceWrapper\nclient.rbux"]
        REST["REST functions\ngen/rbux/services/"]
        RJ["request_json()\ncore/rest_runtime"]
        M["Models\ngen/rbux/models/"]
        E["Error classes\ngen/rbux/error/"]
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

### `GET` `/rbux/v202607alpha1/scopes`

List Focus Scopes

Returns all Focus Scopes for the user's company.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.rbux
    participant API as Kentik REST API

    C->>W: list_scopes()
    W->>API: GET /rbux/v202607alpha1/scopes
    alt success
        API-->>W: v202607alpha1ListScopesResponse (JSON)
        W-->>C: v202607alpha1ListScopesResponse
    else error
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

**gRPC transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.rbux
    participant B as proto bridge
    participant API as Kentik gRPC API

    C->>W: list_scopes()
    W->>B: ParseDict(params, ListScopesRequest)
    B->>API: list_scopes (gRPC/TLS)
    alt success
        API-->>B: v202607alpha1ListScopesResponse proto
        B-->>W: MessageToDict(response)
        W-->>C: v202607alpha1ListScopesResponse
    else gRPC error
        API-->>B: gRPC status + details
        B-->>W: raise HTTPException
        W-->>C: raise HTTPException
    end
```

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `v202607alpha1ListScopesResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.rbux.list_scopes()
```

---

### `POST` `/rbux/v202607alpha1/scopes`

Create Focus Scope

Creates and returns a new Focus Scope.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.rbux
    participant API as Kentik REST API

    C->>W: create_scope(data=Scope(...))
    W->>API: POST /rbux/v202607alpha1/scopes
    alt success
        API-->>W: v202607alpha1CreateScopeResponse (JSON)
        W-->>C: v202607alpha1CreateScopeResponse
    else error
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

**gRPC transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.rbux
    participant B as proto bridge
    participant API as Kentik gRPC API

    C->>W: create_scope(data=Scope(...))
    W->>B: ParseDict(params, CreateScopeRequest)
    B->>API: create_scope (gRPC/TLS)
    alt success
        API-->>B: v202607alpha1CreateScopeResponse proto
        B-->>W: MessageToDict(response)
        W-->>C: v202607alpha1CreateScopeResponse
    else gRPC error
        API-->>B: gRPC status + details
        B-->>W: raise HTTPException
        W-->>C: raise HTTPException
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `data` | body | `v202607alpha1Scope` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `v202607alpha1CreateScopeResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.rbux.create_scope(
    data=Scope(...),
)
```

---

### `GET` `/rbux/v202607alpha1/scopes/{id}`

Get Focus Scope

Returns a single Focus Scope by id.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.rbux
    participant API as Kentik REST API

    C->>W: get_scope(id="id-example")
    W->>API: GET /rbux/v202607alpha1/scopes/{id}
    alt success
        API-->>W: v202607alpha1GetScopeResponse (JSON)
        W-->>C: v202607alpha1GetScopeResponse
    else error
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

**gRPC transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.rbux
    participant B as proto bridge
    participant API as Kentik gRPC API

    C->>W: get_scope(id="id-example")
    W->>B: ParseDict(params, GetScopeRequest)
    B->>API: get_scope (gRPC/TLS)
    alt success
        API-->>B: v202607alpha1GetScopeResponse proto
        B-->>W: MessageToDict(response)
        W-->>C: v202607alpha1GetScopeResponse
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
| 200 | A successful response. | `v202607alpha1GetScopeResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.rbux.get_scope(
    id="id-example",
)
```

---

### `PUT` `/rbux/v202607alpha1/scopes/{id}`

Update Focus Scope

Updates and returns an existing Focus Scope.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.rbux
    participant API as Kentik REST API

    C->>W: update_scope(id="id-example", data=Dict[str, Any](...))
    W->>API: PUT /rbux/v202607alpha1/scopes/{id}
    alt success
        API-->>W: v202607alpha1UpdateScopeResponse (JSON)
        W-->>C: v202607alpha1UpdateScopeResponse
    else error
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

**gRPC transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.rbux
    participant B as proto bridge
    participant API as Kentik gRPC API

    C->>W: update_scope(id="id-example", data=Dict[str, Any](...))
    W->>B: ParseDict(params, UpdateScopeRequest)
    B->>API: update_scope (gRPC/TLS)
    alt success
        API-->>B: v202607alpha1UpdateScopeResponse proto
        B-->>W: MessageToDict(response)
        W-->>C: v202607alpha1UpdateScopeResponse
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
| `data` | body | `object` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `v202607alpha1UpdateScopeResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.rbux.update_scope(
    id="id-example",
    data=Dict[str, Any](...),
)
```

---

### `DELETE` `/rbux/v202607alpha1/scopes/{id}`

Delete Focus Scope

Deletes a Focus Scope.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.rbux
    participant API as Kentik REST API

    C->>W: delete_scope(id="id-example")
    W->>API: DELETE /rbux/v202607alpha1/scopes/{id}
    alt success
        API-->>W: v202607alpha1DeleteScopeResponse (JSON)
        W-->>C: v202607alpha1DeleteScopeResponse
    else error
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

**gRPC transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.rbux
    participant B as proto bridge
    participant API as Kentik gRPC API

    C->>W: delete_scope(id="id-example")
    W->>B: ParseDict(params, DeleteScopeRequest)
    B->>API: delete_scope (gRPC/TLS)
    alt success
        API-->>B: v202607alpha1DeleteScopeResponse proto
        B-->>W: MessageToDict(response)
        W-->>C: v202607alpha1DeleteScopeResponse
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
| 200 | A successful response. | `v202607alpha1DeleteScopeResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.rbux.delete_scope(
    id="id-example",
)
```

## Data Models

<details>
<summary>Model relationships (2 of 17 models)</summary>

```mermaid
classDiagram
    class protobufAny
    class rpcStatus
    rpcStatus --> protobufAny
```

</details>

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.rbux.models.AssetTagSelector
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.rbux.models.CreateScopeResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.rbux.models.DeleteScopeResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.rbux.models.GetScopeResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.rbux.models.ListScopesResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.rbux.models.Scope
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.rbux.models.ScopeConfig
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.rbux.models.ScopeDimensions
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.rbux.models.UpdateScopeResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.rbux.models.protobufAny
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.rbux.models.rpcStatus
```

```{eval-rst}
.. autoclass:: kentik_api.gen.rbux.models.v202501alpha1FilterField
   :members:
```

```{eval-rst}
.. autoclass:: kentik_api.gen.rbux.models.v202501alpha1FilterOperator
   :members:
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.rbux.models.v202501alpha1SavedFilterFilter
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.rbux.models.v202501alpha1SavedFilterFilterGroup
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.rbux.models.v202501alpha1SavedFilterFilterId
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.rbux.models.v202501alpha1SavedFilterFilters
```
