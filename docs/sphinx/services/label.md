<!-- AUTO-GENERATED: scripts/generation/endpoint_docs.py, render_endpoint_docs() -->
<!-- Rebuilt on every `make generate`. Do not edit by hand. -->

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

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.label
    participant API as Kentik REST API

    C->>W: list_labels()
    W->>API: GET /label/v202210/labels
    alt success
        API-->>W: v202210ListLabelsResponse (JSON)
        W-->>C: v202210ListLabelsResponse
    else error
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

**gRPC transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.label
    participant B as proto bridge
    participant API as Kentik gRPC API

    C->>W: list_labels()
    W->>B: ParseDict(params, ListLabelsRequest)
    B->>API: list_labels (gRPC/TLS)
    alt success
        API-->>B: v202210ListLabelsResponse proto
        B-->>W: MessageToDict(response)
        W-->>C: v202210ListLabelsResponse
    else gRPC error
        API-->>B: gRPC status + details
        B-->>W: raise HTTPException
        W-->>C: raise HTTPException
    end
```

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `v202210ListLabelsResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.label.list_labels()
```

---

### `POST` `/label/v202210/labels`

Create a new label.

Creates a new label based on data in the request.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.label
    participant API as Kentik REST API

    C->>W: create_label(data=CreateLabelRequest(...))
    W->>API: POST /label/v202210/labels
    alt success
        API-->>W: v202210CreateLabelResponse (JSON)
        W-->>C: v202210CreateLabelResponse
    else error
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

**gRPC transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.label
    participant B as proto bridge
    participant API as Kentik gRPC API

    C->>W: create_label(data=CreateLabelRequest(...))
    W->>B: ParseDict(params, CreateLabelRequest)
    B->>API: create_label (gRPC/TLS)
    alt success
        API-->>B: v202210CreateLabelResponse proto
        B-->>W: MessageToDict(response)
        W-->>C: v202210CreateLabelResponse
    else gRPC error
        API-->>B: gRPC status + details
        B-->>W: raise HTTPException
        W-->>C: raise HTTPException
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `data` | body | `v202210CreateLabelRequest` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `v202210CreateLabelResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.label.create_label(
    data=CreateLabelRequest(...),
)
```

---

### `POST` `/label/v202210/labels/{id}`

Update an existing label.

Updates configuration of a label.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.label
    participant API as Kentik REST API

    C->>W: update_label(id="id-example", data=LabelServiceUpdateLabelBody(...))
    W->>API: POST /label/v202210/labels/{id}
    alt success
        API-->>W: v202210UpdateLabelResponse (JSON)
        W-->>C: v202210UpdateLabelResponse
    else error
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

**gRPC transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.label
    participant B as proto bridge
    participant API as Kentik gRPC API

    C->>W: update_label(id="id-example", data=LabelServiceUpdateLabelBody(...))
    W->>B: ParseDict(params, UpdateLabelRequest)
    B->>API: update_label (gRPC/TLS)
    alt success
        API-->>B: v202210UpdateLabelResponse proto
        B-->>W: MessageToDict(response)
        W-->>C: v202210UpdateLabelResponse
    else gRPC error
        API-->>B: gRPC status + details
        B-->>W: raise HTTPException
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
| 200 | A successful response. | `v202210UpdateLabelResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.label.update_label(
    id="id-example",
    data=LabelServiceUpdateLabelBody(...),
)
```

---

### `DELETE` `/label/v202210/labels/{id}`

Delete a label.

Deletes label with specified with id.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.label
    participant API as Kentik REST API

    C->>W: delete_label(id="id-example")
    W->>API: DELETE /label/v202210/labels/{id}
    alt success
        API-->>W: v202210DeleteLabelResponse (JSON)
        W-->>C: v202210DeleteLabelResponse
    else error
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

**gRPC transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.label
    participant B as proto bridge
    participant API as Kentik gRPC API

    C->>W: delete_label(id="id-example")
    W->>B: ParseDict(params, DeleteLabelRequest)
    B->>API: delete_label (gRPC/TLS)
    alt success
        API-->>B: v202210DeleteLabelResponse proto
        B-->>W: MessageToDict(response)
        W-->>C: v202210DeleteLabelResponse
    else gRPC error
        API-->>B: gRPC status + details
        B-->>W: raise HTTPException
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
| 200 | A successful response. | `v202210DeleteLabelResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.label.delete_label(
    id="id-example",
)
```

## Data Models

<details>
<summary>Model relationships (3 of 9 models)</summary>

```mermaid
classDiagram
    class LabelServiceUpdateLabelBody
    class protobufAny
    class rpcStatus
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
