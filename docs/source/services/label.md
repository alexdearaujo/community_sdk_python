# Label Service

## Overview

```mermaid
flowchart LR
    subgraph sdk["kentik_api"]
        KA["KentikAPI"]
        W["LabelServiceWrapper\nclient.label"]
        REST["REST functions\ngen/label/services/"]
        RJ["request_json()\ncore/rest_runtime"]
        M["Models\ngen/label/models/"]
        E["Error classes\ngen/label/error/"]
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

### `GET` `/label/v202210/labels`

List all configured labels

Returns list of all labels configured in the account.

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.label
    participant API as Kentik API

    C->>W: list_labels()
    W->>API: GET /label/v202210/labels
    alt success
        API-->>W: ListLabelsResponse
        W-->>C: ListLabelsResponse
    else error status
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `ListLabelsResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

client = KentikAPI()  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.label.list_labels()
```

---

### `POST` `/label/v202210/labels`

Create a new label.

Creates a new label based on data in the request.

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.label
    participant API as Kentik API

    C->>W: create_label(data=CreateLabelRequest(...))
    W->>API: POST /label/v202210/labels
    alt success
        API-->>W: CreateLabelResponse
        W-->>C: CreateLabelResponse
    else error status
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `data` | body | `CreateLabelRequest` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `CreateLabelResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

client = KentikAPI()  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.label.create_label(
    data=CreateLabelRequest(...),
)
```

---

### `POST` `/label/v202210/labels/{id}`

Update an existing label.

Updates configuration of a label.

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.label
    participant API as Kentik API

    C->>W: update_label(id="id-example", data=LabelServiceUpdateLabelBody(...))
    W->>API: POST /label/v202210/labels/{id}
    alt success
        API-->>W: UpdateLabelResponse
        W-->>C: UpdateLabelResponse
    else error status
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `id` | path | `string` | Yes |
| `data` | body | `LabelServiceUpdateLabelBody` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `UpdateLabelResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

client = KentikAPI()  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.label.update_label(
    id="id-example",
    data=LabelServiceUpdateLabelBody(...),
)
```

---

### `DELETE` `/label/v202210/labels/{id}`

Delete a label.

Deletes label with specified with id.

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.label
    participant API as Kentik API

    C->>W: delete_label(id="id-example")
    W->>API: DELETE /label/v202210/labels/{id}
    alt success
        API-->>W: DeleteLabelResponse
        W-->>C: DeleteLabelResponse
    else error status
        API-->>W: error body
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
| 200 | A successful response. | `DeleteLabelResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

client = KentikAPI()  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.label.delete_label(
    id="id-example",
)
```

## Data Models

<details>
<summary>Model relationships (9 of 9 models)</summary>

```mermaid
classDiagram
    class CreateLabelRequest
    class CreateLabelResponse
    class DeleteLabelResponse
    class LabelServiceUpdateLabelBody
    class ListLabelsResponse
    class UpdateLabelResponse
    class labelv202210Label
    class protobufAny
    class rpcStatus
    CreateLabelRequest --> labelv202210Label
    CreateLabelResponse --> labelv202210Label
    ListLabelsResponse --> labelv202210Label
    UpdateLabelResponse --> labelv202210Label
    rpcStatus --> protobufAny
```

</details>

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.label.models.CreateLabelRequest
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.label.models.CreateLabelResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.label.models.DeleteLabelResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.label.models.LabelServiceUpdateLabelBody
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.label.models.ListLabelsResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.label.models.UpdateLabelResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.label.models.labelv202210Label
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.label.models.protobufAny
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.label.models.rpcStatus
```
