# Pathfinder Service

## Overview

```mermaid
flowchart LR
    subgraph sdk["kentik_api"]
        KA["KentikAPI"]
        W["PathfinderServiceWrapper\nclient.pathfinder"]
        REST["REST functions\ngen/pathfinder/services/"]
        RJ["request_json()\ncore/rest_runtime"]
        M["Models\ngen/pathfinder/models/"]
        E["Error classes\ngen/pathfinder/error/"]
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

### `POST` `/pathfinder/v202505beta1/create`

Create a Pathfinder Report.

Create a pathfinder report based on configuration provided in the request.

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.pathfinder
    participant API as Kentik API

    C->>W: create_pathfinder_report(data=CreatePathfinderReportRequest(...))
    W->>API: POST /pathfinder/v202505beta1/create
    alt success
        API-->>W: CreatePathfinderReportResponse
        W-->>C: CreatePathfinderReportResponse
    else error status
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `data` | body | `CreatePathfinderReportRequest` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `CreatePathfinderReportResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.pathfinder.create_pathfinder_report(
    data=CreatePathfinderReportRequest(...),
)
```

## Data Models

<details>
<summary>Model relationships (7 of 7 models)</summary>

```mermaid
classDiagram
    class CloudProvider
    class CreatePathfinderReportRequest
    class CreatePathfinderReportResponse
    class EntityType
    class PathElement
    class protobufAny
    class rpcStatus
    CreatePathfinderReportRequest --> CloudProvider
    CreatePathfinderReportRequest --> EntityType
    CreatePathfinderReportResponse --> PathElement
    rpcStatus --> protobufAny
```

</details>

```{eval-rst}
.. autoclass:: kentik_api.gen.pathfinder.models.CloudProvider
   :members:
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.pathfinder.models.CreatePathfinderReportRequest
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.pathfinder.models.CreatePathfinderReportResponse
```

```{eval-rst}
.. autoclass:: kentik_api.gen.pathfinder.models.EntityType
   :members:
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.pathfinder.models.PathElement
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.pathfinder.models.protobufAny
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.pathfinder.models.rpcStatus
```
