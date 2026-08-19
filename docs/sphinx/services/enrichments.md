# Enrichments Service

## Overview

```mermaid
flowchart LR
    subgraph sdk["kentik_api"]
        KA["KentikAPI"]
        W["EnrichmentsServiceWrapper\nclient.enrichments"]
        REST["REST functions\ngen/enrichments/services/"]
        RJ["request_json()\ncore/rest_runtime"]
        M["Models\ngen/enrichments/models/"]
        E["Error classes\ngen/enrichments/error/"]
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

### `POST` `/enrichments/enumerations/v202601alpha1/values:fetch_by_ids`

Resolve enumeration IDs to values.

Return the string values for the supplied enumeration lookup IDs within the authenticated company. Unknown IDs are omitted from the response.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.enrichments
    participant API as Kentik REST API

    C->>W: fetch_values_by_ids(data=FetchValuesByIdsRequest(...))
    W->>API: POST /enrichments/enumerations/v202601alpha1/values:fetch_by_ids
    alt success
        API-->>W: FetchValuesByIdsResponse (JSON)
        W-->>C: FetchValuesByIdsResponse
    else error
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

**gRPC transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.enrichments
    participant B as proto bridge
    participant API as Kentik gRPC API

    C->>W: fetch_values_by_ids(data=FetchValuesByIdsRequest(...))
    W->>B: ParseDict(params, FetchValuesByIdsRequest)
    B->>API: fetch_values_by_ids (gRPC/TLS)
    alt success
        API-->>B: FetchValuesByIdsResponse proto
        B-->>W: MessageToDict(response)
        W-->>C: FetchValuesByIdsResponse
    else gRPC error
        API-->>B: gRPC status + details
        B-->>W: raise HTTPException
        W-->>C: raise HTTPException
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `data` | body | `FetchValuesByIdsRequest` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `FetchValuesByIdsResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.enrichments.fetch_values_by_ids(
    data=FetchValuesByIdsRequest(...),
)
```

## Data Models

<details>
<summary>Model relationships (4 of 4 models)</summary>

```mermaid
classDiagram
    class FetchValuesByIdsRequest
    class FetchValuesByIdsResponse
    class protobufAny
    class rpcStatus
    rpcStatus --> protobufAny
```

</details>

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.enrichments.models.FetchValuesByIdsRequest
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.enrichments.models.FetchValuesByIdsResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.enrichments.models.protobufAny
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.enrichments.models.rpcStatus
```
