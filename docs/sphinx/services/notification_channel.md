# Notification Channel Service

## Overview

```mermaid
flowchart LR
    subgraph sdk["kentik_api"]
        KA["KentikAPI"]
        W["Notification ChannelServiceWrapper\nclient.notification_channel"]
        REST["REST functions\ngen/notification_channel/services/"]
        RJ["request_json()\ncore/rest_runtime"]
        M["Models\ngen/notification_channel/models/"]
        E["Error classes\ngen/notification_channel/error/"]
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

### `GET` `/notification_channel/v202210/notification_channels`

List available notification channels

Returns list of all configured notification channels.

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.notification_channel
    participant API as Kentik API

    C->>W: list_notification_channels()
    W->>API: GET /notification_channel/v202210/notification_channels
    alt success
        API-->>W: ListNotificationChannelsResponse
        W-->>C: ListNotificationChannelsResponse
    else error status
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `ListNotificationChannelsResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.notification_channel.list_notification_channels()
```

---

### `POST` `/notification_channel/v202210/notification_channels/search`

Retrieve notification channels matching criteria.

Returns list of all notification channels matching request criteria. Match criteria are treated as a logical AND, i.e. all provided criteria must match in order for an entry to be included in the response.

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.notification_channel
    participant API as Kentik API

    C->>W: search_notification_channels(data=SearchNotificationChannelsRequest(...))
    W->>API: POST /notification_channel/v202210/notification_channels/search
    alt success
        API-->>W: SearchNotificationChannelsResponse
        W-->>C: SearchNotificationChannelsResponse
    else error status
        API-->>W: error body
        W-->>C: raise HTTPException
    end
```

#### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `data` | body | `SearchNotificationChannelsRequest` | Yes |

#### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `SearchNotificationChannelsResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.notification_channel.search_notification_channels(
    data=SearchNotificationChannelsRequest(...),
)
```

---

### `GET` `/notification_channel/v202210/notification_channels/{id}`

Get information about a notification channel

Returns information about a notification channel with specific ID.

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.notification_channel
    participant API as Kentik API

    C->>W: get_notification_channel(id="id-example")
    W->>API: GET /notification_channel/v202210/notification_channels/{id}
    alt success
        API-->>W: GetNotificationChannelResponse
        W-->>C: GetNotificationChannelResponse
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
| 200 | A successful response. | `GetNotificationChannelResponse` |
| default | An unexpected error response. | `rpcStatus` |

#### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.notification_channel.get_notification_channel(
    id="id-example",
)
```

## Data Models

<details>
<summary>Model relationships (8 of 8 models)</summary>

```mermaid
classDiagram
    class ChannelType
    class GetNotificationChannelResponse
    class ListNotificationChannelsResponse
    class NotificationChannel
    class SearchNotificationChannelsRequest
    class SearchNotificationChannelsResponse
    class protobufAny
    class rpcStatus
    GetNotificationChannelResponse --> NotificationChannel
    ListNotificationChannelsResponse --> NotificationChannel
    NotificationChannel --> ChannelType
    SearchNotificationChannelsRequest --> ChannelType
    SearchNotificationChannelsResponse --> NotificationChannel
    rpcStatus --> protobufAny
```

</details>

```{eval-rst}
.. autoclass:: kentik_api.gen.notification_channel.models.ChannelType
   :members:
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.notification_channel.models.GetNotificationChannelResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.notification_channel.models.ListNotificationChannelsResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.notification_channel.models.NotificationChannel
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.notification_channel.models.SearchNotificationChannelsRequest
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.notification_channel.models.SearchNotificationChannelsResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.notification_channel.models.protobufAny
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.notification_channel.models.rpcStatus
```
