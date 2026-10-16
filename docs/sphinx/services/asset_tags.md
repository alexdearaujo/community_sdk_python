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
        API-->>W: GetTagValuesResponse (JSON)
        W-->>C: GetTagValuesResponse
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
    participant W as client.asset_tags
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: get_tag_values(assetType="assetType-example", assetId="assetId-example")
    W->>R: build_grpc_request(GetTagValuesRequest, arguments)
    R->>API: AssetTagsService/GetTagValues (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: MessageToDict(response)
        W-->>C: GetTagValuesResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
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
| 200 | A successful response. | `GetTagValuesResponse` |
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
        API-->>W: ListTagKeysResponse (JSON)
        W-->>C: ListTagKeysResponse
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
    participant W as client.asset_tags
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: list_tag_keys()
    W->>R: build_grpc_request(ListTagKeysRequest, arguments)
    R->>API: AssetTagsService/ListTagKeys (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: MessageToDict(response)
        W-->>C: ListTagKeysResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `ListTagKeysResponse` |
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
        API-->>W: CreateTagKeyResponse (JSON)
        W-->>C: CreateTagKeyResponse
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
    participant W as client.asset_tags
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: create_tag_key(data=CreateTagKeyRequest(...))
    W->>R: build_grpc_request(CreateTagKeyRequest, arguments)
    R->>API: AssetTagsService/CreateTagKey (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: MessageToDict(response)
        W-->>C: CreateTagKeyResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `data` | body | `CreateTagKeyRequest` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `CreateTagKeyResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI
from kentik_api.gen.asset_tags.models import CreateTagKeyRequest

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
        API-->>W: GetTagKeyResponse (JSON)
        W-->>C: GetTagKeyResponse
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
    participant W as client.asset_tags
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: get_tag_key(id="id-example")
    W->>R: build_grpc_request(GetTagKeyRequest, arguments)
    R->>API: AssetTagsService/GetTagKey (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: MessageToDict(response)
        W-->>C: GetTagKeyResponse
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
| 200 | A successful response. | `GetTagKeyResponse` |
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
        API-->>W: UpdateTagKeyResponse (JSON)
        W-->>C: UpdateTagKeyResponse
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
    participant W as client.asset_tags
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: update_tag_key(id="id-example", data=AssetTagsServiceUpdateTagKeyBody(...))
    W->>R: build_grpc_request(UpdateTagKeyRequest, arguments)
    R->>API: AssetTagsService/UpdateTagKey (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: MessageToDict(response)
        W-->>C: UpdateTagKeyResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
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
| 200 | A successful response. | `UpdateTagKeyResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI
from kentik_api.gen.asset_tags.models import AssetTagsServiceUpdateTagKeyBody

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
        API-->>W: DeleteTagKeyResponse (JSON)
        W-->>C: DeleteTagKeyResponse
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
    participant W as client.asset_tags
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: delete_tag_key(id="id-example")
    W->>R: build_grpc_request(DeleteTagKeyRequest, arguments)
    R->>API: AssetTagsService/DeleteTagKey (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: MessageToDict(response)
        W-->>C: DeleteTagKeyResponse
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
| 200 | A successful response. | `DeleteTagKeyResponse` |
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
        API-->>W: ListTagValuesResponse (JSON)
        W-->>C: ListTagValuesResponse
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
    participant W as client.asset_tags
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: list_tag_values(tagId="tagId-example", assetType="assetType-example")
    W->>R: build_grpc_request(ListTagValuesRequest, arguments)
    R->>API: AssetTagsService/ListTagValues (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: MessageToDict(response)
        W-->>C: ListTagValuesResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
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
| 200 | A successful response. | `ListTagValuesResponse` |
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
        API-->>W: SetTagValuesResponse (JSON)
        W-->>C: SetTagValuesResponse
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
    participant W as client.asset_tags
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: set_tag_values(data=SetTagValuesRequest(...))
    W->>R: build_grpc_request(SetTagValuesRequest, arguments)
    R->>API: AssetTagsService/SetTagValues (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: MessageToDict(response)
        W-->>C: SetTagValuesResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `data` | body | `SetTagValuesRequest` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `SetTagValuesResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI
from kentik_api.gen.asset_tags.models import SetTagValuesRequest

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
        API-->>W: DeleteTagValuesResponse (JSON)
        W-->>C: DeleteTagValuesResponse
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
    participant W as client.asset_tags
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: delete_tag_values(data=DeleteTagValuesRequest(...))
    W->>R: build_grpc_request(DeleteTagValuesRequest, arguments)
    R->>API: AssetTagsService/DeleteTagValues (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: MessageToDict(response)
        W-->>C: DeleteTagValuesResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `data` | body | `DeleteTagValuesRequest` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `DeleteTagValuesResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI
from kentik_api.gen.asset_tags.models import DeleteTagValuesRequest

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.asset_tags.delete_tag_values(
    data=DeleteTagValuesRequest(...),
)
```

## Data Models

<details>
<summary>Model relationships (18 of 18 models)</summary>

```mermaid
classDiagram
    class AssetTagsServiceUpdateTagKeyBody
    class AssetType
    class CreateTagKeyRequest
    class CreateTagKeyResponse
    class DeleteTagKeyResponse
    class DeleteTagValuesRequest
    class DeleteTagValuesResponse
    class GetTagKeyResponse
    class GetTagValuesResponse
    class ListTagKeysResponse
    class ListTagValuesResponse
    class SetTagValuesRequest
    class SetTagValuesResponse
    class TagKey
    class TagValue
    class UpdateTagKeyResponse
    class protobufAny
    class rpcStatus
    CreateTagKeyResponse --> TagKey
    DeleteTagValuesRequest --> AssetType
    GetTagKeyResponse --> TagKey
    GetTagValuesResponse --> TagValue
    ListTagKeysResponse --> TagKey
    ListTagValuesResponse --> TagValue
    SetTagValuesRequest --> AssetType
    SetTagValuesResponse --> TagValue
    TagValue --> AssetType
    UpdateTagKeyResponse --> TagKey
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
