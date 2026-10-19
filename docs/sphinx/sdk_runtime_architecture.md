<!-- AUTO-GENERATED: scripts/generation/docs_rendering.py, _generate_runtime_architecture_docs() -->
<!-- Rebuilt on every `uv run poe generate`. Do not edit by hand. -->

# SDK Runtime Architecture

This page explains how core runtime modules and generated services connect at runtime.

## Runtime Flow

1. `kentik_api.client.KentikAPI` reads credentials and selects transport.
2. `kentik_api.client_mixin.KentikClientMixin` mounts generated service wrappers.
3. Wrapper classes in `kentik_api.gen.<service>.services.<service>` delegate
   to generated REST functions.
4. Generated REST services use `kentik_api.core.api_config` and `kentik_api.core.rest_runtime`.
5. Generated wrappers on a gRPC transport call `kentik_api.core.grpc_runtime`
   instead, against the compiled proto stubs in `kentik_api.gen.<service>.pb`.
6. Runtime failures are normalized into `kentik_api.errors` and generated
   service-local error classes.

## Module Dependency Graph

```mermaid
flowchart TB
    subgraph client["Client Layer"]
        Client_API["Client API"]
        Client_Mixin["Client Mixin"]
    end
    subgraph generated["Generated Layer"]
        Generated_Error_Classes["Generated Error Classes"]
        Generated_Models["Generated Models"]
        Generated_Proto_Stubs["Generated Proto Stubs"]
        Generated_REST_Services["Generated REST Services"]
        Generated_Service_Wrappers["Generated Service Wrappers"]
    end
    subgraph transport["Transport Layer"]
        REST_Transport["REST Transport"]
        Transport_Base["Transport Base"]
        gRPC_Transport["gRPC Transport"]
    end
    subgraph foundation["Shared Foundation"]
        API_Config["API Config"]
        Auth_Credentials["Auth Credentials"]
        Error_Types["Error Types"]
        REST_Runtime["REST Runtime"]
        Rate_Limit["Rate Limit"]
        gRPC_Runtime["gRPC Runtime"]
    end

    API_Config --> Error_Types
    API_Config --> Rate_Limit
    Client_API --> API_Config
    Client_API --> Auth_Credentials
    Client_API --> Client_Mixin
    Client_API --> Error_Types
    Client_API --> REST_Transport
    Client_API --> gRPC_Transport
    Client_Mixin -->|"x37"| Generated_REST_Services
    Client_Mixin -->|"x37"| Generated_Service_Wrappers
    Client_Mixin --> REST_Transport
    Client_Mixin --> gRPC_Transport
    Generated_REST_Services -->|"x54"| API_Config
    Generated_REST_Services -->|"x54"| Generated_Error_Classes
    Generated_REST_Services -->|"x54"| Generated_Models
    Generated_REST_Services -->|"x54"| REST_Runtime
    Generated_Service_Wrappers -->|"x37"| API_Config
    Generated_Service_Wrappers -->|"x37"| Generated_Models
    Generated_Service_Wrappers -->|"x104"| Generated_Proto_Stubs
    Generated_Service_Wrappers -->|"x54"| Generated_REST_Services
    Generated_Service_Wrappers -->|"x37"| REST_Transport
    Generated_Service_Wrappers -->|"x36"| gRPC_Runtime
    Generated_Service_Wrappers -->|"x37"| gRPC_Transport
    REST_Runtime --> API_Config
    REST_Runtime --> Auth_Credentials
    REST_Runtime --> Error_Types
    REST_Runtime --> Rate_Limit
    REST_Transport --> API_Config
    REST_Transport --> Rate_Limit
    REST_Transport --> Transport_Base
    gRPC_Runtime --> API_Config
    gRPC_Runtime --> Error_Types
    gRPC_Runtime --> REST_Runtime
    gRPC_Runtime --> Rate_Limit
    gRPC_Transport --> API_Config
    gRPC_Transport --> Auth_Credentials
    gRPC_Transport --> Error_Types
    gRPC_Transport --> Rate_Limit
    gRPC_Transport --> Transport_Base
```

## Reading The Graph

- `Client API` and `Client Mixin` are the orchestration entrypoints.
- `Generated Service Wrappers` are transport-aware facades exposed as `client.<service>`.
- `Generated REST Services` host operation functions generated from OpenAPI schemas.
- `Generated Proto Stubs` are the protoc-compiled modules that wrappers call on a gRPC transport.
- `API Config`, `REST Runtime`, `gRPC Runtime`, and `Error Types` form the shared runtime foundation.

## Services Without A Wrapper

Wrapper generation is driven by REST paths in the OpenAPI schema. A Service
whose schema declares no paths produces models and proto stubs but no
wrapper, so it is not mounted on the client. That is intentional: REST
operations are this SDK's contract, and proto-driven wrapper generation is
deliberately out of scope.

6 Services are in that state today: `core`, `deviceconf`, `diagnostic`, `kptr`, `monitoring`, `net`.

Some of these declare gRPC RPCs upstream but carry no `google.api.http`
annotation, which is why no path reaches the schema. Those cases are an
upstream schema gap, not an SDK limitation, and they resolve here
automatically once the annotation is added.

## REST-Only Services

These Services come from the local schema base, `schema/openapi/`:
hand-maintained descriptions of endpoints that upstream does not publish.
Every client mounts them on a REST transport to their own host, so a
client created with `protocol="grpc"` sends their calls over REST too: `v5`.
