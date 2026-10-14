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
        API-->>W: ListScopesResponse (JSON)
        W-->>C: ListScopesResponse
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
    participant W as client.rbux
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: list_scopes()
    W->>R: build_grpc_request(ListScopesRequest, arguments)
    R->>API: ScopeService/ListScopes (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: MessageToDict(response)
        W-->>C: ListScopesResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `ListScopesResponse` |
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
        API-->>W: CreateScopeResponse (JSON)
        W-->>C: CreateScopeResponse
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
    participant W as client.rbux
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: create_scope(data=Scope(...))
    W->>R: build_grpc_request(CreateScopeRequest, arguments)
    R->>API: ScopeService/CreateScope (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: MessageToDict(response)
        W-->>C: CreateScopeResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `data` | body | `Scope` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `CreateScopeResponse` |
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
        API-->>W: GetScopeResponse (JSON)
        W-->>C: GetScopeResponse
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
    participant W as client.rbux
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: get_scope(id="id-example")
    W->>R: build_grpc_request(GetScopeRequest, arguments)
    R->>API: ScopeService/GetScope (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: MessageToDict(response)
        W-->>C: GetScopeResponse
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
| 200 | A successful response. | `GetScopeResponse` |
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

    C->>W: update_scope(id="id-example", data=ScopeServiceUpdateScopeBody(...))
    W->>API: PUT /rbux/v202607alpha1/scopes/{id}
    alt success
        API-->>W: UpdateScopeResponse (JSON)
        W-->>C: UpdateScopeResponse
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
    participant W as client.rbux
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: update_scope(id="id-example", data=ScopeServiceUpdateScopeBody(...))
    W->>R: build_grpc_request(UpdateScopeRequest, arguments)
    R->>API: ScopeService/UpdateScope (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: MessageToDict(response)
        W-->>C: UpdateScopeResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `id` | path | `string` | Yes |
| `data` | body | `ScopeServiceUpdateScopeBody` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `UpdateScopeResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.rbux.update_scope(
    id="id-example",
    data=ScopeServiceUpdateScopeBody(...),
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
        API-->>W: DeleteScopeResponse (JSON)
        W-->>C: DeleteScopeResponse
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
    participant W as client.rbux
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: delete_scope(id="id-example")
    W->>R: build_grpc_request(DeleteScopeRequest, arguments)
    R->>API: ScopeService/DeleteScope (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: MessageToDict(response)
        W-->>C: DeleteScopeResponse
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
| 200 | A successful response. | `DeleteScopeResponse` |
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
<summary>Model relationships (10 of 18 models)</summary>

```mermaid
classDiagram
    class CreateScopeResponse
    class DeleteScopeResponse
    class GetScopeResponse
    class ListScopesResponse
    class Scope
    class ScopeConfig
    class ScopeServiceUpdateScopeBody
    class UpdateScopeResponse
    class protobufAny
    class rpcStatus
    CreateScopeResponse --> Scope
    GetScopeResponse --> Scope
    ListScopesResponse --> Scope
    Scope --> ScopeConfig
    ScopeServiceUpdateScopeBody --> ScopeConfig
    UpdateScopeResponse --> Scope
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
.. autopydantic_model:: kentik_api.gen.rbux.models.ScopeServiceUpdateScopeBody
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
