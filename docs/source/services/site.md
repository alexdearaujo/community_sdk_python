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

    click KA "src/kentik_api/client.py"
    click W "src/kentik_api/gen/site/services/site.py"
    click REST "src/kentik_api/gen/site/services"
    click RJ "src/kentik_api/core/rest_runtime.py"
    click M "src/kentik_api/gen/site/models"
    click E "src/kentik_api/gen/site/error/__init__.py"
```

## Endpoints

### `GET` `/site/v202509/site_markets`

List all site markets.

Returns list of configured site markets.

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.site
    participant API as Kentik API

    C->>W: list_site_markets()
    W->>API: GET /site/v202509/site_markets
    alt success
        API-->>W: ListSiteMarketsResponse
        W-->>C: ListSiteMarketsResponse
    else error status
        API-->>W: error body
        W-->>C: raise HTTPException
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

client = KentikAPI()  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.site.list_site_markets()
```

---

### `POST` `/site/v202509/site_markets`

Configure a new site market.

Create configuration for a new site market. Returns the newly created configuration.

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.site
    participant API as Kentik API

    C->>W: create_site_market(data=CreateSiteMarketRequest(...))
    W->>API: POST /site/v202509/site_markets
    alt success
        API-->>W: CreateSiteMarketResponse
        W-->>C: CreateSiteMarketResponse
    else error status
        API-->>W: error body
        W-->>C: raise HTTPException
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

client = KentikAPI()  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.site.create_site_market(
    data=CreateSiteMarketRequest(...),
)
```

---

### `GET` `/site/v202509/site_markets/{id}`

Retrieve configuration of a site market.

Returns configuration of a site market specified by ID.

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.site
    participant API as Kentik API

    C->>W: get_site_market(id="id-example")
    W->>API: GET /site/v202509/site_markets/{id}
    alt success
        API-->>W: GetSiteMarketResponse
        W-->>C: GetSiteMarketResponse
    else error status
        API-->>W: error body
        W-->>C: raise HTTPException
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

client = KentikAPI()  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.site.get_site_market(
    id="id-example",
)
```

---

### `PUT` `/site/v202509/site_markets/{id}`

Updates configuration of a site market.

Replaces configuration of a site market with attributes in the request. Returns the updated configuration.

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.site
    participant API as Kentik API

    C->>W: update_site_market(id="id-example", data=SiteServiceUpdateSiteMarketBody(...))
    W->>API: PUT /site/v202509/site_markets/{id}
    alt success
        API-->>W: UpdateSiteMarketResponse
        W-->>C: UpdateSiteMarketResponse
    else error status
        API-->>W: error body
        W-->>C: raise HTTPException
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

client = KentikAPI()  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.site.update_site_market(
    id="id-example",
    data=SiteServiceUpdateSiteMarketBody(...),
)
```

---

### `DELETE` `/site/v202509/site_markets/{id}`

Delete configuration of a site market.

Deletes configuration of a site market with specific ID.

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.site
    participant API as Kentik API

    C->>W: delete_site_market(id="id-example")
    W->>API: DELETE /site/v202509/site_markets/{id}
    alt success
        API-->>W: DeleteSiteMarketResponse
        W-->>C: DeleteSiteMarketResponse
    else error status
        API-->>W: error body
        W-->>C: raise HTTPException
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

client = KentikAPI()  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.site.delete_site_market(
    id="id-example",
)
```

---

### `GET` `/site/v202509/sites`

List all sites.

Returns list of configured sites.

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.site
    participant API as Kentik API

    C->>W: list_sites()
    W->>API: GET /site/v202509/sites
    alt success
        API-->>W: ListSitesResponse
        W-->>C: ListSitesResponse
    else error status
        API-->>W: error body
        W-->>C: raise HTTPException
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

client = KentikAPI()  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.site.list_sites()
```

---

### `POST` `/site/v202509/sites`

Configure a new site.

Create configuration for a new site. Returns the newly created configuration.

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.site
    participant API as Kentik API

    C->>W: create_site(data=CreateSiteRequest(...))
    W->>API: POST /site/v202509/sites
    alt success
        API-->>W: CreateSiteResponse
        W-->>C: CreateSiteResponse
    else error status
        API-->>W: error body
        W-->>C: raise HTTPException
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

client = KentikAPI()  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.site.create_site(
    data=CreateSiteRequest(...),
)
```

---

### `GET` `/site/v202509/sites/{id}`

Retrieve configuration of a site.

Returns configuration of a site specified by ID.

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.site
    participant API as Kentik API

    C->>W: get_site(id="id-example")
    W->>API: GET /site/v202509/sites/{id}
    alt success
        API-->>W: GetSiteResponse
        W-->>C: GetSiteResponse
    else error status
        API-->>W: error body
        W-->>C: raise HTTPException
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

client = KentikAPI()  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.site.get_site(
    id="id-example",
)
```

---

### `PUT` `/site/v202509/sites/{id}`

Updates configuration of a site.

Replaces configuration of a site with attributes in the request. Returns the updated configuration.

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.site
    participant API as Kentik API

    C->>W: update_site(id="id-example", data=SiteServiceUpdateSiteBody(...))
    W->>API: PUT /site/v202509/sites/{id}
    alt success
        API-->>W: UpdateSiteResponse
        W-->>C: UpdateSiteResponse
    else error status
        API-->>W: error body
        W-->>C: raise HTTPException
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

client = KentikAPI()  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.site.update_site(
    id="id-example",
    data=SiteServiceUpdateSiteBody(...),
)
```

---

### `DELETE` `/site/v202509/sites/{id}`

Delete configuration of a site.

Deletes configuration of a site with specific ID.

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.site
    participant API as Kentik API

    C->>W: delete_site(id="id-example")
    W->>API: DELETE /site/v202509/sites/{id}
    alt success
        API-->>W: DeleteSiteResponse
        W-->>C: DeleteSiteResponse
    else error status
        API-->>W: error body
        W-->>C: raise HTTPException
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

client = KentikAPI()  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
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
