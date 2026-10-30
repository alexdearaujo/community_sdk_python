<!-- AUTO-GENERATED: scripts/generation/endpoint_docs.py, render_endpoint_docs() -->
<!-- Rebuilt on every `uv run poe generate`. Do not edit by hand. -->

# Bgp Monitoring Service

## Overview

```mermaid
%%{init: {"fontFamily": "ui-monospace, SFMono-Regular, Menlo, monospace", "flowchart": {"curve": "step", "nodeSpacing": 30, "rankSpacing": 70, "wrappingWidth": 400}}}%%
flowchart LR
    code("Your code"):::greenSrc
    subgraph sdk["kentik_api"]
        wrap("BgpMonitoringServiceWrapper<br/>client.bgp_monitoring<br/>8 operations"):::orange
        rest("REST functions<br/>gen/bgp_monitoring/services/"):::blue
        rj("request_json()<br/>core/rest_runtime.py"):::blue
        cg("call_grpc()<br/>core/grpc_runtime.py"):::violet
    end
    grpcapi("Kentik gRPC API<br/>HTTP/2 + protobuf"):::violetSrc
    restapi("Kentik REST API<br/>HTTPS + JSON"):::blueSrc

    code -->|"method call"| wrap
    wrap -->|"Pydantic model from<br/>gen/bgp_monitoring/models/"| code
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

On an error status or a failed call, the SDK raises an error class from `gen/bgp_monitoring/error/`, or a shared type from `kentik_api.errors`.

## Endpoints

### BgpMonitoringDataService

#### `POST` `/bgp_monitoring/v202210/metrics`

Get metrics for a BGP prefix.

Retrieve metric data for single BGP prefix and time interval.

##### REST call flow

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.bgp_monitoring
    participant API as Kentik REST API

    C->>W: get_metrics_for_target(data=GetMetricsForTargetRequest(...))
    W->>API: POST /bgp_monitoring/v202210/metrics
    alt success
        API-->>W: GetMetricsForTargetResponse (JSON)
        W-->>C: GetMetricsForTargetResponse
    else error status
        API-->>W: error body
        W-->>C: raise AuthenticationError (401) or HTTPException
    else no response
        W-->>C: raise TransportError
    end
```

##### gRPC call flow

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.bgp_monitoring
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: get_metrics_for_target(data=GetMetricsForTargetRequest(...))
    W->>R: build_grpc_request(GetMetricsForTargetRequest, arguments)
    R->>API: BgpMonitoringDataService/GetMetricsForTarget (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: parse_grpc_response(response)
        W-->>C: GetMetricsForTargetResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

##### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `data` | body | `GetMetricsForTargetRequest` | Yes |

##### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `GetMetricsForTargetResponse` |
| default | An unexpected error response. | `rpcStatus` |

##### Example

```python
from kentik_api.client import KentikAPI
from kentik_api.gen.bgp_monitoring.models import GetMetricsForTargetRequest

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.bgp_monitoring.get_metrics_for_target(
    data=GetMetricsForTargetRequest(...),
)
```

---

#### `POST` `/bgp_monitoring/v202210/routes`

Get routes for a BGP prefix.

Retrieve snapshot of route information for single BGP prefix at specific time.

##### REST call flow

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.bgp_monitoring
    participant API as Kentik REST API

    C->>W: get_routes_for_target(data=GetRoutesForTargetRequest(...))
    W->>API: POST /bgp_monitoring/v202210/routes
    alt success
        API-->>W: GetRoutesForTargetResponse (JSON)
        W-->>C: GetRoutesForTargetResponse
    else error status
        API-->>W: error body
        W-->>C: raise AuthenticationError (401) or HTTPException
    else no response
        W-->>C: raise TransportError
    end
```

##### gRPC call flow

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.bgp_monitoring
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: get_routes_for_target(data=GetRoutesForTargetRequest(...))
    W->>R: build_grpc_request(GetRoutesForTargetRequest, arguments)
    R->>API: BgpMonitoringDataService/GetRoutesForTarget (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: parse_grpc_response(response)
        W-->>C: GetRoutesForTargetResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

##### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `data` | body | `GetRoutesForTargetRequest` | Yes |

##### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `GetRoutesForTargetResponse` |
| default | An unexpected error response. | `rpcStatus` |

##### Example

```python
from kentik_api.client import KentikAPI
from kentik_api.gen.bgp_monitoring.models import GetRoutesForTargetRequest

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.bgp_monitoring.get_routes_for_target(
    data=GetRoutesForTargetRequest(...),
)
```

### BgpMonitoringAdminService

#### `GET` `/bgp_monitoring/v202210/monitors`

List BGP Monitors.

Returns list of all BGP monitors present in the account.

##### REST call flow

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.bgp_monitoring
    participant API as Kentik REST API

    C->>W: list_monitors()
    W->>API: GET /bgp_monitoring/v202210/monitors
    alt success
        API-->>W: ListMonitorsResponse (JSON)
        W-->>C: ListMonitorsResponse
    else error status
        API-->>W: error body
        W-->>C: raise AuthenticationError (401) or HTTPException
    else no response
        W-->>C: raise TransportError
    end
```

##### gRPC call flow

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.bgp_monitoring
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: list_monitors()
    W->>R: build_grpc_request(ListMonitorsRequest, arguments)
    R->>API: BgpMonitoringAdminService/ListMonitors (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: parse_grpc_response(response)
        W-->>C: ListMonitorsResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

##### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `ListMonitorsResponse` |
| default | An unexpected error response. | `rpcStatus` |

##### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.bgp_monitoring.list_monitors()
```

---

#### `POST` `/bgp_monitoring/v202210/monitors`

Create new BGP Monitor instance.

Creates new BGP Monitor and if successful returns its configuration.

##### REST call flow

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.bgp_monitoring
    participant API as Kentik REST API

    C->>W: create_monitor(data=CreateMonitorRequest(...))
    W->>API: POST /bgp_monitoring/v202210/monitors
    alt success
        API-->>W: CreateMonitorResponse (JSON)
        W-->>C: CreateMonitorResponse
    else error status
        API-->>W: error body
        W-->>C: raise AuthenticationError (401) or HTTPException
    else no response
        W-->>C: raise TransportError
    end
```

##### gRPC call flow

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.bgp_monitoring
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: create_monitor(data=CreateMonitorRequest(...))
    W->>R: build_grpc_request(CreateMonitorRequest, arguments)
    R->>API: BgpMonitoringAdminService/CreateMonitor (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: parse_grpc_response(response)
        W-->>C: CreateMonitorResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

##### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `data` | body | `CreateMonitorRequest` | Yes |

##### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `CreateMonitorResponse` |
| default | An unexpected error response. | `rpcStatus` |

##### Example

```python
from kentik_api.client import KentikAPI
from kentik_api.gen.bgp_monitoring.models import CreateMonitorRequest

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.bgp_monitoring.create_monitor(
    data=CreateMonitorRequest(...),
)
```

---

#### `GET` `/bgp_monitoring/v202210/monitors/{id}`

Get BGP Monitor configuration.

Returns configuration of existing BGP monitor with specific ID.

##### REST call flow

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.bgp_monitoring
    participant API as Kentik REST API

    C->>W: get_monitor(id="id-example")
    W->>API: GET /bgp_monitoring/v202210/monitors/{id}
    alt success
        API-->>W: GetMonitorResponse (JSON)
        W-->>C: GetMonitorResponse
    else error status
        API-->>W: error body
        W-->>C: raise AuthenticationError (401) or HTTPException
    else no response
        W-->>C: raise TransportError
    end
```

##### gRPC call flow

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.bgp_monitoring
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: get_monitor(id="id-example")
    W->>R: build_grpc_request(GetMonitorRequest, arguments)
    R->>API: BgpMonitoringAdminService/GetMonitor (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: parse_grpc_response(response)
        W-->>C: GetMonitorResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

##### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `id` | path | `string` | Yes |

##### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `GetMonitorResponse` |
| default | An unexpected error response. | `rpcStatus` |

##### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.bgp_monitoring.get_monitor(
    id="id-example",
)
```

---

#### `PUT` `/bgp_monitoring/v202210/monitors/{id}`

Update configuration of a BGP monitor.

Updates configuration of BGP monitor with specific ID and returns updated  configuration.

##### REST call flow

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.bgp_monitoring
    participant API as Kentik REST API

    C->>W: update_monitor(id="id-example", data=BgpMonitoringAdminServiceUpdateMonitorBody(...))
    W->>API: PUT /bgp_monitoring/v202210/monitors/{id}
    alt success
        API-->>W: UpdateMonitorResponse (JSON)
        W-->>C: UpdateMonitorResponse
    else error status
        API-->>W: error body
        W-->>C: raise AuthenticationError (401) or HTTPException
    else no response
        W-->>C: raise TransportError
    end
```

##### gRPC call flow

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.bgp_monitoring
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: update_monitor(id="id-example", data=BgpMonitoringAdminServiceUpdateMonitorBody(...))
    W->>R: build_grpc_request(UpdateMonitorRequest, arguments)
    R->>API: BgpMonitoringAdminService/UpdateMonitor (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: parse_grpc_response(response)
        W-->>C: UpdateMonitorResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

##### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `id` | path | `string` | Yes |
| `data` | body | `BgpMonitoringAdminServiceUpdateMonitorBody` | Yes |

##### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `UpdateMonitorResponse` |
| default | An unexpected error response. | `rpcStatus` |

##### Example

```python
from kentik_api.client import KentikAPI
from kentik_api.gen.bgp_monitoring.models import (
    BgpMonitoringAdminServiceUpdateMonitorBody,
)

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.bgp_monitoring.update_monitor(
    id="id-example",
    data=BgpMonitoringAdminServiceUpdateMonitorBody(...),
)
```

---

#### `DELETE` `/bgp_monitoring/v202210/monitors/{id}`

Delete existing BGP Monitor.

Delete BGP monitor with with specific ID.

##### REST call flow

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.bgp_monitoring
    participant API as Kentik REST API

    C->>W: delete_monitor(id="id-example")
    W->>API: DELETE /bgp_monitoring/v202210/monitors/{id}
    alt success
        API-->>W: DeleteMonitorResponse (JSON)
        W-->>C: DeleteMonitorResponse
    else error status
        API-->>W: error body
        W-->>C: raise AuthenticationError (401) or HTTPException
    else no response
        W-->>C: raise TransportError
    end
```

##### gRPC call flow

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.bgp_monitoring
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: delete_monitor(id="id-example")
    W->>R: build_grpc_request(DeleteMonitorRequest, arguments)
    R->>API: BgpMonitoringAdminService/DeleteMonitor (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: parse_grpc_response(response)
        W-->>C: DeleteMonitorResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

##### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `id` | path | `string` | Yes |

##### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `DeleteMonitorResponse` |
| default | An unexpected error response. | `rpcStatus` |

##### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.bgp_monitoring.delete_monitor(
    id="id-example",
)
```

---

#### `PUT` `/bgp_monitoring/v202210/monitors/{id}/status`

Sets administrative status of a BGP monitor.

Sets administrative status of BGP monitor with specific ID.

##### REST call flow

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.bgp_monitoring
    participant API as Kentik REST API

    C->>W: set_monitor_status(id="id-example", data=BgpMonitoringAdminServiceSetMonitorStatusBody(...))
    W->>API: PUT /bgp_monitoring/v202210/monitors/{id}/status
    alt success
        API-->>W: SetMonitorStatusResponse (JSON)
        W-->>C: SetMonitorStatusResponse
    else error status
        API-->>W: error body
        W-->>C: raise AuthenticationError (401) or HTTPException
    else no response
        W-->>C: raise TransportError
    end
```

##### gRPC call flow

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.bgp_monitoring
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: set_monitor_status(id="id-example", data=BgpMonitoringAdminServiceSetMonitorStatusBody(...))
    W->>R: build_grpc_request(SetMonitorStatusRequest, arguments)
    R->>API: BgpMonitoringAdminService/SetMonitorStatus (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: parse_grpc_response(response)
        W-->>C: SetMonitorStatusResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

##### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `id` | path | `string` | Yes |
| `data` | body | `BgpMonitoringAdminServiceSetMonitorStatusBody` | Yes |

##### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `SetMonitorStatusResponse` |
| default | An unexpected error response. | `rpcStatus` |

##### Example

```python
from kentik_api.client import KentikAPI
from kentik_api.gen.bgp_monitoring.models import (
    BgpMonitoringAdminServiceSetMonitorStatusBody,
)

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.bgp_monitoring.set_monitor_status(
    id="id-example",
    data=BgpMonitoringAdminServiceSetMonitorStatusBody(...),
)
```

## Data Models

<details>
<summary>Model relationships (21 of 28 models)</summary>

Each arrow points from a model to a model that one of its fields holds. The label names the field.

```mermaid
classDiagram
    class BgpMetric
    class BgpMetricType
    class BgpMonitor
    class BgpMonitorStatus
    class BgpMonitoringAdminServiceSetMonitorStatusBody
    class BgpMonitoringAdminServiceUpdateMonitorBody
    class CreateMonitorRequest
    class CreateMonitorResponse
    class DeleteMonitorResponse
    class GetMetricsForTargetRequest
    class GetMetricsForTargetResponse
    class GetMonitorResponse
    class GetRoutesForTargetRequest
    class GetRoutesForTargetResponse
    class ListMonitorsResponse
    class Nlri
    class RouteInfo
    class SetMonitorStatusResponse
    class UpdateMonitorResponse
    class protobufAny
    class rpcStatus
    BgpMetric --> Nlri : nlri
    BgpMonitor --> BgpMonitorStatus : status
    BgpMonitoringAdminServiceSetMonitorStatusBody --> BgpMonitorStatus : status
    CreateMonitorRequest --> BgpMonitor : monitor
    CreateMonitorResponse --> BgpMonitor : monitor
    GetMetricsForTargetRequest --> BgpMetricType : metrics
    GetMetricsForTargetRequest --> Nlri : target
    GetMetricsForTargetResponse --> BgpMetric : metrics
    GetMonitorResponse --> BgpMonitor : monitor
    GetRoutesForTargetRequest --> Nlri : target
    GetRoutesForTargetResponse --> RouteInfo : routes
    ListMonitorsResponse --> BgpMonitor : monitors
    RouteInfo --> Nlri : nlri
    UpdateMonitorResponse --> BgpMonitor : monitor
    rpcStatus --> protobufAny : details
```

</details>

```{eval-rst}
.. autoclass:: kentik_api.gen.bgp_monitoring.models.Afi
   :members:
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.bgp_monitoring.models.BgpHealthSettings
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.bgp_monitoring.models.BgpMetric
```

```{eval-rst}
.. autoclass:: kentik_api.gen.bgp_monitoring.models.BgpMetricType
   :members:
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.bgp_monitoring.models.BgpMonitor
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.bgp_monitoring.models.BgpMonitorSettings
```

```{eval-rst}
.. autoclass:: kentik_api.gen.bgp_monitoring.models.BgpMonitorStatus
   :members:
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.bgp_monitoring.models.BgpMonitoringAdminServiceSetMonitorStatusBody
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.bgp_monitoring.models.BgpMonitoringAdminServiceUpdateMonitorBody
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.bgp_monitoring.models.CreateMonitorRequest
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.bgp_monitoring.models.CreateMonitorResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.bgp_monitoring.models.DeleteMonitorResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.bgp_monitoring.models.GetMetricsForTargetRequest
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.bgp_monitoring.models.GetMetricsForTargetResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.bgp_monitoring.models.GetMonitorResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.bgp_monitoring.models.GetRoutesForTargetRequest
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.bgp_monitoring.models.GetRoutesForTargetResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.bgp_monitoring.models.ListMonitorsResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.bgp_monitoring.models.Nlri
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.bgp_monitoring.models.RouteInfo
```

```{eval-rst}
.. autoclass:: kentik_api.gen.bgp_monitoring.models.RpkiStatus
   :members:
```

```{eval-rst}
.. autoclass:: kentik_api.gen.bgp_monitoring.models.Safi
   :members:
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.bgp_monitoring.models.SetMonitorStatusResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.bgp_monitoring.models.UpdateMonitorResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.bgp_monitoring.models.UserInfo
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.bgp_monitoring.models.VantagePoint
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.bgp_monitoring.models.protobufAny
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.bgp_monitoring.models.rpcStatus
```
