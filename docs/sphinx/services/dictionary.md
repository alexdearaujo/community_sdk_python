<!-- AUTO-GENERATED: scripts/generation/endpoint_docs.py, render_endpoint_docs() -->
<!-- Rebuilt on every `make generate`. Do not edit by hand. -->

# Dictionary Service

## Overview

```mermaid
flowchart LR
    subgraph sdk["kentik_api"]
        KA["KentikAPI"]
        W["DictionaryServiceWrapper\nclient.dictionary"]
        REST["REST functions\ngen/dictionary/services/"]
        RJ["request_json()\ncore/rest_runtime"]
        M["Models\ngen/dictionary/models/"]
        E["Error classes\ngen/dictionary/error/"]
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

### `GET` `/dictionary/v20260604alpha1`

Get Dictionary

Returns the full UDE dictionary for the authenticated company, including all measurements with their dimension and metric fields, operator sets, and metric family definitions.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.dictionary
    participant API as Kentik REST API

    C->>W: get_dictionary()
    W->>API: GET /dictionary/v20260604alpha1
    alt success
        API-->>W: v20260604alpha1GetDictionaryResponse (JSON)
        W-->>C: v20260604alpha1GetDictionaryResponse
    else error
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

**gRPC transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.dictionary
    participant B as proto bridge
    participant API as Kentik gRPC API

    C->>W: get_dictionary()
    W->>B: ParseDict(params, GetDictionaryRequest)
    B->>API: get_dictionary (gRPC/TLS)
    alt success
        API-->>B: v20260604alpha1GetDictionaryResponse proto
        B-->>W: MessageToDict(response)
        W-->>C: v20260604alpha1GetDictionaryResponse
    else gRPC error
        API-->>B: gRPC status + details
        B-->>W: raise HTTPException
        W-->>C: raise HTTPException
    end
```

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `v20260604alpha1GetDictionaryResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.dictionary.get_dictionary()
```

## Data Models

<details>
<summary>Model relationships (2 of 15 models)</summary>

```mermaid
classDiagram
    class protobufAny
    class rpcStatus
    rpcStatus --> protobufAny
```

</details>

```{eval-rst}
.. autoclass:: kentik_api.gen.dictionary.models.BaseUnit
   :members:
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.dictionary.models.DimensionField
```

```{eval-rst}
.. autoclass:: kentik_api.gen.dictionary.models.FieldDataType
   :members:
```

```{eval-rst}
.. autoclass:: kentik_api.gen.dictionary.models.FieldDirection
   :members:
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.dictionary.models.GetDictionaryResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.dictionary.models.MeasurementDetail
```

```{eval-rst}
.. autoclass:: kentik_api.gen.dictionary.models.MeasurementFamily
   :members:
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.dictionary.models.MetricFamilyDef
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.dictionary.models.MetricField
```

```{eval-rst}
.. autoclass:: kentik_api.gen.dictionary.models.MetricQuantity
   :members:
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.dictionary.models.Operator
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.dictionary.models.OperatorSet
```

```{eval-rst}
.. autoclass:: kentik_api.gen.dictionary.models.OperatorSetKey
   :members:
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.dictionary.models.protobufAny
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.dictionary.models.rpcStatus
```
