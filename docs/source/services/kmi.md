# Kmi Service

## Overview

```mermaid
flowchart LR
    Client["client.kmi"]
    RJ["request_json()"]
    OK["success: response model"]
    ERR["per-operation error class"]
    Client --> G0["KmiService (5 ops)"]
    G0 --> RJ
    RJ --> OK
    RJ -->|"error status"| ERR
```

## Endpoints

### `GET` `/kmi/v202212/insights`

List global KMI insights.

Returns list of global KMI insights.

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `limit` | query | `integer (int64)` | No |
| `marketId` | query | `string` | No |
| `ip` | query | `string` | No |
| `lookback` | query | `integer (int64)` | No |
| `types` | query | `string[]` | No |
| `magnitude` | query | `integer (int64)` | No |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `GetGlobalInsightsResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

client = KentikAPI()  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.kmi.get_global_insights()
```

---

### `GET` `/kmi/v202212/insights/{asn}`

List ASN-specific KMI insights.

Returns list of KMI insights for a specific Autonomous System.

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `asn` | path | `string` | Yes |
| `limit` | query | `integer (int64)` | No |
| `marketId` | query | `string` | No |
| `ip` | query | `string` | No |
| `lookback` | query | `integer (int64)` | No |
| `types` | query | `string[]` | No |
| `magnitude` | query | `integer (int64)` | No |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `GetASNInsightsResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

client = KentikAPI()  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.kmi.get_a_s_n_insights(
    asn="asn-example",
)
```

---

### `POST` `/kmi/v202212/market/{marketId}/network/{asn}/{type}`

List metadata and list of customers, providers, and peers for an Autonomous System.

Returns metadata and list of customers, providers, and peers for an Autonomous System.

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `marketId` | path | `string` | Yes |
| `asn` | path | `string` | Yes |
| `type` | path | `string` | Yes |
| `data` | body | `KmiServiceGetASNDetailsBody` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `GetASNDetailsResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

client = KentikAPI()  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.kmi.get_a_s_n_details(
    marketId="marketId-example",
    asn="asn-example",
    type="type-example",
    data=KmiServiceGetASNDetailsBody(...),
)
```

---

### `POST` `/kmi/v202212/market/{marketId}/rankings/{rankType}/ip/{ip}`

List KMI rankings by geo market and rank type.

Returns list of KMI rankings.

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `marketId` | path | `string` | Yes |
| `rankType` | path | `string` | Yes |
| `ip` | path | `string` | Yes |
| `data` | body | `KmiServiceGetRankingsBody` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `GetRankingsResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

client = KentikAPI()  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.kmi.get_rankings(
    marketId="marketId-example",
    rankType="rankType-example",
    ip="ip-example",
    data=KmiServiceGetRankingsBody(...),
)
```

---

### `GET` `/kmi/v202212/markets`

List all geo markets for KMI.

Returns list of geo markets for KMI.

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `ListMarketsResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

client = KentikAPI()  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.kmi.list_markets()
```

## Data Models

<details>
<summary>Model relationships (13 of 15 models)</summary>

```mermaid
classDiagram
    class ASNDetails
    class GetASNDetailsResponse
    class GetASNInsightsResponse
    class GetGlobalInsightsResponse
    class GetRankingsResponse
    class Insight
    class KmiServiceGetASNDetailsBody
    class KmiServiceGetRankingsBody
    class ListMarketsResponse
    class Market
    class Ranking
    class protobufAny
    class rpcStatus
    GetASNDetailsResponse --> ASNDetails
    GetASNInsightsResponse --> Insight
    GetGlobalInsightsResponse --> Insight
    GetRankingsResponse --> Ranking
    ListMarketsResponse --> Market
    rpcStatus --> protobufAny
```

</details>

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.kmi.models.ASNDetails
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.kmi.models.CustomerProvider
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.kmi.models.GetASNDetailsResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.kmi.models.GetASNInsightsResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.kmi.models.GetGlobalInsightsResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.kmi.models.GetRankingsResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.kmi.models.Insight
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.kmi.models.KmiServiceGetASNDetailsBody
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.kmi.models.KmiServiceGetRankingsBody
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.kmi.models.ListMarketsResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.kmi.models.Market
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.kmi.models.Peer
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.kmi.models.Ranking
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.kmi.models.protobufAny
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.kmi.models.rpcStatus
```
