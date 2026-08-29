<!-- AUTO-GENERATED: scripts/generation/endpoint_docs.py, render_endpoint_docs() -->
<!-- Rebuilt on every `make generate`. Do not edit by hand. -->

# User Service

## Overview

```mermaid
flowchart LR
    subgraph sdk["kentik_api"]
        KA["KentikAPI"]
        W["UserServiceWrapper\nclient.user"]
        REST["REST functions\ngen/user/services/"]
        RJ["request_json()\ncore/rest_runtime"]
        M["Models\ngen/user/models/"]
        E["Error classes\ngen/user/error/"]
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

### `GET` `/user/v202211/users`

List all users.

Returns a list of all user accounts in the company.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.user
    participant API as Kentik REST API

    C->>W: list_users()
    W->>API: GET /user/v202211/users
    alt success
        API-->>W: v202211ListUsersResponse (JSON)
        W-->>C: v202211ListUsersResponse
    else error
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

**gRPC transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.user
    participant B as proto bridge
    participant API as Kentik gRPC API

    C->>W: list_users()
    W->>B: ParseDict(params, ListUsersRequest)
    B->>API: list_users (gRPC/TLS)
    alt success
        API-->>B: v202211ListUsersResponse proto
        B-->>W: MessageToDict(response)
        W-->>C: v202211ListUsersResponse
    else gRPC error
        API-->>B: gRPC status + details
        B-->>W: raise HTTPException
        W-->>C: raise HTTPException
    end
```

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `v202211ListUsersResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.user.list_users()
```

---

### `POST` `/user/v202211/users`

Create new user account.

Creates new user account based on attributes in the request. Returns attributes of the newly created account.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.user
    participant API as Kentik REST API

    C->>W: create_user(data=CreateUserRequest(...))
    W->>API: POST /user/v202211/users
    alt success
        API-->>W: v202211CreateUserResponse (JSON)
        W-->>C: v202211CreateUserResponse
    else error
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

**gRPC transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.user
    participant B as proto bridge
    participant API as Kentik gRPC API

    C->>W: create_user(data=CreateUserRequest(...))
    W->>B: ParseDict(params, CreateUserRequest)
    B->>API: create_user (gRPC/TLS)
    alt success
        API-->>B: v202211CreateUserResponse proto
        B-->>W: MessageToDict(response)
        W-->>C: v202211CreateUserResponse
    else gRPC error
        API-->>B: gRPC status + details
        B-->>W: raise HTTPException
        W-->>C: raise HTTPException
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `data` | body | `v202211CreateUserRequest` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `v202211CreateUserResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.user.create_user(
    data=CreateUserRequest(...),
)
```

---

### `GET` `/user/v202211/users/{id}`

Get attributes of a user account.

Returns attributes of a user account specified by ID.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.user
    participant API as Kentik REST API

    C->>W: get_user(id="id-example")
    W->>API: GET /user/v202211/users/{id}
    alt success
        API-->>W: v202211GetUserResponse (JSON)
        W-->>C: v202211GetUserResponse
    else error
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

**gRPC transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.user
    participant B as proto bridge
    participant API as Kentik gRPC API

    C->>W: get_user(id="id-example")
    W->>B: ParseDict(params, GetUserRequest)
    B->>API: get_user (gRPC/TLS)
    alt success
        API-->>B: v202211GetUserResponse proto
        B-->>W: MessageToDict(response)
        W-->>C: v202211GetUserResponse
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
| 200 | A successful response. | `v202211GetUserResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.user.get_user(
    id="id-example",
)
```

---

### `PUT` `/user/v202211/users/{id}`

Update attributes of a user account.

Replaces all attributes of a user account specified by ID with attributes in the request. Returns updated attributes.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.user
    participant API as Kentik REST API

    C->>W: update_user(id="id-example", data=UserServiceUpdateUserBody(...))
    W->>API: PUT /user/v202211/users/{id}
    alt success
        API-->>W: v202211UpdateUserResponse (JSON)
        W-->>C: v202211UpdateUserResponse
    else error
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

**gRPC transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.user
    participant B as proto bridge
    participant API as Kentik gRPC API

    C->>W: update_user(id="id-example", data=UserServiceUpdateUserBody(...))
    W->>B: ParseDict(params, UpdateUserRequest)
    B->>API: update_user (gRPC/TLS)
    alt success
        API-->>B: v202211UpdateUserResponse proto
        B-->>W: MessageToDict(response)
        W-->>C: v202211UpdateUserResponse
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
| `data` | body | `UserServiceUpdateUserBody` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `v202211UpdateUserResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.user.update_user(
    id="id-example",
    data=UserServiceUpdateUserBody(...),
)
```

---

### `DELETE` `/user/v202211/users/{id}`

Delete a user account.

Deletes user account specified by ID.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.user
    participant API as Kentik REST API

    C->>W: delete_user(id="id-example")
    W->>API: DELETE /user/v202211/users/{id}
    alt success
        API-->>W: v202211DeleteUserResponse (JSON)
        W-->>C: v202211DeleteUserResponse
    else error
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

**gRPC transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.user
    participant B as proto bridge
    participant API as Kentik gRPC API

    C->>W: delete_user(id="id-example")
    W->>B: ParseDict(params, DeleteUserRequest)
    B->>API: delete_user (gRPC/TLS)
    alt success
        API-->>B: v202211DeleteUserResponse proto
        B-->>W: MessageToDict(response)
        W-->>C: v202211DeleteUserResponse
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
| 200 | A successful response. | `v202211DeleteUserResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.user.delete_user(
    id="id-example",
)
```

---

### `PUT` `/user/v202211/users/{id}/reset_active_sessions`

Resets active sessions for a user.

Resets active sessions for a user specified by ID.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.user
    participant API as Kentik REST API

    C->>W: reset_active_sessions(id="id-example")
    W->>API: PUT /user/v202211/users/{id}/reset_active_sessions
    alt success
        API-->>W: v202211ResetActiveSessionsResponse (JSON)
        W-->>C: v202211ResetActiveSessionsResponse
    else error
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

**gRPC transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.user
    participant B as proto bridge
    participant API as Kentik gRPC API

    C->>W: reset_active_sessions(id="id-example")
    W->>B: ParseDict(params, ResetActiveSessionsRequest)
    B->>API: reset_active_sessions (gRPC/TLS)
    alt success
        API-->>B: v202211ResetActiveSessionsResponse proto
        B-->>W: MessageToDict(response)
        W-->>C: v202211ResetActiveSessionsResponse
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
| 200 | A successful response. | `v202211ResetActiveSessionsResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.user.reset_active_sessions(
    id="id-example",
)
```

---

### `PUT` `/user/v202211/users/{id}/reset_api_token`

Reset API token for a user.

Resets API token for a user specified by ID.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.user
    participant API as Kentik REST API

    C->>W: reset_api_token(id="id-example")
    W->>API: PUT /user/v202211/users/{id}/reset_api_token
    alt success
        API-->>W: v202211ResetApiTokenResponse (JSON)
        W-->>C: v202211ResetApiTokenResponse
    else error
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

**gRPC transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.user
    participant B as proto bridge
    participant API as Kentik gRPC API

    C->>W: reset_api_token(id="id-example")
    W->>B: ParseDict(params, ResetApiTokenRequest)
    B->>API: reset_api_token (gRPC/TLS)
    alt success
        API-->>B: v202211ResetApiTokenResponse proto
        B-->>W: MessageToDict(response)
        W-->>C: v202211ResetApiTokenResponse
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
| 200 | A successful response. | `v202211ResetApiTokenResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.user.reset_api_token(
    id="id-example",
)
```

## Data Models

<details>
<summary>Model relationships (3 of 15 models)</summary>

```mermaid
classDiagram
    class UserServiceUpdateUserBody
    class protobufAny
    class rpcStatus
    rpcStatus --> protobufAny
```

</details>

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.user.models.CreateUserRequest
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.user.models.CreateUserResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.user.models.DeleteUserResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.user.models.GetUserResponse
```

```{eval-rst}
.. autoclass:: kentik_api.gen.user.models.LandingType
   :members:
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.user.models.ListUsersResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.user.models.PermissionEntry
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.user.models.ResetActiveSessionsResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.user.models.ResetApiTokenResponse
```

```{eval-rst}
.. autoclass:: kentik_api.gen.user.models.Role
   :members:
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.user.models.UpdateUserResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.user.models.User
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.user.models.UserServiceUpdateUserBody
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.user.models.protobufAny
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.user.models.rpcStatus
```
