<!-- AUTO-GENERATED: scripts/generation/endpoint_docs.py, render_endpoint_docs() -->
<!-- Rebuilt on every `make generate`. Do not edit by hand. -->

# Device Service

## Overview

```mermaid
flowchart LR
    subgraph sdk["kentik_api"]
        KA["KentikAPI"]
        W["DeviceServiceWrapper\nclient.device"]
        REST["REST functions\ngen/device/services/"]
        RJ["request_json()\ncore/rest_runtime"]
        M["Models\ngen/device/models/"]
        E["Error classes\ngen/device/error/"]
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

### `GET` `/device/v202504beta2/device`

List all devices.

Returns list of configured devices. Use the 'view' parameter to control response detail: FULL (default), BASIC (id, name, status), or ID_ONLY (id only). See [About Devices](https://kb.kentik.com/v4/Cb01.htm).

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.device
    participant API as Kentik REST API

    C->>W: list_devices()
    W->>API: GET /device/v202504beta2/device
    alt success
        API-->>W: v202504beta2ListDevicesResponse (JSON)
        W-->>C: v202504beta2ListDevicesResponse
    else error
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

**gRPC transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.device
    participant B as proto bridge
    participant API as Kentik gRPC API

    C->>W: list_devices()
    W->>B: ParseDict(params, ListDevicesRequest)
    B->>API: list_devices (gRPC/TLS)
    alt success
        API-->>B: v202504beta2ListDevicesResponse proto
        B-->>W: MessageToDict(response)
        W-->>C: v202504beta2ListDevicesResponse
    else gRPC error
        API-->>B: gRPC status + details
        B-->>W: raise HTTPException
        W-->>C: raise HTTPException
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `querynoCustomColumns` | query | `boolean` | No |
| `view` | query | `string` | No |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `v202504beta2ListDevicesResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.device.list_devices()
```

---

### `POST` `/device/v202504beta2/device`

Configure a new device.

Create configuration for a new device. Returns the newly created configuration (see [About Devices](https://kb.kentik.com/v4/Cb01.htm)).

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.device
    participant API as Kentik REST API

    C->>W: create_device(data=CreateDeviceRequest(...))
    W->>API: POST /device/v202504beta2/device
    alt success
        API-->>W: v202504beta2CreateDeviceResponse (JSON)
        W-->>C: v202504beta2CreateDeviceResponse
    else error
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

**gRPC transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.device
    participant B as proto bridge
    participant API as Kentik gRPC API

    C->>W: create_device(data=CreateDeviceRequest(...))
    W->>B: ParseDict(params, CreateDeviceRequest)
    B->>API: create_device (gRPC/TLS)
    alt success
        API-->>B: v202504beta2CreateDeviceResponse proto
        B-->>W: MessageToDict(response)
        W-->>C: v202504beta2CreateDeviceResponse
    else gRPC error
        API-->>B: gRPC status + details
        B-->>W: raise HTTPException
        W-->>C: raise HTTPException
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `data` | body | `v202504beta2CreateDeviceRequest` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `v202504beta2CreateDeviceResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.device.create_device(
    data=CreateDeviceRequest(...),
)
```

---

### `POST` `/device/v202504beta2/device/batch_create`

Configure multiple devices (max 100).

Create configuration for multiple devices. Returns the newly created configurations (see [About Devices](https://kb.kentik.com/v4/Cb01.htm)).

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.device
    participant API as Kentik REST API

    C->>W: create_devices(data=CreateDevicesRequest(...))
    W->>API: POST /device/v202504beta2/device/batch_create
    alt success
        API-->>W: v202504beta2CreateDevicesResponse (JSON)
        W-->>C: v202504beta2CreateDevicesResponse
    else error
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

**gRPC transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.device
    participant B as proto bridge
    participant API as Kentik gRPC API

    C->>W: create_devices(data=CreateDevicesRequest(...))
    W->>B: ParseDict(params, CreateDevicesRequest)
    B->>API: create_devices (gRPC/TLS)
    alt success
        API-->>B: v202504beta2CreateDevicesResponse proto
        B-->>W: MessageToDict(response)
        W-->>C: v202504beta2CreateDevicesResponse
    else gRPC error
        API-->>B: gRPC status + details
        B-->>W: raise HTTPException
        W-->>C: raise HTTPException
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `data` | body | `v202504beta2CreateDevicesRequest` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `v202504beta2CreateDevicesResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.device.create_devices(
    data=CreateDevicesRequest(...),
)
```

---

### `POST` `/device/v202504beta2/device/batch_delete`

Delete configuration of multiple devices.

Deletes configuration of multiple devices with specific IDs (see [About Devices](https://kb.kentik.com/v4/Cb01.htm)).

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.device
    participant API as Kentik REST API

    C->>W: delete_devices(data=DeleteDevicesRequest(...))
    W->>API: POST /device/v202504beta2/device/batch_delete
    alt success
        API-->>W: v202504beta2DeleteDevicesResponse (JSON)
        W-->>C: v202504beta2DeleteDevicesResponse
    else error
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

**gRPC transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.device
    participant B as proto bridge
    participant API as Kentik gRPC API

    C->>W: delete_devices(data=DeleteDevicesRequest(...))
    W->>B: ParseDict(params, DeleteDevicesRequest)
    B->>API: delete_devices (gRPC/TLS)
    alt success
        API-->>B: v202504beta2DeleteDevicesResponse proto
        B-->>W: MessageToDict(response)
        W-->>C: v202504beta2DeleteDevicesResponse
    else gRPC error
        API-->>B: gRPC status + details
        B-->>W: raise HTTPException
        W-->>C: raise HTTPException
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `data` | body | `v202504beta2DeleteDevicesRequest` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `v202504beta2DeleteDevicesResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.device.delete_devices(
    data=DeleteDevicesRequest(...),
)
```

---

### `PUT` `/device/v202504beta2/device/batch_update`

Updates configuration of multiple devices (max 100).

Replaces configuration of multiple devices with attributes in the request. Returns the updated configurations (see [About Devices](https://kb.kentik.com/v4/Cb01.htm)).

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.device
    participant API as Kentik REST API

    C->>W: update_devices(data=UpdateDevicesRequest(...))
    W->>API: PUT /device/v202504beta2/device/batch_update
    alt success
        API-->>W: v202504beta2UpdateDevicesResponse (JSON)
        W-->>C: v202504beta2UpdateDevicesResponse
    else error
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

**gRPC transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.device
    participant B as proto bridge
    participant API as Kentik gRPC API

    C->>W: update_devices(data=UpdateDevicesRequest(...))
    W->>B: ParseDict(params, UpdateDevicesRequest)
    B->>API: update_devices (gRPC/TLS)
    alt success
        API-->>B: v202504beta2UpdateDevicesResponse proto
        B-->>W: MessageToDict(response)
        W-->>C: v202504beta2UpdateDevicesResponse
    else gRPC error
        API-->>B: gRPC status + details
        B-->>W: raise HTTPException
        W-->>C: raise HTTPException
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `data` | body | `v202504beta2UpdateDevicesRequest` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `v202504beta2UpdateDevicesResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.device.update_devices(
    data=UpdateDevicesRequest(...),
)
```

---

### `GET` `/device/v202504beta2/device/name/{deviceName}`

Retrieve configuration of a device by name.

Returns configuration of a device specified by name (see [About Devices](https://kb.kentik.com/v4/Cb01.htm)).

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.device
    participant API as Kentik REST API

    C->>W: get_device_by_name(deviceName="deviceName-example")
    W->>API: GET /device/v202504beta2/device/name/{deviceName}
    alt success
        API-->>W: v202504beta2GetDeviceByNameResponse (JSON)
        W-->>C: v202504beta2GetDeviceByNameResponse
    else error
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

**gRPC transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.device
    participant B as proto bridge
    participant API as Kentik gRPC API

    C->>W: get_device_by_name(deviceName="deviceName-example")
    W->>B: ParseDict(params, GetDeviceByNameRequest)
    B->>API: get_device_by_name (gRPC/TLS)
    alt success
        API-->>B: v202504beta2GetDeviceByNameResponse proto
        B-->>W: MessageToDict(response)
        W-->>C: v202504beta2GetDeviceByNameResponse
    else gRPC error
        API-->>B: gRPC status + details
        B-->>W: raise HTTPException
        W-->>C: raise HTTPException
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `deviceName` | path | `string` | Yes |
| `querynoCustomColumns` | query | `boolean` | No |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `v202504beta2GetDeviceByNameResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.device.get_device_by_name(
    deviceName="deviceName-example",
)
```

---

### `GET` `/device/v202504beta2/device/{device.id}`

Retrieve configuration of a device.

Returns configuration of a device specified by ID (see [About Devices](https://kb.kentik.com/v4/Cb01.htm)).

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.device
    participant API as Kentik REST API

    C->>W: get_device(deviceid="deviceid-example")
    W->>API: GET /device/v202504beta2/device/{device.id}
    alt success
        API-->>W: v202504beta2GetDeviceResponse (JSON)
        W-->>C: v202504beta2GetDeviceResponse
    else error
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

**gRPC transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.device
    participant B as proto bridge
    participant API as Kentik gRPC API

    C->>W: get_device(deviceid="deviceid-example")
    W->>B: ParseDict(params, GetDeviceRequest)
    B->>API: get_device (gRPC/TLS)
    alt success
        API-->>B: v202504beta2GetDeviceResponse proto
        B-->>W: MessageToDict(response)
        W-->>C: v202504beta2GetDeviceResponse
    else gRPC error
        API-->>B: gRPC status + details
        B-->>W: raise HTTPException
        W-->>C: raise HTTPException
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `deviceid` | path | `string` | Yes |
| `querynoCustomColumns` | query | `boolean` | No |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `v202504beta2GetDeviceResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.device.get_device(
    deviceid="deviceid-example",
)
```

---

### `PUT` `/device/v202504beta2/device/{device.id}`

Updates configuration of a device.

Replaces configuration of a device with attributes in the request. Returns the updated configuration (see [About Devices](https://kb.kentik.com/v4/Cb01.htm)).

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.device
    participant API as Kentik REST API

    C->>W: update_device(deviceid="deviceid-example", data=DeviceServiceUpdateDeviceBody(...))
    W->>API: PUT /device/v202504beta2/device/{device.id}
    alt success
        API-->>W: v202504beta2UpdateDeviceResponse (JSON)
        W-->>C: v202504beta2UpdateDeviceResponse
    else error
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

**gRPC transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.device
    participant B as proto bridge
    participant API as Kentik gRPC API

    C->>W: update_device(deviceid="deviceid-example", data=DeviceServiceUpdateDeviceBody(...))
    W->>B: ParseDict(params, UpdateDeviceRequest)
    B->>API: update_device (gRPC/TLS)
    alt success
        API-->>B: v202504beta2UpdateDeviceResponse proto
        B-->>W: MessageToDict(response)
        W-->>C: v202504beta2UpdateDeviceResponse
    else gRPC error
        API-->>B: gRPC status + details
        B-->>W: raise HTTPException
        W-->>C: raise HTTPException
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `deviceid` | path | `string` | Yes |
| `data` | body | `DeviceServiceUpdateDeviceBody` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `v202504beta2UpdateDeviceResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.device.update_device(
    deviceid="deviceid-example",
    data=DeviceServiceUpdateDeviceBody(...),
)
```

---

### `DELETE` `/device/v202504beta2/device/{device.id}`

Delete configuration of a device.

Deletes configuration of a device with specific ID (see [About Devices](https://kb.kentik.com/v4/Cb01.htm)).

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.device
    participant API as Kentik REST API

    C->>W: delete_device(deviceid="deviceid-example")
    W->>API: DELETE /device/v202504beta2/device/{device.id}
    alt success
        API-->>W: v202504beta2DeleteDeviceResponse (JSON)
        W-->>C: v202504beta2DeleteDeviceResponse
    else error
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

**gRPC transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.device
    participant B as proto bridge
    participant API as Kentik gRPC API

    C->>W: delete_device(deviceid="deviceid-example")
    W->>B: ParseDict(params, DeleteDeviceRequest)
    B->>API: delete_device (gRPC/TLS)
    alt success
        API-->>B: v202504beta2DeleteDeviceResponse proto
        B-->>W: MessageToDict(response)
        W-->>C: v202504beta2DeleteDeviceResponse
    else gRPC error
        API-->>B: gRPC status + details
        B-->>W: raise HTTPException
        W-->>C: raise HTTPException
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `deviceid` | path | `string` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `v202504beta2DeleteDeviceResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.device.delete_device(
    deviceid="deviceid-example",
)
```

---

### `PUT` `/device/v202504beta2/device/{id}/labels`

Updates labels of a device.

Removes all existing labels from the device and applies the device labels (see [About Device Labels](https://kb.kentik.com/v4/Cb16.htm)) specified by id. Returns the updated configuration.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.device
    participant API as Kentik REST API

    C->>W: update_device_labels(id="id-example", data=DeviceServiceUpdateDeviceLabelsBody(...))
    W->>API: PUT /device/v202504beta2/device/{id}/labels
    alt success
        API-->>W: v202504beta2UpdateDeviceLabelsResponse (JSON)
        W-->>C: v202504beta2UpdateDeviceLabelsResponse
    else error
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

**gRPC transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.device
    participant B as proto bridge
    participant API as Kentik gRPC API

    C->>W: update_device_labels(id="id-example", data=DeviceServiceUpdateDeviceLabelsBody(...))
    W->>B: ParseDict(params, UpdateDeviceLabelsRequest)
    B->>API: update_device_labels (gRPC/TLS)
    alt success
        API-->>B: v202504beta2UpdateDeviceLabelsResponse proto
        B-->>W: MessageToDict(response)
        W-->>C: v202504beta2UpdateDeviceLabelsResponse
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
| `data` | body | `DeviceServiceUpdateDeviceLabelsBody` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `v202504beta2UpdateDeviceLabelsResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.device.update_device_labels(
    id="id-example",
    data=DeviceServiceUpdateDeviceLabelsBody(...),
)
```

## Data Models

<details>
<summary>Model relationships (5 of 33 models)</summary>

```mermaid
classDiagram
    class DeviceServiceUpdateDeviceBody
    class DeviceServiceUpdateDeviceLabelsBody
    class LabelConcise
    class protobufAny
    class rpcStatus
    DeviceServiceUpdateDeviceLabelsBody --> LabelConcise
    rpcStatus --> protobufAny
```

</details>

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.device.models.CreateDeviceRequest
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.device.models.CreateDeviceResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.device.models.CreateDevicesRequest
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.device.models.CreateDevicesResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.device.models.CustomColumnData
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.device.models.DeleteDeviceResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.device.models.DeleteDevicesRequest
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.device.models.DeleteDevicesResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.device.models.DeviceConcise
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.device.models.DeviceDetailed
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.device.models.DeviceNmsConfig
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.device.models.DeviceNmsSnmpConfig
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.device.models.DeviceNmsStConfig
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.device.models.DeviceQuery
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.device.models.DeviceServiceUpdateDeviceBody
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.device.models.DeviceServiceUpdateDeviceLabelsBody
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.device.models.DeviceSnmpV3Conf
```

```{eval-rst}
.. autoclass:: kentik_api.gen.device.models.DeviceView
   :members:
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.device.models.GetDeviceByNameResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.device.models.GetDeviceResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.device.models.GnmiV1Conf
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.device.models.Interface
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.device.models.LabelConcise
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.device.models.ListDevicesResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.device.models.Plan
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.device.models.Site
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.device.models.UpdateDeviceLabelsResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.device.models.UpdateDeviceResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.device.models.UpdateDevicesRequest
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.device.models.UpdateDevicesResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.device.models.devicev202504beta2Label
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.device.models.protobufAny
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.device.models.rpcStatus
```
