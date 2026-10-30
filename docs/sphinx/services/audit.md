<!-- AUTO-GENERATED: scripts/generation/endpoint_docs.py, render_endpoint_docs() -->
<!-- Rebuilt on every `uv run poe generate`. Do not edit by hand. -->

# Audit Service

## Overview

```mermaid
%%{init: {"fontFamily": "ui-monospace, SFMono-Regular, Menlo, monospace", "flowchart": {"curve": "step", "nodeSpacing": 30, "rankSpacing": 70, "wrappingWidth": 400}}}%%
flowchart LR
    code("Your code"):::greenSrc
    subgraph sdk["kentik_api"]
        wrap("AuditServiceWrapper<br/>client.audit<br/>3 operations"):::orange
        rest("REST functions<br/>gen/audit/services/"):::blue
        rj("request_json()<br/>core/rest_runtime.py"):::blue
        cg("call_grpc()<br/>core/grpc_runtime.py"):::violet
    end
    grpcapi("Kentik gRPC API<br/>HTTP/2 + protobuf"):::violetSrc
    restapi("Kentik REST API<br/>HTTPS + JSON"):::blueSrc

    code -->|"method call"| wrap
    wrap -->|"Pydantic model from<br/>gen/audit/models/"| code
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

On an error status or a failed call, the SDK raises an error class from `gen/audit/error/`, or a shared type from `kentik_api.errors`.

## Endpoints

### `GET` `/audit/v202601/events`

List Audit Events.

Returns a list of audit events.

#### REST call flow

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.audit
    participant API as Kentik REST API

    C->>W: list_events()
    W->>API: GET /audit/v202601/events
    alt success
        API-->>W: ListAuditEventsResponse (JSON)
        W-->>C: ListAuditEventsResponse
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
    participant W as client.audit
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: list_events()
    W->>R: build_grpc_request(ListAuditEventsRequest, arguments)
    R->>API: AuditService/ListAuditEvents (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: parse_grpc_response(response)
        W-->>C: ListAuditEventsResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `startTime` | query | `string` | No |
| `endTime` | query | `string` | No |
| `offset` | query | `string (uint64)` | No |
| `limit` | query | `string (uint64)` | No |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `ListAuditEventsResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.audit.list_events()
```

---

### `GET` `/audit/v202601/events/{id}`

Get an Audit Event

Return a specific audit event.

#### REST call flow

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.audit
    participant API as Kentik REST API

    C->>W: get_event(id="id-example")
    W->>API: GET /audit/v202601/events/{id}
    alt success
        API-->>W: GetAuditEventResponse (JSON)
        W-->>C: GetAuditEventResponse
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
    participant W as client.audit
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: get_event(id="id-example")
    W->>R: build_grpc_request(GetAuditEventRequest, arguments)
    R->>API: AuditService/GetAuditEvent (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: parse_grpc_response(response)
        W-->>C: GetAuditEventResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `id` | path | `string (int64)` | Yes |
| `ctime` | query | `string (date-time)` | No |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `GetAuditEventResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.audit.get_event(
    id="id-example",
)
```

---

### `GET` `/audit/v202601/events/{id}/{ctime}`

Get an Audit Event

Return a specific audit event.

#### REST call flow

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.audit
    participant API as Kentik REST API

    C->>W: get_event_by_ctime(id="id-example", ctime="ctime-example")
    W->>API: GET /audit/v202601/events/{id}/{ctime}
    alt success
        API-->>W: GetAuditEventResponse (JSON)
        W-->>C: GetAuditEventResponse
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
    participant W as client.audit
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: get_event_by_ctime(id="id-example", ctime="ctime-example")
    W->>R: build_grpc_request(GetAuditEventRequest, arguments)
    R->>API: AuditService/GetAuditEvent (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: parse_grpc_response(response)
        W-->>C: GetAuditEventResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `id` | path | `string (int64)` | Yes |
| `ctime` | path | `string (date-time)` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `GetAuditEventResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.audit.get_event_by_ctime(
    id="id-example",
    ctime="ctime-example",
)
```

## Data Models

<details>
<summary>Model relationships (5 of 6 models)</summary>

Each arrow points from a model to a model that one of its fields holds. The label names the field.

```mermaid
classDiagram
    class AuditEvent
    class GetAuditEventResponse
    class ListAuditEventsResponse
    class protobufAny
    class rpcStatus
    GetAuditEventResponse --> AuditEvent : event
    ListAuditEventsResponse --> AuditEvent : events
    rpcStatus --> protobufAny : details
```

</details>

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.audit.models.AuditEvent
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.audit.models.GenericEvent
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.audit.models.GetAuditEventResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.audit.models.ListAuditEventsResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.audit.models.protobufAny
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.audit.models.rpcStatus
```
