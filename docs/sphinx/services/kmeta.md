<!-- AUTO-GENERATED: scripts/generation/endpoint_docs.py, render_endpoint_docs() -->
<!-- Rebuilt on every `make generate`. Do not edit by hand. -->

# Kmeta Service

## Overview

```mermaid
flowchart LR
    subgraph sdk["kentik_api"]
        KA["KentikAPI"]
        W["KmetaServiceWrapper\nclient.kmeta"]
        REST["REST functions\ngen/kmeta/services/"]
        RJ["request_json()\ncore/rest_runtime"]
        M["Models\ngen/kmeta/models/"]
        E["Error classes\ngen/kmeta/error/"]
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

### `GET` `/kmeta/v202607alpha1/{cid}/servicenow/config`

List ServiceNow Configs

Returns all ServiceNow integration configurations for the specified company.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.kmeta
    participant API as Kentik REST API

    C->>W: list_service_now_configs(cid="cid-example")
    W->>API: GET /kmeta/v202607alpha1/{cid}/servicenow/config
    alt success
        API-->>W: ListServiceNowConfigsResponse (JSON)
        W-->>C: ListServiceNowConfigsResponse
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
    participant W as client.kmeta
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: list_service_now_configs(cid="cid-example")
    W->>R: build_grpc_request(ListServiceNowConfigsRequest, arguments)
    R->>API: KmetaService/ListServiceNowConfigs (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: MessageToDict(response)
        W-->>C: ListServiceNowConfigsResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `cid` | path | `string` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `ListServiceNowConfigsResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.kmeta.list_service_now_configs(
    cid="cid-example",
)
```

---

### `POST` `/kmeta/v202607alpha1/{cid}/servicenow/config`

Create ServiceNow Config

Creates a new ServiceNow integration configuration for the specified company.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.kmeta
    participant API as Kentik REST API

    C->>W: create_service_now_config(cid="cid-example", data=ServiceNowConfig(...))
    W->>API: POST /kmeta/v202607alpha1/{cid}/servicenow/config
    alt success
        API-->>W: CreateServiceNowConfigResponse (JSON)
        W-->>C: CreateServiceNowConfigResponse
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
    participant W as client.kmeta
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: create_service_now_config(cid="cid-example", data=ServiceNowConfig(...))
    W->>R: build_grpc_request(CreateServiceNowConfigRequest, arguments)
    R->>API: KmetaService/CreateServiceNowConfig (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: MessageToDict(response)
        W-->>C: CreateServiceNowConfigResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `cid` | path | `string` | Yes |
| `data` | body | `ServiceNowConfig` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `CreateServiceNowConfigResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.kmeta.create_service_now_config(
    cid="cid-example",
    data=ServiceNowConfig(...),
)
```

---

### `GET` `/kmeta/v202607alpha1/{cid}/servicenow/config/{id}`

Get ServiceNow Config

Returns a single ServiceNow integration configuration.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.kmeta
    participant API as Kentik REST API

    C->>W: get_service_now_config(cid="cid-example", id="id-example")
    W->>API: GET /kmeta/v202607alpha1/{cid}/servicenow/config/{id}
    alt success
        API-->>W: GetServiceNowConfigResponse (JSON)
        W-->>C: GetServiceNowConfigResponse
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
    participant W as client.kmeta
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: get_service_now_config(cid="cid-example", id="id-example")
    W->>R: build_grpc_request(GetServiceNowConfigRequest, arguments)
    R->>API: KmetaService/GetServiceNowConfig (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: MessageToDict(response)
        W-->>C: GetServiceNowConfigResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `cid` | path | `string` | Yes |
| `id` | path | `string` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `GetServiceNowConfigResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.kmeta.get_service_now_config(
    cid="cid-example",
    id="id-example",
)
```

---

### `PUT` `/kmeta/v202607alpha1/{cid}/servicenow/config/{id}`

Update ServiceNow Config

Updates an existing ServiceNow integration configuration.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.kmeta
    participant API as Kentik REST API

    C->>W: update_service_now_config(cid="cid-example", id="id-example", data=ServiceNowConfig(...))
    W->>API: PUT /kmeta/v202607alpha1/{cid}/servicenow/config/{id}
    alt success
        API-->>W: UpdateServiceNowConfigResponse (JSON)
        W-->>C: UpdateServiceNowConfigResponse
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
    participant W as client.kmeta
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: update_service_now_config(cid="cid-example", id="id-example", data=ServiceNowConfig(...))
    W->>R: build_grpc_request(UpdateServiceNowConfigRequest, arguments)
    R->>API: KmetaService/UpdateServiceNowConfig (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: MessageToDict(response)
        W-->>C: UpdateServiceNowConfigResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `cid` | path | `string` | Yes |
| `id` | path | `string` | Yes |
| `data` | body | `ServiceNowConfig` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `UpdateServiceNowConfigResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.kmeta.update_service_now_config(
    cid="cid-example",
    id="id-example",
    data=ServiceNowConfig(...),
)
```

---

### `DELETE` `/kmeta/v202607alpha1/{cid}/servicenow/config/{id}`

Delete ServiceNow Config

Deletes a ServiceNow integration configuration.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.kmeta
    participant API as Kentik REST API

    C->>W: delete_service_now_config(cid="cid-example", id="id-example")
    W->>API: DELETE /kmeta/v202607alpha1/{cid}/servicenow/config/{id}
    alt success
        API-->>W: DeleteServiceNowConfigResponse (JSON)
        W-->>C: DeleteServiceNowConfigResponse
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
    participant W as client.kmeta
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: delete_service_now_config(cid="cid-example", id="id-example")
    W->>R: build_grpc_request(DeleteServiceNowConfigRequest, arguments)
    R->>API: KmetaService/DeleteServiceNowConfig (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: MessageToDict(response)
        W-->>C: DeleteServiceNowConfigResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `cid` | path | `string` | Yes |
| `id` | path | `string` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `DeleteServiceNowConfigResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.kmeta.delete_service_now_config(
    cid="cid-example",
    id="id-example",
)
```

## Data Models

<details>
<summary>Model relationships (8 of 8 models)</summary>

```mermaid
classDiagram
    class CreateServiceNowConfigResponse
    class DeleteServiceNowConfigResponse
    class GetServiceNowConfigResponse
    class ListServiceNowConfigsResponse
    class ServiceNowConfig
    class UpdateServiceNowConfigResponse
    class protobufAny
    class rpcStatus
    CreateServiceNowConfigResponse --> ServiceNowConfig
    GetServiceNowConfigResponse --> ServiceNowConfig
    ListServiceNowConfigsResponse --> ServiceNowConfig
    UpdateServiceNowConfigResponse --> ServiceNowConfig
    rpcStatus --> protobufAny
```

</details>

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.kmeta.models.CreateServiceNowConfigResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.kmeta.models.DeleteServiceNowConfigResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.kmeta.models.GetServiceNowConfigResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.kmeta.models.ListServiceNowConfigsResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.kmeta.models.ServiceNowConfig
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.kmeta.models.UpdateServiceNowConfigResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.kmeta.models.protobufAny
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.kmeta.models.rpcStatus
```
