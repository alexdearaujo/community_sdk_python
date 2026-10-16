<!-- AUTO-GENERATED: scripts/generation/endpoint_docs.py, render_endpoint_docs() -->
<!-- Rebuilt on every `make generate`. Do not edit by hand. -->

# Journeys Service

## Overview

```mermaid
flowchart LR
    subgraph sdk["kentik_api"]
        KA["KentikAPI"]
        W["JourneysServiceWrapper\nclient.journeys"]
        REST["REST functions\ngen/journeys/services/"]
        RJ["request_json()\ncore/rest_runtime"]
        M["Models\ngen/journeys/models/"]
        E["Error classes\ngen/journeys/error/"]
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

### `GET` `/journeys/v202406/GetJourneysNlq`

Journeys AI NLQ Service

Perform Natural Language (NLQ) to query object translation

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.journeys
    participant API as Kentik REST API

    C->>W: get_journeys_nlq(prompt="prompt-example")
    W->>API: GET /journeys/v202406/GetJourneysNlq
    alt success
        API-->>W: v202406GetJourneysNlqResponse (JSON)
        W-->>C: v202406GetJourneysNlqResponse
    else error
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

**gRPC transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.journeys
    participant B as proto bridge
    participant API as Kentik gRPC API

    C->>W: get_journeys_nlq(prompt="prompt-example")
    W->>B: ParseDict(params, GetJourneysNlqRequest)
    B->>API: get_journeys_nlq (gRPC/TLS)
    alt success
        API-->>B: v202406GetJourneysNlqResponse proto
        B-->>W: MessageToDict(response)
        W-->>C: v202406GetJourneysNlqResponse
    else gRPC error
        API-->>B: gRPC status + details
        B-->>W: raise HTTPException
        W-->>C: raise HTTPException
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `prompt` | query | `string` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `v202406GetJourneysNlqResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.journeys.get_journeys_nlq(
    prompt="prompt-example",
)
```

## Data Models

<details>
<summary>Model relationships (2 of 5 models)</summary>

```mermaid
classDiagram
    class protobufAny
    class rpcStatus
    rpcStatus --> protobufAny
```

</details>

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.journeys.models.GetJourneysNlqResponse
```

```{eval-rst}
.. autoclass:: kentik_api.gen.journeys.models.ResultFormat
   :members:
```

```{eval-rst}
.. autoclass:: kentik_api.gen.journeys.models.ResultType
   :members:
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.journeys.models.protobufAny
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.journeys.models.rpcStatus
```
