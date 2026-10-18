<!-- AUTO-GENERATED: scripts/generation/endpoint_docs.py, render_endpoint_docs() -->
<!-- Rebuilt on every `uv run poe generate`. Do not edit by hand. -->

# Custom Dimension Service

## Overview

```mermaid
flowchart LR
    subgraph sdk["kentik_api"]
        KA["KentikAPI"]
        W["Custom DimensionServiceWrapper\nclient.custom_dimension"]
        REST["REST functions\ngen/custom_dimension/services/"]
        RJ["request_json()\ncore/rest_runtime"]
        M["Models\ngen/custom_dimension/models/"]
        E["Error classes\ngen/custom_dimension/error/"]
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

### `GET` `/custom_dimensions/v202411alpha1`

List Custom Dimensions

Returns an array of custom dimension objects that each contain information about an individual custom dimension.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.custom_dimension
    participant API as Kentik REST API

    C->>W: list()
    W->>API: GET /custom_dimensions/v202411alpha1
    alt success
        API-->>W: ListCustomDimensionsResponse (JSON)
        W-->>C: ListCustomDimensionsResponse
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
    participant W as client.custom_dimension
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: list()
    W->>R: build_grpc_request(ListCustomDimensionsRequest, arguments)
    R->>API: CustomDimensionService/ListCustomDimensions (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: parse_grpc_response(response)
        W-->>C: ListCustomDimensionsResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `ListCustomDimensionsResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.custom_dimension.list()
```

---

### `GET` `/custom_dimensions/v202411alpha1/{customDimensionId}`

Custom Dimension Info

Returns a custom dimension object containing information about an individual custom dimension.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.custom_dimension
    participant API as Kentik REST API

    C->>W: get_info(customDimensionId="customDimensionId-example")
    W->>API: GET /custom_dimensions/v202411alpha1/{customDimensionId}
    alt success
        API-->>W: GetCustomDimensionInfoResponse (JSON)
        W-->>C: GetCustomDimensionInfoResponse
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
    participant W as client.custom_dimension
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: get_info(customDimensionId="customDimensionId-example")
    W->>R: build_grpc_request(GetCustomDimensionInfoRequest, arguments)
    R->>API: CustomDimensionService/GetCustomDimensionInfo (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: parse_grpc_response(response)
        W-->>C: GetCustomDimensionInfoResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `customDimensionId` | path | `string` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `GetCustomDimensionInfoResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.custom_dimension.get_info(
    customDimensionId="customDimensionId-example",
)
```

---

### `PUT` `/custom_dimensions/v202411alpha1/{customDimensionId}`

Update Custom Dimension

Updates and returns a custom dimension object containing information about an individual custom dimension (see About Custom Dimensions). Populators are not sent back in the response body. To get them use 'Custom Dimension info' API instead.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.custom_dimension
    participant API as Kentik REST API

    C->>W: update(customDimensionId="customDimensionId-example", data=CustomDimension(...))
    W->>API: PUT /custom_dimensions/v202411alpha1/{customDimensionId}
    alt success
        API-->>W: UpdateCustomDimensionResponse (JSON)
        W-->>C: UpdateCustomDimensionResponse
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
    participant W as client.custom_dimension
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: update(customDimensionId="customDimensionId-example", data=CustomDimension(...))
    W->>R: build_grpc_request(UpdateCustomDimensionRequest, arguments)
    R->>API: CustomDimensionService/UpdateCustomDimension (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: parse_grpc_response(response)
        W-->>C: UpdateCustomDimensionResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `customDimensionId` | path | `string` | Yes |
| `data` | body | `CustomDimension` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `UpdateCustomDimensionResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI
from kentik_api.gen.custom_dimension.models import CustomDimension

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.custom_dimension.update(
    customDimensionId="customDimensionId-example",
    data=CustomDimension(...),
)
```

---

### `DELETE` `/custom_dimensions/v202411alpha1/{customDimensionId}`

Delete Custom Dimension

Deletes a custom dimension.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.custom_dimension
    participant API as Kentik REST API

    C->>W: delete(customDimensionId="customDimensionId-example")
    W->>API: DELETE /custom_dimensions/v202411alpha1/{customDimensionId}
    alt success
        API-->>W: DeleteCustomDimensionResponse (JSON)
        W-->>C: DeleteCustomDimensionResponse
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
    participant W as client.custom_dimension
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: delete(customDimensionId="customDimensionId-example")
    W->>R: build_grpc_request(DeleteCustomDimensionRequest, arguments)
    R->>API: CustomDimensionService/DeleteCustomDimension (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: parse_grpc_response(response)
        W-->>C: DeleteCustomDimensionResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `customDimensionId` | path | `string` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `DeleteCustomDimensionResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.custom_dimension.delete(
    customDimensionId="customDimensionId-example",
)
```

---

### `POST` `/custom_dimensions/v202411alpha1/{customDimensionId}/populator`

Create Populator

Creates and returns a populator object containing information about an individual populator.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.custom_dimension
    participant API as Kentik REST API

    C->>W: create_populator(customDimensionId="customDimensionId-example", data=Populator(...))
    W->>API: POST /custom_dimensions/v202411alpha1/{customDimensionId}/populator
    alt success
        API-->>W: CreatePopulatorResponse (JSON)
        W-->>C: CreatePopulatorResponse
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
    participant W as client.custom_dimension
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: create_populator(customDimensionId="customDimensionId-example", data=Populator(...))
    W->>R: build_grpc_request(CreatePopulatorRequest, arguments)
    R->>API: CustomDimensionService/CreatePopulator (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: parse_grpc_response(response)
        W-->>C: CreatePopulatorResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `customDimensionId` | path | `string` | Yes |
| `data` | body | `Populator` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `CreatePopulatorResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI
from kentik_api.gen.custom_dimension.models import Populator

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.custom_dimension.create_populator(
    customDimensionId="customDimensionId-example",
    data=Populator(...),
)
```

---

### `GET` `/custom_dimensions/v202411alpha1/{customDimensionId}/populator/{populatorId}`

Get Populator

Get Populator by Dimension and Populator ID.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.custom_dimension
    participant API as Kentik REST API

    C->>W: get_populator(customDimensionId="customDimensionId-example", populatorId="populatorId-example")
    W->>API: GET /custom_dimensions/v202411alpha1/{customDimensionId}/populator/{populatorId}
    alt success
        API-->>W: GetPopulatorResponse (JSON)
        W-->>C: GetPopulatorResponse
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
    participant W as client.custom_dimension
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: get_populator(customDimensionId="customDimensionId-example", populatorId="populatorId-example")
    W->>R: build_grpc_request(GetPopulatorRequest, arguments)
    R->>API: CustomDimensionService/GetPopulator (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: parse_grpc_response(response)
        W-->>C: GetPopulatorResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `customDimensionId` | path | `string` | Yes |
| `populatorId` | path | `string` | Yes |
| `fieldLimit` | query | `integer (int64)` | No |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `GetPopulatorResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.custom_dimension.get_populator(
    customDimensionId="customDimensionId-example",
    populatorId="populatorId-example",
)
```

---

### `PUT` `/custom_dimensions/v202411alpha1/{customDimensionId}/populator/{populatorId}`

Update Populator

Updates and returns a populator object containing information about an individual populator.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.custom_dimension
    participant API as Kentik REST API

    C->>W: update_populator(customDimensionId="customDimensionId-example", populatorId="populatorId-example", data=Populator(...))
    W->>API: PUT /custom_dimensions/v202411alpha1/{customDimensionId}/populator/{populatorId}
    alt success
        API-->>W: UpdatePopulatorResponse (JSON)
        W-->>C: UpdatePopulatorResponse
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
    participant W as client.custom_dimension
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: update_populator(customDimensionId="customDimensionId-example", populatorId="populatorId-example", data=Populator(...))
    W->>R: build_grpc_request(UpdatePopulatorRequest, arguments)
    R->>API: CustomDimensionService/UpdatePopulator (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: parse_grpc_response(response)
        W-->>C: UpdatePopulatorResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `customDimensionId` | path | `string` | Yes |
| `populatorId` | path | `string` | Yes |
| `data` | body | `Populator` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `UpdatePopulatorResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI
from kentik_api.gen.custom_dimension.models import Populator

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.custom_dimension.update_populator(
    customDimensionId="customDimensionId-example",
    populatorId="populatorId-example",
    data=Populator(...),
)
```

---

### `DELETE` `/custom_dimensions/v202411alpha1/{customDimensionId}/populator/{populatorId}`

Delete Populator

Deletes a populator.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.custom_dimension
    participant API as Kentik REST API

    C->>W: delete_populator(customDimensionId="customDimensionId-example", populatorId="populatorId-example")
    W->>API: DELETE /custom_dimensions/v202411alpha1/{customDimensionId}/populator/{populatorId}
    alt success
        API-->>W: DeletePopulatorResponse (JSON)
        W-->>C: DeletePopulatorResponse
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
    participant W as client.custom_dimension
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: delete_populator(customDimensionId="customDimensionId-example", populatorId="populatorId-example")
    W->>R: build_grpc_request(DeletePopulatorRequest, arguments)
    R->>API: CustomDimensionService/DeletePopulator (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: parse_grpc_response(response)
        W-->>C: DeletePopulatorResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `customDimensionId` | path | `string` | Yes |
| `populatorId` | path | `string` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `DeletePopulatorResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.custom_dimension.delete_populator(
    customDimensionId="customDimensionId-example",
    populatorId="populatorId-example",
)
```

---

### `GET` `/custom_dimensions/v202411alpha1/{customDimensionId}/populator/{populatorId}/field/{fieldName}`

Get Populator Field

Get Populator field by Dimension, Populator ID, and field name.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.custom_dimension
    participant API as Kentik REST API

    C->>W: get_populator_field(customDimensionId="customDimensionId-example", populatorId="populatorId-example", fieldName="fieldName-example")
    W->>API: GET /custom_dimensions/v202411alpha1/{customDimensionId}/populator/{populatorId}/field/{fieldName}
    alt success
        API-->>W: GetPopulatorFieldResponse (JSON)
        W-->>C: GetPopulatorFieldResponse
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
    participant W as client.custom_dimension
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: get_populator_field(customDimensionId="customDimensionId-example", populatorId="populatorId-example", fieldName="fieldName-example")
    W->>R: build_grpc_request(GetPopulatorFieldRequest, arguments)
    R->>API: CustomDimensionService/GetPopulatorField (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: parse_grpc_response(response)
        W-->>C: GetPopulatorFieldResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `customDimensionId` | path | `string` | Yes |
| `populatorId` | path | `string` | Yes |
| `fieldName` | path | `string` | Yes |
| `offset` | query | `integer (int32)` | No |
| `limit` | query | `integer (int32)` | No |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `GetPopulatorFieldResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.custom_dimension.get_populator_field(
    customDimensionId="customDimensionId-example",
    populatorId="populatorId-example",
    fieldName="fieldName-example",
)
```

---

### `POST` `/v1/customdimension`

Create Custom Dimension

Creates and returns a custom dimension object containing information about an individual custom dimension

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.custom_dimension
    participant API as Kentik REST API

    C->>W: create(data=CustomDimension(...))
    W->>API: POST /v1/customdimension
    alt success
        API-->>W: CreateCustomDimensionResponse (JSON)
        W-->>C: CreateCustomDimensionResponse
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
    participant W as client.custom_dimension
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: create(data=CustomDimension(...))
    W->>R: build_grpc_request(CreateCustomDimensionRequest, arguments)
    R->>API: CustomDimensionService/CreateCustomDimension (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: parse_grpc_response(response)
        W-->>C: CreateCustomDimensionResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `data` | body | `CustomDimension` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `CreateCustomDimensionResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI
from kentik_api.gen.custom_dimension.models import CustomDimension

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.custom_dimension.create(
    data=CustomDimension(...),
)
```

## Data Models

<details>
<summary>Model relationships (14 of 15 models)</summary>

```mermaid
classDiagram
    class CreateCustomDimensionResponse
    class CreatePopulatorResponse
    class CustomDimension
    class DeleteCustomDimensionResponse
    class DeletePopulatorResponse
    class GetCustomDimensionInfoResponse
    class GetPopulatorFieldResponse
    class GetPopulatorResponse
    class ListCustomDimensionsResponse
    class Populator
    class UpdateCustomDimensionResponse
    class UpdatePopulatorResponse
    class protobufAny
    class rpcStatus
    CreateCustomDimensionResponse --> CustomDimension
    CreatePopulatorResponse --> Populator
    CustomDimension --> Populator
    GetCustomDimensionInfoResponse --> CustomDimension
    GetPopulatorResponse --> Populator
    ListCustomDimensionsResponse --> CustomDimension
    UpdateCustomDimensionResponse --> CustomDimension
    UpdatePopulatorResponse --> Populator
    rpcStatus --> protobufAny
```

</details>

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.custom_dimension.models.CreateCustomDimensionResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.custom_dimension.models.CreatePopulatorResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.custom_dimension.models.CustomDimension
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.custom_dimension.models.DeleteCustomDimensionResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.custom_dimension.models.DeletePopulatorResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.custom_dimension.models.ExtendedField
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.custom_dimension.models.GetCustomDimensionInfoResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.custom_dimension.models.GetPopulatorFieldResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.custom_dimension.models.GetPopulatorResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.custom_dimension.models.ListCustomDimensionsResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.custom_dimension.models.Populator
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.custom_dimension.models.UpdateCustomDimensionResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.custom_dimension.models.UpdatePopulatorResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.custom_dimension.models.protobufAny
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.custom_dimension.models.rpcStatus
```
