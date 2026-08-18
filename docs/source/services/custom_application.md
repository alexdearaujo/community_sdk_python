# Custom Application Service

## Overview

```mermaid
flowchart LR
    Client["client.custom_application"]
    RJ["request_json()"]
    OK["success: response model"]
    ERR["per-operation error class"]
    Client --> G0["CustomApplicationService (5 ops)"]
    G0 --> RJ
    RJ --> OK
    RJ -->|"error status"| ERR
```

## Endpoints

### `GET` `/custom_application/v202501alpha1`

List Custom Applications

Returns an array of custom application objects that each contain information about an individual custom application.

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `ListCustomApplicationsResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

client = KentikAPI()  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.custom_application.list_custom_applications()
```

---

### `POST` `/custom_application/v202501alpha1`

Create Custom Application

Creates and returns a custom application object containing information about an individual custom application.

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

client = KentikAPI()  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.custom_application.create_custom_application()
```

---

### `GET` `/custom_application/v202501alpha1/{customApplicationId}`

Custom Application Info

Returns a custom application object containing information about an individual custom application.

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

client = KentikAPI()  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.custom_application.get_custom_application(
    customApplicationId="customApplicationId-example",
)
```

---

### `PUT` `/custom_application/v202501alpha1/{customApplicationId}`

Update Custom Application

Updates and returns a custom application object containing information about an individual custom application.

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

client = KentikAPI()  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.custom_application.update_custom_application(
    customApplicationId="customApplicationId-example",
)
```

---

### `DELETE` `/custom_application/v202501alpha1/{customApplicationId}`

Delete Custom Application

Deletes a custom application.

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

client = KentikAPI()  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
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
