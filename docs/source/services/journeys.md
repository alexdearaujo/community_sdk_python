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

    click KA "src/kentik_api/client.py"
    click W "src/kentik_api/gen/journeys/services/journeys.py"
    click REST "src/kentik_api/gen/journeys/services"
    click RJ "src/kentik_api/core/rest_runtime.py"
    click M "src/kentik_api/gen/journeys/models"
    click E "src/kentik_api/gen/journeys/error/__init__.py"
```

## Endpoints

### `GET` `/journeys/v202406/GetJourneysNlq`

Journeys AI NLQ Service

Perform Natural Language (NLQ) to query object translation

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.journeys
    participant API as Kentik API

    C->>W: get_journeys_nlq(prompt="prompt-example")
    W->>API: GET /journeys/v202406/GetJourneysNlq
    alt success
        API-->>W: GetJourneysNlqResponse
        W-->>C: GetJourneysNlqResponse
    else error status
        API-->>W: error body
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
| 200 | A successful response. | `GetJourneysNlqResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

client = KentikAPI()  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.journeys.get_journeys_nlq(
    prompt="prompt-example",
)
```

## Data Models

<details>
<summary>Model relationships (5 of 5 models)</summary>

```mermaid
classDiagram
    class GetJourneysNlqResponse
    class ResultFormat
    class ResultType
    class protobufAny
    class rpcStatus
    GetJourneysNlqResponse --> ResultFormat
    GetJourneysNlqResponse --> ResultType
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
