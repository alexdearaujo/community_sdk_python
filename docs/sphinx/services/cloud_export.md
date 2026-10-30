<!-- AUTO-GENERATED: scripts/generation/endpoint_docs.py, render_endpoint_docs() -->
<!-- Rebuilt on every `uv run poe generate`. Do not edit by hand. -->

# Cloud Export Service

## Overview

```mermaid
%%{init: {"fontFamily": "ui-monospace, SFMono-Regular, Menlo, monospace", "flowchart": {"curve": "step", "nodeSpacing": 30, "rankSpacing": 70, "wrappingWidth": 400}}}%%
flowchart LR
    code("Your code"):::greenSrc
    subgraph sdk["kentik_api"]
        wrap("CloudExportServiceWrapper<br/>client.cloud_export<br/>5 operations"):::orange
        rest("REST functions<br/>gen/cloud_export/services/"):::blue
        rj("request_json()<br/>core/rest_runtime.py"):::blue
        cg("call_grpc()<br/>core/grpc_runtime.py"):::violet
    end
    grpcapi("Kentik gRPC API<br/>HTTP/2 + protobuf"):::violetSrc
    restapi("Kentik REST API<br/>HTTPS + JSON"):::blueSrc

    code -->|"method call"| wrap
    wrap -->|"Pydantic model from<br/>gen/cloud_export/models/"| code
    wrap -->|"arguments"| rest
    rest -->|"Pydantic model"| wrap
    rest -->|"method, path, body"| rj
    rj -->|"JSON dict"| rest
    rj -->|"HTTPS request"| restapi
    restapi -->|"JSON response"| rj
    wrap -->|"proto request"| cg
    cg -->|"proto response"| wrap
    cg -->|"gRPC call"| grpcapi
    grpcapi -->|"proto response"| cg

    classDef greenSrc fill:#b2f2bb,stroke:#2f9e44,color:#2b8a3e
    classDef orange fill:#fff4e6,stroke:#e8590c,color:#d9480f
    classDef blue fill:#e7f5ff,stroke:#1971c2,color:#1864ab
    classDef blueSrc fill:#a5d8ff,stroke:#1971c2,color:#1864ab
    classDef violet fill:#f3f0ff,stroke:#7048e8,color:#5f3dc4
    classDef violetSrc fill:#d0bfff,stroke:#7048e8,color:#5f3dc4
    classDef greenSrc,orange,blue,blueSrc,violet,violetSrc stroke-width:2px,rx:10px
    style sdk fill:none,stroke:#868e96,stroke-width:2px
    linkStyle default stroke-width:2px,stroke-linecap:round,stroke-linejoin:round
```

On an error status or a failed call, the SDK raises an error class from `gen/cloud_export/error/`, or a shared type from `kentik_api.errors`.

## Endpoints

### `GET` `/cloud_export/v202506/exports`

List cloud exports.

Returns a list of all cloud exports in the account.

#### REST call flow

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.cloud_export
    participant API as Kentik REST API

    C->>W: list()
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

#### gRPC call flow

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.cloud_export
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: list()
    W->>R: build_grpc_request(ListCloudExportsRequest, arguments)
    R->>API: CloudExportAdminService/ListCloudExports (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: parse_grpc_response(response)
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
response = client.cloud_export.list()
```

---

### `POST` `/cloud_export/v202506/exports`

Create Cloud Export.

Create new cloud export based on configuration in the request.

#### REST call flow

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.cloud_export
    participant API as Kentik REST API

    C->>W: create(data=CreateCloudExportRequest(...))
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

#### gRPC call flow

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.cloud_export
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: create(data=CreateCloudExportRequest(...))
    W->>R: build_grpc_request(CreateCloudExportRequest, arguments)
    R->>API: CloudExportAdminService/CreateCloudExport (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: parse_grpc_response(response)
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
response = client.cloud_export.create(
    data=CreateCloudExportRequest(...),
)
```

---

### `GET` `/cloud_export/v202506/exports/{export.id}`

Get cloud export configuration and status.

Returns configuration and status of cloud export with specified ID.

#### REST call flow

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.cloud_export
    participant API as Kentik REST API

    C->>W: get(exportid="exportid-example")
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

#### gRPC call flow

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.cloud_export
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: get(exportid="exportid-example")
    W->>R: build_grpc_request(GetCloudExportRequest, arguments)
    R->>API: CloudExportAdminService/GetCloudExport (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: parse_grpc_response(response)
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
response = client.cloud_export.get(
    exportid="exportid-example",
)
```

---

### `PUT` `/cloud_export/v202506/exports/{export.id}`

Update configuration of cloud export.

Replace complete configuration of a cloud export with data in the request.

#### REST call flow

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.cloud_export
    participant API as Kentik REST API

    C->>W: update(exportid="exportid-example", data=CloudExportAdminServiceUpdateCloudExportBody(...))
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

#### gRPC call flow

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.cloud_export
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: update(exportid="exportid-example", data=CloudExportAdminServiceUpdateCloudExportBody(...))
    W->>R: build_grpc_request(UpdateCloudExportRequest, arguments)
    R->>API: CloudExportAdminService/UpdateCloudExport (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: parse_grpc_response(response)
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
from kentik_api.gen.cloud_export.models import (
    CloudExportAdminServiceUpdateCloudExportBody,
)

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.cloud_export.update(
    exportid="exportid-example",
    data=CloudExportAdminServiceUpdateCloudExportBody(...),
)
```

---

### `DELETE` `/cloud_export/v202506/exports/{export.id}`

Delete a cloud export.

Delete cloud export with specified ID.

#### REST call flow

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.cloud_export
    participant API as Kentik REST API

    C->>W: delete(exportid="exportid-example")
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

#### gRPC call flow

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.cloud_export
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: delete(exportid="exportid-example")
    W->>R: build_grpc_request(DeleteCloudExportRequest, arguments)
    R->>API: CloudExportAdminService/DeleteCloudExport (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: parse_grpc_response(response)
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
response = client.cloud_export.delete(
    exportid="exportid-example",
)
```

## Data Models

<details>
<summary>Model relationships (10 of 19 models)</summary>

Each arrow points from a model to a model that one of its fields holds. The label names the field.

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
    CreateCloudExportRequest --> CloudExport : export
    CreateCloudExportResponse --> CloudExport : export
    GetCloudExportResponse --> CloudExport : export
    ListCloudExportsResponse --> CloudExport : exports
    UpdateCloudExportResponse --> CloudExport : export
    rpcStatus --> protobufAny : details
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
