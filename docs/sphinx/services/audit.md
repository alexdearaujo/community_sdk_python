# Audit Service

## Overview

```mermaid
flowchart LR
    subgraph sdk["kentik_api"]
        KA["KentikAPI"]
        W["AuditServiceWrapper\nclient.audit"]
        REST["REST functions\ngen/audit/services/"]
        RJ["request_json()\ncore/rest_runtime"]
        M["Models\ngen/audit/models/"]
        E["Error classes\ngen/audit/error/"]
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

### `GET` `/audit/v202601/events`

List Audit Events.

Returns a list of audit events.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.audit
    participant API as Kentik REST API

    C->>W: list_audit_events()
    W->>API: GET /audit/v202601/events
    alt success
        API-->>W: ListAuditEventsResponse (JSON)
        W-->>C: ListAuditEventsResponse
    else error
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

**gRPC transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.audit
    participant B as proto bridge
    participant API as Kentik gRPC API

    C->>W: list_audit_events()
    W->>B: ParseDict(params, ListAuditEventsRequest)
    B->>API: list_audit_events (gRPC/TLS)
    alt success
        API-->>B: ListAuditEventsResponse proto
        B-->>W: MessageToDict(response)
        W-->>C: ListAuditEventsResponse
    else gRPC error
        API-->>B: gRPC status + details
        B-->>W: raise HTTPException
        W-->>C: raise HTTPException
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
response = client.audit.list_audit_events()
```

---

### `GET` `/audit/v202601/events/{id}`

Get an Audit Event

Return a specific audit event.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.audit
    participant API as Kentik REST API

    C->>W: get_audit_event(id="id-example")
    W->>API: GET /audit/v202601/events/{id}
    alt success
        API-->>W: GetAuditEventResponse (JSON)
        W-->>C: GetAuditEventResponse
    else error
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

**gRPC transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.audit
    participant B as proto bridge
    participant API as Kentik gRPC API

    C->>W: get_audit_event(id="id-example")
    W->>B: ParseDict(params, GetAuditEventRequest)
    B->>API: get_audit_event (gRPC/TLS)
    alt success
        API-->>B: GetAuditEventResponse proto
        B-->>W: MessageToDict(response)
        W-->>C: GetAuditEventResponse
    else gRPC error
        API-->>B: gRPC status + details
        B-->>W: raise HTTPException
        W-->>C: raise HTTPException
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
response = client.audit.get_audit_event(
    id="id-example",
)
```

---

### `GET` `/audit/v202601/events/{id}/{ctime}`

Get an Audit Event

Return a specific audit event.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.audit
    participant API as Kentik REST API

    C->>W: get_audit_event_2(id="id-example", ctime="ctime-example")
    W->>API: GET /audit/v202601/events/{id}/{ctime}
    alt success
        API-->>W: GetAuditEventResponse (JSON)
        W-->>C: GetAuditEventResponse
    else error
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

**gRPC transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.audit
    participant B as proto bridge
    participant API as Kentik gRPC API

    C->>W: get_audit_event_2(id="id-example", ctime="ctime-example")
    W->>B: ParseDict(params, GetAuditEventRequest)
    B->>API: get_audit_event_2 (gRPC/TLS)
    alt success
        API-->>B: GetAuditEventResponse proto
        B-->>W: MessageToDict(response)
        W-->>C: GetAuditEventResponse
    else gRPC error
        API-->>B: gRPC status + details
        B-->>W: raise HTTPException
        W-->>C: raise HTTPException
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
response = client.audit.get_audit_event_2(
    id="id-example",
    ctime="ctime-example",
)
```

## Data Models

<details>
<summary>Model relationships (5 of 6 models)</summary>

```mermaid
classDiagram
    class AuditEvent
    class GetAuditEventResponse
    class ListAuditEventsResponse
    class protobufAny
    class rpcStatus
    GetAuditEventResponse --> AuditEvent
    ListAuditEventsResponse --> AuditEvent
    rpcStatus --> protobufAny
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
