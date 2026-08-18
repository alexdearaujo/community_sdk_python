# As Group Service

## Endpoints

### `GET` `/as_group/v202212/as_group`

List all AS groups.

Returns list of configured AS groups.

**Responses**

| Status | Description | Model |
|--------|--------------|-------|
| 200 | A successful response. | `ListASGroupsResponse` |
| default | An unexpected error response. | `rpcStatus` |

**Example**

```python
from kentik_api.client import KentikAPI

client = KentikAPI()  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.as_group.list_a_s_groups()
```

---

### `POST` `/as_group/v202212/as_group`

Configure a new AS group.

Create configuration for a new AS group. Returns the newly created configuration.

**Parameters**

| Name | In | Type | Required |
|------|----|------|----------|
| `data` | body | `CreateASGroupRequest` | Yes |

**Responses**

| Status | Description | Model |
|--------|--------------|-------|
| 200 | A successful response. | `CreateASGroupResponse` |
| default | An unexpected error response. | `rpcStatus` |

**Example**

```python
from kentik_api.client import KentikAPI

client = KentikAPI()  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.as_group.create_a_s_group(
    data=CreateASGroupRequest(...),
)
```

---

### `GET` `/as_group/v202212/as_group/{asGroup.id}`

Retrieve configuration of a AS group.

Returns configuration of a AS group specified by ID.

**Parameters**

| Name | In | Type | Required |
|------|----|------|----------|
| `asGroupid` | path | `string` | Yes |

**Responses**

| Status | Description | Model |
|--------|--------------|-------|
| 200 | A successful response. | `GetASGroupResponse` |
| default | An unexpected error response. | `rpcStatus` |

**Example**

```python
from kentik_api.client import KentikAPI

client = KentikAPI()  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.as_group.get_a_s_group(
    asGroupid="asGroupid-example",
)
```

---

### `PUT` `/as_group/v202212/as_group/{asGroup.id}`

Updates configuration of a AS group.

Replaces configuration of a AS group with attributes in the request. Returns the updated configuration.

**Parameters**

| Name | In | Type | Required |
|------|----|------|----------|
| `asGroupid` | path | `string` | Yes |
| `data` | body | `ASGroupServiceUpdateASGroupBody` | Yes |

**Responses**

| Status | Description | Model |
|--------|--------------|-------|
| 200 | A successful response. | `UpdateASGroupResponse` |
| default | An unexpected error response. | `rpcStatus` |

**Example**

```python
from kentik_api.client import KentikAPI

client = KentikAPI()  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.as_group.update_a_s_group(
    asGroupid="asGroupid-example",
    data=ASGroupServiceUpdateASGroupBody(...),
)
```

---

### `DELETE` `/as_group/v202212/as_group/{asGroup.id}`

Delete configuration of a AS group.

Deletes configuration of a AS group with specific ID.

**Parameters**

| Name | In | Type | Required |
|------|----|------|----------|
| `asGroupid` | path | `string` | Yes |

**Responses**

| Status | Description | Model |
|--------|--------------|-------|
| 200 | A successful response. | `DeleteASGroupResponse` |
| default | An unexpected error response. | `rpcStatus` |

**Example**

```python
from kentik_api.client import KentikAPI

client = KentikAPI()  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.as_group.delete_a_s_group(
    asGroupid="asGroupid-example",
)
```

## Data Models

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.as_group.models.ASGroupConcise
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.as_group.models.ASGroupDetailed
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.as_group.models.ASGroupServiceUpdateASGroupBody
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.as_group.models.AutonomousSystem
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.as_group.models.CreateASGroupRequest
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.as_group.models.CreateASGroupResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.as_group.models.DeleteASGroupResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.as_group.models.GetASGroupResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.as_group.models.ListASGroupsResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.as_group.models.UpdateASGroupResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.as_group.models.protobufAny
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.as_group.models.rpcStatus
```
