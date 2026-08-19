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

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.custom_dimension
    participant API as Kentik API

    C->>W: list_custom_dimensions()
    W->>API: GET /custom_dimensions/v202411alpha1
    alt success
        API-->>W: ListCustomDimensionsResponse
        W-->>C: ListCustomDimensionsResponse
    else error status
        API-->>W: error body
        W-->>C: raise HTTPException
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

client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.custom_dimension.list_custom_dimensions()
```

---

### `GET` `/custom_dimensions/v202411alpha1/{customDimensionId}`

Custom Dimension Info

Returns a custom dimension object containing information about an individual custom dimension.

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.custom_dimension
    participant API as Kentik API

    C->>W: get_custom_dimension_info(customDimensionId="customDimensionId-example")
    W->>API: GET /custom_dimensions/v202411alpha1/{customDimensionId}
    alt success
        API-->>W: GetCustomDimensionInfoResponse
        W-->>C: GetCustomDimensionInfoResponse
    else error status
        API-->>W: error body
        W-->>C: raise HTTPException
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

client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.custom_dimension.get_custom_dimension_info(
    customDimensionId="customDimensionId-example",
)
```

---

### `PUT` `/custom_dimensions/v202411alpha1/{customDimensionId}`

Update Custom Dimension

Updates and returns a custom dimension object containing information about an individual custom dimension (see About Custom Dimensions). Populators are not sent back in the response body. To get them use 'Custom Dimension info' API instead.

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.custom_dimension
    participant API as Kentik API

    C->>W: update_custom_dimension(customDimensionId="customDimensionId-example")
    W->>API: PUT /custom_dimensions/v202411alpha1/{customDimensionId}
    alt success
        API-->>W: UpdateCustomDimensionResponse
        W-->>C: UpdateCustomDimensionResponse
    else error status
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `customDimensionId` | path | `string` | Yes |
| `data` | body | `-` | No |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `UpdateCustomDimensionResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.custom_dimension.update_custom_dimension(
    customDimensionId="customDimensionId-example",
)
```

---

### `DELETE` `/custom_dimensions/v202411alpha1/{customDimensionId}`

Delete Custom Dimension

Deletes a custom dimension.

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.custom_dimension
    participant API as Kentik API

    C->>W: delete_custom_dimension(customDimensionId="customDimensionId-example")
    W->>API: DELETE /custom_dimensions/v202411alpha1/{customDimensionId}
    alt success
        API-->>W: DeleteCustomDimensionResponse
        W-->>C: DeleteCustomDimensionResponse
    else error status
        API-->>W: error body
        W-->>C: raise HTTPException
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

client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.custom_dimension.delete_custom_dimension(
    customDimensionId="customDimensionId-example",
)
```

---

### `POST` `/custom_dimensions/v202411alpha1/{customDimensionId}/populator`

Create Populator

Creates and returns a populator object containing information about an individual populator.

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.custom_dimension
    participant API as Kentik API

    C->>W: create_populator(customDimensionId="customDimensionId-example")
    W->>API: POST /custom_dimensions/v202411alpha1/{customDimensionId}/populator
    alt success
        API-->>W: CreatePopulatorResponse
        W-->>C: CreatePopulatorResponse
    else error status
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `customDimensionId` | path | `string` | Yes |
| `data` | body | `-` | No |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `CreatePopulatorResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.custom_dimension.create_populator(
    customDimensionId="customDimensionId-example",
)
```

---

### `GET` `/custom_dimensions/v202411alpha1/{customDimensionId}/populator/{populatorId}`

Get Populator

Get Populator by Dimension and Populator ID.

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.custom_dimension
    participant API as Kentik API

    C->>W: get_populator(customDimensionId="customDimensionId-example", populatorId="populatorId-example")
    W->>API: GET /custom_dimensions/v202411alpha1/{customDimensionId}/populator/{populatorId}
    alt success
        API-->>W: GetPopulatorResponse
        W-->>C: GetPopulatorResponse
    else error status
        API-->>W: error body
        W-->>C: raise HTTPException
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

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.custom_dimension
    participant API as Kentik API

    C->>W: update_populator(customDimensionId="customDimensionId-example", populatorId="populatorId-example")
    W->>API: PUT /custom_dimensions/v202411alpha1/{customDimensionId}/populator/{populatorId}
    alt success
        API-->>W: UpdatePopulatorResponse
        W-->>C: UpdatePopulatorResponse
    else error status
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `customDimensionId` | path | `string` | Yes |
| `populatorId` | path | `string` | Yes |
| `data` | body | `-` | No |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `UpdatePopulatorResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.custom_dimension.update_populator(
    customDimensionId="customDimensionId-example",
    populatorId="populatorId-example",
)
```

---

### `DELETE` `/custom_dimensions/v202411alpha1/{customDimensionId}/populator/{populatorId}`

Delete Populator

Deletes a populator.

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.custom_dimension
    participant API as Kentik API

    C->>W: delete_populator(customDimensionId="customDimensionId-example", populatorId="populatorId-example")
    W->>API: DELETE /custom_dimensions/v202411alpha1/{customDimensionId}/populator/{populatorId}
    alt success
        API-->>W: DeletePopulatorResponse
        W-->>C: DeletePopulatorResponse
    else error status
        API-->>W: error body
        W-->>C: raise HTTPException
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

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.custom_dimension
    participant API as Kentik API

    C->>W: get_populator_field(customDimensionId="customDimensionId-example", populatorId="populatorId-example", fieldName="fieldName-example")
    W->>API: GET /custom_dimensions/v202411alpha1/{customDimensionId}/populator/{populatorId}/field/{fieldName}
    alt success
        API-->>W: GetPopulatorFieldResponse
        W-->>C: GetPopulatorFieldResponse
    else error status
        API-->>W: error body
        W-->>C: raise HTTPException
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

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.custom_dimension
    participant API as Kentik API

    C->>W: create_custom_dimension()
    W->>API: POST /v1/customdimension
    alt success
        API-->>W: CreateCustomDimensionResponse
        W-->>C: CreateCustomDimensionResponse
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
| 200 | A successful response. | `CreateCustomDimensionResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.custom_dimension.create_custom_dimension()
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
