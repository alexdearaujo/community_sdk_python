# Plan Service

## Overview

```mermaid
flowchart LR
    Client["client.plan"]
    RJ["request_json()"]
    OK["success: response model"]
    ERR["per-operation error class"]
    Client --> G0["PlanService (1 op)"]
    G0 --> RJ
    RJ --> OK
    RJ -->|"error status"| ERR
```

## Endpoints

### `GET` `/plans/v202501alpha1`

List Plans

Returns all plans configured for the user's company.

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
