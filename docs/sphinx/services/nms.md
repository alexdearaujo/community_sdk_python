<!-- AUTO-GENERATED: scripts/generation/endpoint_docs.py, render_endpoint_docs() -->
<!-- Rebuilt on every `make generate`. Do not edit by hand. -->

# Nms Service

## Overview

```mermaid
flowchart LR
    subgraph sdk["kentik_api"]
        KA["KentikAPI"]
        W["NmsServiceWrapper\nclient.nms"]
        REST["REST functions\ngen/nms/services/"]
        RJ["request_json()\ncore/rest_runtime"]
        M["Models\ngen/nms/models/"]
        E["Error classes\ngen/nms/error/"]
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

### `GET` `/nms/v202505/metrics_schema`

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.nms
    participant API as Kentik REST API

    C->>W: metrics_schema_service__get_metrics_schema()
    W->>API: GET /nms/v202505/metrics_schema
    alt success
        API-->>W: v202505GetMetricsSchemaResponse (JSON)
        W-->>C: v202505GetMetricsSchemaResponse
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
    participant W as client.nms
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: metrics_schema_service__get_metrics_schema()
    W->>R: build_grpc_request(GetMetricsSchemaRequest, arguments)
    R->>API: MetricsSchemaService/GetMetricsSchema (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: MessageToDict(response)
        W-->>C: v202505GetMetricsSchemaResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `v202505GetMetricsSchemaResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.nms.metrics_schema_service__get_metrics_schema()
```

## Data Models

<details>
<summary>Model relationships (2 of 9 models)</summary>

```mermaid
classDiagram
    class protobufAny
    class rpcStatus
    rpcStatus --> protobufAny
```

</details>

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.nms.models.FieldDisplay
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.nms.models.FieldSchema
```

```{eval-rst}
.. autoclass:: kentik_api.gen.nms.models.FieldType
   :members:
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.nms.models.GetMetricsSchemaResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.nms.models.MeasurementSchema
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.nms.models.MetricsSchema
```

```{eval-rst}
.. autoclass:: kentik_api.gen.nms.models.Usage
   :members:
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.nms.models.protobufAny
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.nms.models.rpcStatus
```
