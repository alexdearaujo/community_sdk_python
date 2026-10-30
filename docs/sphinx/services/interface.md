<!-- AUTO-GENERATED: scripts/generation/endpoint_docs.py, render_endpoint_docs() -->
<!-- Rebuilt on every `uv run poe generate`. Do not edit by hand. -->

# Interface Service

## Overview

```mermaid
%%{init: {"fontFamily": "ui-monospace, SFMono-Regular, Menlo, monospace", "flowchart": {"curve": "step", "nodeSpacing": 30, "rankSpacing": 70, "wrappingWidth": 400}}}%%
flowchart LR
    code("Your code"):::greenSrc
    subgraph sdk["kentik_api"]
        wrap("InterfaceServiceWrapper<br/>client.interface<br/>6 operations"):::orange
        rest("REST functions<br/>gen/interface/services/"):::blue
        rj("request_json()<br/>core/rest_runtime.py"):::blue
        cg("call_grpc()<br/>core/grpc_runtime.py"):::violet
    end
    grpcapi("Kentik gRPC API<br/>HTTP/2 + protobuf"):::violetSrc
    restapi("Kentik REST API<br/>HTTPS + JSON"):::blueSrc

    code -->|"method call"| wrap
    wrap -->|"Pydantic model from<br/>gen/interface/models/"| code
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

On an error status or a failed call, the SDK raises an error class from `gen/interface/error/`, or a shared type from `kentik_api.errors`.

## Endpoints

### `GET` `/interface/v202108alpha1/interfaces`

Fetch Search Interfaces

Return list of interfaces matches search critera.

#### REST call flow

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.interface
    participant API as Kentik REST API

    C->>W: list()
    W->>API: GET /interface/v202108alpha1/interfaces
    alt success
        API-->>W: ListInterfaceResponse (JSON)
        W-->>C: ListInterfaceResponse
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
    participant W as client.interface
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: list()
    W->>R: build_grpc_request(ListInterfaceRequest, arguments)
    R->>API: InterfaceService/ListInterface (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: parse_grpc_response(response)
        W-->>C: ListInterfaceResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
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

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.interface.list()
```

---

### `POST` `/interface/v202108alpha1/interfaces`

Create a interface.

Create a interface from request. returns created.

#### REST call flow

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.interface
    participant API as Kentik REST API

    C->>W: create(data=CreateInterfaceRequest(...))
    W->>API: POST /interface/v202108alpha1/interfaces
    alt success
        API-->>W: CreateInterfaceResponse (JSON)
        W-->>C: CreateInterfaceResponse
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
    participant W as client.interface
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: create(data=CreateInterfaceRequest(...))
    W->>R: build_grpc_request(CreateInterfaceRequest, arguments)
    R->>API: InterfaceService/CreateInterface (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: parse_grpc_response(response)
        W-->>C: CreateInterfaceResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
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
from kentik_api.gen.interface.models import CreateInterfaceRequest

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.interface.create(
    data=CreateInterfaceRequest(...),
)
```

---

### `GET` `/interface/v202108alpha1/interfaces/{id}`

Get a interface.

Returns information about a interface specified with ID.

#### REST call flow

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.interface
    participant API as Kentik REST API

    C->>W: get(id="id-example")
    W->>API: GET /interface/v202108alpha1/interfaces/{id}
    alt success
        API-->>W: GetInterfaceResponse (JSON)
        W-->>C: GetInterfaceResponse
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
    participant W as client.interface
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: get(id="id-example")
    W->>R: build_grpc_request(GetInterfaceRequest, arguments)
    R->>API: InterfaceService/GetInterface (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: parse_grpc_response(response)
        W-->>C: GetInterfaceResponse
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
| 200 | A successful response. | `GetInterfaceResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.interface.get(
    id="id-example",
)
```

---

### `PUT` `/interface/v202108alpha1/interfaces/{id}`

Update a interface.

Replaces the entire interface attributes specified with id.

#### REST call flow

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.interface
    participant API as Kentik REST API

    C->>W: update(id="id-example", data=InterfaceServiceUpdateInterfaceBody(...))
    W->>API: PUT /interface/v202108alpha1/interfaces/{id}
    alt success
        API-->>W: UpdateInterfaceResponse (JSON)
        W-->>C: UpdateInterfaceResponse
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
    participant W as client.interface
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: update(id="id-example", data=InterfaceServiceUpdateInterfaceBody(...))
    W->>R: build_grpc_request(UpdateInterfaceRequest, arguments)
    R->>API: InterfaceService/UpdateInterface (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: parse_grpc_response(response)
        W-->>C: UpdateInterfaceResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
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
from kentik_api.gen.interface.models import InterfaceServiceUpdateInterfaceBody

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.interface.update(
    id="id-example",
    data=InterfaceServiceUpdateInterfaceBody(...),
)
```

---

### `DELETE` `/interface/v202108alpha1/interfaces/{id}`

Delete a interface.

Deletes the interface specified with id.

#### REST call flow

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.interface
    participant API as Kentik REST API

    C->>W: delete(id="id-example")
    W->>API: DELETE /interface/v202108alpha1/interfaces/{id}
    alt success
        API-->>W: DeleteInterfaceResponse (JSON)
        W-->>C: DeleteInterfaceResponse
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
    participant W as client.interface
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: delete(id="id-example")
    W->>R: build_grpc_request(DeleteInterfaceRequest, arguments)
    R->>API: InterfaceService/DeleteInterface (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: parse_grpc_response(response)
        W-->>C: DeleteInterfaceResponse
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
| 200 | A successful response. | `DeleteInterfaceResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.interface.delete(
    id="id-example",
)
```

---

### `POST` `/interface/v202108alpha1/manual_classify`

Manual Classify Interface

Manually set interface(s) classification.

#### REST call flow

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.interface
    participant API as Kentik REST API

    C->>W: manual_classify(data=ManualClassifyRequest(...))
    W->>API: POST /interface/v202108alpha1/manual_classify
    alt success
        API-->>W: ManualClassifyResponse (JSON)
        W-->>C: ManualClassifyResponse
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
    participant W as client.interface
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: manual_classify(data=ManualClassifyRequest(...))
    W->>R: build_grpc_request(ManualClassifyRequest, arguments)
    R->>API: InterfaceService/ManualClassify (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: parse_grpc_response(response)
        W-->>C: ManualClassifyResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
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
from kentik_api.gen.interface.models import ManualClassifyRequest

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.interface.manual_classify(
    data=ManualClassifyRequest(...),
)
```

## Data Models

<details>
<summary>Model relationships (14 of 17 models)</summary>

Each arrow points from a model to a model that one of its fields holds. The label names the field.

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
    CreateInterfaceRequest --> Interface : interface
    CreateInterfaceResponse --> Interface : interface
    GetInterfaceResponse --> Interface : interface
    Interface --> ConnectivityType : connectivityType, initialConnectivityType
    Interface --> NetworkBoundary : networkBoundary, initialNetworkBoundary
    ListInterfaceResponse --> Interface : interfaces
    ManualClassifyRequest --> ConnectivityType : connectivityType
    ManualClassifyRequest --> NetworkBoundary : networkBoundary
    UpdateInterfaceResponse --> Interface : interface
    rpcStatus --> protobufAny : details
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
