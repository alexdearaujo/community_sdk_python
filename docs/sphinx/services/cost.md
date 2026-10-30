<!-- AUTO-GENERATED: scripts/generation/endpoint_docs.py, render_endpoint_docs() -->
<!-- Rebuilt on every `uv run poe generate`. Do not edit by hand. -->

# Cost Service

## Overview

```mermaid
%%{init: {"fontFamily": "ui-monospace, SFMono-Regular, Menlo, monospace", "flowchart": {"curve": "step", "nodeSpacing": 30, "rankSpacing": 70, "wrappingWidth": 400}}}%%
flowchart LR
    code("Your code"):::greenSrc
    subgraph sdk["kentik_api"]
        wrap("CostServiceWrapper<br/>client.cost<br/>3 operations"):::orange
        rest("REST functions<br/>gen/cost/services/"):::blue
        rj("request_json()<br/>core/rest_runtime.py"):::blue
        cg("call_grpc()<br/>core/grpc_runtime.py"):::violet
    end
    grpcapi("Kentik gRPC API<br/>HTTP/2 + protobuf"):::violetSrc
    restapi("Kentik REST API<br/>HTTPS + JSON"):::blueSrc

    code -->|"method call"| wrap
    wrap -->|"Pydantic model from<br/>gen/cost/models/"| code
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

On an error status or a failed call, the SDK raises an error class from `gen/cost/error/`, or a shared type from `kentik_api.errors`.

## Endpoints

### `GET` `/cost/v202308/cost/providers`

List all cost providers.

Returns list of configured cost providers.

#### REST call flow

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.cost
    participant API as Kentik REST API

    C->>W: list_providers()
    W->>API: GET /cost/v202308/cost/providers
    alt success
        API-->>W: ListCostProvidersResponse (JSON)
        W-->>C: ListCostProvidersResponse
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
    participant W as client.cost
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: list_providers()
    W->>R: build_grpc_request(ListCostProvidersRequest, arguments)
    R->>API: CostService/ListCostProviders (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: parse_grpc_response(response)
        W-->>C: ListCostProvidersResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `ListCostProvidersResponse` |
| default | An unexpected error response. | `googlerpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.cost.list_providers()
```

---

### `GET` `/cost/v202308/cost/summary`

List all cost provider summaries.

Returns list of summaries of configured cost providers.

#### REST call flow

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.cost
    participant API as Kentik REST API

    C->>W: list_provider_summaries()
    W->>API: GET /cost/v202308/cost/summary
    alt success
        API-->>W: ListCostProviderSummariesResponse (JSON)
        W-->>C: ListCostProviderSummariesResponse
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
    participant W as client.cost
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: list_provider_summaries()
    W->>R: build_grpc_request(ListCostProviderSummariesRequest, arguments)
    R->>API: CostService/ListCostProviderSummaries (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: parse_grpc_response(response)
        W-->>C: ListCostProviderSummariesResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `date` | query | `string` | No |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `ListCostProviderSummariesResponse` |
| default | An unexpected error response. | `googlerpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.cost.list_provider_summaries()
```

---

### `GET` `/cost/v202308/cost/summary/{id}`

Get cost provider summary.

Returns summary of configured cost provider.

#### REST call flow

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.cost
    participant API as Kentik REST API

    C->>W: get_provider_summary(id="id-example")
    W->>API: GET /cost/v202308/cost/summary/{id}
    alt success
        API-->>W: GetCostProviderSummaryResponse (JSON)
        W-->>C: GetCostProviderSummaryResponse
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
    participant W as client.cost
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: get_provider_summary(id="id-example")
    W->>R: build_grpc_request(GetCostProviderSummaryRequest, arguments)
    R->>API: CostService/GetCostProviderSummary (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: parse_grpc_response(response)
        W-->>C: GetCostProviderSummaryResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `id` | path | `string` | Yes |
| `date` | query | `string` | No |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `GetCostProviderSummaryResponse` |
| default | An unexpected error response. | `googlerpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.cost.get_provider_summary(
    id="id-example",
)
```

## Data Models

<details>
<summary>Model relationships (7 of 8 models)</summary>

Each arrow points from a model to a model that one of its fields holds. The label names the field.

```mermaid
classDiagram
    class CostProviderConcise
    class CostProviderSummary
    class GetCostProviderSummaryResponse
    class ListCostProviderSummariesResponse
    class ListCostProvidersResponse
    class googlerpcStatus
    class protobufAny
    GetCostProviderSummaryResponse --> CostProviderSummary : providers
    ListCostProviderSummariesResponse --> CostProviderSummary : providers
    ListCostProvidersResponse --> CostProviderConcise : providers
    googlerpcStatus --> protobufAny : details
```

</details>

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.cost.models.CostProviderConcise
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.cost.models.CostProviderSummary
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.cost.models.GetCostProviderSummaryResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.cost.models.ListCostProviderSummariesResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.cost.models.ListCostProvidersResponse
```

```{eval-rst}
.. autoclass:: kentik_api.gen.cost.models.Status
   :members:
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.cost.models.googlerpcStatus
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.cost.models.protobufAny
```
