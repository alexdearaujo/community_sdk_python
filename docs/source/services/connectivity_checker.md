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

    click KA "../../../src/kentik_api/client.py"
    click W "../../../src/kentik_api/gen/connectivity_checker/services/connectivity_checker.py"
    click REST "../../../src/kentik_api/gen/connectivity_checker/services/"
    click RJ "../../../src/kentik_api/core/rest_runtime.py"
    click M "../../../src/kentik_api/gen/connectivity_checker/models/"
    click E "../../../src/kentik_api/gen/connectivity_checker/error/__init__.py"
```

## Endpoints

### `POST` `/connectivity_checker/v202410beta1/create`

Create a Connectivity Checker Report.

Create a connectivity checker report based on configuration provided in the request.

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.connectivity_checker
    participant API as Kentik API

    C->>W: create_connectivity_report(data=CreateConnectivityReportRequest(...))
    W->>API: POST /connectivity_checker/v202410beta1/create
    alt success
        API-->>W: CreateConnectivityReportResponse
        W-->>C: CreateConnectivityReportResponse
    else error status
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `data` | body | `CreateConnectivityReportRequest` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `CreateConnectivityReportResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

client = KentikAPI()  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.connectivity_checker.create_connectivity_report(
    data=CreateConnectivityReportRequest(...),
)
```

## Data Models

<details>
<summary>Model relationships (6 of 6 models)</summary>

```mermaid
classDiagram
    class CloudProvider
    class CreateConnectivityReportRequest
    class CreateConnectivityReportResponse
    class EntityType
    class protobufAny
    class rpcStatus
    CreateConnectivityReportRequest --> CloudProvider
    CreateConnectivityReportRequest --> EntityType
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
