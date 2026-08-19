# Ktbgp Service

## Overview

```mermaid
flowchart LR
    subgraph sdk["kentik_api"]
        KA["KentikAPI"]
        W["KtbgpServiceWrapper\nclient.ktbgp"]
        REST["REST functions\ngen/ktbgp/services/"]
        RJ["request_json()\ncore/rest_runtime"]
        M["Models\ngen/ktbgp/models/"]
        E["Error classes\ngen/ktbgp/error/"]
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

### `POST` `/routes/announce`

Announce a BGP route to a specified set of devices

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.ktbgp
    participant API as Kentik API

    C->>W: route_service__announce(data=RouteServiceAnnounceRequest(...))
    W->>API: POST /routes/announce
    alt success
        API-->>W: RouteServiceAnnounceResponse
        W-->>C: RouteServiceAnnounceResponse
    else error status
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `data` | body | `RouteServiceAnnounceRequest` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `RouteServiceAnnounceResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.ktbgp.route_service__announce(
    data=RouteServiceAnnounceRequest(...),
)
```

---

### `POST` `/routes/list`

List active BGP updates for a specified set of devices

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.ktbgp
    participant API as Kentik API

    C->>W: route_service__list(data=RouteServiceListRequest(...))
    W->>API: POST /routes/list
    alt success
        API-->>W: RouteServiceListResponse
        W-->>C: RouteServiceListResponse
    else error status
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `data` | body | `RouteServiceListRequest` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `RouteServiceListResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.ktbgp.route_service__list(
    data=RouteServiceListRequest(...),
)
```

---

### `POST` `/routes/withdraw`

Withdraw active BGP updates from devices

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.ktbgp
    participant API as Kentik API

    C->>W: route_service__withdraw(data=RouteServiceWithdrawRequest(...))
    W->>API: POST /routes/withdraw
    alt success
        API-->>W: RouteServiceWithdrawResponse
        W-->>C: RouteServiceWithdrawResponse
    else error status
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `data` | body | `RouteServiceWithdrawRequest` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `RouteServiceWithdrawResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.ktbgp.route_service__withdraw(
    data=RouteServiceWithdrawRequest(...),
)
```

## Data Models

<details>
<summary>Model relationships (14 of 45 models)</summary>

```mermaid
classDiagram
    class DeviceAdverts
    class FlowspecUpdate
    class RTBHUpdate
    class RouteServiceAnnounceRequest
    class RouteServiceAnnounceResponse
    class RouteServiceListRequest
    class RouteServiceListResponse
    class RouteServiceWithdrawRequest
    class RouteServiceWithdrawResponse
    class RoutesFilter
    class UpdateResult
    class ktbgpv202501Withdraw
    class protobufAny
    class rpcStatus
    DeviceAdverts --> FlowspecUpdate
    DeviceAdverts --> RTBHUpdate
    RouteServiceAnnounceRequest --> FlowspecUpdate
    RouteServiceAnnounceRequest --> RTBHUpdate
    RouteServiceAnnounceResponse --> UpdateResult
    RouteServiceListRequest --> RoutesFilter
    RouteServiceListResponse --> DeviceAdverts
    RouteServiceWithdrawRequest --> ktbgpv202501Withdraw
    RouteServiceWithdrawResponse --> UpdateResult
    rpcStatus --> protobufAny
```

</details>

```{eval-rst}
.. autoclass:: kentik_api.gen.ktbgp.models.AdvertStatus
   :members:
```

```{eval-rst}
.. autoclass:: kentik_api.gen.ktbgp.models.BitwiseOp
   :members:
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.ktbgp.models.DeviceAdverts
```

```{eval-rst}
.. autoclass:: kentik_api.gen.ktbgp.models.ExtendedCommunityRouteType
   :members:
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.ktbgp.models.FlowspecAction
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.ktbgp.models.FlowspecActionAccept
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.ktbgp.models.FlowspecActionDiscard
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.ktbgp.models.FlowspecActionExtendedCommunity
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.ktbgp.models.FlowspecActionIPNextHopCopy
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.ktbgp.models.FlowspecActionIPNextHopRedirect
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.ktbgp.models.FlowspecActionLargeCommunity
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.ktbgp.models.FlowspecActionMarkDSCP
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.ktbgp.models.FlowspecActionRegularCommunity
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.ktbgp.models.FlowspecActionRouteTargetRedirect
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.ktbgp.models.FlowspecActionTerminalSample
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.ktbgp.models.FlowspecActionTrafficRateBytes
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.ktbgp.models.FlowspecMatch
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.ktbgp.models.FlowspecUpdate
```

```{eval-rst}
.. autoclass:: kentik_api.gen.ktbgp.models.Fragment
   :members:
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.ktbgp.models.FragmentFormula
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.ktbgp.models.FragmentPredicate
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.ktbgp.models.FragmentPredicateGroup
```

```{eval-rst}
.. autoclass:: kentik_api.gen.ktbgp.models.InetType
   :members:
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.ktbgp.models.NumericFormula
```

```{eval-rst}
.. autoclass:: kentik_api.gen.ktbgp.models.NumericOp
   :members:
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.ktbgp.models.NumericPredicate
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.ktbgp.models.NumericPredicateGroup
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.ktbgp.models.RTBHAction
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.ktbgp.models.RTBHMatch
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.ktbgp.models.RTBHUpdate
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.ktbgp.models.RouteServiceAnnounceRequest
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.ktbgp.models.RouteServiceAnnounceResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.ktbgp.models.RouteServiceListRequest
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.ktbgp.models.RouteServiceListResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.ktbgp.models.RouteServiceWithdrawRequest
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.ktbgp.models.RouteServiceWithdrawResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.ktbgp.models.RoutesFilter
```

```{eval-rst}
.. autoclass:: kentik_api.gen.ktbgp.models.TCPFlag
   :members:
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.ktbgp.models.TCPFlagsFormula
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.ktbgp.models.TCPFlagsPredicate
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.ktbgp.models.TCPFlagsPredicateGroup
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.ktbgp.models.UpdateResult
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.ktbgp.models.ktbgpv202501Withdraw
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.ktbgp.models.protobufAny
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.ktbgp.models.rpcStatus
```
