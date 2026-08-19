# SDK Runtime Architecture

This page explains how core runtime modules and generated services connect at runtime.

## Runtime Flow

1. `kentik_api.client.KentikAPI` reads credentials and selects transport.
2. `kentik_api.client_mixin.KentikClientMixin` mounts generated service wrappers.
3. Wrapper classes in `kentik_api.gen.<service>.services.<service>` delegate
   to generated REST functions.
4. Generated REST services use `kentik_api.core.api_config` and `kentik_api.core.rest_runtime`.
5. Runtime failures are normalized into `kentik_api.errors` and generated
   service-local error classes.

## Module Dependency Graph

```mermaid
flowchart LR
    API_Config["API Config"]
    Auth_Credentials["Auth Credentials"]
    Client_API["Client API"]
    Client_Mixin["Client Mixin"]
    Error_Types["Error Types"]
    Generated_Error_Classes["Generated Error Classes"]
    Generated_Models["Generated Models"]
    Generated_REST_Services["Generated REST Services"]
    Generated_Service_Wrappers["Generated Service Wrappers"]
    REST_Runtime["REST Runtime"]
    REST_Transport["REST Transport"]
    Transport_Base["Transport Base"]
    gRPC_Transport["gRPC Transport"]

    API_Config --> Error_Types
    Client_API --> Auth_Credentials
    Client_API --> Client_Mixin
    Client_API --> REST_Transport
    Client_API --> gRPC_Transport
    Client_Mixin -->|"x32"| Generated_Service_Wrappers
    Client_Mixin --> REST_Transport
    Client_Mixin --> gRPC_Transport
    Generated_REST_Services -->|"x43"| API_Config
    Generated_REST_Services -->|"x43"| Generated_Error_Classes
    Generated_REST_Services -->|"x43"| Generated_Models
    Generated_REST_Services -->|"x43"| REST_Runtime
    Generated_Service_Wrappers -->|"x43"| Generated_REST_Services
    Generated_Service_Wrappers -->|"x32"| REST_Transport
    Generated_Service_Wrappers -->|"x32"| gRPC_Transport
    REST_Runtime --> API_Config
    REST_Runtime --> Error_Types
    REST_Transport --> API_Config
    REST_Transport --> Auth_Credentials
    REST_Transport --> Transport_Base
    gRPC_Transport --> Auth_Credentials
    gRPC_Transport --> Transport_Base

    click API_Config "../../src/kentik_api/core/api_config.py"
    click Auth_Credentials "../../src/kentik_api/auth/credentials.py"
    click Client_API "../../src/kentik_api/client.py"
    click Client_Mixin "../../src/kentik_api/client_mixin.py"
    click Error_Types "../../src/kentik_api/errors/__init__.py"
    click Generated_Error_Classes "../../src/kentik_api/gen/"
    click Generated_Models "../../src/kentik_api/gen/"
    click Generated_REST_Services "../../src/kentik_api/gen/"
    click Generated_Service_Wrappers "../../src/kentik_api/gen/"
    click REST_Runtime "../../src/kentik_api/core/rest_runtime.py"
    click REST_Transport "../../src/kentik_api/transports/rest_client.py"
    click Transport_Base "../../src/kentik_api/transports/base.py"
    click gRPC_Transport "../../src/kentik_api/transports/grpc_client.py"
```

## Reading The Graph

- `Client API` and `Client Mixin` are the orchestration entrypoints.
- `Generated Service Wrappers` are transport-aware facades exposed as `client.<service>`.
- `Generated REST Services` host operation functions generated from OpenAPI schemas.
- `API Config`, `REST Runtime`, and `Error Types` form the shared runtime foundation.
