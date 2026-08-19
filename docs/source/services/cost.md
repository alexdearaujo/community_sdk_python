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

    click KA "../../../src/kentik_api/client.py"
    click W "../../../src/kentik_api/gen/cost/services/cost.py"
    click REST "../../../src/kentik_api/gen/cost/services/"
    click RJ "../../../src/kentik_api/core/rest_runtime.py"
    click M "../../../src/kentik_api/gen/cost/models/"
    click E "../../../src/kentik_api/gen/cost/error/__init__.py"
```

## Endpoints

### `GET` `/cost/v202308/cost/providers`

List all cost providers.

Returns list of configured cost providers.

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.cost
    participant API as Kentik API

    C->>W: list_cost_providers()
    W->>API: GET /cost/v202308/cost/providers
    alt success
        API-->>W: ListCostProvidersResponse
        W-->>C: ListCostProvidersResponse
    else error status
        API-->>W: error body
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

client = KentikAPI()  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.cost.list_cost_providers()
```

---

### `GET` `/cost/v202308/cost/summary`

List all cost provider summaries.

Returns list of summaries of configured cost providers.

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.cost
    participant API as Kentik API

    C->>W: list_cost_provider_summaries()
    W->>API: GET /cost/v202308/cost/summary
    alt success
        API-->>W: ListCostProviderSummariesResponse
        W-->>C: ListCostProviderSummariesResponse
    else error status
        API-->>W: error body
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

client = KentikAPI()  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.cost.list_cost_provider_summaries()
```

---

### `GET` `/cost/v202308/cost/summary/{id}`

Get cost provider summary.

Returns summary of configured cost provider.

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.cost
    participant API as Kentik API

    C->>W: get_cost_provider_summary(id="id-example")
    W->>API: GET /cost/v202308/cost/summary/{id}
    alt success
        API-->>W: GetCostProviderSummaryResponse
        W-->>C: GetCostProviderSummaryResponse
    else error status
        API-->>W: error body
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

client = KentikAPI()  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
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
