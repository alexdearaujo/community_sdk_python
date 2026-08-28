<!-- AUTO-GENERATED: scripts/generation/endpoint_docs.py, _render_sphinx_stubs() -->
<!-- Rebuilt on every `make generate`. Do not edit by hand. -->

# Custom Application Service

## Overview

```mermaid
flowchart LR
    subgraph sdk["kentik_api"]
        KA["KentikAPI"]
        W["Custom ApplicationServiceWrapper\nclient.custom_application"]
        REST["REST functions\ngen/custom_application/services/"]
        RJ["request_json()\ncore/rest_runtime"]
        M["Models\ngen/custom_application/models/"]
        E["Error classes\ngen/custom_application/error/"]
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

### `GET` `/custom_application/v202501alpha1`

List Custom Applications

Returns an array of custom application objects that each contain information about an individual custom application.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.custom_application
    participant API as Kentik REST API

    C->>W: list_custom_applications()
    W->>API: GET /custom_application/v202501alpha1
    alt success
        API-->>W: v202501alpha1ListCustomApplicationsResponse (JSON)
        W-->>C: v202501alpha1ListCustomApplicationsResponse
    else error
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

**gRPC transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.custom_application
    participant B as proto bridge
    participant API as Kentik gRPC API

    C->>W: list_custom_applications()
    W->>B: ParseDict(params, ListCustomApplicationsRequest)
    B->>API: list_custom_applications (gRPC/TLS)
    alt success
        API-->>B: v202501alpha1ListCustomApplicationsResponse proto
        B-->>W: MessageToDict(response)
        W-->>C: v202501alpha1ListCustomApplicationsResponse
    else gRPC error
        API-->>B: gRPC status + details
        B-->>W: raise HTTPException
        W-->>C: raise HTTPException
    end
```

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `v202501alpha1ListCustomApplicationsResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.custom_application.list_custom_applications()
```

---

### `POST` `/custom_application/v202501alpha1`

Create Custom Application

Creates and returns a custom application object containing information about an individual custom application.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.custom_application
    participant API as Kentik REST API

    C->>W: create_custom_application(data=CustomApplication(...))
    W->>API: POST /custom_application/v202501alpha1
    alt success
        API-->>W: v202501alpha1CreateCustomApplicationResponse (JSON)
        W-->>C: v202501alpha1CreateCustomApplicationResponse
    else error
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

**gRPC transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.custom_application
    participant B as proto bridge
    participant API as Kentik gRPC API

    C->>W: create_custom_application(data=CustomApplication(...))
    W->>B: ParseDict(params, CreateCustomApplicationRequest)
    B->>API: create_custom_application (gRPC/TLS)
    alt success
        API-->>B: v202501alpha1CreateCustomApplicationResponse proto
        B-->>W: MessageToDict(response)
        W-->>C: v202501alpha1CreateCustomApplicationResponse
    else gRPC error
        API-->>B: gRPC status + details
        B-->>W: raise HTTPException
        W-->>C: raise HTTPException
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `data` | body | `-` | No |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `v202501alpha1CreateCustomApplicationResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.custom_application.create_custom_application(
    data=CustomApplication(...),
)
```

---

### `GET` `/custom_application/v202501alpha1/{customApplicationId}`

Custom Application Info

Returns a custom application object containing information about an individual custom application.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.custom_application
    participant API as Kentik REST API

    C->>W: get_custom_application(customApplicationId="customApplicationId-example")
    W->>API: GET /custom_application/v202501alpha1/{customApplicationId}
    alt success
        API-->>W: v202501alpha1GetCustomApplicationResponse (JSON)
        W-->>C: v202501alpha1GetCustomApplicationResponse
    else error
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

**gRPC transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.custom_application
    participant B as proto bridge
    participant API as Kentik gRPC API

    C->>W: get_custom_application(customApplicationId="customApplicationId-example")
    W->>B: ParseDict(params, GetCustomApplicationRequest)
    B->>API: get_custom_application (gRPC/TLS)
    alt success
        API-->>B: v202501alpha1GetCustomApplicationResponse proto
        B-->>W: MessageToDict(response)
        W-->>C: v202501alpha1GetCustomApplicationResponse
    else gRPC error
        API-->>B: gRPC status + details
        B-->>W: raise HTTPException
        W-->>C: raise HTTPException
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `customApplicationId` | path | `string` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `v202501alpha1GetCustomApplicationResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.custom_application.get_custom_application(
    customApplicationId="customApplicationId-example",
)
```

---

### `PUT` `/custom_application/v202501alpha1/{customApplicationId}`

Update Custom Application

Updates and returns a custom application object containing information about an individual custom application.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.custom_application
    participant API as Kentik REST API

    C->>W: update_custom_application(customApplicationId="customApplicationId-example", data=CustomApplication(...))
    W->>API: PUT /custom_application/v202501alpha1/{customApplicationId}
    alt success
        API-->>W: v202501alpha1UpdateCustomApplicationResponse (JSON)
        W-->>C: v202501alpha1UpdateCustomApplicationResponse
    else error
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

**gRPC transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.custom_application
    participant B as proto bridge
    participant API as Kentik gRPC API

    C->>W: update_custom_application(customApplicationId="customApplicationId-example", data=CustomApplication(...))
    W->>B: ParseDict(params, UpdateCustomApplicationRequest)
    B->>API: update_custom_application (gRPC/TLS)
    alt success
        API-->>B: v202501alpha1UpdateCustomApplicationResponse proto
        B-->>W: MessageToDict(response)
        W-->>C: v202501alpha1UpdateCustomApplicationResponse
    else gRPC error
        API-->>B: gRPC status + details
        B-->>W: raise HTTPException
        W-->>C: raise HTTPException
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `customApplicationId` | path | `string` | Yes |
| `data` | body | `-` | No |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `v202501alpha1UpdateCustomApplicationResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.custom_application.update_custom_application(
    customApplicationId="customApplicationId-example",
    data=CustomApplication(...),
)
```

---

### `DELETE` `/custom_application/v202501alpha1/{customApplicationId}`

Delete Custom Application

Deletes a custom application.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.custom_application
    participant API as Kentik REST API

    C->>W: delete_custom_application(customApplicationId="customApplicationId-example")
    W->>API: DELETE /custom_application/v202501alpha1/{customApplicationId}
    alt success
        API-->>W: v202501alpha1DeleteCustomApplicationResponse (JSON)
        W-->>C: v202501alpha1DeleteCustomApplicationResponse
    else error
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

**gRPC transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.custom_application
    participant B as proto bridge
    participant API as Kentik gRPC API

    C->>W: delete_custom_application(customApplicationId="customApplicationId-example")
    W->>B: ParseDict(params, DeleteCustomApplicationRequest)
    B->>API: delete_custom_application (gRPC/TLS)
    alt success
        API-->>B: v202501alpha1DeleteCustomApplicationResponse proto
        B-->>W: MessageToDict(response)
        W-->>C: v202501alpha1DeleteCustomApplicationResponse
    else gRPC error
        API-->>B: gRPC status + details
        B-->>W: raise HTTPException
        W-->>C: raise HTTPException
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `customApplicationId` | path | `string` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `v202501alpha1DeleteCustomApplicationResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.custom_application.delete_custom_application(
    customApplicationId="customApplicationId-example",
)
```

## Data Models

<details>
<summary>Model relationships (2 of 8 models)</summary>

```mermaid
classDiagram
    class protobufAny
    class rpcStatus
    rpcStatus --> protobufAny
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
