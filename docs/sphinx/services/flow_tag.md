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

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.flow_tag
    participant API as Kentik API

    C->>W: search_flow_tag()
    W->>API: GET /flow_tag/v202404alpha1/tag
    alt success
        API-->>W: SearchFlowTagResponse
        W-->>C: SearchFlowTagResponse
    else error status
        API-->>W: error body
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
| 200 | A successful response. | `SearchFlowTagResponse` |
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

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.flow_tag
    participant API as Kentik API

    C->>W: create_flow_tag(data=CreateFlowTagRequest(...))
    W->>API: POST /flow_tag/v202404alpha1/tag
    alt success
        API-->>W: CreateFlowTagResponse
        W-->>C: CreateFlowTagResponse
    else error status
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `data` | body | `CreateFlowTagRequest` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `CreateFlowTagResponse` |
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

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.flow_tag
    participant API as Kentik API

    C->>W: get_flow_tag(flowTagid="flowTagid-example")
    W->>API: GET /flow_tag/v202404alpha1/tag/{flowTag.id}
    alt success
        API-->>W: GetFlowTagResponse
        W-->>C: GetFlowTagResponse
    else error status
        API-->>W: error body
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
| 200 | A successful response. | `GetFlowTagResponse` |
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

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.flow_tag
    participant API as Kentik API

    C->>W: update_flow_tag(flowTagid="flowTagid-example", data=FlowTagServiceUpdateFlowTagBody(...))
    W->>API: PUT /flow_tag/v202404alpha1/tag/{flowTag.id}
    alt success
        API-->>W: UpdateFlowTagResponse
        W-->>C: UpdateFlowTagResponse
    else error status
        API-->>W: error body
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
| 200 | A successful response. | `UpdateFlowTagResponse` |
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

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.flow_tag
    participant API as Kentik API

    C->>W: delete_flow_tag(flowTagid="flowTagid-example")
    W->>API: DELETE /flow_tag/v202404alpha1/tag/{flowTag.id}
    alt success
        API-->>W: DeleteFlowTagResponse
        W-->>C: DeleteFlowTagResponse
    else error status
        API-->>W: error body
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
| 200 | A successful response. | `DeleteFlowTagResponse` |
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
<summary>Model relationships (10 of 15 models)</summary>

```mermaid
classDiagram
    class CreateFlowTagRequest
    class CreateFlowTagResponse
    class DeleteFlowTagResponse
    class FlowTag
    class FlowTagServiceUpdateFlowTagBody
    class GetFlowTagResponse
    class SearchFlowTagResponse
    class UpdateFlowTagResponse
    class protobufAny
    class rpcStatus
    CreateFlowTagRequest --> FlowTag
    CreateFlowTagResponse --> FlowTag
    GetFlowTagResponse --> FlowTag
    SearchFlowTagResponse --> FlowTag
    UpdateFlowTagResponse --> FlowTag
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
