<!-- AUTO-GENERATED: scripts/generation/endpoint_docs.py, render_endpoint_docs() -->
<!-- Rebuilt on every `uv run poe generate`. Do not edit by hand. -->

# Ktbgp Service

## Overview

```mermaid
%%{init: {"fontFamily": "ui-monospace, SFMono-Regular, Menlo, monospace", "flowchart": {"curve": "step", "nodeSpacing": 30, "rankSpacing": 70, "wrappingWidth": 400}}}%%
flowchart LR
    code("Your code"):::greenSrc
    subgraph sdk["kentik_api"]
        wrap("KtbgpServiceWrapper<br/>client.ktbgp<br/>3 operations"):::orange
        rest("REST functions<br/>gen/ktbgp/services/"):::blue
        rj("request_json()<br/>core/rest_runtime.py"):::blue
        cg("call_grpc()<br/>core/grpc_runtime.py"):::violet
    end
    grpcapi("Kentik gRPC API<br/>HTTP/2 + protobuf"):::violetSrc
    restapi("Kentik REST API<br/>HTTPS + JSON"):::blueSrc

    code -->|"method call"| wrap
    wrap -->|"Pydantic model from<br/>gen/ktbgp/models/"| code
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

On an error status or a failed call, the SDK raises an error class from `gen/ktbgp/error/`, or a shared type from `kentik_api.errors`.

## Endpoints

### `POST` `/routes/announce`

Announce a BGP route to a specified set of devices

#### REST call flow

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.ktbgp
    participant API as Kentik REST API

    C->>W: route_announce(data=RouteServiceAnnounceRequest(...))
    W->>API: POST /routes/announce
    alt success
        API-->>W: RouteServiceAnnounceResponse (JSON)
        W-->>C: RouteServiceAnnounceResponse
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
    participant W as client.ktbgp
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: route_announce(data=RouteServiceAnnounceRequest(...))
    W->>R: build_grpc_request(RouteServiceAnnounceRequest, arguments)
    R->>API: RouteService/Announce (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: parse_grpc_response(response)
        W-->>C: RouteServiceAnnounceResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
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
from kentik_api.gen.ktbgp.models import RouteServiceAnnounceRequest

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.ktbgp.route_announce(
    data=RouteServiceAnnounceRequest(...),
)
```

---

### `POST` `/routes/list`

List active BGP updates for a specified set of devices

#### REST call flow

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.ktbgp
    participant API as Kentik REST API

    C->>W: route_list(data=RouteServiceListRequest(...))
    W->>API: POST /routes/list
    alt success
        API-->>W: RouteServiceListResponse (JSON)
        W-->>C: RouteServiceListResponse
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
    participant W as client.ktbgp
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: route_list(data=RouteServiceListRequest(...))
    W->>R: build_grpc_request(RouteServiceListRequest, arguments)
    R->>API: RouteService/List (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: parse_grpc_response(response)
        W-->>C: RouteServiceListResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
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
from kentik_api.gen.ktbgp.models import RouteServiceListRequest

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.ktbgp.route_list(
    data=RouteServiceListRequest(...),
)
```

---

### `POST` `/routes/withdraw`

Withdraw active BGP updates from devices

#### REST call flow

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.ktbgp
    participant API as Kentik REST API

    C->>W: route_withdraw(data=RouteServiceWithdrawRequest(...))
    W->>API: POST /routes/withdraw
    alt success
        API-->>W: RouteServiceWithdrawResponse (JSON)
        W-->>C: RouteServiceWithdrawResponse
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
    participant W as client.ktbgp
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: route_withdraw(data=RouteServiceWithdrawRequest(...))
    W->>R: build_grpc_request(RouteServiceWithdrawRequest, arguments)
    R->>API: RouteService/Withdraw (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: parse_grpc_response(response)
        W-->>C: RouteServiceWithdrawResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
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
from kentik_api.gen.ktbgp.models import RouteServiceWithdrawRequest

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.ktbgp.route_withdraw(
    data=RouteServiceWithdrawRequest(...),
)
```

## Data Models

<details>
<summary>Model relationships (14 of 45 models)</summary>

Each arrow points from a model to a model that one of its fields holds. The label names the field.

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
    class Withdraw
    class protobufAny
    class rpcStatus
    DeviceAdverts --> FlowspecUpdate : flowspec
    DeviceAdverts --> RTBHUpdate : rtbh
    RouteServiceAnnounceRequest --> FlowspecUpdate : flowspec
    RouteServiceAnnounceRequest --> RTBHUpdate : rtbh
    RouteServiceAnnounceResponse --> UpdateResult : results
    RouteServiceListRequest --> RoutesFilter : filters
    RouteServiceListResponse --> DeviceAdverts : result
    RouteServiceWithdrawRequest --> Withdraw : withdraw
    RouteServiceWithdrawResponse --> UpdateResult : results
    rpcStatus --> protobufAny : details
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
.. autopydantic_model:: kentik_api.gen.ktbgp.models.Withdraw
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.ktbgp.models.protobufAny
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.ktbgp.models.rpcStatus
```
