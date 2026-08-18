# Interface Service

## Endpoints

### `GET` `/interface/v202108alpha1/interfaces`

Fetch Search Interfaces

Return list of interfaces matches search critera.

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `filterstext` | query | `string` | No |
| `filtersdeviceIds` | query | `string[]` | No |
| `filtersconnectivityTypes` | query | `string[]` | No |
| `filtersnetworkBoundaries` | query | `string[]` | No |
| `filtersproviders` | query | `string[]` | No |
| `filterssnmpSpeeds` | query | `integer (int32)[]` | No |
| `filtersipTypes` | query | `string[]` | No |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `ListInterfaceResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

client = KentikAPI()  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.interface.list_interface()
```

---

### `POST` `/interface/v202108alpha1/interfaces`

Create a interface.

Create a interface from request. returns created.

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `data` | body | `CreateInterfaceRequest` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `CreateInterfaceResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

client = KentikAPI()  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.interface.interface_create(
    data=CreateInterfaceRequest(...),
)
```

---

### `GET` `/interface/v202108alpha1/interfaces/{id}`

Get a interface.

Returns information about a interface specified with ID.

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `id` | path | `string` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `GetInterfaceResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

client = KentikAPI()  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.interface.interface_get(
    id="id-example",
)
```

---

### `PUT` `/interface/v202108alpha1/interfaces/{id}`

Update a interface.

Replaces the entire interface attributes specified with id.

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `id` | path | `string` | Yes |
| `data` | body | `InterfaceServiceUpdateInterfaceBody` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `UpdateInterfaceResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

client = KentikAPI()  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.interface.interface_update(
    id="id-example",
    data=InterfaceServiceUpdateInterfaceBody(...),
)
```

---

### `DELETE` `/interface/v202108alpha1/interfaces/{id}`

Delete a interface.

Deletes the interface specified with id.

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `id` | path | `string` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `DeleteInterfaceResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

client = KentikAPI()  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.interface.interface_delete(
    id="id-example",
)
```

---

### `POST` `/interface/v202108alpha1/manual_classify`

Manual Classify Interface

Manually set interface(s) classification.

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `data` | body | `ManualClassifyRequest` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `ManualClassifyResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

client = KentikAPI()  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.interface.manual_classify(
    data=ManualClassifyRequest(...),
)
```

## Data Models

```{eval-rst}
.. autoclass:: kentik_api.gen.interface.models.ConnectivityType
   :members:
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.interface.models.CreateInterfaceRequest
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.interface.models.CreateInterfaceResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.interface.models.DeleteInterfaceResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.interface.models.GetInterfaceResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.interface.models.Interface
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.interface.models.InterfaceFilter
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.interface.models.InterfaceServiceUpdateInterfaceBody
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.interface.models.InterfaceVrf
```

```{eval-rst}
.. autoclass:: kentik_api.gen.interface.models.IpFilter
   :members:
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.interface.models.ListInterfaceResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.interface.models.ManualClassifyRequest
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.interface.models.ManualClassifyResponse
```

```{eval-rst}
.. autoclass:: kentik_api.gen.interface.models.NetworkBoundary
   :members:
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.interface.models.UpdateInterfaceResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.interface.models.protobufAny
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.interface.models.rpcStatus
```
