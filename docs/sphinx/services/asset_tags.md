<!-- AUTO-GENERATED: scripts/generation/endpoint_docs.py, render_endpoint_docs() -->
<!-- Rebuilt on every `make generate`. Do not edit by hand. -->

# Asset Tags Service

## Overview

```mermaid
flowchart LR
    subgraph sdk["kentik_api"]
        KA["KentikAPI"]
        W["Asset TagsServiceWrapper\nclient.asset_tags"]
        REST["REST functions\ngen/asset_tags/services/"]
        RJ["request_json()\ncore/rest_runtime"]
        M["Models\ngen/asset_tags/models/"]
        E["Error classes\ngen/asset_tags/error/"]
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

### `GET` `/asset_tags/v20260515beta1/assets/{assetType}/{assetId}/values`

Gets tag values by asset id and type.

Returns a list of tag values.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.asset_tags
    participant API as Kentik REST API

    C->>W: get_tag_values(assetType="assetType-example", assetId="assetId-example")
    W->>API: GET /asset_tags/v20260515beta1/assets/{assetType}/{assetId}/values
    alt success
        API-->>W: v20260515beta1GetTagValuesResponse (JSON)
        W-->>C: v20260515beta1GetTagValuesResponse
    else error
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

**gRPC transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.asset_tags
    participant B as proto bridge
    participant API as Kentik gRPC API

    C->>W: get_tag_values(assetType="assetType-example", assetId="assetId-example")
    W->>B: ParseDict(params, GetTagValuesRequest)
    B->>API: get_tag_values (gRPC/TLS)
    alt success
        API-->>B: v20260515beta1GetTagValuesResponse proto
        B-->>W: MessageToDict(response)
        W-->>C: v20260515beta1GetTagValuesResponse
    else gRPC error
        API-->>B: gRPC status + details
        B-->>W: raise HTTPException
        W-->>C: raise HTTPException
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `assetType` | path | `string` | Yes |
| `assetId` | path | `string` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `v20260515beta1GetTagValuesResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.asset_tags.get_tag_values(
    assetType="assetType-example",
    assetId="assetId-example",
)
```

---

### `GET` `/asset_tags/v20260515beta1/keys`

Lists all tag keys.

Returns a list of tag keys.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.asset_tags
    participant API as Kentik REST API

    C->>W: list_tag_keys()
    W->>API: GET /asset_tags/v20260515beta1/keys
    alt success
        API-->>W: v20260515beta1ListTagKeysResponse (JSON)
        W-->>C: v20260515beta1ListTagKeysResponse
    else error
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

**gRPC transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.asset_tags
    participant B as proto bridge
    participant API as Kentik gRPC API

    C->>W: list_tag_keys()
    W->>B: ParseDict(params, ListTagKeysRequest)
    B->>API: list_tag_keys (gRPC/TLS)
    alt success
        API-->>B: v20260515beta1ListTagKeysResponse proto
        B-->>W: MessageToDict(response)
        W-->>C: v20260515beta1ListTagKeysResponse
    else gRPC error
        API-->>B: gRPC status + details
        B-->>W: raise HTTPException
        W-->>C: raise HTTPException
    end
```

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `v20260515beta1ListTagKeysResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.asset_tags.list_tag_keys()
```

---

### `POST` `/asset_tags/v20260515beta1/keys`

Creates a new tag key.

Returns the created tag key.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.asset_tags
    participant API as Kentik REST API

    C->>W: create_tag_key(data=CreateTagKeyRequest(...))
    W->>API: POST /asset_tags/v20260515beta1/keys
    alt success
        API-->>W: v20260515beta1CreateTagKeyResponse (JSON)
        W-->>C: v20260515beta1CreateTagKeyResponse
    else error
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

**gRPC transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.asset_tags
    participant B as proto bridge
    participant API as Kentik gRPC API

    C->>W: create_tag_key(data=CreateTagKeyRequest(...))
    W->>B: ParseDict(params, CreateTagKeyRequest)
    B->>API: create_tag_key (gRPC/TLS)
    alt success
        API-->>B: v20260515beta1CreateTagKeyResponse proto
        B-->>W: MessageToDict(response)
        W-->>C: v20260515beta1CreateTagKeyResponse
    else gRPC error
        API-->>B: gRPC status + details
        B-->>W: raise HTTPException
        W-->>C: raise HTTPException
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `data` | body | `v20260515beta1CreateTagKeyRequest` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `v20260515beta1CreateTagKeyResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.asset_tags.create_tag_key(
    data=CreateTagKeyRequest(...),
)
```

---

### `GET` `/asset_tags/v20260515beta1/keys/{id}`

Get a single tag key by id.

Returns a single tag key.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.asset_tags
    participant API as Kentik REST API

    C->>W: get_tag_key(id="id-example")
    W->>API: GET /asset_tags/v20260515beta1/keys/{id}
    alt success
        API-->>W: v20260515beta1GetTagKeyResponse (JSON)
        W-->>C: v20260515beta1GetTagKeyResponse
    else error
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

**gRPC transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.asset_tags
    participant B as proto bridge
    participant API as Kentik gRPC API

    C->>W: get_tag_key(id="id-example")
    W->>B: ParseDict(params, GetTagKeyRequest)
    B->>API: get_tag_key (gRPC/TLS)
    alt success
        API-->>B: v20260515beta1GetTagKeyResponse proto
        B-->>W: MessageToDict(response)
        W-->>C: v20260515beta1GetTagKeyResponse
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
| 200 | A successful response. | `v20260515beta1GetTagKeyResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.asset_tags.get_tag_key(
    id="id-example",
)
```

---

### `PUT` `/asset_tags/v20260515beta1/keys/{id}`

Updates the display name of a tag key.

Returns the updated tag key.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.asset_tags
    participant API as Kentik REST API

    C->>W: update_tag_key(id="id-example", data=AssetTagsServiceUpdateTagKeyBody(...))
    W->>API: PUT /asset_tags/v20260515beta1/keys/{id}
    alt success
        API-->>W: v20260515beta1UpdateTagKeyResponse (JSON)
        W-->>C: v20260515beta1UpdateTagKeyResponse
    else error
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

**gRPC transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.asset_tags
    participant B as proto bridge
    participant API as Kentik gRPC API

    C->>W: update_tag_key(id="id-example", data=AssetTagsServiceUpdateTagKeyBody(...))
    W->>B: ParseDict(params, UpdateTagKeyRequest)
    B->>API: update_tag_key (gRPC/TLS)
    alt success
        API-->>B: v20260515beta1UpdateTagKeyResponse proto
        B-->>W: MessageToDict(response)
        W-->>C: v20260515beta1UpdateTagKeyResponse
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
| `data` | body | `AssetTagsServiceUpdateTagKeyBody` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `v20260515beta1UpdateTagKeyResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.asset_tags.update_tag_key(
    id="id-example",
    data=AssetTagsServiceUpdateTagKeyBody(...),
)
```

---

### `DELETE` `/asset_tags/v20260515beta1/keys/{id}`

Deletes a tag key by id.

Returns an empty response

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.asset_tags
    participant API as Kentik REST API

    C->>W: delete_tag_key(id="id-example")
    W->>API: DELETE /asset_tags/v20260515beta1/keys/{id}
    alt success
        API-->>W: v20260515beta1DeleteTagKeyResponse (JSON)
        W-->>C: v20260515beta1DeleteTagKeyResponse
    else error
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

**gRPC transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.asset_tags
    participant B as proto bridge
    participant API as Kentik gRPC API

    C->>W: delete_tag_key(id="id-example")
    W->>B: ParseDict(params, DeleteTagKeyRequest)
    B->>API: delete_tag_key (gRPC/TLS)
    alt success
        API-->>B: v20260515beta1DeleteTagKeyResponse proto
        B-->>W: MessageToDict(response)
        W-->>C: v20260515beta1DeleteTagKeyResponse
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
| 200 | A successful response. | `v20260515beta1DeleteTagKeyResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.asset_tags.delete_tag_key(
    id="id-example",
)
```

---

### `GET` `/asset_tags/v20260515beta1/keys/{tagId}/{assetType}/values`

Lists all tag values by id, optionally filtered by asset type.

Returns a list of tag values.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.asset_tags
    participant API as Kentik REST API

    C->>W: list_tag_values(tagId="tagId-example", assetType="assetType-example")
    W->>API: GET /asset_tags/v20260515beta1/keys/{tagId}/{assetType}/values
    alt success
        API-->>W: v20260515beta1ListTagValuesResponse (JSON)
        W-->>C: v20260515beta1ListTagValuesResponse
    else error
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

**gRPC transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.asset_tags
    participant B as proto bridge
    participant API as Kentik gRPC API

    C->>W: list_tag_values(tagId="tagId-example", assetType="assetType-example")
    W->>B: ParseDict(params, ListTagValuesRequest)
    B->>API: list_tag_values (gRPC/TLS)
    alt success
        API-->>B: v20260515beta1ListTagValuesResponse proto
        B-->>W: MessageToDict(response)
        W-->>C: v20260515beta1ListTagValuesResponse
    else gRPC error
        API-->>B: gRPC status + details
        B-->>W: raise HTTPException
        W-->>C: raise HTTPException
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `tagId` | path | `string` | Yes |
| `assetType` | path | `string` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `v20260515beta1ListTagValuesResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.asset_tags.list_tag_values(
    tagId="tagId-example",
    assetType="assetType-example",
)
```

---

### `PUT` `/asset_tags/v20260515beta1/values`

Bulk upserts a tag value for a list of asset ids of a given type.

Returns a list of tag values.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.asset_tags
    participant API as Kentik REST API

    C->>W: set_tag_values(data=SetTagValuesRequest(...))
    W->>API: PUT /asset_tags/v20260515beta1/values
    alt success
        API-->>W: v20260515beta1SetTagValuesResponse (JSON)
        W-->>C: v20260515beta1SetTagValuesResponse
    else error
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

**gRPC transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.asset_tags
    participant B as proto bridge
    participant API as Kentik gRPC API

    C->>W: set_tag_values(data=SetTagValuesRequest(...))
    W->>B: ParseDict(params, SetTagValuesRequest)
    B->>API: set_tag_values (gRPC/TLS)
    alt success
        API-->>B: v20260515beta1SetTagValuesResponse proto
        B-->>W: MessageToDict(response)
        W-->>C: v20260515beta1SetTagValuesResponse
    else gRPC error
        API-->>B: gRPC status + details
        B-->>W: raise HTTPException
        W-->>C: raise HTTPException
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `data` | body | `v20260515beta1SetTagValuesRequest` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `v20260515beta1SetTagValuesResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.asset_tags.set_tag_values(
    data=SetTagValuesRequest(...),
)
```

---

### `POST` `/asset_tags/v20260515beta1/values/delete`

Bulk deletes a tag values for a list of asset ids of a given type.

Returns an empty response.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.asset_tags
    participant API as Kentik REST API

    C->>W: delete_tag_values(data=DeleteTagValuesRequest(...))
    W->>API: POST /asset_tags/v20260515beta1/values/delete
    alt success
        API-->>W: v20260515beta1DeleteTagValuesResponse (JSON)
        W-->>C: v20260515beta1DeleteTagValuesResponse
    else error
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

**gRPC transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.asset_tags
    participant B as proto bridge
    participant API as Kentik gRPC API

    C->>W: delete_tag_values(data=DeleteTagValuesRequest(...))
    W->>B: ParseDict(params, DeleteTagValuesRequest)
    B->>API: delete_tag_values (gRPC/TLS)
    alt success
        API-->>B: v20260515beta1DeleteTagValuesResponse proto
        B-->>W: MessageToDict(response)
        W-->>C: v20260515beta1DeleteTagValuesResponse
    else gRPC error
        API-->>B: gRPC status + details
        B-->>W: raise HTTPException
        W-->>C: raise HTTPException
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `data` | body | `v20260515beta1DeleteTagValuesRequest` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `v20260515beta1DeleteTagValuesResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.asset_tags.delete_tag_values(
    data=DeleteTagValuesRequest(...),
)
```

## Data Models

<details>
<summary>Model relationships (3 of 18 models)</summary>

```mermaid
classDiagram
    class AssetTagsServiceUpdateTagKeyBody
    class protobufAny
    class rpcStatus
    rpcStatus --> protobufAny
```

</details>

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.asset_tags.models.AssetTagsServiceUpdateTagKeyBody
```

```{eval-rst}
.. autoclass:: kentik_api.gen.asset_tags.models.AssetType
   :members:
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.asset_tags.models.CreateTagKeyRequest
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.asset_tags.models.CreateTagKeyResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.asset_tags.models.DeleteTagKeyResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.asset_tags.models.DeleteTagValuesRequest
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.asset_tags.models.DeleteTagValuesResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.asset_tags.models.GetTagKeyResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.asset_tags.models.GetTagValuesResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.asset_tags.models.ListTagKeysResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.asset_tags.models.ListTagValuesResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.asset_tags.models.SetTagValuesRequest
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.asset_tags.models.SetTagValuesResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.asset_tags.models.TagKey
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.asset_tags.models.TagValue
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.asset_tags.models.UpdateTagKeyResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.asset_tags.models.protobufAny
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.asset_tags.models.rpcStatus
```
