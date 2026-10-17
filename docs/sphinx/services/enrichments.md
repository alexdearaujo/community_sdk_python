<!-- AUTO-GENERATED: scripts/generation/endpoint_docs.py, render_endpoint_docs() -->
<!-- Rebuilt on every `uv run poe generate`. Do not edit by hand. -->

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
    participant W as client.enrichments
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: fetch_values_by_ids(data=FetchValuesByIdsRequest(...))
    W->>R: build_grpc_request(FetchValuesByIdsRequest, arguments)
    R->>API: EnumerationsAdminService/FetchValuesByIds (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: parse_grpc_response(response)
        W-->>C: FetchValuesByIdsResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
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
from kentik_api.gen.enrichments.models import FetchValuesByIdsRequest

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
