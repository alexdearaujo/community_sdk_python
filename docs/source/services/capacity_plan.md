# Capacity Plan Service

## Overview

```mermaid
flowchart LR
    subgraph sdk["kentik_api"]
        KA["KentikAPI"]
        W["Capacity PlanServiceWrapper\nclient.capacity_plan"]
        REST["REST functions\ngen/capacity_plan/services/"]
        RJ["request_json()\ncore/rest_runtime"]
        M["Models\ngen/capacity_plan/models/"]
        E["Error classes\ngen/capacity_plan/error/"]
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

### `GET` `/capacity_plan/v202212/capacity_plan`

List all capacity plans.

Returns list of capacity plans.

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.capacity_plan
    participant API as Kentik API

    C->>W: list_capacity_plans()
    W->>API: GET /capacity_plan/v202212/capacity_plan
    alt success
        API-->>W: ListCapacityPlansResponse
        W-->>C: ListCapacityPlansResponse
    else error status
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `ListCapacityPlansResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Use protocol="grpc" to route through gRPC instead of REST.
# See docs/source/grpc_implementation_spec.md for current gRPC status.
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.capacity_plan.list_capacity_plans()
```

---

### `GET` `/capacity_plan/v202212/capacity_plan/summary`

List all capacity summaries.

Returns list of capacity summaries.

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.capacity_plan
    participant API as Kentik API

    C->>W: list_capacity_summaries()
    W->>API: GET /capacity_plan/v202212/capacity_plan/summary
    alt success
        API-->>W: ListCapacitySummariesResponse
        W-->>C: ListCapacitySummariesResponse
    else error status
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `ListCapacitySummariesResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Use protocol="grpc" to route through gRPC instead of REST.
# See docs/source/grpc_implementation_spec.md for current gRPC status.
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.capacity_plan.list_capacity_summaries()
```

---

### `GET` `/capacity_plan/v202212/capacity_plan/{id}`

Retrieve capacity plan.

Returns capacity plan specified by ID.

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.capacity_plan
    participant API as Kentik API

    C->>W: get_capacity_plan(id="id-example")
    W->>API: GET /capacity_plan/v202212/capacity_plan/{id}
    alt success
        API-->>W: GetCapacityPlanResponse
        W-->>C: GetCapacityPlanResponse
    else error status
        API-->>W: error body
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
| 200 | A successful response. | `GetCapacityPlanResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Use protocol="grpc" to route through gRPC instead of REST.
# See docs/source/grpc_implementation_spec.md for current gRPC status.
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.capacity_plan.get_capacity_plan(
    id="id-example",
)
```

---

### `GET` `/capacity_plan/v202212/capacity_plan/{id}/summary`

Retrieve capacity plan summary.

Returns capacity plan summary specified by ID.

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.capacity_plan
    participant API as Kentik API

    C->>W: get_capacity_summary(id="id-example")
    W->>API: GET /capacity_plan/v202212/capacity_plan/{id}/summary
    alt success
        API-->>W: GetCapacitySummaryResponse
        W-->>C: GetCapacitySummaryResponse
    else error status
        API-->>W: error body
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
| 200 | A successful response. | `GetCapacitySummaryResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Use protocol="grpc" to route through gRPC instead of REST.
# See docs/source/grpc_implementation_spec.md for current gRPC status.
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.capacity_plan.get_capacity_summary(
    id="id-example",
)
```

## Data Models

<details>
<summary>Model relationships (8 of 17 models)</summary>

```mermaid
classDiagram
    class CapacityPlan
    class CapacitySummary
    class GetCapacityPlanResponse
    class GetCapacitySummaryResponse
    class ListCapacityPlansResponse
    class ListCapacitySummariesResponse
    class protobufAny
    class rpcStatus
    GetCapacityPlanResponse --> CapacityPlan
    GetCapacitySummaryResponse --> CapacitySummary
    ListCapacityPlansResponse --> CapacityPlan
    ListCapacitySummariesResponse --> CapacitySummary
    rpcStatus --> protobufAny
```

</details>

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.capacity_plan.models.CapacityPlan
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.capacity_plan.models.CapacityPlanInterfaceDetail
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.capacity_plan.models.CapacitySummary
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.capacity_plan.models.CapacitySummaryInterfacesDetail
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.capacity_plan.models.Config
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.capacity_plan.models.ConfigRunoutConfig
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.capacity_plan.models.ConfigUtilConfig
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.capacity_plan.models.GetCapacityPlanResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.capacity_plan.models.GetCapacitySummaryResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.capacity_plan.models.InterfacesDetailStatusDetail
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.capacity_plan.models.ListCapacityPlansResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.capacity_plan.models.ListCapacitySummariesResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.capacity_plan.models.SummaryStatus
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.capacity_plan.models.SummaryStatusRunoutStatus
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.capacity_plan.models.SummaryStatusUtilStatus
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.capacity_plan.models.protobufAny
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.capacity_plan.models.rpcStatus
```
