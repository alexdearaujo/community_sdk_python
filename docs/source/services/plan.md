# Plan Service

## Overview

```mermaid
flowchart LR
    subgraph sdk["kentik_api"]
        KA["KentikAPI"]
        W["PlanServiceWrapper\nclient.plan"]
        REST["REST functions\ngen/plan/services/"]
        RJ["request_json()\ncore/rest_runtime"]
        M["Models\ngen/plan/models/"]
        E["Error classes\ngen/plan/error/"]
    end
    API["Kentik API"]

    KA --> W
    W --> REST
    REST --> RJ
    REST --> M
    REST --> E
    RJ --> API

    click KA "src/kentik_api/client.py"
    click W "src/kentik_api/gen/plan/services/plan.py"
    click REST "src/kentik_api/gen/plan/services"
    click RJ "src/kentik_api/core/rest_runtime.py"
    click M "src/kentik_api/gen/plan/models"
    click E "src/kentik_api/gen/plan/error/__init__.py"
```

## Endpoints

### `GET` `/plans/v202501alpha1`

List Plans

Returns all plans configured for the user's company.

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.plan
    participant API as Kentik API

    C->>W: list_plans()
    W->>API: GET /plans/v202501alpha1
    alt success
        API-->>W: ListPlansResponse
        W-->>C: ListPlansResponse
    else error status
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `ListPlansResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

client = KentikAPI()  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.plan.list_plans()
```

## Data Models

<details>
<summary>Model relationships (4 of 6 models)</summary>

```mermaid
classDiagram
    class ListPlansResponse
    class Plan
    class protobufAny
    class rpcStatus
    ListPlansResponse --> Plan
    rpcStatus --> protobufAny
```

</details>

```{eval-rst}
.. autoclass:: kentik_api.gen.plan.models.DeviceSubtype
   :members:
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.plan.models.ListPlansResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.plan.models.Plan
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.plan.models.PlanDevice
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.plan.models.protobufAny
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.plan.models.rpcStatus
```
