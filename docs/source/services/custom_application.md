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

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.custom_application
    participant API as Kentik API

    C->>W: list_custom_applications()
    W->>API: GET /custom_application/v202501alpha1
    alt success
        API-->>W: ListCustomApplicationsResponse
        W-->>C: ListCustomApplicationsResponse
    else error status
        API-->>W: error body
        W-->>C: raise HTTPException
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

# Use protocol="grpc" to route through gRPC instead of REST.
# See docs/source/grpc_implementation_spec.md for current gRPC status.
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.custom_application.list_custom_applications()
```

---

### `POST` `/custom_application/v202501alpha1`

Create Custom Application

Creates and returns a custom application object containing information about an individual custom application.

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.custom_application
    participant API as Kentik API

    C->>W: create_custom_application()
    W->>API: POST /custom_application/v202501alpha1
    alt success
        API-->>W: CreateCustomApplicationResponse
        W-->>C: CreateCustomApplicationResponse
    else error status
        API-->>W: error body
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
| 200 | A successful response. | `CreateCustomApplicationResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Use protocol="grpc" to route through gRPC instead of REST.
# See docs/source/grpc_implementation_spec.md for current gRPC status.
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.custom_application.create_custom_application()
```

---

### `GET` `/custom_application/v202501alpha1/{customApplicationId}`

Custom Application Info

Returns a custom application object containing information about an individual custom application.

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.custom_application
    participant API as Kentik API

    C->>W: get_custom_application(customApplicationId="customApplicationId-example")
    W->>API: GET /custom_application/v202501alpha1/{customApplicationId}
    alt success
        API-->>W: GetCustomApplicationResponse
        W-->>C: GetCustomApplicationResponse
    else error status
        API-->>W: error body
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
| 200 | A successful response. | `GetCustomApplicationResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Use protocol="grpc" to route through gRPC instead of REST.
# See docs/source/grpc_implementation_spec.md for current gRPC status.
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.custom_application.get_custom_application(
    customApplicationId="customApplicationId-example",
)
```

---

### `PUT` `/custom_application/v202501alpha1/{customApplicationId}`

Update Custom Application

Updates and returns a custom application object containing information about an individual custom application.

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.custom_application
    participant API as Kentik API

    C->>W: update_custom_application(customApplicationId="customApplicationId-example")
    W->>API: PUT /custom_application/v202501alpha1/{customApplicationId}
    alt success
        API-->>W: UpdateCustomApplicationResponse
        W-->>C: UpdateCustomApplicationResponse
    else error status
        API-->>W: error body
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
| 200 | A successful response. | `UpdateCustomApplicationResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Use protocol="grpc" to route through gRPC instead of REST.
# See docs/source/grpc_implementation_spec.md for current gRPC status.
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.custom_application.update_custom_application(
    customApplicationId="customApplicationId-example",
)
```

---

### `DELETE` `/custom_application/v202501alpha1/{customApplicationId}`

Delete Custom Application

Deletes a custom application.

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.custom_application
    participant API as Kentik API

    C->>W: delete_custom_application(customApplicationId="customApplicationId-example")
    W->>API: DELETE /custom_application/v202501alpha1/{customApplicationId}
    alt success
        API-->>W: DeleteCustomApplicationResponse
        W-->>C: DeleteCustomApplicationResponse
    else error status
        API-->>W: error body
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
| 200 | A successful response. | `DeleteCustomApplicationResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Use protocol="grpc" to route through gRPC instead of REST.
# See docs/source/grpc_implementation_spec.md for current gRPC status.
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.custom_application.delete_custom_application(
    customApplicationId="customApplicationId-example",
)
```

## Data Models

<details>
<summary>Model relationships (8 of 8 models)</summary>

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
    CreateCustomApplicationResponse --> CustomApplication
    GetCustomApplicationResponse --> CustomApplication
    ListCustomApplicationsResponse --> CustomApplication
    UpdateCustomApplicationResponse --> CustomApplication
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
