<!-- AUTO-GENERATED: scripts/generation/endpoint_docs.py, render_endpoint_docs() -->
<!-- Rebuilt on every `make generate`. Do not edit by hand. -->

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
```

## Endpoints

### `GET` `/plans/v202501alpha1`

List Plans

Returns all plans configured for the user's company.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.plan
    participant API as Kentik REST API

    C->>W: list_plans()
    W->>API: GET /plans/v202501alpha1
    alt success
        API-->>W: v202501alpha1ListPlansResponse (JSON)
        W-->>C: v202501alpha1ListPlansResponse
    else error
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

**gRPC transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.plan
    participant B as proto bridge
    participant API as Kentik gRPC API

    C->>W: list_plans()
    W->>B: ParseDict(params, ListPlansRequest)
    B->>API: list_plans (gRPC/TLS)
    alt success
        API-->>B: v202501alpha1ListPlansResponse proto
        B-->>W: MessageToDict(response)
        W-->>C: v202501alpha1ListPlansResponse
    else gRPC error
        API-->>B: gRPC status + details
        B-->>W: raise HTTPException
        W-->>C: raise HTTPException
    end
```

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `v202501alpha1ListPlansResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.plan.list_plans()
```

## Data Models

<details>
<summary>Model relationships (2 of 6 models)</summary>

```mermaid
classDiagram
    class protobufAny
    class rpcStatus
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
