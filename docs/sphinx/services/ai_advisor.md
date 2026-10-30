<!-- AUTO-GENERATED: scripts/generation/endpoint_docs.py, render_endpoint_docs() -->
<!-- Rebuilt on every `uv run poe generate`. Do not edit by hand. -->

# Ai Advisor Service

## Overview

```mermaid
%%{init: {"fontFamily": "ui-monospace, SFMono-Regular, Menlo, monospace", "flowchart": {"curve": "step", "nodeSpacing": 30, "rankSpacing": 70, "wrappingWidth": 400}}}%%
flowchart LR
    code("Your code"):::greenSrc
    subgraph sdk["kentik_api"]
        wrap("AiAdvisorServiceWrapper<br/>client.ai_advisor<br/>3 operations"):::orange
        rest("REST functions<br/>gen/ai_advisor/services/"):::blue
        rj("request_json()<br/>core/rest_runtime.py"):::blue
        cg("call_grpc()<br/>core/grpc_runtime.py"):::violet
    end
    grpcapi("Kentik gRPC API<br/>HTTP/2 + protobuf"):::violetSrc
    restapi("Kentik REST API<br/>HTTPS + JSON"):::blueSrc

    code -->|"method call"| wrap
    wrap -->|"Pydantic model from<br/>gen/ai_advisor/models/"| code
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

On an error status or a failed call, the SDK raises an error class from `gen/ai_advisor/error/`, or a shared type from `kentik_api.errors`.

## Endpoints

### `POST` `/ai_advisor/v202511/chat`

Create AI Advisor Chat Session

Create a new AI Advisor Chat session with a prompt

#### REST call flow

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.ai_advisor
    participant API as Kentik REST API

    C->>W: create_chat_session(data=CreateChatSessionRequest(...))
    W->>API: POST /ai_advisor/v202511/chat
    alt success
        API-->>W: CreateChatSessionResponse (JSON)
        W-->>C: CreateChatSessionResponse
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
    participant W as client.ai_advisor
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: create_chat_session(data=CreateChatSessionRequest(...))
    W->>R: build_grpc_request(CreateChatSessionRequest, arguments)
    R->>API: AiAdvisorDataService/CreateChatSession (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: parse_grpc_response(response)
        W-->>C: CreateChatSessionResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `data` | body | `CreateChatSessionRequest` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `CreateChatSessionResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI
from kentik_api.gen.ai_advisor.models import CreateChatSessionRequest

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

#### REST call flow

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.ai_advisor
    participant API as Kentik REST API

    C->>W: update_chat_session(data=UpdateChatSessionRequest(...))
    W->>API: PUT /ai_advisor/v202511/chat
    alt success
        API-->>W: UpdateChatSessionResponse (JSON)
        W-->>C: UpdateChatSessionResponse
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
    participant W as client.ai_advisor
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: update_chat_session(data=UpdateChatSessionRequest(...))
    W->>R: build_grpc_request(UpdateChatSessionRequest, arguments)
    R->>API: AiAdvisorDataService/UpdateChatSession (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: parse_grpc_response(response)
        W-->>C: UpdateChatSessionResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `data` | body | `UpdateChatSessionRequest` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `UpdateChatSessionResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI
from kentik_api.gen.ai_advisor.models import UpdateChatSessionRequest

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

#### REST call flow

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.ai_advisor
    participant API as Kentik REST API

    C->>W: get_chat_session(id="id-example")
    W->>API: GET /ai_advisor/v202511/chat/{id}
    alt success
        API-->>W: GetChatSessionResponse (JSON)
        W-->>C: GetChatSessionResponse
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
    participant W as client.ai_advisor
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: get_chat_session(id="id-example")
    W->>R: build_grpc_request(GetChatSessionRequest, arguments)
    R->>API: AiAdvisorDataService/GetChatSession (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: parse_grpc_response(response)
        W-->>C: GetChatSessionResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `id` | path | `string` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `GetChatSessionResponse` |
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
<summary>Model relationships (9 of 9 models)</summary>

Each arrow points from a model to a model that one of its fields holds. The label names the field.

```mermaid
classDiagram
    class ChatMessage
    class CreateChatSessionRequest
    class CreateChatSessionResponse
    class GetChatSessionResponse
    class SessionStatus
    class UpdateChatSessionRequest
    class UpdateChatSessionResponse
    class protobufAny
    class rpcStatus
    ChatMessage --> SessionStatus : status
    CreateChatSessionResponse --> SessionStatus : status
    GetChatSessionResponse --> ChatMessage : messages
    GetChatSessionResponse --> SessionStatus : status
    UpdateChatSessionResponse --> SessionStatus : status
    rpcStatus --> protobufAny : details
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
