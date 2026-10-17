<!-- AUTO-GENERATED: scripts/generation/endpoint_docs.py, render_endpoint_docs() -->
<!-- Rebuilt on every `uv run poe generate`. Do not edit by hand. -->

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

    C->>W: list()
    W->>API: GET /as_group/v202212/as_group
    alt success
        API-->>W: ListASGroupsResponse (JSON)
        W-->>C: ListASGroupsResponse
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
    participant W as client.as_group
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: list()
    W->>R: build_grpc_request(ListASGroupsRequest, arguments)
    R->>API: ASGroupService/ListASGroups (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: parse_grpc_response(response)
        W-->>C: ListASGroupsResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `ListASGroupsResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.as_group.list()
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

    C->>W: create(data=CreateASGroupRequest(...))
    W->>API: POST /as_group/v202212/as_group
    alt success
        API-->>W: CreateASGroupResponse (JSON)
        W-->>C: CreateASGroupResponse
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
    participant W as client.as_group
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: create(data=CreateASGroupRequest(...))
    W->>R: build_grpc_request(CreateASGroupRequest, arguments)
    R->>API: ASGroupService/CreateASGroup (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: parse_grpc_response(response)
        W-->>C: CreateASGroupResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `data` | body | `CreateASGroupRequest` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `CreateASGroupResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI
from kentik_api.gen.as_group.models import CreateASGroupRequest

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.as_group.create(
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

    C->>W: get(asGroupid="asGroupid-example")
    W->>API: GET /as_group/v202212/as_group/{asGroup.id}
    alt success
        API-->>W: GetASGroupResponse (JSON)
        W-->>C: GetASGroupResponse
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
    participant W as client.as_group
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: get(asGroupid="asGroupid-example")
    W->>R: build_grpc_request(GetASGroupRequest, arguments)
    R->>API: ASGroupService/GetASGroup (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: parse_grpc_response(response)
        W-->>C: GetASGroupResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `asGroupid` | path | `string` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `GetASGroupResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.as_group.get(
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

    C->>W: update(asGroupid="asGroupid-example", data=ASGroupServiceUpdateASGroupBody(...))
    W->>API: PUT /as_group/v202212/as_group/{asGroup.id}
    alt success
        API-->>W: UpdateASGroupResponse (JSON)
        W-->>C: UpdateASGroupResponse
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
    participant W as client.as_group
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: update(asGroupid="asGroupid-example", data=ASGroupServiceUpdateASGroupBody(...))
    W->>R: build_grpc_request(UpdateASGroupRequest, arguments)
    R->>API: ASGroupService/UpdateASGroup (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: parse_grpc_response(response)
        W-->>C: UpdateASGroupResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
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
| 200 | A successful response. | `UpdateASGroupResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI
from kentik_api.gen.as_group.models import ASGroupServiceUpdateASGroupBody

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.as_group.update(
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

    C->>W: delete(asGroupid="asGroupid-example")
    W->>API: DELETE /as_group/v202212/as_group/{asGroup.id}
    alt success
        API-->>W: DeleteASGroupResponse (JSON)
        W-->>C: DeleteASGroupResponse
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
    participant W as client.as_group
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: delete(asGroupid="asGroupid-example")
    W->>R: build_grpc_request(DeleteASGroupRequest, arguments)
    R->>API: ASGroupService/DeleteASGroup (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: parse_grpc_response(response)
        W-->>C: DeleteASGroupResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `asGroupid` | path | `string` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `DeleteASGroupResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.as_group.delete(
    asGroupid="asGroupid-example",
)
```

## Data Models

<details>
<summary>Model relationships (11 of 12 models)</summary>

```mermaid
classDiagram
    class ASGroupConcise
    class ASGroupDetailed
    class ASGroupServiceUpdateASGroupBody
    class CreateASGroupRequest
    class CreateASGroupResponse
    class DeleteASGroupResponse
    class GetASGroupResponse
    class ListASGroupsResponse
    class UpdateASGroupResponse
    class protobufAny
    class rpcStatus
    CreateASGroupRequest --> ASGroupConcise
    CreateASGroupResponse --> ASGroupDetailed
    GetASGroupResponse --> ASGroupDetailed
    ListASGroupsResponse --> ASGroupDetailed
    UpdateASGroupResponse --> ASGroupDetailed
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
