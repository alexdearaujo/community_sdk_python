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

    C->>W: list()
    W->>API: GET /plans/v202501alpha1
    alt success
        API-->>W: ListPlansResponse (JSON)
        W-->>C: ListPlansResponse
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
    participant W as client.plan
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: list()
    W->>R: build_grpc_request(ListPlansRequest, arguments)
    R->>API: PlanService/ListPlans (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: parse_grpc_response(response)
        W-->>C: ListPlansResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
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

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.plan.list()
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
