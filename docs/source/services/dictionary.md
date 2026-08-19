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

    click KA "../../../src/kentik_api/client.py"
    click W "../../../src/kentik_api/gen/dictionary/services/dictionary.py"
    click REST "../../../src/kentik_api/gen/dictionary/services/"
    click RJ "../../../src/kentik_api/core/rest_runtime.py"
    click M "../../../src/kentik_api/gen/dictionary/models/"
    click E "../../../src/kentik_api/gen/dictionary/error/__init__.py"
```

## Endpoints

### `GET` `/dictionary/v20260604alpha1`

Get Dictionary

Returns the full UDE dictionary for the authenticated company, including all measurements with their dimension and metric fields, operator sets, and metric family definitions.

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.dictionary
    participant API as Kentik API

    C->>W: get_dictionary()
    W->>API: GET /dictionary/v20260604alpha1
    alt success
        API-->>W: GetDictionaryResponse
        W-->>C: GetDictionaryResponse
    else error status
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `GetDictionaryResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

client = KentikAPI()  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.dictionary.get_dictionary()
```

## Data Models

<details>
<summary>Model relationships (6 of 15 models)</summary>

```mermaid
classDiagram
    class GetDictionaryResponse
    class MeasurementDetail
    class MetricFamilyDef
    class OperatorSet
    class protobufAny
    class rpcStatus
    GetDictionaryResponse --> MeasurementDetail
    GetDictionaryResponse --> MetricFamilyDef
    GetDictionaryResponse --> OperatorSet
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
