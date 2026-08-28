<!-- AUTO-GENERATED: scripts/generation/endpoint_docs.py, _render_sphinx_stubs() -->
<!-- Rebuilt on every `make generate`. Do not edit by hand. -->

# Flow Tag Service

## Overview

```mermaid
flowchart LR
    subgraph sdk["kentik_api"]
        KA["KentikAPI"]
        W["Flow TagServiceWrapper\nclient.flow_tag"]
        REST["REST functions\ngen/flow_tag/services/"]
        RJ["request_json()\ncore/rest_runtime"]
        M["Models\ngen/flow_tag/models/"]
        E["Error classes\ngen/flow_tag/error/"]
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

### `GET` `/flow_tag/v202404alpha1/tag`

Search flow tag configuration.

Returns configuration of flow tag with search parameters.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.flow_tag
    participant API as Kentik REST API

    C->>W: search_flow_tag()
    W->>API: GET /flow_tag/v202404alpha1/tag
    alt success
        API-->>W: v202404alpha1SearchFlowTagResponse (JSON)
        W-->>C: v202404alpha1SearchFlowTagResponse
    else error
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

**gRPC transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.flow_tag
    participant B as proto bridge
    participant API as Kentik gRPC API

    C->>W: search_flow_tag()
    W->>B: ParseDict(params, SearchFlowTagRequest)
    B->>API: search_flow_tag (gRPC/TLS)
    alt success
        API-->>B: v202404alpha1SearchFlowTagResponse proto
        B-->>W: MessageToDict(response)
        W-->>C: v202404alpha1SearchFlowTagResponse
    else gRPC error
        API-->>B: gRPC status + details
        B-->>W: raise HTTPException
        W-->>C: raise HTTPException
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `searchlimit` | query | `integer (int32)` | No |
| `searchoffset` | query | `integer (int32)` | No |
| `searchlookupFields` | query | `string[]` | No |
| `searchlookupValues` | query | `string[]` | No |
| `searchfieldLimit` | query | `integer (int32)` | No |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `v202404alpha1SearchFlowTagResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.flow_tag.search_flow_tag()
```

---

### `POST` `/flow_tag/v202404alpha1/tag`

Create flow tag configuration.

Create a flow tag configuration.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.flow_tag
    participant API as Kentik REST API

    C->>W: create_flow_tag(data=CreateFlowTagRequest(...))
    W->>API: POST /flow_tag/v202404alpha1/tag
    alt success
        API-->>W: v202404alpha1CreateFlowTagResponse (JSON)
        W-->>C: v202404alpha1CreateFlowTagResponse
    else error
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

**gRPC transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.flow_tag
    participant B as proto bridge
    participant API as Kentik gRPC API

    C->>W: create_flow_tag(data=CreateFlowTagRequest(...))
    W->>B: ParseDict(params, CreateFlowTagRequest)
    B->>API: create_flow_tag (gRPC/TLS)
    alt success
        API-->>B: v202404alpha1CreateFlowTagResponse proto
        B-->>W: MessageToDict(response)
        W-->>C: v202404alpha1CreateFlowTagResponse
    else gRPC error
        API-->>B: gRPC status + details
        B-->>W: raise HTTPException
        W-->>C: raise HTTPException
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `data` | body | `v202404alpha1CreateFlowTagRequest` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `v202404alpha1CreateFlowTagResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.flow_tag.create_flow_tag(
    data=CreateFlowTagRequest(...),
)
```

---

### `GET` `/flow_tag/v202404alpha1/tag/{flowTag.id}`

Get flow tag configuration.

Returns configuration of flow tag with specified ID.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.flow_tag
    participant API as Kentik REST API

    C->>W: get_flow_tag(flowTagid="flowTagid-example")
    W->>API: GET /flow_tag/v202404alpha1/tag/{flowTag.id}
    alt success
        API-->>W: v202404alpha1GetFlowTagResponse (JSON)
        W-->>C: v202404alpha1GetFlowTagResponse
    else error
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

**gRPC transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.flow_tag
    participant B as proto bridge
    participant API as Kentik gRPC API

    C->>W: get_flow_tag(flowTagid="flowTagid-example")
    W->>B: ParseDict(params, GetFlowTagRequest)
    B->>API: get_flow_tag (gRPC/TLS)
    alt success
        API-->>B: v202404alpha1GetFlowTagResponse proto
        B-->>W: MessageToDict(response)
        W-->>C: v202404alpha1GetFlowTagResponse
    else gRPC error
        API-->>B: gRPC status + details
        B-->>W: raise HTTPException
        W-->>C: raise HTTPException
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `flowTagid` | path | `string` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `v202404alpha1GetFlowTagResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.flow_tag.get_flow_tag(
    flowTagid="flowTagid-example",
)
```

---

### `PUT` `/flow_tag/v202404alpha1/tag/{flowTag.id}`

Update flow tag configuration.

Update a flow tag configuration.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.flow_tag
    participant API as Kentik REST API

    C->>W: update_flow_tag(flowTagid="flowTagid-example", data=FlowTagServiceUpdateFlowTagBody(...))
    W->>API: PUT /flow_tag/v202404alpha1/tag/{flowTag.id}
    alt success
        API-->>W: v202404alpha1UpdateFlowTagResponse (JSON)
        W-->>C: v202404alpha1UpdateFlowTagResponse
    else error
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

**gRPC transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.flow_tag
    participant B as proto bridge
    participant API as Kentik gRPC API

    C->>W: update_flow_tag(flowTagid="flowTagid-example", data=FlowTagServiceUpdateFlowTagBody(...))
    W->>B: ParseDict(params, UpdateFlowTagRequest)
    B->>API: update_flow_tag (gRPC/TLS)
    alt success
        API-->>B: v202404alpha1UpdateFlowTagResponse proto
        B-->>W: MessageToDict(response)
        W-->>C: v202404alpha1UpdateFlowTagResponse
    else gRPC error
        API-->>B: gRPC status + details
        B-->>W: raise HTTPException
        W-->>C: raise HTTPException
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `flowTagid` | path | `string` | Yes |
| `data` | body | `FlowTagServiceUpdateFlowTagBody` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `v202404alpha1UpdateFlowTagResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.flow_tag.update_flow_tag(
    flowTagid="flowTagid-example",
    data=FlowTagServiceUpdateFlowTagBody(...),
)
```

---

### `DELETE` `/flow_tag/v202404alpha1/tag/{flowTag.id}`

Delete flow tag configuration.

Delete a flow tag configuration with id.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.flow_tag
    participant API as Kentik REST API

    C->>W: delete_flow_tag(flowTagid="flowTagid-example")
    W->>API: DELETE /flow_tag/v202404alpha1/tag/{flowTag.id}
    alt success
        API-->>W: v202404alpha1DeleteFlowTagResponse (JSON)
        W-->>C: v202404alpha1DeleteFlowTagResponse
    else error
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

**gRPC transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.flow_tag
    participant B as proto bridge
    participant API as Kentik gRPC API

    C->>W: delete_flow_tag(flowTagid="flowTagid-example")
    W->>B: ParseDict(params, DeleteFlowTagRequest)
    B->>API: delete_flow_tag (gRPC/TLS)
    alt success
        API-->>B: v202404alpha1DeleteFlowTagResponse proto
        B-->>W: MessageToDict(response)
        W-->>C: v202404alpha1DeleteFlowTagResponse
    else gRPC error
        API-->>B: gRPC status + details
        B-->>W: raise HTTPException
        W-->>C: raise HTTPException
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `flowTagid` | path | `string` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `v202404alpha1DeleteFlowTagResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.flow_tag.delete_flow_tag(
    flowTagid="flowTagid-example",
)
```

## Data Models

<details>
<summary>Model relationships (3 of 15 models)</summary>

```mermaid
classDiagram
    class FlowTagServiceUpdateFlowTagBody
    class protobufAny
    class rpcStatus
    rpcStatus --> protobufAny
```

</details>

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.flow_tag.models.AddressInfo
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.flow_tag.models.CreateFlowTagRequest
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.flow_tag.models.CreateFlowTagResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.flow_tag.models.DeleteFlowTagResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.flow_tag.models.FlowTag
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.flow_tag.models.FlowTagSearch
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.flow_tag.models.FlowTagServiceUpdateFlowTagBody
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.flow_tag.models.GetFlowTagResponse
```

```{eval-rst}
.. autoclass:: kentik_api.gen.flow_tag.models.LookupField
   :members:
```

```{eval-rst}
.. autoclass:: kentik_api.gen.flow_tag.models.OrderDirection
   :members:
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.flow_tag.models.OrderField
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.flow_tag.models.SearchFlowTagResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.flow_tag.models.UpdateFlowTagResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.flow_tag.models.protobufAny
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.flow_tag.models.rpcStatus
```
