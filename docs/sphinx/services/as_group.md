<!-- AUTO-GENERATED: scripts/generation/endpoint_docs.py, _render_sphinx_stubs() -->
<!-- Rebuilt on every `make generate`. Do not edit by hand. -->

# As Group Service

## Overview

```mermaid
flowchart LR
    subgraph sdk["kentik_api"]
        KA["KentikAPI"]
        W["As GroupServiceWrapper\nclient.as_group"]
        REST["REST functions\ngen/as_group/services/"]
        RJ["request_json()\ncore/rest_runtime"]
        M["Models\ngen/as_group/models/"]
        E["Error classes\ngen/as_group/error/"]
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

### `GET` `/as_group/v202212/as_group`

List all AS groups.

Returns list of configured AS groups.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.as_group
    participant API as Kentik REST API

    C->>W: list_as_groups()
    W->>API: GET /as_group/v202212/as_group
    alt success
        API-->>W: v202212ListASGroupsResponse (JSON)
        W-->>C: v202212ListASGroupsResponse
    else error
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

**gRPC transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.as_group
    participant B as proto bridge
    participant API as Kentik gRPC API

    C->>W: list_as_groups()
    W->>B: ParseDict(params, ListASGroupsRequest)
    B->>API: list_as_groups (gRPC/TLS)
    alt success
        API-->>B: v202212ListASGroupsResponse proto
        B-->>W: MessageToDict(response)
        W-->>C: v202212ListASGroupsResponse
    else gRPC error
        API-->>B: gRPC status + details
        B-->>W: raise HTTPException
        W-->>C: raise HTTPException
    end
```

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `v202212ListASGroupsResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.as_group.list_as_groups()
```

---

### `POST` `/as_group/v202212/as_group`

Configure a new AS group.

Create configuration for a new AS group. Returns the newly created configuration.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.as_group
    participant API as Kentik REST API

    C->>W: create_as_group(data=CreateASGroupRequest(...))
    W->>API: POST /as_group/v202212/as_group
    alt success
        API-->>W: v202212CreateASGroupResponse (JSON)
        W-->>C: v202212CreateASGroupResponse
    else error
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

**gRPC transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.as_group
    participant B as proto bridge
    participant API as Kentik gRPC API

    C->>W: create_as_group(data=CreateASGroupRequest(...))
    W->>B: ParseDict(params, CreateASGroupRequest)
    B->>API: create_as_group (gRPC/TLS)
    alt success
        API-->>B: v202212CreateASGroupResponse proto
        B-->>W: MessageToDict(response)
        W-->>C: v202212CreateASGroupResponse
    else gRPC error
        API-->>B: gRPC status + details
        B-->>W: raise HTTPException
        W-->>C: raise HTTPException
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `data` | body | `v202212CreateASGroupRequest` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `v202212CreateASGroupResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.as_group.create_as_group(
    data=CreateASGroupRequest(...),
)
```

---

### `GET` `/as_group/v202212/as_group/{asGroup.id}`

Retrieve configuration of a AS group.

Returns configuration of a AS group specified by ID.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.as_group
    participant API as Kentik REST API

    C->>W: get_as_group(asGroupid="asGroupid-example")
    W->>API: GET /as_group/v202212/as_group/{asGroup.id}
    alt success
        API-->>W: v202212GetASGroupResponse (JSON)
        W-->>C: v202212GetASGroupResponse
    else error
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

**gRPC transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.as_group
    participant B as proto bridge
    participant API as Kentik gRPC API

    C->>W: get_as_group(asGroupid="asGroupid-example")
    W->>B: ParseDict(params, GetASGroupRequest)
    B->>API: get_as_group (gRPC/TLS)
    alt success
        API-->>B: v202212GetASGroupResponse proto
        B-->>W: MessageToDict(response)
        W-->>C: v202212GetASGroupResponse
    else gRPC error
        API-->>B: gRPC status + details
        B-->>W: raise HTTPException
        W-->>C: raise HTTPException
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `asGroupid` | path | `string` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `v202212GetASGroupResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.as_group.get_as_group(
    asGroupid="asGroupid-example",
)
```

---

### `PUT` `/as_group/v202212/as_group/{asGroup.id}`

Updates configuration of a AS group.

Replaces configuration of a AS group with attributes in the request. Returns the updated configuration.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.as_group
    participant API as Kentik REST API

    C->>W: update_as_group(asGroupid="asGroupid-example", data=ASGroupServiceUpdateASGroupBody(...))
    W->>API: PUT /as_group/v202212/as_group/{asGroup.id}
    alt success
        API-->>W: v202212UpdateASGroupResponse (JSON)
        W-->>C: v202212UpdateASGroupResponse
    else error
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

**gRPC transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.as_group
    participant B as proto bridge
    participant API as Kentik gRPC API

    C->>W: update_as_group(asGroupid="asGroupid-example", data=ASGroupServiceUpdateASGroupBody(...))
    W->>B: ParseDict(params, UpdateASGroupRequest)
    B->>API: update_as_group (gRPC/TLS)
    alt success
        API-->>B: v202212UpdateASGroupResponse proto
        B-->>W: MessageToDict(response)
        W-->>C: v202212UpdateASGroupResponse
    else gRPC error
        API-->>B: gRPC status + details
        B-->>W: raise HTTPException
        W-->>C: raise HTTPException
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `asGroupid` | path | `string` | Yes |
| `data` | body | `ASGroupServiceUpdateASGroupBody` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `v202212UpdateASGroupResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.as_group.update_as_group(
    asGroupid="asGroupid-example",
    data=ASGroupServiceUpdateASGroupBody(...),
)
```

---

### `DELETE` `/as_group/v202212/as_group/{asGroup.id}`

Delete configuration of a AS group.

Deletes configuration of a AS group with specific ID.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.as_group
    participant API as Kentik REST API

    C->>W: delete_as_group(asGroupid="asGroupid-example")
    W->>API: DELETE /as_group/v202212/as_group/{asGroup.id}
    alt success
        API-->>W: v202212DeleteASGroupResponse (JSON)
        W-->>C: v202212DeleteASGroupResponse
    else error
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

**gRPC transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.as_group
    participant B as proto bridge
    participant API as Kentik gRPC API

    C->>W: delete_as_group(asGroupid="asGroupid-example")
    W->>B: ParseDict(params, DeleteASGroupRequest)
    B->>API: delete_as_group (gRPC/TLS)
    alt success
        API-->>B: v202212DeleteASGroupResponse proto
        B-->>W: MessageToDict(response)
        W-->>C: v202212DeleteASGroupResponse
    else gRPC error
        API-->>B: gRPC status + details
        B-->>W: raise HTTPException
        W-->>C: raise HTTPException
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `asGroupid` | path | `string` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `v202212DeleteASGroupResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.as_group.delete_as_group(
    asGroupid="asGroupid-example",
)
```

## Data Models

<details>
<summary>Model relationships (3 of 12 models)</summary>

```mermaid
classDiagram
    class ASGroupServiceUpdateASGroupBody
    class protobufAny
    class rpcStatus
    rpcStatus --> protobufAny
```

</details>

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.as_group.models.ASGroupConcise
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.as_group.models.ASGroupDetailed
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.as_group.models.ASGroupServiceUpdateASGroupBody
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.as_group.models.AutonomousSystem
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.as_group.models.CreateASGroupRequest
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.as_group.models.CreateASGroupResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.as_group.models.DeleteASGroupResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.as_group.models.GetASGroupResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.as_group.models.ListASGroupsResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.as_group.models.UpdateASGroupResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.as_group.models.protobufAny
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.as_group.models.rpcStatus
```
