<!-- HAND-WRITTEN: not modified by [`make generate`](Makefile). Edit directly. -->

# Changelog

This file lists the changes a caller of the SDK can see. The generated API
surface (services, operations, model fields, and enum values) has its own
record in [`api_surface.json`](api_surface.json). To list surface changes
between two releases, run
[`scripts/release_notes.py`](scripts/release_notes.py):

```bash
make release-notes SINCE=v1.0.7
```

Each release appends that list to its GitHub release notes. A pull request
whose surface change can break a caller (a removed or retyped field, for
example) fails `make check-changelog` until this file names the change.

`make generate` does not edit this file. When a regeneration ends with
`⚠️ API SURFACE CHANGED`, add an entry here for each listed change before you
commit. See "Update the release notes after every regeneration" in
[the generation guide](docs/sphinx/guides/generation.md).

## Unreleased

This is the first release of the SDK for Kentik's V6 API, and it replaces
kentik-api 1.x completely. If you come from 1.x, read
[Migrating from 1.x](docs/sphinx/guides/migrating-from-1x.md) instead of the
tables below, which compare against earlier development builds of this SDK.

### Breaking changes

Each change below can stop an existing `except` clause or call from working.

| Before | After | What to change |
| --- | --- | --- |
| `KentikAPI(...)` raised `ValueError` for missing credentials, an unknown region, or an unknown protocol | It raises `ConfigurationError` | Catch `ConfigurationError` or `KentikError` |
| A REST 401 raised the operation's generated `HTTPException` subclass | It raises `AuthenticationError`, as gRPC does | Catch `AuthenticationError` |
| gRPC `CANCELLED`, `DEADLINE_EXCEEDED`, and `UNAVAILABLE` raised `HTTPException` with status 500 or 503 | They raise `TransportError`, as REST does for the same failures | Catch `TransportError` |
| A gRPC status code with no mapping raised `HTTPException(500)` | Every code has an explicit mapping; an unrecognized code raises `TransportError` | See the table in [the error handling guide](docs/sphinx/guides/error_handling.md) |
| A gRPC call had no deadline and could block forever | Every gRPC call has a deadline, 60 seconds by default | Set `timeout` or `grpc_deadline` for longer calls |
| `call_grpc()` wrapped any exception from the stub in `TransportError` | Only a gRPC error is converted; other exceptions propagate unchanged | Catch the original exception type |
| `call_grpc()` returned the response | It returns `(response, rate_limit)` | Unpack the tuple |
| `KentikCredentials.get_rest_headers()` existed | It is removed | Use `kentik_api.auth.credentials.auth_headers(email, api_token)` |
| An `APIConfig` with no credentials failed inside httpx with `TypeError` | It raises `ConfigurationError` before the SDK sends a request | Give the config `auth_email` and `auth_token` |
| `KentikAPI(...)` loaded every key of the nearest `.env` into `os.environ`, even when you passed credentials | It reads only `KENTIK_EMAIL` and `KENTIK_API_TOKEN`, into memory, and only when an argument or environment variable is missing | Load other `.env` keys yourself, for example with `dotenv.load_dotenv()` |
| `kmeta` `ServiceNowConfig.credentialVaultId` held a credential vault entry ID | Upstream renamed it `credentialVaultName`; it holds the entry's name and always resolves to the entry's latest version | Read and send `credentialVaultName` |

### Added

- **`kmeta` service.** `client.kmeta` manages ServiceNow configurations: list,
  get, create, update, and delete. It predates `api_surface.json`, so
  `make release-notes` does not list it.
- **`nms` service.** `client.nms.metrics_schema_service__get_metrics_schema()`
  returns the NMS metrics schema: each measurement and its fields, on REST
  and gRPC. The response's `schema` field is `schema_` in Python, because
  `schema` is a `BaseModel` attribute.
- **Static agent addresses.** `synthetics` `AgentMetadata` has read-only
  `staticIpv4` and `staticIpv6`, true when the agent's public address does not
  change.
- **`env_file` argument.** `KentikAPI(env_file=path)` reads credentials from
  that file. `env_file=None` turns off file lookup. See
  [Authentication](docs/sphinx/authentication.md) for use with encrypted
  secrets such as sops.
- **Timeouts.** `KentikAPI` and `APIConfig` accept `timeout` (both transports),
  `rest_timeout` (a number or a per-phase `httpx.Timeout`), and
  `grpc_deadline`. A zero or negative value raises `ConfigurationError`.
- **Per-call overrides.** Every service method accepts `api_config_override`.
  `client.api_config.with_timeout(300)` gives a copy with a longer timeout
  that shares the client's connection and credentials. An override replaces
  the client's configuration for that call. On gRPC, only its deadline
  applies.
- **Quota reporting.** `kentik_api.rate_limit_of(result)` returns the quota
  that the call reported. Every SDK exception has a `rate_limit` attribute.
  `client._transport.rate_limits` holds the latest quota for each endpoint.
  See [the rate limiting guide](docs/sphinx/guides/rate_limiting.md).
- **`HTTPException.grpc_status_code`** holds the gRPC status name verbatim.
- **Connection reuse.** A `KentikAPI` client uses one HTTP connection for all
  its REST calls. `close()` releases it. A call after `close()` raises
  `ConfigurationError`.
- **Connection retries.** The SDK retries a failed connection attempt twice.
  It never retries a request that reached the server. A call through a proxy
  is not retried, because httpcore does not support retries for proxy
  connections.
- **Proxies.** REST calls honor `HTTPS_PROXY`, `HTTP_PROXY`, `ALL_PROXY`, and
  `NO_PROXY` (either case). gRPC already honored the lowercase `https_proxy` and
  `no_proxy`. There is no `proxy=` argument.

### Fixed

- **gRPC calls reach the right RPC.** In a Service with more than one proto
  service, such as `alerting`, a gRPC call went to whichever service declared
  an RPC of the same name last. For example, deleting an AlertAutoAck called
  `SuppressionService.Delete`. Each call now goes to the RPC that shares its
  REST operation's HTTP rule. No proto declares `MitigationsService`, so on
  gRPC its `list`, `create`, and `get` now raise `NotImplementedError`, as its
  other operations already did, instead of calling SuppressionService.
- **gRPC calls send every argument.** Path and query arguments were sent
  under their Python names, which match no proto field, and were dropped.
  For example, `client.device.get_device(deviceid="42")` sent an empty `id`,
  and pagination and filter arguments had no effect. They now set the request
  field that grpc-gateway sets for the same REST call.
- **More operations work on gRPC.** 32 operations that raised
  `NotImplementedError` on gRPC now make the call, because their REST name
  differed from their RPC name.
- **REST path arguments are encoded.** A path argument went into the URL
  as is, so `client.device.delete_device(deviceid="../../user/7")` sent the
  DELETE to another resource, and a `?` or `#` cut the path short. Each path
  argument is now percent-encoded into its own segment. An empty string, `.`,
  or `..`, which encoding cannot keep in place, raises `ValueError` before the
  SDK sends a request.

### Dependencies

The generated gRPC and protobuf modules refuse to import on older runtimes, so
the declared floors match them:

| Package | Before | After |
| --- | --- | --- |
| `grpcio` | `>=1.78.0` | `>=1.84.0` |
| `protobuf` | not declared | `>=7.35.1,<8` |

### Documentation

- The quickstart, REST, gRPC, error handling, and generation guides are part
  of the published documentation.
- A new [rate limiting guide](docs/sphinx/guides/rate_limiting.md) covers the
  quota headers and the three limits that no header shows.
