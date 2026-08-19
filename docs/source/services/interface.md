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

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.interface
    participant API as Kentik API

    C->>W: list_interface()
    W->>API: GET /interface/v202108alpha1/interfaces
    alt success
        API-->>W: ListInterfaceResponse
        W-->>C: ListInterfaceResponse
    else error status
        API-->>W: error body
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
| 200 | A successful response. | `ListInterfaceResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Use protocol="grpc" to route through gRPC instead of REST.
# See docs/source/grpc_implementation_spec.md for current gRPC status.
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.interface.list_interface()
```

---

### `POST` `/interface/v202108alpha1/interfaces`

Create a interface.

Create a interface from request. returns created.

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.interface
    participant API as Kentik API

    C->>W: interface_create(data=CreateInterfaceRequest(...))
    W->>API: POST /interface/v202108alpha1/interfaces
    alt success
        API-->>W: CreateInterfaceResponse
        W-->>C: CreateInterfaceResponse
    else error status
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `data` | body | `CreateInterfaceRequest` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `CreateInterfaceResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Use protocol="grpc" to route through gRPC instead of REST.
# See docs/source/grpc_implementation_spec.md for current gRPC status.
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.interface.interface_create(
    data=CreateInterfaceRequest(...),
)
```

---

### `GET` `/interface/v202108alpha1/interfaces/{id}`

Get a interface.

Returns information about a interface specified with ID.

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.interface
    participant API as Kentik API

    C->>W: interface_get(id="id-example")
    W->>API: GET /interface/v202108alpha1/interfaces/{id}
    alt success
        API-->>W: GetInterfaceResponse
        W-->>C: GetInterfaceResponse
    else error status
        API-->>W: error body
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
| 200 | A successful response. | `GetInterfaceResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Use protocol="grpc" to route through gRPC instead of REST.
# See docs/source/grpc_implementation_spec.md for current gRPC status.
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.interface.interface_get(
    id="id-example",
)
```

---

### `PUT` `/interface/v202108alpha1/interfaces/{id}`

Update a interface.

Replaces the entire interface attributes specified with id.

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.interface
    participant API as Kentik API

    C->>W: interface_update(id="id-example", data=InterfaceServiceUpdateInterfaceBody(...))
    W->>API: PUT /interface/v202108alpha1/interfaces/{id}
    alt success
        API-->>W: UpdateInterfaceResponse
        W-->>C: UpdateInterfaceResponse
    else error status
        API-->>W: error body
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
| 200 | A successful response. | `UpdateInterfaceResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Use protocol="grpc" to route through gRPC instead of REST.
# See docs/source/grpc_implementation_spec.md for current gRPC status.
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

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.interface
    participant API as Kentik API

    C->>W: interface_delete(id="id-example")
    W->>API: DELETE /interface/v202108alpha1/interfaces/{id}
    alt success
        API-->>W: DeleteInterfaceResponse
        W-->>C: DeleteInterfaceResponse
    else error status
        API-->>W: error body
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
| 200 | A successful response. | `DeleteInterfaceResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Use protocol="grpc" to route through gRPC instead of REST.
# See docs/source/grpc_implementation_spec.md for current gRPC status.
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.interface.interface_delete(
    id="id-example",
)
```

---

### `POST` `/interface/v202108alpha1/manual_classify`

Manual Classify Interface

Manually set interface(s) classification.

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.interface
    participant API as Kentik API

    C->>W: manual_classify(data=ManualClassifyRequest(...))
    W->>API: POST /interface/v202108alpha1/manual_classify
    alt success
        API-->>W: ManualClassifyResponse
        W-->>C: ManualClassifyResponse
    else error status
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `data` | body | `ManualClassifyRequest` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `ManualClassifyResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Use protocol="grpc" to route through gRPC instead of REST.
# See docs/source/grpc_implementation_spec.md for current gRPC status.
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.interface.manual_classify(
    data=ManualClassifyRequest(...),
)
```

## Data Models

<details>
<summary>Model relationships (14 of 17 models)</summary>

```mermaid
classDiagram
    class ConnectivityType
    class CreateInterfaceRequest
    class CreateInterfaceResponse
    class DeleteInterfaceResponse
    class GetInterfaceResponse
    class Interface
    class InterfaceServiceUpdateInterfaceBody
    class ListInterfaceResponse
    class ManualClassifyRequest
    class ManualClassifyResponse
    class NetworkBoundary
    class UpdateInterfaceResponse
    class protobufAny
    class rpcStatus
    CreateInterfaceRequest --> Interface
    CreateInterfaceResponse --> Interface
    GetInterfaceResponse --> Interface
    Interface --> ConnectivityType
    Interface --> NetworkBoundary
    ListInterfaceResponse --> Interface
    ManualClassifyRequest --> ConnectivityType
    ManualClassifyRequest --> NetworkBoundary
    UpdateInterfaceResponse --> Interface
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
