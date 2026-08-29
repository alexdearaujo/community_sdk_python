<!-- AUTO-GENERATED: scripts/generation/endpoint_docs.py, render_endpoint_docs() -->
<!-- Rebuilt on every `make generate`. Do not edit by hand. -->

# Network Class Service

## Overview

```mermaid
flowchart LR
    subgraph sdk["kentik_api"]
        KA["KentikAPI"]
        W["Network ClassServiceWrapper\nclient.network_class"]
        REST["REST functions\ngen/network_class/services/"]
        RJ["request_json()\ncore/rest_runtime"]
        M["Models\ngen/network_class/models/"]
        E["Error classes\ngen/network_class/error/"]
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

### `GET` `/network_class/v202109alpha1/network_class`

Get a network classification.

Returns information about a network classification for the company.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.network_class
    participant API as Kentik REST API

    C->>W: network_class_get()
    W->>API: GET /network_class/v202109alpha1/network_class
    alt success
        API-->>W: v202109alpha1GetNetworkClassResponse (JSON)
        W-->>C: v202109alpha1GetNetworkClassResponse
    else error
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

**gRPC transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.network_class
    participant B as proto bridge
    participant API as Kentik gRPC API

    C->>W: network_class_get()
    W->>B: ParseDict(params, NetworkClassGetRequest)
    B->>API: network_class_get (gRPC/TLS)
    alt success
        API-->>B: v202109alpha1GetNetworkClassResponse proto
        B-->>W: MessageToDict(response)
        W-->>C: v202109alpha1GetNetworkClassResponse
    else gRPC error
        API-->>B: gRPC status + details
        B-->>W: raise HTTPException
        W-->>C: raise HTTPException
    end
```

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `v202109alpha1GetNetworkClassResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.network_class.network_class_get()
```

---

### `POST` `/network_class/v202109alpha1/network_class`

Update a network classification.

Replaces the entire network classification attributes for the company.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.network_class
    participant API as Kentik REST API

    C->>W: network_class_update(data=UpdateNetworkClassRequest(...))
    W->>API: POST /network_class/v202109alpha1/network_class
    alt success
        API-->>W: v202109alpha1UpdateNetworkClassResponse (JSON)
        W-->>C: v202109alpha1UpdateNetworkClassResponse
    else error
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

**gRPC transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.network_class
    participant B as proto bridge
    participant API as Kentik gRPC API

    C->>W: network_class_update(data=UpdateNetworkClassRequest(...))
    W->>B: ParseDict(params, NetworkClassUpdateRequest)
    B->>API: network_class_update (gRPC/TLS)
    alt success
        API-->>B: v202109alpha1UpdateNetworkClassResponse proto
        B-->>W: MessageToDict(response)
        W-->>C: v202109alpha1UpdateNetworkClassResponse
    else gRPC error
        API-->>B: gRPC status + details
        B-->>W: raise HTTPException
        W-->>C: raise HTTPException
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `data` | body | `v202109alpha1UpdateNetworkClassRequest` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `v202109alpha1UpdateNetworkClassResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.network_class.network_class_update(
    data=UpdateNetworkClassRequest(...),
)
```

## Data Models

<details>
<summary>Model relationships (2 of 8 models)</summary>

```mermaid
classDiagram
    class protobufAny
    class rpcStatus
    rpcStatus --> protobufAny
```

</details>

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.network_class.models.CloudSubnet
```

```{eval-rst}
.. autoclass:: kentik_api.gen.network_class.models.CloudType
   :members:
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.network_class.models.GetNetworkClassResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.network_class.models.NetworkClass
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.network_class.models.UpdateNetworkClassRequest
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.network_class.models.UpdateNetworkClassResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.network_class.models.protobufAny
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.network_class.models.rpcStatus
```
