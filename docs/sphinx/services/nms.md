<!-- AUTO-GENERATED: scripts/generation/endpoint_docs.py, render_endpoint_docs() -->
<!-- Rebuilt on every `uv run poe generate`. Do not edit by hand. -->

# Nms Service

## Overview

```mermaid
%%{init: {"fontFamily": "ui-monospace, SFMono-Regular, Menlo, monospace", "flowchart": {"curve": "step", "nodeSpacing": 30, "rankSpacing": 70, "wrappingWidth": 400}}}%%
flowchart LR
    code("Your code"):::greenSrc
    subgraph sdk["kentik_api"]
        wrap("NmsServiceWrapper<br/>client.nms<br/>1 operations"):::orange
        rest("REST functions<br/>gen/nms/services/"):::blue
        rj("request_json()<br/>core/rest_runtime.py"):::blue
        cg("call_grpc()<br/>core/grpc_runtime.py"):::violet
    end
    grpcapi("Kentik gRPC API<br/>HTTP/2 + protobuf"):::violetSrc
    restapi("Kentik REST API<br/>HTTPS + JSON"):::blueSrc

    code -->|"method call"| wrap
    wrap -->|"Pydantic model from<br/>gen/nms/models/"| code
    wrap -->|"arguments"| rest
    rest -->|"Pydantic model"| wrap
    rest -->|"method, path, body"| rj
    rj -->|"JSON dict"| rest
    rj -->|"HTTPS request"| restapi
    restapi -->|"JSON response"| rj
    wrap -->|"proto request"| cg
    cg -->|"proto response"| wrap
    cg -->|"gRPC call"| grpcapi
    grpcapi -->|"proto response"| cg

    classDef greenSrc fill:#b2f2bb,stroke:#2f9e44,color:#2b8a3e
    classDef orange fill:#fff4e6,stroke:#e8590c,color:#d9480f
    classDef blue fill:#e7f5ff,stroke:#1971c2,color:#1864ab
    classDef blueSrc fill:#a5d8ff,stroke:#1971c2,color:#1864ab
    classDef violet fill:#f3f0ff,stroke:#7048e8,color:#5f3dc4
    classDef violetSrc fill:#d0bfff,stroke:#7048e8,color:#5f3dc4
    classDef greenSrc,orange,blue,blueSrc,violet,violetSrc stroke-width:2px,rx:10px
    style sdk fill:none,stroke:#868e96,stroke-width:2px
    linkStyle default stroke-width:2px,stroke-linecap:round,stroke-linejoin:round
```

On an error status or a failed call, the SDK raises an error class from `gen/nms/error/`, or a shared type from `kentik_api.errors`.

## Endpoints

### `GET` `/nms/v202505/metrics_schema`

#### REST call flow

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

#### gRPC call flow

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

Each arrow points from a model to a model that one of its fields holds. The label names the field.

```mermaid
classDiagram
    class GetMetricsSchemaResponse
    class MetricsSchema
    class protobufAny
    class rpcStatus
    GetMetricsSchemaResponse --> MetricsSchema : schema_
    rpcStatus --> protobufAny : details
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
