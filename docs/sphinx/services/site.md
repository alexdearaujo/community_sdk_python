<!-- AUTO-GENERATED: scripts/generation/endpoint_docs.py, render_endpoint_docs() -->
<!-- Rebuilt on every `make generate`. Do not edit by hand. -->

# Site Service

## Overview

```mermaid
flowchart LR
    subgraph sdk["kentik_api"]
        KA["KentikAPI"]
        W["SiteServiceWrapper\nclient.site"]
        REST["REST functions\ngen/site/services/"]
        RJ["request_json()\ncore/rest_runtime"]
        M["Models\ngen/site/models/"]
        E["Error classes\ngen/site/error/"]
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

### `GET` `/site/v202509/site_markets`

List all site markets.

Returns list of configured site markets.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.site
    participant API as Kentik REST API

    C->>W: list_markets()
    W->>API: GET /site/v202509/site_markets
    alt success
        API-->>W: ListSiteMarketsResponse (JSON)
        W-->>C: ListSiteMarketsResponse
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
    participant W as client.site
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: list_markets()
    W->>R: build_grpc_request(ListSiteMarketsRequest, arguments)
    R->>API: SiteService/ListSiteMarkets (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: MessageToDict(response)
        W-->>C: ListSiteMarketsResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `ListSiteMarketsResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.site.list_markets()
```

---

### `POST` `/site/v202509/site_markets`

Configure a new site market.

Create configuration for a new site market. Returns the newly created configuration.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.site
    participant API as Kentik REST API

    C->>W: create_market(data=CreateSiteMarketRequest(...))
    W->>API: POST /site/v202509/site_markets
    alt success
        API-->>W: CreateSiteMarketResponse (JSON)
        W-->>C: CreateSiteMarketResponse
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
    participant W as client.site
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: create_market(data=CreateSiteMarketRequest(...))
    W->>R: build_grpc_request(CreateSiteMarketRequest, arguments)
    R->>API: SiteService/CreateSiteMarket (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: MessageToDict(response)
        W-->>C: CreateSiteMarketResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `data` | body | `CreateSiteMarketRequest` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `CreateSiteMarketResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI
from kentik_api.gen.site.models import CreateSiteMarketRequest

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.site.create_market(
    data=CreateSiteMarketRequest(...),
)
```

---

### `GET` `/site/v202509/site_markets/{id}`

Retrieve configuration of a site market.

Returns configuration of a site market specified by ID.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.site
    participant API as Kentik REST API

    C->>W: get_market(id="id-example")
    W->>API: GET /site/v202509/site_markets/{id}
    alt success
        API-->>W: GetSiteMarketResponse (JSON)
        W-->>C: GetSiteMarketResponse
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
    participant W as client.site
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: get_market(id="id-example")
    W->>R: build_grpc_request(GetSiteMarketRequest, arguments)
    R->>API: SiteService/GetSiteMarket (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: MessageToDict(response)
        W-->>C: GetSiteMarketResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `id` | path | `string` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `GetSiteMarketResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.site.get_market(
    id="id-example",
)
```

---

### `PUT` `/site/v202509/site_markets/{id}`

Updates configuration of a site market.

Replaces configuration of a site market with attributes in the request. Returns the updated configuration.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.site
    participant API as Kentik REST API

    C->>W: update_market(id="id-example", data=SiteServiceUpdateSiteMarketBody(...))
    W->>API: PUT /site/v202509/site_markets/{id}
    alt success
        API-->>W: UpdateSiteMarketResponse (JSON)
        W-->>C: UpdateSiteMarketResponse
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
    participant W as client.site
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: update_market(id="id-example", data=SiteServiceUpdateSiteMarketBody(...))
    W->>R: build_grpc_request(UpdateSiteMarketRequest, arguments)
    R->>API: SiteService/UpdateSiteMarket (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: MessageToDict(response)
        W-->>C: UpdateSiteMarketResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `id` | path | `string` | Yes |
| `data` | body | `SiteServiceUpdateSiteMarketBody` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `UpdateSiteMarketResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI
from kentik_api.gen.site.models import SiteServiceUpdateSiteMarketBody

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.site.update_market(
    id="id-example",
    data=SiteServiceUpdateSiteMarketBody(...),
)
```

---

### `DELETE` `/site/v202509/site_markets/{id}`

Delete configuration of a site market.

Deletes configuration of a site market with specific ID.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.site
    participant API as Kentik REST API

    C->>W: delete_market(id="id-example")
    W->>API: DELETE /site/v202509/site_markets/{id}
    alt success
        API-->>W: DeleteSiteMarketResponse (JSON)
        W-->>C: DeleteSiteMarketResponse
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
    participant W as client.site
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: delete_market(id="id-example")
    W->>R: build_grpc_request(DeleteSiteMarketRequest, arguments)
    R->>API: SiteService/DeleteSiteMarket (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: MessageToDict(response)
        W-->>C: DeleteSiteMarketResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `id` | path | `string` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `DeleteSiteMarketResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.site.delete_market(
    id="id-example",
)
```

---

### `GET` `/site/v202509/sites`

List all sites.

Returns list of configured sites.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.site
    participant API as Kentik REST API

    C->>W: list_sites()
    W->>API: GET /site/v202509/sites
    alt success
        API-->>W: ListSitesResponse (JSON)
        W-->>C: ListSitesResponse
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
    participant W as client.site
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: list_sites()
    W->>R: build_grpc_request(ListSitesRequest, arguments)
    R->>API: SiteService/ListSites (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: MessageToDict(response)
        W-->>C: ListSitesResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `ListSitesResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.site.list_sites()
```

---

### `POST` `/site/v202509/sites`

Configure a new site.

Create configuration for a new site. Returns the newly created configuration.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.site
    participant API as Kentik REST API

    C->>W: create_site(data=CreateSiteRequest(...))
    W->>API: POST /site/v202509/sites
    alt success
        API-->>W: CreateSiteResponse (JSON)
        W-->>C: CreateSiteResponse
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
    participant W as client.site
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: create_site(data=CreateSiteRequest(...))
    W->>R: build_grpc_request(CreateSiteRequest, arguments)
    R->>API: SiteService/CreateSite (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: MessageToDict(response)
        W-->>C: CreateSiteResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `data` | body | `CreateSiteRequest` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `CreateSiteResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI
from kentik_api.gen.site.models import CreateSiteRequest

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.site.create_site(
    data=CreateSiteRequest(...),
)
```

---

### `GET` `/site/v202509/sites/{id}`

Retrieve configuration of a site.

Returns configuration of a site specified by ID.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.site
    participant API as Kentik REST API

    C->>W: get_site(id="id-example")
    W->>API: GET /site/v202509/sites/{id}
    alt success
        API-->>W: GetSiteResponse (JSON)
        W-->>C: GetSiteResponse
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
    participant W as client.site
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: get_site(id="id-example")
    W->>R: build_grpc_request(GetSiteRequest, arguments)
    R->>API: SiteService/GetSite (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: MessageToDict(response)
        W-->>C: GetSiteResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `id` | path | `string` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `GetSiteResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.site.get_site(
    id="id-example",
)
```

---

### `PUT` `/site/v202509/sites/{id}`

Updates configuration of a site.

Replaces configuration of a site with attributes in the request. Returns the updated configuration.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.site
    participant API as Kentik REST API

    C->>W: update_site(id="id-example", data=SiteServiceUpdateSiteBody(...))
    W->>API: PUT /site/v202509/sites/{id}
    alt success
        API-->>W: UpdateSiteResponse (JSON)
        W-->>C: UpdateSiteResponse
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
    participant W as client.site
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: update_site(id="id-example", data=SiteServiceUpdateSiteBody(...))
    W->>R: build_grpc_request(UpdateSiteRequest, arguments)
    R->>API: SiteService/UpdateSite (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: MessageToDict(response)
        W-->>C: UpdateSiteResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `id` | path | `string` | Yes |
| `data` | body | `SiteServiceUpdateSiteBody` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `UpdateSiteResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI
from kentik_api.gen.site.models import SiteServiceUpdateSiteBody

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.site.update_site(
    id="id-example",
    data=SiteServiceUpdateSiteBody(...),
)
```

---

### `DELETE` `/site/v202509/sites/{id}`

Delete configuration of a site.

Deletes configuration of a site with specific ID.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.site
    participant API as Kentik REST API

    C->>W: delete_site(id="id-example")
    W->>API: DELETE /site/v202509/sites/{id}
    alt success
        API-->>W: DeleteSiteResponse (JSON)
        W-->>C: DeleteSiteResponse
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
    participant W as client.site
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: delete_site(id="id-example")
    W->>R: build_grpc_request(DeleteSiteRequest, arguments)
    R->>API: SiteService/DeleteSite (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: MessageToDict(response)
        W-->>C: DeleteSiteResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `id` | path | `string` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `DeleteSiteResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.site.delete_site(
    id="id-example",
)
```

## Data Models

<details>
<summary>Model relationships (18 of 24 models)</summary>

```mermaid
classDiagram
    class CreateSiteMarketRequest
    class CreateSiteMarketResponse
    class CreateSiteRequest
    class CreateSiteResponse
    class DeleteSiteMarketResponse
    class DeleteSiteResponse
    class GetSiteMarketResponse
    class GetSiteResponse
    class ListSiteMarketsResponse
    class ListSitesResponse
    class Site
    class SiteMarket
    class SiteServiceUpdateSiteBody
    class SiteServiceUpdateSiteMarketBody
    class UpdateSiteMarketResponse
    class UpdateSiteResponse
    class protobufAny
    class rpcStatus
    CreateSiteMarketRequest --> SiteMarket
    CreateSiteMarketResponse --> SiteMarket
    CreateSiteRequest --> Site
    CreateSiteResponse --> Site
    GetSiteMarketResponse --> SiteMarket
    GetSiteResponse --> Site
    ListSiteMarketsResponse --> SiteMarket
    ListSitesResponse --> Site
    Site --> SiteMarket
    UpdateSiteMarketResponse --> SiteMarket
    UpdateSiteResponse --> Site
    rpcStatus --> protobufAny
```

</details>

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.site.models.CreateSiteMarketRequest
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.site.models.CreateSiteMarketResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.site.models.CreateSiteRequest
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.site.models.CreateSiteResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.site.models.DeleteSiteMarketResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.site.models.DeleteSiteResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.site.models.GetSiteMarketResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.site.models.GetSiteResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.site.models.Layer
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.site.models.LayerSet
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.site.models.ListSiteMarketsResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.site.models.ListSitesResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.site.models.PeeringDBSiteMapping
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.site.models.PostalAddress
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.site.models.Site
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.site.models.SiteIpAddressClassification
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.site.models.SiteMarket
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.site.models.SiteServiceUpdateSiteBody
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.site.models.SiteServiceUpdateSiteMarketBody
```

```{eval-rst}
.. autoclass:: kentik_api.gen.site.models.SiteType
   :members:
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.site.models.UpdateSiteMarketResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.site.models.UpdateSiteResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.site.models.protobufAny
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.site.models.rpcStatus
```
