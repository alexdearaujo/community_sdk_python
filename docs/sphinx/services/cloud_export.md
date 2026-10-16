<!-- AUTO-GENERATED: scripts/generation/endpoint_docs.py, render_endpoint_docs() -->
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
        API-->>W: ListCloudExportsResponse (JSON)
        W-->>C: ListCloudExportsResponse
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
    participant W as client.cloud_export
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: list_cloud_exports()
    W->>R: build_grpc_request(ListCloudExportsRequest, arguments)
    R->>API: CloudExportAdminService/ListCloudExports (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: MessageToDict(response)
        W-->>C: ListCloudExportsResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `ListCloudExportsResponse` |
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
        API-->>W: CreateCloudExportResponse (JSON)
        W-->>C: CreateCloudExportResponse
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
    participant W as client.cloud_export
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: create_cloud_export(data=CreateCloudExportRequest(...))
    W->>R: build_grpc_request(CreateCloudExportRequest, arguments)
    R->>API: CloudExportAdminService/CreateCloudExport (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: MessageToDict(response)
        W-->>C: CreateCloudExportResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `data` | body | `CreateCloudExportRequest` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `CreateCloudExportResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI
from kentik_api.gen.cloud_export.models import CreateCloudExportRequest

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
        API-->>W: GetCloudExportResponse (JSON)
        W-->>C: GetCloudExportResponse
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
    participant W as client.cloud_export
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: get_cloud_export(exportid="exportid-example")
    W->>R: build_grpc_request(GetCloudExportRequest, arguments)
    R->>API: CloudExportAdminService/GetCloudExport (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: MessageToDict(response)
        W-->>C: GetCloudExportResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `exportid` | path | `string` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `GetCloudExportResponse` |
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
        API-->>W: UpdateCloudExportResponse (JSON)
        W-->>C: UpdateCloudExportResponse
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
    participant W as client.cloud_export
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: update_cloud_export(exportid="exportid-example", data=CloudExportAdminServiceUpdateCloudExportBody(...))
    W->>R: build_grpc_request(UpdateCloudExportRequest, arguments)
    R->>API: CloudExportAdminService/UpdateCloudExport (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: MessageToDict(response)
        W-->>C: UpdateCloudExportResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
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
| 200 | A successful response. | `UpdateCloudExportResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI
from kentik_api.gen.cloud_export.models import CloudExportAdminServiceUpdateCloudExportBody

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
        API-->>W: DeleteCloudExportResponse (JSON)
        W-->>C: DeleteCloudExportResponse
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
    participant W as client.cloud_export
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: delete_cloud_export(exportid="exportid-example")
    W->>R: build_grpc_request(DeleteCloudExportRequest, arguments)
    R->>API: CloudExportAdminService/DeleteCloudExport (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: MessageToDict(response)
        W-->>C: DeleteCloudExportResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `exportid` | path | `string` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `DeleteCloudExportResponse` |
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
<summary>Model relationships (10 of 19 models)</summary>

```mermaid
classDiagram
    class CloudExport
    class CloudExportAdminServiceUpdateCloudExportBody
    class CreateCloudExportRequest
    class CreateCloudExportResponse
    class DeleteCloudExportResponse
    class GetCloudExportResponse
    class ListCloudExportsResponse
    class UpdateCloudExportResponse
    class protobufAny
    class rpcStatus
    CreateCloudExportRequest --> CloudExport
    CreateCloudExportResponse --> CloudExport
    GetCloudExportResponse --> CloudExport
    ListCloudExportsResponse --> CloudExport
    UpdateCloudExportResponse --> CloudExport
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
