<!-- AUTO-GENERATED: scripts/generation/endpoint_docs.py, render_endpoint_docs() -->
<!-- Rebuilt on every `make generate`. Do not edit by hand. -->

# Ai Advisor Service

## Overview

```mermaid
flowchart LR
    subgraph sdk["kentik_api"]
        KA["KentikAPI"]
        W["Ai AdvisorServiceWrapper\nclient.ai_advisor"]
        REST["REST functions\ngen/ai_advisor/services/"]
        RJ["request_json()\ncore/rest_runtime"]
        M["Models\ngen/ai_advisor/models/"]
        E["Error classes\ngen/ai_advisor/error/"]
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

### `POST` `/ai_advisor/v202511/chat`

Create AI Advisor Chat Session

Create a new AI Advisor Chat session with a prompt

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.ai_advisor
    participant API as Kentik REST API

    C->>W: create_chat_session(data=CreateChatSessionRequest(...))
    W->>API: POST /ai_advisor/v202511/chat
    alt success
        API-->>W: v202511CreateChatSessionResponse (JSON)
        W-->>C: v202511CreateChatSessionResponse
    else error
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

**gRPC transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.ai_advisor
    participant B as proto bridge
    participant API as Kentik gRPC API

    C->>W: create_chat_session(data=CreateChatSessionRequest(...))
    W->>B: ParseDict(params, CreateChatSessionRequest)
    B->>API: create_chat_session (gRPC/TLS)
    alt success
        API-->>B: v202511CreateChatSessionResponse proto
        B-->>W: MessageToDict(response)
        W-->>C: v202511CreateChatSessionResponse
    else gRPC error
        API-->>B: gRPC status + details
        B-->>W: raise HTTPException
        W-->>C: raise HTTPException
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `data` | body | `v202511CreateChatSessionRequest` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `v202511CreateChatSessionResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.ai_advisor.create_chat_session(
    data=CreateChatSessionRequest(...),
)
```

---

### `PUT` `/ai_advisor/v202511/chat`

Update AI Advisor Chat Session

Update AI Advisor Chat session with a prompt

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.ai_advisor
    participant API as Kentik REST API

    C->>W: update_chat_session(data=UpdateChatSessionRequest(...))
    W->>API: PUT /ai_advisor/v202511/chat
    alt success
        API-->>W: v202511UpdateChatSessionResponse (JSON)
        W-->>C: v202511UpdateChatSessionResponse
    else error
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

**gRPC transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.ai_advisor
    participant B as proto bridge
    participant API as Kentik gRPC API

    C->>W: update_chat_session(data=UpdateChatSessionRequest(...))
    W->>B: ParseDict(params, UpdateChatSessionRequest)
    B->>API: update_chat_session (gRPC/TLS)
    alt success
        API-->>B: v202511UpdateChatSessionResponse proto
        B-->>W: MessageToDict(response)
        W-->>C: v202511UpdateChatSessionResponse
    else gRPC error
        API-->>B: gRPC status + details
        B-->>W: raise HTTPException
        W-->>C: raise HTTPException
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `data` | body | `v202511UpdateChatSessionRequest` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `v202511UpdateChatSessionResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.ai_advisor.update_chat_session(
    data=UpdateChatSessionRequest(...),
)
```

---

### `GET` `/ai_advisor/v202511/chat/{id}`

Get AI Advisor Chat Session

Retrieve the status and results of an AI Advisor chat session

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.ai_advisor
    participant API as Kentik REST API

    C->>W: get_chat_session(id="id-example")
    W->>API: GET /ai_advisor/v202511/chat/{id}
    alt success
        API-->>W: v202511GetChatSessionResponse (JSON)
        W-->>C: v202511GetChatSessionResponse
    else error
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

**gRPC transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.ai_advisor
    participant B as proto bridge
    participant API as Kentik gRPC API

    C->>W: get_chat_session(id="id-example")
    W->>B: ParseDict(params, GetChatSessionRequest)
    B->>API: get_chat_session (gRPC/TLS)
    alt success
        API-->>B: v202511GetChatSessionResponse proto
        B-->>W: MessageToDict(response)
        W-->>C: v202511GetChatSessionResponse
    else gRPC error
        API-->>B: gRPC status + details
        B-->>W: raise HTTPException
        W-->>C: raise HTTPException
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `id` | path | `string` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `v202511GetChatSessionResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.ai_advisor.get_chat_session(
    id="id-example",
)
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
.. autopydantic_model:: kentik_api.gen.ai_advisor.models.ChatMessage
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.ai_advisor.models.CreateChatSessionRequest
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.ai_advisor.models.CreateChatSessionResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.ai_advisor.models.GetChatSessionResponse
```

```{eval-rst}
.. autoclass:: kentik_api.gen.ai_advisor.models.SessionStatus
   :members:
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.ai_advisor.models.UpdateChatSessionRequest
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.ai_advisor.models.UpdateChatSessionResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.ai_advisor.models.protobufAny
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.ai_advisor.models.rpcStatus
```
