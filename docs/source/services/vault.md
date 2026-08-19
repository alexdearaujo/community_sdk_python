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

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.vault
    participant API as Kentik API

    C->>W: list_secret(names=["names-example"])
    W->>API: GET /vault/v202312alpha1/secrets
    alt success
        API-->>W: ListSecretResponse
        W-->>C: ListSecretResponse
    else error status
        API-->>W: error body
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

# Use protocol="grpc" to route through gRPC instead of REST.
# See docs/source/grpc_implementation_spec.md for current gRPC status.
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.vault.list_secret(
    names=["names-example"],
)
```

---

### `GET` `/vault/v202312alpha1/secrets/{name}`

Get a secret by name.

Returns a secret value stored in Kentik vault.

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.vault
    participant API as Kentik API

    C->>W: get_secret(name="name-example")
    W->>API: GET /vault/v202312alpha1/secrets/{name}
    alt success
        API-->>W: GetSecretResponse
        W-->>C: GetSecretResponse
    else error status
        API-->>W: error body
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

# Use protocol="grpc" to route through gRPC instead of REST.
# See docs/source/grpc_implementation_spec.md for current gRPC status.
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
