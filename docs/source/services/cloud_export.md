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

    click KA "../../../src/kentik_api/client.py"
    click W "../../../src/kentik_api/gen/cloud_export/services/cloud_export.py"
    click REST "../../../src/kentik_api/gen/cloud_export/services/"
    click RJ "../../../src/kentik_api/core/rest_runtime.py"
    click M "../../../src/kentik_api/gen/cloud_export/models/"
    click E "../../../src/kentik_api/gen/cloud_export/error/__init__.py"
```

## Endpoints

### `GET` `/cloud_export/v202506/exports`

List cloud exports.

Returns a list of all cloud exports in the account.

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.cloud_export
    participant API as Kentik API

    C->>W: list_cloud_exports()
    W->>API: GET /cloud_export/v202506/exports
    alt success
        API-->>W: ListCloudExportsResponse
        W-->>C: ListCloudExportsResponse
    else error status
        API-->>W: error body
        W-->>C: raise HTTPException
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

client = KentikAPI()  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.cloud_export.list_cloud_exports()
```

---

### `POST` `/cloud_export/v202506/exports`

Create Cloud Export.

Create new cloud export based on configuration in the request.

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.cloud_export
    participant API as Kentik API

    C->>W: create_cloud_export(data=CreateCloudExportRequest(...))
    W->>API: POST /cloud_export/v202506/exports
    alt success
        API-->>W: CreateCloudExportResponse
        W-->>C: CreateCloudExportResponse
    else error status
        API-->>W: error body
        W-->>C: raise HTTPException
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

client = KentikAPI()  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.cloud_export.create_cloud_export(
    data=CreateCloudExportRequest(...),
)
```

---

### `GET` `/cloud_export/v202506/exports/{export.id}`

Get cloud export configuration and status.

Returns configuration and status of cloud export with specified ID.

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.cloud_export
    participant API as Kentik API

    C->>W: get_cloud_export(exportid="exportid-example")
    W->>API: GET /cloud_export/v202506/exports/{export.id}
    alt success
        API-->>W: GetCloudExportResponse
        W-->>C: GetCloudExportResponse
    else error status
        API-->>W: error body
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
| 200 | A successful response. | `GetCloudExportResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

client = KentikAPI()  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.cloud_export.get_cloud_export(
    exportid="exportid-example",
)
```

---

### `PUT` `/cloud_export/v202506/exports/{export.id}`

Update configuration of cloud export.

Replace complete configuration of a cloud export with data in the request.

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.cloud_export
    participant API as Kentik API

    C->>W: update_cloud_export(exportid="exportid-example", data=CloudExportAdminServiceUpdateCloudExportBody(...))
    W->>API: PUT /cloud_export/v202506/exports/{export.id}
    alt success
        API-->>W: UpdateCloudExportResponse
        W-->>C: UpdateCloudExportResponse
    else error status
        API-->>W: error body
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
| 200 | A successful response. | `UpdateCloudExportResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

client = KentikAPI()  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.cloud_export.update_cloud_export(
    exportid="exportid-example",
    data=CloudExportAdminServiceUpdateCloudExportBody(...),
)
```

---

### `DELETE` `/cloud_export/v202506/exports/{export.id}`

Delete a cloud export.

Delete cloud export with specified ID.

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.cloud_export
    participant API as Kentik API

    C->>W: delete_cloud_export(exportid="exportid-example")
    W->>API: DELETE /cloud_export/v202506/exports/{export.id}
    alt success
        API-->>W: DeleteCloudExportResponse
        W-->>C: DeleteCloudExportResponse
    else error status
        API-->>W: error body
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
| 200 | A successful response. | `DeleteCloudExportResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

client = KentikAPI()  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
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
