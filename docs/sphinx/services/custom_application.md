<!-- AUTO-GENERATED: scripts/generation/endpoint_docs.py, render_endpoint_docs() -->
<!-- Rebuilt on every `uv run poe generate`. Do not edit by hand. -->

# Custom Application Service

## Overview

```mermaid
%%{init: {"fontFamily": "ui-monospace, SFMono-Regular, Menlo, monospace", "flowchart": {"curve": "step", "nodeSpacing": 30, "rankSpacing": 70, "wrappingWidth": 400}}}%%
flowchart LR
    code("Your code"):::greenSrc
    subgraph sdk["kentik_api"]
        wrap("CustomApplicationServiceWrapper<br/>client.custom_application<br/>5 operations"):::orange
        rest("REST functions<br/>gen/custom_application/services/"):::blue
        rj("request_json()<br/>core/rest_runtime.py"):::blue
        cg("call_grpc()<br/>core/grpc_runtime.py"):::violet
    end
    grpcapi("Kentik gRPC API<br/>HTTP/2 + protobuf"):::violetSrc
    restapi("Kentik REST API<br/>HTTPS + JSON"):::blueSrc

    code -->|"method call"| wrap
    wrap -->|"Pydantic model from<br/>gen/custom_application/models/"| code
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

On an error status or a failed call, the SDK raises an error class from `gen/custom_application/error/`, or a shared type from `kentik_api.errors`.

## Endpoints

### `GET` `/custom_application/v202501alpha1`

List Custom Applications

Returns an array of custom application objects that each contain information about an individual custom application.

#### REST call flow

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.custom_application
    participant API as Kentik REST API

    C->>W: list()
    W->>API: GET /custom_application/v202501alpha1
    alt success
        API-->>W: ListCustomApplicationsResponse (JSON)
        W-->>C: ListCustomApplicationsResponse
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
    participant W as client.custom_application
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: list()
    W->>R: build_grpc_request(ListCustomApplicationsRequest, arguments)
    R->>API: CustomApplicationService/ListCustomApplications (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: parse_grpc_response(response)
        W-->>C: ListCustomApplicationsResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `ListCustomApplicationsResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.custom_application.list()
```

---

### `POST` `/custom_application/v202501alpha1`

Create Custom Application

Creates and returns a custom application object containing information about an individual custom application.

#### REST call flow

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.custom_application
    participant API as Kentik REST API

    C->>W: create(data=CustomApplication(...))
    W->>API: POST /custom_application/v202501alpha1
    alt success
        API-->>W: CreateCustomApplicationResponse (JSON)
        W-->>C: CreateCustomApplicationResponse
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
    participant W as client.custom_application
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: create(data=CustomApplication(...))
    W->>R: build_grpc_request(CreateCustomApplicationRequest, arguments)
    R->>API: CustomApplicationService/CreateCustomApplication (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: parse_grpc_response(response)
        W-->>C: CreateCustomApplicationResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `data` | body | `CustomApplication` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `CreateCustomApplicationResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI
from kentik_api.gen.custom_application.models import CustomApplication

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.custom_application.create(
    data=CustomApplication(...),
)
```

---

### `GET` `/custom_application/v202501alpha1/{customApplicationId}`

Custom Application Info

Returns a custom application object containing information about an individual custom application.

#### REST call flow

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.custom_application
    participant API as Kentik REST API

    C->>W: get(customApplicationId="customApplicationId-example")
    W->>API: GET /custom_application/v202501alpha1/{customApplicationId}
    alt success
        API-->>W: GetCustomApplicationResponse (JSON)
        W-->>C: GetCustomApplicationResponse
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
    participant W as client.custom_application
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: get(customApplicationId="customApplicationId-example")
    W->>R: build_grpc_request(GetCustomApplicationRequest, arguments)
    R->>API: CustomApplicationService/GetCustomApplication (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: parse_grpc_response(response)
        W-->>C: GetCustomApplicationResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `customApplicationId` | path | `string` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `GetCustomApplicationResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.custom_application.get(
    customApplicationId="customApplicationId-example",
)
```

---

### `PUT` `/custom_application/v202501alpha1/{customApplicationId}`

Update Custom Application

Updates and returns a custom application object containing information about an individual custom application.

#### REST call flow

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.custom_application
    participant API as Kentik REST API

    C->>W: update(customApplicationId="customApplicationId-example", data=CustomApplication(...))
    W->>API: PUT /custom_application/v202501alpha1/{customApplicationId}
    alt success
        API-->>W: UpdateCustomApplicationResponse (JSON)
        W-->>C: UpdateCustomApplicationResponse
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
    participant W as client.custom_application
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: update(customApplicationId="customApplicationId-example", data=CustomApplication(...))
    W->>R: build_grpc_request(UpdateCustomApplicationRequest, arguments)
    R->>API: CustomApplicationService/UpdateCustomApplication (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: parse_grpc_response(response)
        W-->>C: UpdateCustomApplicationResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `customApplicationId` | path | `string` | Yes |
| `data` | body | `CustomApplication` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `UpdateCustomApplicationResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI
from kentik_api.gen.custom_application.models import CustomApplication

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.custom_application.update(
    customApplicationId="customApplicationId-example",
    data=CustomApplication(...),
)
```

---

### `DELETE` `/custom_application/v202501alpha1/{customApplicationId}`

Delete Custom Application

Deletes a custom application.

#### REST call flow

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.custom_application
    participant API as Kentik REST API

    C->>W: delete(customApplicationId="customApplicationId-example")
    W->>API: DELETE /custom_application/v202501alpha1/{customApplicationId}
    alt success
        API-->>W: DeleteCustomApplicationResponse (JSON)
        W-->>C: DeleteCustomApplicationResponse
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
    participant W as client.custom_application
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: delete(customApplicationId="customApplicationId-example")
    W->>R: build_grpc_request(DeleteCustomApplicationRequest, arguments)
    R->>API: CustomApplicationService/DeleteCustomApplication (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: parse_grpc_response(response)
        W-->>C: DeleteCustomApplicationResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `customApplicationId` | path | `string` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `DeleteCustomApplicationResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.custom_application.delete(
    customApplicationId="customApplicationId-example",
)
```

## Data Models

<details>
<summary>Model relationships (8 of 8 models)</summary>

Each arrow points from a model to a model that one of its fields holds. The label names the field.

```mermaid
classDiagram
    class CreateCustomApplicationResponse
    class CustomApplication
    class DeleteCustomApplicationResponse
    class GetCustomApplicationResponse
    class ListCustomApplicationsResponse
    class UpdateCustomApplicationResponse
    class protobufAny
    class rpcStatus
    CreateCustomApplicationResponse --> CustomApplication : application
    GetCustomApplicationResponse --> CustomApplication : application
    ListCustomApplicationsResponse --> CustomApplication : applications
    UpdateCustomApplicationResponse --> CustomApplication : application
    rpcStatus --> protobufAny : details
```

</details>

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.custom_application.models.CreateCustomApplicationResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.custom_application.models.CustomApplication
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.custom_application.models.DeleteCustomApplicationResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.custom_application.models.GetCustomApplicationResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.custom_application.models.ListCustomApplicationsResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.custom_application.models.UpdateCustomApplicationResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.custom_application.models.protobufAny
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.custom_application.models.rpcStatus
```
