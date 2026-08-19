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

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.as_group
    participant API as Kentik API

    C->>W: list_a_s_groups()
    W->>API: GET /as_group/v202212/as_group
    alt success
        API-->>W: ListASGroupsResponse
        W-->>C: ListASGroupsResponse
    else error status
        API-->>W: error body
        W-->>C: raise HTTPException
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
response = client.as_group.list_a_s_groups()
```

---

### `POST` `/as_group/v202212/as_group`

Configure a new AS group.

Create configuration for a new AS group. Returns the newly created configuration.

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.as_group
    participant API as Kentik API

    C->>W: create_a_s_group(data=CreateASGroupRequest(...))
    W->>API: POST /as_group/v202212/as_group
    alt success
        API-->>W: CreateASGroupResponse
        W-->>C: CreateASGroupResponse
    else error status
        API-->>W: error body
        W-->>C: raise HTTPException
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

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.as_group.create_a_s_group(
    data=CreateASGroupRequest(...),
)
```

---

### `GET` `/as_group/v202212/as_group/{asGroup.id}`

Retrieve configuration of a AS group.

Returns configuration of a AS group specified by ID.

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.as_group
    participant API as Kentik API

    C->>W: get_a_s_group(asGroupid="asGroupid-example")
    W->>API: GET /as_group/v202212/as_group/{asGroup.id}
    alt success
        API-->>W: GetASGroupResponse
        W-->>C: GetASGroupResponse
    else error status
        API-->>W: error body
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
| 200 | A successful response. | `GetASGroupResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.as_group.get_a_s_group(
    asGroupid="asGroupid-example",
)
```

---

### `PUT` `/as_group/v202212/as_group/{asGroup.id}`

Updates configuration of a AS group.

Replaces configuration of a AS group with attributes in the request. Returns the updated configuration.

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.as_group
    participant API as Kentik API

    C->>W: update_a_s_group(asGroupid="asGroupid-example", data=ASGroupServiceUpdateASGroupBody(...))
    W->>API: PUT /as_group/v202212/as_group/{asGroup.id}
    alt success
        API-->>W: UpdateASGroupResponse
        W-->>C: UpdateASGroupResponse
    else error status
        API-->>W: error body
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
| 200 | A successful response. | `UpdateASGroupResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.as_group.update_a_s_group(
    asGroupid="asGroupid-example",
    data=ASGroupServiceUpdateASGroupBody(...),
)
```

---

### `DELETE` `/as_group/v202212/as_group/{asGroup.id}`

Delete configuration of a AS group.

Deletes configuration of a AS group with specific ID.

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.as_group
    participant API as Kentik API

    C->>W: delete_a_s_group(asGroupid="asGroupid-example")
    W->>API: DELETE /as_group/v202212/as_group/{asGroup.id}
    alt success
        API-->>W: DeleteASGroupResponse
        W-->>C: DeleteASGroupResponse
    else error status
        API-->>W: error body
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
| 200 | A successful response. | `DeleteASGroupResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.as_group.delete_a_s_group(
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
