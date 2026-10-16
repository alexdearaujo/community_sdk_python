<!-- HAND-WRITTEN: not modified by [`make generate`](../../../Makefile). Edit directly. -->

# Migrating from 1.x

Version 2 is a new SDK with the same package name. It shares no code with
[kentik-api 1.x](https://github.com/kentik/community_sdk_python/tree/v1.0.7).
Version 1 wrapped the V5 REST API, which Kentik discontinued in January 2025,
plus two V6 gRPC services. Version 2 is generated from Kentik's V6 API schema,
and it covers every V6 service that the schema publishes.

There is no compatibility layer. Rewrite each call against the new client.

## At a glance

| | 1.x | 2.x |
| --- | --- | --- |
| Python | 3.8 and later | 3.12 and later |
| API | V5 REST, plus V6 gRPC for synthetics and cloud export | V6, over REST or gRPC |
| Import | `from kentik_api import KentikAPI` | `from kentik_api.client import KentikAPI` |
| Credentials | `KentikAPI(email, token)`, or a profile in `~/.kentik/` | Arguments, `KENTIK_EMAIL` / `KENTIK_API_TOKEN`, or a `.env` file |
| Region | `api_host="api.kentik.eu"` | `region="eu"` |
| Resources | `client.sites`, `client.devices` | `client.site`, `client.device`, one attribute per service |
| Methods | `get_all()`, `get(id)`, `create(obj)` | Named after the API operation: `list_sites()`, `get_site(id=...)` |
| Arguments | Positional | Keyword only |
| Data types | Hand-written classes such as `Site` | Generated Pydantic models |
| Errors | `KentikAPIError` and subclasses | `KentikError` and subclasses |
| Timeout | `timeout=(10.0, 60.0)` | `timeout=60.0`, or `rest_timeout=httpx.Timeout(...)` |
| Retries | `retry_strategy=Retry(...)` | Failed connection attempts only, twice. No retry after the server responds. |
| Proxy | `proxy="http://..."` | The `https_proxy` and `no_proxy` environment variables, on both transports |

## One call, before and after

1.x:

```python
from kentik_api import KentikAPI, Site

client = KentikAPI(email, token)
created = client.sites.create(Site(site_name="lab", latitude=49, longitude=12))
got = client.sites.get(created.id)
```

2.x:

```python
from kentik_api.client import KentikAPI
from kentik_api.gen.site.models import CreateSiteRequest, Site, SiteType

with KentikAPI(email=email, api_token=token) as client:
    created = client.site.create_site(
        data=CreateSiteRequest(
            site=Site(title="lab", lat=49, lon=12, type=SiteType.SITE_TYPE_DATA_CENTER)
        )
    )
    got = client.site.get_site(id=created.site.id)
```

Field names follow the V6 schema, not 1.x. In this example, `site_name` becomes
`title`, and `latitude` becomes `lat`. Each service's reference page lists its
operations and models, for example [site](../services/site.md).

## Credentials

1.x read `KTAPI_AUTH_EMAIL` and `KTAPI_AUTH_TOKEN` in its examples, or a JSON
profile under `~/.kentik/`. 2.x reads neither. See
[Authentication](../authentication.md) for the order in which 2.x looks for
credentials, and for how to keep them encrypted.

## Errors

| 1.x | 2.x |
| --- | --- |
| `KentikAPIError` | `KentikError` |
| `AuthError` | `AuthenticationError` |
| `TimedOutError`, `UnavailabilityError` | `TransportError` |
| `NotFoundError`, `BadRequestError` | `HTTPException`, with `status_code` 404 or 400 |
| `RateLimitExceededError` | `HTTPException` with `status_code` 429. The quota is in `exc.rate_limit`. |

See the [error handling guide](error_handling.md).

## Features that 1.x had and 2.x does not

| 1.x feature | In 2.x |
| --- | --- |
| `client.query` (V5 query API) | V5 is discontinued. There is no V6 equivalent in the schema. |
| `client.batch` (V5 batch API) | V5 is discontinued. |
| `kentik_api.analytics` (pandas helpers) | Removed. |
| `retry_strategy` | Removed. See the [rate limiting guide](rate_limiting.md) for why the SDK does not retry after a response. |
