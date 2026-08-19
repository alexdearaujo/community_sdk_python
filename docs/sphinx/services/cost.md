# Cost Service

## Overview

```mermaid
flowchart LR
    subgraph sdk["kentik_api"]
        KA["KentikAPI"]
        W["CostServiceWrapper\nclient.cost"]
        REST["REST functions\ngen/cost/services/"]
        RJ["request_json()\ncore/rest_runtime"]
        M["Models\ngen/cost/models/"]
        E["Error classes\ngen/cost/error/"]
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

### `GET` `/cost/v202308/cost/providers`

List all cost providers.

Returns list of configured cost providers.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.cost
    participant API as Kentik REST API

    C->>W: list_cost_providers()
    W->>API: GET /cost/v202308/cost/providers
    alt success
        API-->>W: ListCostProvidersResponse (JSON)
        W-->>C: ListCostProvidersResponse
    else error
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

**gRPC transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.cost
    participant B as proto bridge
    participant API as Kentik gRPC API

    C->>W: list_cost_providers()
    W->>B: ParseDict(params, ListCostProvidersRequest)
    B->>API: list_cost_providers (gRPC/TLS)
    alt success
        API-->>B: ListCostProvidersResponse proto
        B-->>W: MessageToDict(response)
        W-->>C: ListCostProvidersResponse
    else gRPC error
        API-->>B: gRPC status + details
        B-->>W: raise HTTPException
        W-->>C: raise HTTPException
    end
```

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `ListCostProvidersResponse` |
| default | An unexpected error response. | `googlerpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.cost.list_cost_providers()
```

---

### `GET` `/cost/v202308/cost/summary`

List all cost provider summaries.

Returns list of summaries of configured cost providers.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.cost
    participant API as Kentik REST API

    C->>W: list_cost_provider_summaries()
    W->>API: GET /cost/v202308/cost/summary
    alt success
        API-->>W: ListCostProviderSummariesResponse (JSON)
        W-->>C: ListCostProviderSummariesResponse
    else error
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

**gRPC transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.cost
    participant B as proto bridge
    participant API as Kentik gRPC API

    C->>W: list_cost_provider_summaries()
    W->>B: ParseDict(params, ListCostProviderSummariesRequest)
    B->>API: list_cost_provider_summaries (gRPC/TLS)
    alt success
        API-->>B: ListCostProviderSummariesResponse proto
        B-->>W: MessageToDict(response)
        W-->>C: ListCostProviderSummariesResponse
    else gRPC error
        API-->>B: gRPC status + details
        B-->>W: raise HTTPException
        W-->>C: raise HTTPException
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `date` | query | `string` | No |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `ListCostProviderSummariesResponse` |
| default | An unexpected error response. | `googlerpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.cost.list_cost_provider_summaries()
```

---

### `GET` `/cost/v202308/cost/summary/{id}`

Get cost provider summary.

Returns summary of configured cost provider.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.cost
    participant API as Kentik REST API

    C->>W: get_cost_provider_summary(id="id-example")
    W->>API: GET /cost/v202308/cost/summary/{id}
    alt success
        API-->>W: GetCostProviderSummaryResponse (JSON)
        W-->>C: GetCostProviderSummaryResponse
    else error
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

**gRPC transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.cost
    participant B as proto bridge
    participant API as Kentik gRPC API

    C->>W: get_cost_provider_summary(id="id-example")
    W->>B: ParseDict(params, GetCostProviderSummaryRequest)
    B->>API: get_cost_provider_summary (gRPC/TLS)
    alt success
        API-->>B: GetCostProviderSummaryResponse proto
        B-->>W: MessageToDict(response)
        W-->>C: GetCostProviderSummaryResponse
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
| `date` | query | `string` | No |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `GetCostProviderSummaryResponse` |
| default | An unexpected error response. | `googlerpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.cost.get_cost_provider_summary(
    id="id-example",
)
```

## Data Models

<details>
<summary>Model relationships (7 of 8 models)</summary>

```mermaid
classDiagram
    class CostProviderConcise
    class CostProviderSummary
    class GetCostProviderSummaryResponse
    class ListCostProviderSummariesResponse
    class ListCostProvidersResponse
    class googlerpcStatus
    class protobufAny
    GetCostProviderSummaryResponse --> CostProviderSummary
    ListCostProviderSummariesResponse --> CostProviderSummary
    ListCostProvidersResponse --> CostProviderConcise
    googlerpcStatus --> protobufAny
```

</details>

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.cost.models.CostProviderConcise
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.cost.models.CostProviderSummary
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.cost.models.GetCostProviderSummaryResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.cost.models.ListCostProviderSummariesResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.cost.models.ListCostProvidersResponse
```

```{eval-rst}
.. autoclass:: kentik_api.gen.cost.models.costv202308Status
   :members:
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.cost.models.googlerpcStatus
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.cost.models.protobufAny
```
