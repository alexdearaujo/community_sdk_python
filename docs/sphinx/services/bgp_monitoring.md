<!-- AUTO-GENERATED: scripts/generation/endpoint_docs.py, _render_sphinx_stubs() -->
<!-- Rebuilt on every `make generate`. Do not edit by hand. -->

# Bgp Monitoring Service

## Overview

```mermaid
flowchart LR
    subgraph sdk["kentik_api"]
        KA["KentikAPI"]
        W["Bgp MonitoringServiceWrapper\nclient.bgp_monitoring"]
        REST["REST functions\ngen/bgp_monitoring/services/"]
        RJ["request_json()\ncore/rest_runtime"]
        M["Models\ngen/bgp_monitoring/models/"]
        E["Error classes\ngen/bgp_monitoring/error/"]
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

### BgpMonitoringDataService

#### `POST` `/bgp_monitoring/v202210/metrics`

Get metrics for a BGP prefix.

Retrieve metric data for single BGP prefix and time interval.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.bgp_monitoring
    participant API as Kentik REST API

    C->>W: get_metrics_for_target(data=GetMetricsForTargetRequest(...))
    W->>API: POST /bgp_monitoring/v202210/metrics
    alt success
        API-->>W: v202210GetMetricsForTargetResponse (JSON)
        W-->>C: v202210GetMetricsForTargetResponse
    else error
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

**gRPC transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.bgp_monitoring
    participant B as proto bridge
    participant API as Kentik gRPC API

    C->>W: get_metrics_for_target(data=GetMetricsForTargetRequest(...))
    W->>B: ParseDict(params, GetMetricsForTargetRequest)
    B->>API: get_metrics_for_target (gRPC/TLS)
    alt success
        API-->>B: v202210GetMetricsForTargetResponse proto
        B-->>W: MessageToDict(response)
        W-->>C: v202210GetMetricsForTargetResponse
    else gRPC error
        API-->>B: gRPC status + details
        B-->>W: raise HTTPException
        W-->>C: raise HTTPException
    end
```

##### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `data` | body | `v202210GetMetricsForTargetRequest` | Yes |

##### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `v202210GetMetricsForTargetResponse` |
| default | An unexpected error response. | `rpcStatus` |

##### Example

```python
from kentik_api.client import KentikAPI

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

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.bgp_monitoring
    participant API as Kentik REST API

    C->>W: get_routes_for_target(data=GetRoutesForTargetRequest(...))
    W->>API: POST /bgp_monitoring/v202210/routes
    alt success
        API-->>W: v202210GetRoutesForTargetResponse (JSON)
        W-->>C: v202210GetRoutesForTargetResponse
    else error
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

**gRPC transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.bgp_monitoring
    participant B as proto bridge
    participant API as Kentik gRPC API

    C->>W: get_routes_for_target(data=GetRoutesForTargetRequest(...))
    W->>B: ParseDict(params, GetRoutesForTargetRequest)
    B->>API: get_routes_for_target (gRPC/TLS)
    alt success
        API-->>B: v202210GetRoutesForTargetResponse proto
        B-->>W: MessageToDict(response)
        W-->>C: v202210GetRoutesForTargetResponse
    else gRPC error
        API-->>B: gRPC status + details
        B-->>W: raise HTTPException
        W-->>C: raise HTTPException
    end
```

##### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `data` | body | `v202210GetRoutesForTargetRequest` | Yes |

##### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `v202210GetRoutesForTargetResponse` |
| default | An unexpected error response. | `rpcStatus` |

##### Example

```python
from kentik_api.client import KentikAPI

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

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.bgp_monitoring
    participant API as Kentik REST API

    C->>W: list_monitors()
    W->>API: GET /bgp_monitoring/v202210/monitors
    alt success
        API-->>W: v202210ListMonitorsResponse (JSON)
        W-->>C: v202210ListMonitorsResponse
    else error
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

**gRPC transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.bgp_monitoring
    participant B as proto bridge
    participant API as Kentik gRPC API

    C->>W: list_monitors()
    W->>B: ParseDict(params, ListMonitorsRequest)
    B->>API: list_monitors (gRPC/TLS)
    alt success
        API-->>B: v202210ListMonitorsResponse proto
        B-->>W: MessageToDict(response)
        W-->>C: v202210ListMonitorsResponse
    else gRPC error
        API-->>B: gRPC status + details
        B-->>W: raise HTTPException
        W-->>C: raise HTTPException
    end
```

##### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `v202210ListMonitorsResponse` |
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

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.bgp_monitoring
    participant API as Kentik REST API

    C->>W: create_monitor(data=CreateMonitorRequest(...))
    W->>API: POST /bgp_monitoring/v202210/monitors
    alt success
        API-->>W: v202210CreateMonitorResponse (JSON)
        W-->>C: v202210CreateMonitorResponse
    else error
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

**gRPC transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.bgp_monitoring
    participant B as proto bridge
    participant API as Kentik gRPC API

    C->>W: create_monitor(data=CreateMonitorRequest(...))
    W->>B: ParseDict(params, CreateMonitorRequest)
    B->>API: create_monitor (gRPC/TLS)
    alt success
        API-->>B: v202210CreateMonitorResponse proto
        B-->>W: MessageToDict(response)
        W-->>C: v202210CreateMonitorResponse
    else gRPC error
        API-->>B: gRPC status + details
        B-->>W: raise HTTPException
        W-->>C: raise HTTPException
    end
```

##### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `data` | body | `v202210CreateMonitorRequest` | Yes |

##### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `v202210CreateMonitorResponse` |
| default | An unexpected error response. | `rpcStatus` |

##### Example

```python
from kentik_api.client import KentikAPI

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

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.bgp_monitoring
    participant API as Kentik REST API

    C->>W: get_monitor(id="id-example")
    W->>API: GET /bgp_monitoring/v202210/monitors/{id}
    alt success
        API-->>W: v202210GetMonitorResponse (JSON)
        W-->>C: v202210GetMonitorResponse
    else error
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

**gRPC transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.bgp_monitoring
    participant B as proto bridge
    participant API as Kentik gRPC API

    C->>W: get_monitor(id="id-example")
    W->>B: ParseDict(params, GetMonitorRequest)
    B->>API: get_monitor (gRPC/TLS)
    alt success
        API-->>B: v202210GetMonitorResponse proto
        B-->>W: MessageToDict(response)
        W-->>C: v202210GetMonitorResponse
    else gRPC error
        API-->>B: gRPC status + details
        B-->>W: raise HTTPException
        W-->>C: raise HTTPException
    end
```

##### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `id` | path | `string` | Yes |

##### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `v202210GetMonitorResponse` |
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

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.bgp_monitoring
    participant API as Kentik REST API

    C->>W: update_monitor(id="id-example", data=BgpMonitoringAdminServiceUpdateMonitorBody(...))
    W->>API: PUT /bgp_monitoring/v202210/monitors/{id}
    alt success
        API-->>W: v202210UpdateMonitorResponse (JSON)
        W-->>C: v202210UpdateMonitorResponse
    else error
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

**gRPC transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.bgp_monitoring
    participant B as proto bridge
    participant API as Kentik gRPC API

    C->>W: update_monitor(id="id-example", data=BgpMonitoringAdminServiceUpdateMonitorBody(...))
    W->>B: ParseDict(params, UpdateMonitorRequest)
    B->>API: update_monitor (gRPC/TLS)
    alt success
        API-->>B: v202210UpdateMonitorResponse proto
        B-->>W: MessageToDict(response)
        W-->>C: v202210UpdateMonitorResponse
    else gRPC error
        API-->>B: gRPC status + details
        B-->>W: raise HTTPException
        W-->>C: raise HTTPException
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
| 200 | A successful response. | `v202210UpdateMonitorResponse` |
| default | An unexpected error response. | `rpcStatus` |

##### Example

```python
from kentik_api.client import KentikAPI

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

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.bgp_monitoring
    participant API as Kentik REST API

    C->>W: delete_monitor(id="id-example")
    W->>API: DELETE /bgp_monitoring/v202210/monitors/{id}
    alt success
        API-->>W: v202210DeleteMonitorResponse (JSON)
        W-->>C: v202210DeleteMonitorResponse
    else error
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

**gRPC transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.bgp_monitoring
    participant B as proto bridge
    participant API as Kentik gRPC API

    C->>W: delete_monitor(id="id-example")
    W->>B: ParseDict(params, DeleteMonitorRequest)
    B->>API: delete_monitor (gRPC/TLS)
    alt success
        API-->>B: v202210DeleteMonitorResponse proto
        B-->>W: MessageToDict(response)
        W-->>C: v202210DeleteMonitorResponse
    else gRPC error
        API-->>B: gRPC status + details
        B-->>W: raise HTTPException
        W-->>C: raise HTTPException
    end
```

##### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `id` | path | `string` | Yes |

##### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `v202210DeleteMonitorResponse` |
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

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.bgp_monitoring
    participant API as Kentik REST API

    C->>W: set_monitor_status(id="id-example", data=BgpMonitoringAdminServiceSetMonitorStatusBody(...))
    W->>API: PUT /bgp_monitoring/v202210/monitors/{id}/status
    alt success
        API-->>W: v202210SetMonitorStatusResponse (JSON)
        W-->>C: v202210SetMonitorStatusResponse
    else error
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

**gRPC transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.bgp_monitoring
    participant B as proto bridge
    participant API as Kentik gRPC API

    C->>W: set_monitor_status(id="id-example", data=BgpMonitoringAdminServiceSetMonitorStatusBody(...))
    W->>B: ParseDict(params, SetMonitorStatusRequest)
    B->>API: set_monitor_status (gRPC/TLS)
    alt success
        API-->>B: v202210SetMonitorStatusResponse proto
        B-->>W: MessageToDict(response)
        W-->>C: v202210SetMonitorStatusResponse
    else gRPC error
        API-->>B: gRPC status + details
        B-->>W: raise HTTPException
        W-->>C: raise HTTPException
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
| 200 | A successful response. | `v202210SetMonitorStatusResponse` |
| default | An unexpected error response. | `rpcStatus` |

##### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.bgp_monitoring.set_monitor_status(
    id="id-example",
    data=BgpMonitoringAdminServiceSetMonitorStatusBody(...),
)
```

## Data Models

<details>
<summary>Model relationships (5 of 28 models)</summary>

```mermaid
classDiagram
    class BgpMonitorStatus
    class BgpMonitoringAdminServiceSetMonitorStatusBody
    class BgpMonitoringAdminServiceUpdateMonitorBody
    class protobufAny
    class rpcStatus
    BgpMonitoringAdminServiceSetMonitorStatusBody --> BgpMonitorStatus
    rpcStatus --> protobufAny
```

</details>

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
.. autopydantic_model:: kentik_api.gen.bgp_monitoring.models.SetMonitorStatusResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.bgp_monitoring.models.UpdateMonitorResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.bgp_monitoring.models.protobufAny
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.bgp_monitoring.models.rpcStatus
```

```{eval-rst}
.. autoclass:: kentik_api.gen.bgp_monitoring.models.v202303Afi
   :members:
```

```{eval-rst}
.. autoclass:: kentik_api.gen.bgp_monitoring.models.v202303RpkiStatus
   :members:
```

```{eval-rst}
.. autoclass:: kentik_api.gen.bgp_monitoring.models.v202303Safi
   :members:
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.bgp_monitoring.models.v202303UserInfo
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.bgp_monitoring.models.v202303VantagePoint
```
