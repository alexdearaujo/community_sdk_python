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
        API-->>W: ListUsersResponse (JSON)
        W-->>C: ListUsersResponse
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
    participant W as client.user
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: list_users()
    W->>R: build_grpc_request(ListUsersRequest, arguments)
    R->>API: UserService/ListUsers (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: MessageToDict(response)
        W-->>C: ListUsersResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `ListUsersResponse` |
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
        API-->>W: CreateUserResponse (JSON)
        W-->>C: CreateUserResponse
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
    participant W as client.user
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: create_user(data=CreateUserRequest(...))
    W->>R: build_grpc_request(CreateUserRequest, arguments)
    R->>API: UserService/CreateUser (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: MessageToDict(response)
        W-->>C: CreateUserResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `data` | body | `CreateUserRequest` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `CreateUserResponse` |
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
        API-->>W: GetUserResponse (JSON)
        W-->>C: GetUserResponse
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
    participant W as client.user
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: get_user(id="id-example")
    W->>R: build_grpc_request(GetUserRequest, arguments)
    R->>API: UserService/GetUser (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: MessageToDict(response)
        W-->>C: GetUserResponse
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
| 200 | A successful response. | `GetUserResponse` |
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
        API-->>W: UpdateUserResponse (JSON)
        W-->>C: UpdateUserResponse
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
    participant W as client.user
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: update_user(id="id-example", data=UserServiceUpdateUserBody(...))
    W->>R: build_grpc_request(UpdateUserRequest, arguments)
    R->>API: UserService/UpdateUser (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: MessageToDict(response)
        W-->>C: UpdateUserResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
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
| 200 | A successful response. | `UpdateUserResponse` |
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
        API-->>W: DeleteUserResponse (JSON)
        W-->>C: DeleteUserResponse
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
    participant W as client.user
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: delete_user(id="id-example")
    W->>R: build_grpc_request(DeleteUserRequest, arguments)
    R->>API: UserService/DeleteUser (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: MessageToDict(response)
        W-->>C: DeleteUserResponse
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
| 200 | A successful response. | `DeleteUserResponse` |
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
        API-->>W: ResetActiveSessionsResponse (JSON)
        W-->>C: ResetActiveSessionsResponse
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
    participant W as client.user
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: reset_active_sessions(id="id-example")
    W->>R: build_grpc_request(ResetActiveSessionsRequest, arguments)
    R->>API: UserService/ResetActiveSessions (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: MessageToDict(response)
        W-->>C: ResetActiveSessionsResponse
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
| 200 | A successful response. | `ResetActiveSessionsResponse` |
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
        API-->>W: ResetApiTokenResponse (JSON)
        W-->>C: ResetApiTokenResponse
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
    participant W as client.user
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: reset_api_token(id="id-example")
    W->>R: build_grpc_request(ResetApiTokenRequest, arguments)
    R->>API: UserService/ResetApiToken (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: MessageToDict(response)
        W-->>C: ResetApiTokenResponse
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
| 200 | A successful response. | `ResetApiTokenResponse` |
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
<summary>Model relationships (12 of 15 models)</summary>

```mermaid
classDiagram
    class CreateUserRequest
    class CreateUserResponse
    class DeleteUserResponse
    class GetUserResponse
    class ListUsersResponse
    class ResetActiveSessionsResponse
    class ResetApiTokenResponse
    class UpdateUserResponse
    class User
    class UserServiceUpdateUserBody
    class protobufAny
    class rpcStatus
    CreateUserRequest --> User
    CreateUserResponse --> User
    GetUserResponse --> User
    ListUsersResponse --> User
    UpdateUserResponse --> User
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
