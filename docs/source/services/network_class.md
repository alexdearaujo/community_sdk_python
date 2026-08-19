# Network Class Service

## Overview

```mermaid
flowchart LR
    subgraph sdk["kentik_api"]
        KA["KentikAPI"]
        W["Network ClassServiceWrapper\nclient.network_class"]
        REST["REST functions\ngen/network_class/services/"]
        RJ["request_json()\ncore/rest_runtime"]
        M["Models\ngen/network_class/models/"]
        E["Error classes\ngen/network_class/error/"]
    end
    API["Kentik API"]

    KA --> W
    W --> REST
    REST --> RJ
    REST --> M
    REST --> E
    RJ --> API

    click KA "../../../src/kentik_api/client.py"
    click W "../../../src/kentik_api/gen/network_class/services/network_class.py"
    click REST "../../../src/kentik_api/gen/network_class/services/"
    click RJ "../../../src/kentik_api/core/rest_runtime.py"
    click M "../../../src/kentik_api/gen/network_class/models/"
    click E "../../../src/kentik_api/gen/network_class/error/__init__.py"
```

## Endpoints

### `GET` `/network_class/v202109alpha1/network_class`

Get a network classification.

Returns information about a network classification for the company.

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.network_class
    participant API as Kentik API

    C->>W: network_class_get()
    W->>API: GET /network_class/v202109alpha1/network_class
    alt success
        API-->>W: GetNetworkClassResponse
        W-->>C: GetNetworkClassResponse
    else error status
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `GetNetworkClassResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

client = KentikAPI()  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.network_class.network_class_get()
```

---

### `POST` `/network_class/v202109alpha1/network_class`

Update a network classification.

Replaces the entire network classification attributes for the company.

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.network_class
    participant API as Kentik API

    C->>W: network_class_update(data=UpdateNetworkClassRequest(...))
    W->>API: POST /network_class/v202109alpha1/network_class
    alt success
        API-->>W: UpdateNetworkClassResponse
        W-->>C: UpdateNetworkClassResponse
    else error status
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `data` | body | `UpdateNetworkClassRequest` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `UpdateNetworkClassResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

client = KentikAPI()  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.network_class.network_class_update(
    data=UpdateNetworkClassRequest(...),
)
```

## Data Models

<details>
<summary>Model relationships (6 of 8 models)</summary>

```mermaid
classDiagram
    class GetNetworkClassResponse
    class NetworkClass
    class UpdateNetworkClassRequest
    class UpdateNetworkClassResponse
    class protobufAny
    class rpcStatus
    GetNetworkClassResponse --> NetworkClass
    UpdateNetworkClassRequest --> NetworkClass
    UpdateNetworkClassResponse --> NetworkClass
    rpcStatus --> protobufAny
```

</details>

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.network_class.models.CloudSubnet
```

```{eval-rst}
.. autoclass:: kentik_api.gen.network_class.models.CloudType
   :members:
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.network_class.models.GetNetworkClassResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.network_class.models.NetworkClass
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.network_class.models.UpdateNetworkClassRequest
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.network_class.models.UpdateNetworkClassResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.network_class.models.protobufAny
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.network_class.models.rpcStatus
```
