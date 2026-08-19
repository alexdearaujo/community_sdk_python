# Vault Service

## Overview

```mermaid
flowchart LR
    subgraph sdk["kentik_api"]
        KA["KentikAPI"]
        W["VaultServiceWrapper\nclient.vault"]
        REST["REST functions\ngen/vault/services/"]
        RJ["request_json()\ncore/rest_runtime"]
        M["Models\ngen/vault/models/"]
        E["Error classes\ngen/vault/error/"]
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

### `GET` `/vault/v202312alpha1/secrets`

List secrets.

Returns list of secret values stored in Kentik vault.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.vault
    participant API as Kentik REST API

    C->>W: list_secret(names=["names-example"])
    W->>API: GET /vault/v202312alpha1/secrets
    alt success
        API-->>W: ListSecretResponse (JSON)
        W-->>C: ListSecretResponse
    else error
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

**gRPC transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.vault
    participant B as proto bridge
    participant API as Kentik gRPC API

    C->>W: list_secret(names=["names-example"])
    W->>B: ParseDict(params, ListSecretRequest)
    B->>API: list_secret (gRPC/TLS)
    alt success
        API-->>B: ListSecretResponse proto
        B-->>W: MessageToDict(response)
        W-->>C: ListSecretResponse
    else gRPC error
        API-->>B: gRPC status + details
        B-->>W: raise HTTPException
        W-->>C: raise HTTPException
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `names` | query | `string[]` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `ListSecretResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.vault.list_secret(
    names=["names-example"],
)
```

---

### `GET` `/vault/v202312alpha1/secrets/{name}`

Get a secret by name.

Returns a secret value stored in Kentik vault.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.vault
    participant API as Kentik REST API

    C->>W: get_secret(name="name-example")
    W->>API: GET /vault/v202312alpha1/secrets/{name}
    alt success
        API-->>W: GetSecretResponse (JSON)
        W-->>C: GetSecretResponse
    else error
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

**gRPC transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.vault
    participant B as proto bridge
    participant API as Kentik gRPC API

    C->>W: get_secret(name="name-example")
    W->>B: ParseDict(params, GetSecretRequest)
    B->>API: get_secret (gRPC/TLS)
    alt success
        API-->>B: GetSecretResponse proto
        B-->>W: MessageToDict(response)
        W-->>C: GetSecretResponse
    else gRPC error
        API-->>B: gRPC status + details
        B-->>W: raise HTTPException
        W-->>C: raise HTTPException
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `name` | path | `string` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `GetSecretResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.vault.get_secret(
    name="name-example",
)
```

## Data Models

<details>
<summary>Model relationships (5 of 6 models)</summary>

```mermaid
classDiagram
    class GetSecretResponse
    class ListSecretResponse
    class Secret
    class protobufAny
    class rpcStatus
    GetSecretResponse --> Secret
    ListSecretResponse --> Secret
    rpcStatus --> protobufAny
```

</details>

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.vault.models.GetSecretResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.vault.models.ListSecretResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.vault.models.Secret
```

```{eval-rst}
.. autoclass:: kentik_api.gen.vault.models.SecretType
   :members:
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.vault.models.protobufAny
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.vault.models.rpcStatus
```
