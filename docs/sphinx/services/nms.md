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

    C->>W: get_metrics_schema()
    W->>API: GET /nms/v202505/metrics_schema
    alt success
        API-->>W: GetMetricsSchemaResponse (JSON)
        W-->>C: GetMetricsSchemaResponse
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

    C->>W: get_metrics_schema()
    W->>R: build_grpc_request(GetMetricsSchemaRequest, arguments)
    R->>API: MetricsSchemaService/GetMetricsSchema (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: parse_grpc_response(response)
        W-->>C: GetMetricsSchemaResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `GetMetricsSchemaResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.nms.get_metrics_schema()
```

## Data Models

<details>
<summary>Model relationships (4 of 9 models)</summary>

```mermaid
classDiagram
    class GetMetricsSchemaResponse
    class MetricsSchema
    class protobufAny
    class rpcStatus
    GetMetricsSchemaResponse --> MetricsSchema
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
