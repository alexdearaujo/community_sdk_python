<!-- AUTO-GENERATED: scripts/generation/endpoint_docs.py, render_endpoint_docs() -->
<!-- Rebuilt on every `make generate`. Do not edit by hand. -->

# Connectivity Checker Service

## Overview

```mermaid
flowchart LR
    subgraph sdk["kentik_api"]
        KA["KentikAPI"]
        W["Connectivity CheckerServiceWrapper\nclient.connectivity_checker"]
        REST["REST functions\ngen/connectivity_checker/services/"]
        RJ["request_json()\ncore/rest_runtime"]
        M["Models\ngen/connectivity_checker/models/"]
        E["Error classes\ngen/connectivity_checker/error/"]
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

### `POST` `/connectivity_checker/v202410beta1/create`

Create a Connectivity Checker Report.

Create a connectivity checker report based on configuration provided in the request.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.connectivity_checker
    participant API as Kentik REST API

    C->>W: create_connectivity_report(data=CreateConnectivityReportRequest(...))
    W->>API: POST /connectivity_checker/v202410beta1/create
    alt success
        API-->>W: v202410beta1CreateConnectivityReportResponse (JSON)
        W-->>C: v202410beta1CreateConnectivityReportResponse
    else error
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

**gRPC transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.connectivity_checker
    participant B as proto bridge
    participant API as Kentik gRPC API

    C->>W: create_connectivity_report(data=CreateConnectivityReportRequest(...))
    W->>B: ParseDict(params, CreateConnectivityReportRequest)
    B->>API: create_connectivity_report (gRPC/TLS)
    alt success
        API-->>B: v202410beta1CreateConnectivityReportResponse proto
        B-->>W: MessageToDict(response)
        W-->>C: v202410beta1CreateConnectivityReportResponse
    else gRPC error
        API-->>B: gRPC status + details
        B-->>W: raise HTTPException
        W-->>C: raise HTTPException
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `data` | body | `v202410beta1CreateConnectivityReportRequest` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `v202410beta1CreateConnectivityReportResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.connectivity_checker.create_connectivity_report(
    data=CreateConnectivityReportRequest(...),
)
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
.. autoclass:: kentik_api.gen.connectivity_checker.models.CloudProvider
   :members:
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.connectivity_checker.models.CreateConnectivityReportRequest
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.connectivity_checker.models.CreateConnectivityReportResponse
```

```{eval-rst}
.. autoclass:: kentik_api.gen.connectivity_checker.models.EntityType
   :members:
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.connectivity_checker.models.protobufAny
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.connectivity_checker.models.rpcStatus
```
