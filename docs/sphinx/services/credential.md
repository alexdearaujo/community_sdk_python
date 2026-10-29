<!-- AUTO-GENERATED: scripts/generation/endpoint_docs.py, render_endpoint_docs() -->
<!-- Rebuilt on every `uv run poe generate`. Do not edit by hand. -->

# Credential Service

## Overview

```mermaid
flowchart LR
    subgraph sdk["kentik_api"]
        KA["KentikAPI"]
        W["CredentialServiceWrapper\nclient.credential"]
        REST["REST functions\ngen/credential/services/"]
        RJ["request_json()\ncore/rest_runtime"]
        M["Models\ngen/credential/models/"]
        E["Error classes\ngen/credential/error/"]
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

### `GET` `/credential/v202407alpha1/group`

List credential groups.

Returns list of credential group information in Kentik vault.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.credential
    participant API as Kentik REST API

    C->>W: list_group()
    W->>API: GET /credential/v202407alpha1/group
    alt success
        API-->>W: ListCredentialGroupResponse (JSON)
        W-->>C: ListCredentialGroupResponse
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
    participant W as client.credential
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: list_group()
    W->>R: build_grpc_request(ListCredentialGroupRequest, arguments)
    R->>API: CredentialService/ListCredentialGroup (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: parse_grpc_response(response)
        W-->>C: ListCredentialGroupResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `ListCredentialGroupResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.credential.list_group()
```

---

### `GET` `/credential/v202407alpha1/group/{id}`

Get a credential group by id.

Returns specific credential group information in Kentik vault.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.credential
    participant API as Kentik REST API

    C->>W: get_group(id="id-example")
    W->>API: GET /credential/v202407alpha1/group/{id}
    alt success
        API-->>W: GetCredentialGroupResponse (JSON)
        W-->>C: GetCredentialGroupResponse
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
    participant W as client.credential
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: get_group(id="id-example")
    W->>R: build_grpc_request(GetCredentialGroupRequest, arguments)
    R->>API: CredentialService/GetCredentialGroup (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: parse_grpc_response(response)
        W-->>C: GetCredentialGroupResponse
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
| 200 | A successful response. | `GetCredentialGroupResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.credential.get_group(
    id="id-example",
)
```

## Data Models

<details>
<summary>Model relationships (5 of 11 models)</summary>

```mermaid
classDiagram
    class CredentialGroup
    class GetCredentialGroupResponse
    class ListCredentialGroupResponse
    class protobufAny
    class rpcStatus
    GetCredentialGroupResponse --> CredentialGroup
    ListCredentialGroupResponse --> CredentialGroup
    rpcStatus --> protobufAny
```

</details>

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.credential.models.CredentialGroup
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.credential.models.GetCredentialGroupResponse
```

```{eval-rst}
.. autoclass:: kentik_api.gen.credential.models.LandingType
   :members:
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.credential.models.ListCredentialGroupResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.credential.models.PermissionEntry
```

```{eval-rst}
.. autoclass:: kentik_api.gen.credential.models.Role
   :members:
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.credential.models.Secret
```

```{eval-rst}
.. autoclass:: kentik_api.gen.credential.models.SecretType
   :members:
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.credential.models.User
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.credential.models.protobufAny
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.credential.models.rpcStatus
```
