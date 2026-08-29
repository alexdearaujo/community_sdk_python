<!-- AUTO-GENERATED: scripts/generation/endpoint_docs.py, render_endpoint_docs() -->
<!-- Rebuilt on every `make generate`. Do not edit by hand. -->

# Interface Service

## Overview

```mermaid
flowchart LR
    subgraph sdk["kentik_api"]
        KA["KentikAPI"]
        W["InterfaceServiceWrapper\nclient.interface"]
        REST["REST functions\ngen/interface/services/"]
        RJ["request_json()\ncore/rest_runtime"]
        M["Models\ngen/interface/models/"]
        E["Error classes\ngen/interface/error/"]
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

### `GET` `/interface/v202108alpha1/interfaces`

Fetch Search Interfaces

Return list of interfaces matches search critera.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.interface
    participant API as Kentik REST API

    C->>W: list_interface()
    W->>API: GET /interface/v202108alpha1/interfaces
    alt success
        API-->>W: v202108alpha1ListInterfaceResponse (JSON)
        W-->>C: v202108alpha1ListInterfaceResponse
    else error
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

**gRPC transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.interface
    participant B as proto bridge
    participant API as Kentik gRPC API

    C->>W: list_interface()
    W->>B: ParseDict(params, ListInterfaceRequest)
    B->>API: list_interface (gRPC/TLS)
    alt success
        API-->>B: v202108alpha1ListInterfaceResponse proto
        B-->>W: MessageToDict(response)
        W-->>C: v202108alpha1ListInterfaceResponse
    else gRPC error
        API-->>B: gRPC status + details
        B-->>W: raise HTTPException
        W-->>C: raise HTTPException
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `filterstext` | query | `string` | No |
| `filtersdeviceIds` | query | `string[]` | No |
| `filtersconnectivityTypes` | query | `string[]` | No |
| `filtersnetworkBoundaries` | query | `string[]` | No |
| `filtersproviders` | query | `string[]` | No |
| `filterssnmpSpeeds` | query | `integer (int32)[]` | No |
| `filtersipTypes` | query | `string[]` | No |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `v202108alpha1ListInterfaceResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.interface.list_interface()
```

---

### `POST` `/interface/v202108alpha1/interfaces`

Create a interface.

Create a interface from request. returns created.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.interface
    participant API as Kentik REST API

    C->>W: interface_create(data=CreateInterfaceRequest(...))
    W->>API: POST /interface/v202108alpha1/interfaces
    alt success
        API-->>W: v202108alpha1CreateInterfaceResponse (JSON)
        W-->>C: v202108alpha1CreateInterfaceResponse
    else error
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

**gRPC transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.interface
    participant B as proto bridge
    participant API as Kentik gRPC API

    C->>W: interface_create(data=CreateInterfaceRequest(...))
    W->>B: ParseDict(params, InterfaceCreateRequest)
    B->>API: interface_create (gRPC/TLS)
    alt success
        API-->>B: v202108alpha1CreateInterfaceResponse proto
        B-->>W: MessageToDict(response)
        W-->>C: v202108alpha1CreateInterfaceResponse
    else gRPC error
        API-->>B: gRPC status + details
        B-->>W: raise HTTPException
        W-->>C: raise HTTPException
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `data` | body | `v202108alpha1CreateInterfaceRequest` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `v202108alpha1CreateInterfaceResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.interface.interface_create(
    data=CreateInterfaceRequest(...),
)
```

---

### `GET` `/interface/v202108alpha1/interfaces/{id}`

Get a interface.

Returns information about a interface specified with ID.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.interface
    participant API as Kentik REST API

    C->>W: interface_get(id="id-example")
    W->>API: GET /interface/v202108alpha1/interfaces/{id}
    alt success
        API-->>W: v202108alpha1GetInterfaceResponse (JSON)
        W-->>C: v202108alpha1GetInterfaceResponse
    else error
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

**gRPC transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.interface
    participant B as proto bridge
    participant API as Kentik gRPC API

    C->>W: interface_get(id="id-example")
    W->>B: ParseDict(params, InterfaceGetRequest)
    B->>API: interface_get (gRPC/TLS)
    alt success
        API-->>B: v202108alpha1GetInterfaceResponse proto
        B-->>W: MessageToDict(response)
        W-->>C: v202108alpha1GetInterfaceResponse
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
| 200 | A successful response. | `v202108alpha1GetInterfaceResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.interface.interface_get(
    id="id-example",
)
```

---

### `PUT` `/interface/v202108alpha1/interfaces/{id}`

Update a interface.

Replaces the entire interface attributes specified with id.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.interface
    participant API as Kentik REST API

    C->>W: interface_update(id="id-example", data=InterfaceServiceUpdateInterfaceBody(...))
    W->>API: PUT /interface/v202108alpha1/interfaces/{id}
    alt success
        API-->>W: v202108alpha1UpdateInterfaceResponse (JSON)
        W-->>C: v202108alpha1UpdateInterfaceResponse
    else error
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

**gRPC transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.interface
    participant B as proto bridge
    participant API as Kentik gRPC API

    C->>W: interface_update(id="id-example", data=InterfaceServiceUpdateInterfaceBody(...))
    W->>B: ParseDict(params, InterfaceUpdateRequest)
    B->>API: interface_update (gRPC/TLS)
    alt success
        API-->>B: v202108alpha1UpdateInterfaceResponse proto
        B-->>W: MessageToDict(response)
        W-->>C: v202108alpha1UpdateInterfaceResponse
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
| `data` | body | `InterfaceServiceUpdateInterfaceBody` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `v202108alpha1UpdateInterfaceResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.interface.interface_update(
    id="id-example",
    data=InterfaceServiceUpdateInterfaceBody(...),
)
```

---

### `DELETE` `/interface/v202108alpha1/interfaces/{id}`

Delete a interface.

Deletes the interface specified with id.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.interface
    participant API as Kentik REST API

    C->>W: interface_delete(id="id-example")
    W->>API: DELETE /interface/v202108alpha1/interfaces/{id}
    alt success
        API-->>W: v202108alpha1DeleteInterfaceResponse (JSON)
        W-->>C: v202108alpha1DeleteInterfaceResponse
    else error
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

**gRPC transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.interface
    participant B as proto bridge
    participant API as Kentik gRPC API

    C->>W: interface_delete(id="id-example")
    W->>B: ParseDict(params, InterfaceDeleteRequest)
    B->>API: interface_delete (gRPC/TLS)
    alt success
        API-->>B: v202108alpha1DeleteInterfaceResponse proto
        B-->>W: MessageToDict(response)
        W-->>C: v202108alpha1DeleteInterfaceResponse
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
| 200 | A successful response. | `v202108alpha1DeleteInterfaceResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.interface.interface_delete(
    id="id-example",
)
```

---

### `POST` `/interface/v202108alpha1/manual_classify`

Manual Classify Interface

Manually set interface(s) classification.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.interface
    participant API as Kentik REST API

    C->>W: manual_classify(data=ManualClassifyRequest(...))
    W->>API: POST /interface/v202108alpha1/manual_classify
    alt success
        API-->>W: v202108alpha1ManualClassifyResponse (JSON)
        W-->>C: v202108alpha1ManualClassifyResponse
    else error
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

**gRPC transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.interface
    participant B as proto bridge
    participant API as Kentik gRPC API

    C->>W: manual_classify(data=ManualClassifyRequest(...))
    W->>B: ParseDict(params, ManualClassifyRequest)
    B->>API: manual_classify (gRPC/TLS)
    alt success
        API-->>B: v202108alpha1ManualClassifyResponse proto
        B-->>W: MessageToDict(response)
        W-->>C: v202108alpha1ManualClassifyResponse
    else gRPC error
        API-->>B: gRPC status + details
        B-->>W: raise HTTPException
        W-->>C: raise HTTPException
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `data` | body | `v202108alpha1ManualClassifyRequest` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `v202108alpha1ManualClassifyResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.interface.manual_classify(
    data=ManualClassifyRequest(...),
)
```

## Data Models

<details>
<summary>Model relationships (3 of 17 models)</summary>

```mermaid
classDiagram
    class InterfaceServiceUpdateInterfaceBody
    class protobufAny
    class rpcStatus
    rpcStatus --> protobufAny
```

</details>

```{eval-rst}
.. autoclass:: kentik_api.gen.interface.models.ConnectivityType
   :members:
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.interface.models.CreateInterfaceRequest
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.interface.models.CreateInterfaceResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.interface.models.DeleteInterfaceResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.interface.models.GetInterfaceResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.interface.models.Interface
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.interface.models.InterfaceFilter
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.interface.models.InterfaceServiceUpdateInterfaceBody
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.interface.models.InterfaceVrf
```

```{eval-rst}
.. autoclass:: kentik_api.gen.interface.models.IpFilter
   :members:
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.interface.models.ListInterfaceResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.interface.models.ManualClassifyRequest
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.interface.models.ManualClassifyResponse
```

```{eval-rst}
.. autoclass:: kentik_api.gen.interface.models.NetworkBoundary
   :members:
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.interface.models.UpdateInterfaceResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.interface.models.protobufAny
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.interface.models.rpcStatus
```
