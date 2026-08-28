<!-- AUTO-GENERATED: scripts/generation/endpoint_docs.py, _render_sphinx_stubs() -->
<!-- Rebuilt on every `make generate`. Do not edit by hand. -->

# Cloud Export Service

## Overview

```mermaid
flowchart LR
    subgraph sdk["kentik_api"]
        KA["KentikAPI"]
        W["Cloud ExportServiceWrapper\nclient.cloud_export"]
        REST["REST functions\ngen/cloud_export/services/"]
        RJ["request_json()\ncore/rest_runtime"]
        M["Models\ngen/cloud_export/models/"]
        E["Error classes\ngen/cloud_export/error/"]
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

### `GET` `/cloud_export/v202506/exports`

List cloud exports.

Returns a list of all cloud exports in the account.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.cloud_export
    participant API as Kentik REST API

    C->>W: list_cloud_exports()
    W->>API: GET /cloud_export/v202506/exports
    alt success
        API-->>W: v202506ListCloudExportsResponse (JSON)
        W-->>C: v202506ListCloudExportsResponse
    else error
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

**gRPC transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.cloud_export
    participant B as proto bridge
    participant API as Kentik gRPC API

    C->>W: list_cloud_exports()
    W->>B: ParseDict(params, ListCloudExportsRequest)
    B->>API: list_cloud_exports (gRPC/TLS)
    alt success
        API-->>B: v202506ListCloudExportsResponse proto
        B-->>W: MessageToDict(response)
        W-->>C: v202506ListCloudExportsResponse
    else gRPC error
        API-->>B: gRPC status + details
        B-->>W: raise HTTPException
        W-->>C: raise HTTPException
    end
```

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `v202506ListCloudExportsResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.cloud_export.list_cloud_exports()
```

---

### `POST` `/cloud_export/v202506/exports`

Create Cloud Export.

Create new cloud export based on configuration in the request.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.cloud_export
    participant API as Kentik REST API

    C->>W: create_cloud_export(data=CreateCloudExportRequest(...))
    W->>API: POST /cloud_export/v202506/exports
    alt success
        API-->>W: v202506CreateCloudExportResponse (JSON)
        W-->>C: v202506CreateCloudExportResponse
    else error
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

**gRPC transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.cloud_export
    participant B as proto bridge
    participant API as Kentik gRPC API

    C->>W: create_cloud_export(data=CreateCloudExportRequest(...))
    W->>B: ParseDict(params, CreateCloudExportRequest)
    B->>API: create_cloud_export (gRPC/TLS)
    alt success
        API-->>B: v202506CreateCloudExportResponse proto
        B-->>W: MessageToDict(response)
        W-->>C: v202506CreateCloudExportResponse
    else gRPC error
        API-->>B: gRPC status + details
        B-->>W: raise HTTPException
        W-->>C: raise HTTPException
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `data` | body | `v202506CreateCloudExportRequest` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `v202506CreateCloudExportResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.cloud_export.create_cloud_export(
    data=CreateCloudExportRequest(...),
)
```

---

### `GET` `/cloud_export/v202506/exports/{export.id}`

Get cloud export configuration and status.

Returns configuration and status of cloud export with specified ID.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.cloud_export
    participant API as Kentik REST API

    C->>W: get_cloud_export(exportid="exportid-example")
    W->>API: GET /cloud_export/v202506/exports/{export.id}
    alt success
        API-->>W: v202506GetCloudExportResponse (JSON)
        W-->>C: v202506GetCloudExportResponse
    else error
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

**gRPC transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.cloud_export
    participant B as proto bridge
    participant API as Kentik gRPC API

    C->>W: get_cloud_export(exportid="exportid-example")
    W->>B: ParseDict(params, GetCloudExportRequest)
    B->>API: get_cloud_export (gRPC/TLS)
    alt success
        API-->>B: v202506GetCloudExportResponse proto
        B-->>W: MessageToDict(response)
        W-->>C: v202506GetCloudExportResponse
    else gRPC error
        API-->>B: gRPC status + details
        B-->>W: raise HTTPException
        W-->>C: raise HTTPException
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `exportid` | path | `string` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `v202506GetCloudExportResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.cloud_export.get_cloud_export(
    exportid="exportid-example",
)
```

---

### `PUT` `/cloud_export/v202506/exports/{export.id}`

Update configuration of cloud export.

Replace complete configuration of a cloud export with data in the request.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.cloud_export
    participant API as Kentik REST API

    C->>W: update_cloud_export(exportid="exportid-example", data=CloudExportAdminServiceUpdateCloudExportBody(...))
    W->>API: PUT /cloud_export/v202506/exports/{export.id}
    alt success
        API-->>W: v202506UpdateCloudExportResponse (JSON)
        W-->>C: v202506UpdateCloudExportResponse
    else error
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

**gRPC transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.cloud_export
    participant B as proto bridge
    participant API as Kentik gRPC API

    C->>W: update_cloud_export(exportid="exportid-example", data=CloudExportAdminServiceUpdateCloudExportBody(...))
    W->>B: ParseDict(params, UpdateCloudExportRequest)
    B->>API: update_cloud_export (gRPC/TLS)
    alt success
        API-->>B: v202506UpdateCloudExportResponse proto
        B-->>W: MessageToDict(response)
        W-->>C: v202506UpdateCloudExportResponse
    else gRPC error
        API-->>B: gRPC status + details
        B-->>W: raise HTTPException
        W-->>C: raise HTTPException
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `exportid` | path | `string` | Yes |
| `data` | body | `CloudExportAdminServiceUpdateCloudExportBody` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `v202506UpdateCloudExportResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.cloud_export.update_cloud_export(
    exportid="exportid-example",
    data=CloudExportAdminServiceUpdateCloudExportBody(...),
)
```

---

### `DELETE` `/cloud_export/v202506/exports/{export.id}`

Delete a cloud export.

Delete cloud export with specified ID.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.cloud_export
    participant API as Kentik REST API

    C->>W: delete_cloud_export(exportid="exportid-example")
    W->>API: DELETE /cloud_export/v202506/exports/{export.id}
    alt success
        API-->>W: v202506DeleteCloudExportResponse (JSON)
        W-->>C: v202506DeleteCloudExportResponse
    else error
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

**gRPC transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.cloud_export
    participant B as proto bridge
    participant API as Kentik gRPC API

    C->>W: delete_cloud_export(exportid="exportid-example")
    W->>B: ParseDict(params, DeleteCloudExportRequest)
    B->>API: delete_cloud_export (gRPC/TLS)
    alt success
        API-->>B: v202506DeleteCloudExportResponse proto
        B-->>W: MessageToDict(response)
        W-->>C: v202506DeleteCloudExportResponse
    else gRPC error
        API-->>B: gRPC status + details
        B-->>W: raise HTTPException
        W-->>C: raise HTTPException
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `exportid` | path | `string` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `v202506DeleteCloudExportResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.cloud_export.delete_cloud_export(
    exportid="exportid-example",
)
```

## Data Models

<details>
<summary>Model relationships (3 of 19 models)</summary>

```mermaid
classDiagram
    class CloudExportAdminServiceUpdateCloudExportBody
    class protobufAny
    class rpcStatus
    rpcStatus --> protobufAny
```

</details>

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.cloud_export.models.AwsProperties
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.cloud_export.models.AzureProperties
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.cloud_export.models.CloudExport
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.cloud_export.models.CloudExportAdminServiceUpdateCloudExportBody
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.cloud_export.models.CloudExportSamplingProperties
```

```{eval-rst}
.. autoclass:: kentik_api.gen.cloud_export.models.CloudExportSamplingType
   :members:
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.cloud_export.models.CloudExportStatus
```

```{eval-rst}
.. autoclass:: kentik_api.gen.cloud_export.models.CloudExportType
   :members:
```

```{eval-rst}
.. autoclass:: kentik_api.gen.cloud_export.models.CloudProvider
   :members:
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.cloud_export.models.CreateCloudExportRequest
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.cloud_export.models.CreateCloudExportResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.cloud_export.models.DeleteCloudExportResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.cloud_export.models.GceProperties
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.cloud_export.models.GetCloudExportResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.cloud_export.models.ListCloudExportsResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.cloud_export.models.OciProperties
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.cloud_export.models.UpdateCloudExportResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.cloud_export.models.protobufAny
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.cloud_export.models.rpcStatus
```
