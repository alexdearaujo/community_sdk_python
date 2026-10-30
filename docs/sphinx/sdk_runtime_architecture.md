<!-- AUTO-GENERATED: scripts/generation/docs_rendering.py, _generate_runtime_architecture_docs() -->
<!-- Rebuilt on every `uv run poe generate`. Do not edit by hand. -->

# SDK Runtime Architecture

This page shows how a call moves through the SDK, and how the hand-written
runtime modules and the generated services depend on each other.

## Call Path

Each method call on `client.<service>` takes one of two paths. The transport
that the client uses selects the path. Both paths return the same Pydantic
models and raise the same exception types.

```mermaid
%%{init: {"fontFamily": "ui-monospace, SFMono-Regular, Menlo, monospace", "flowchart": {"curve": "step", "nodeSpacing": 30, "rankSpacing": 70, "wrappingWidth": 400}}}%%
flowchart LR
    code("Your code"):::greenSrc
    subgraph sdk["kentik_api"]
        wrap("Service wrapper<br/>client.{service}<br/>37 services, 240 operations"):::orange
        rest("REST function<br/>gen/{service}/services/"):::blue
        rj("request_json()<br/>auth headers, quota, errors"):::blue
        cg("call_grpc()<br/>deadline, quota, errors"):::violet
    end
    restapi("Kentik REST API<br/>HTTPS + JSON"):::blueSrc
    grpcapi("Kentik gRPC API<br/>HTTP/2 + protobuf"):::violetSrc

    code -->|"method call"| wrap
    wrap -->|"Pydantic model,<br/>or a raised KentikError"| code
    wrap -->|"arguments"| rest
    rest -->|"Pydantic model"| wrap
    rest -->|"method, path, body,<br/>APIConfig"| rj
    rj -->|"JSON dict + quota"| rest
    rj -->|"HTTPS request"| restapi
    restapi -->|"JSON response"| rj
    wrap -->|"stub method +<br/>proto request"| cg
    cg -->|"proto response + quota"| wrap
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

1. `kentik_api.client.KentikAPI` reads the credentials and selects the transport.
2. `kentik_api.client_mixin.KentikClientMixin` mounts one generated service
   wrapper per service.
3. On a REST transport, a wrapper calls the generated REST function in
   `kentik_api.gen.<service>.services`. That function calls `request_json()`
   in `kentik_api.core.rest_runtime`, with the shared `APIConfig`.
4. On a gRPC transport, a wrapper calls `call_grpc()` in
   `kentik_api.core.grpc_runtime`, with the compiled proto stubs in
   `kentik_api.gen.<service>.pb`.
5. Both runtimes turn each failure into a `kentik_api.errors` type, or into
   the error class that the service generates for that operation.

## Module Dependency Graph

Each arrow points from a module group to a group that it imports. A number
on an arrow counts the import statements. The generator reads the imports
from the source on every run. Colors match the call path: blue is REST,
violet is gRPC, orange is the client and its wrappers, and gray is shared.

```mermaid
%%{init: {"fontFamily": "ui-monospace, SFMono-Regular, Menlo, monospace", "flowchart": {"curve": "step", "nodeSpacing": 30, "rankSpacing": 70, "wrappingWidth": 400}}}%%
flowchart LR
    subgraph client["Client Layer"]
        Client_API("Client API<br/>client.py"):::orange
        Client_Mixin("Client Mixin<br/>client_mixin.py"):::orange
    end
    subgraph generated["Generated Layer"]
        Generated_Error_Classes("Generated Error Classes<br/>gen/{service}/error/"):::hub
        Generated_Models("Generated Models<br/>gen/{service}/models/"):::hub
        Generated_Proto_Stubs("Generated Proto Stubs<br/>gen/{service}/pb/"):::violet
        Generated_REST_Services("Generated REST Services<br/>gen/{service}/services/"):::blue
        Generated_Service_Wrappers("Generated Service Wrappers<br/>gen/{service}/services/{service}.py"):::orange
    end
    subgraph transport["Transport Layer"]
        REST_Transport("REST Transport<br/>transports/rest_client.py"):::blue
        Transport_Base("Transport Base<br/>transports/base.py"):::hub
        gRPC_Transport("gRPC Transport<br/>transports/grpc_client.py"):::violet
    end
    subgraph foundation["Shared Foundation"]
        API_Config("API Config<br/>core/api_config.py"):::hub
        Auth_Credentials("Auth Credentials<br/>auth/"):::hub
        Error_Types("Error Types<br/>errors/"):::hub
        REST_Runtime("REST Runtime<br/>core/rest_runtime.py"):::blue
        Rate_Limit("Rate Limit<br/>core/rate_limit.py"):::hub
        gRPC_Runtime("gRPC Runtime<br/>core/grpc_runtime.py"):::violet
    end

    API_Config -->|"1 import"| Error_Types
    API_Config -->|"1 import"| Rate_Limit
    Client_API -->|"1 import"| API_Config
    Client_API -->|"1 import"| Auth_Credentials
    Client_API -->|"1 import"| Client_Mixin
    Client_API -->|"1 import"| Error_Types
    Client_API -->|"1 import"| REST_Transport
    Client_API -->|"1 import"| gRPC_Transport
    Client_Mixin -->|"37 imports"| Generated_REST_Services
    Client_Mixin -->|"37 imports"| Generated_Service_Wrappers
    Client_Mixin -->|"1 import"| REST_Transport
    Client_Mixin -->|"1 import"| gRPC_Transport
    Generated_REST_Services -->|"54 imports"| API_Config
    Generated_REST_Services -->|"54 imports"| Generated_Error_Classes
    Generated_REST_Services -->|"54 imports"| Generated_Models
    Generated_REST_Services -->|"54 imports"| REST_Runtime
    Generated_Service_Wrappers -->|"37 imports"| API_Config
    Generated_Service_Wrappers -->|"37 imports"| Generated_Models
    Generated_Service_Wrappers -->|"104 imports"| Generated_Proto_Stubs
    Generated_Service_Wrappers -->|"54 imports"| Generated_REST_Services
    Generated_Service_Wrappers -->|"37 imports"| REST_Transport
    Generated_Service_Wrappers -->|"36 imports"| gRPC_Runtime
    Generated_Service_Wrappers -->|"37 imports"| gRPC_Transport
    REST_Runtime -->|"1 import"| API_Config
    REST_Runtime -->|"1 import"| Auth_Credentials
    REST_Runtime -->|"1 import"| Error_Types
    REST_Runtime -->|"1 import"| Rate_Limit
    REST_Transport -->|"1 import"| API_Config
    REST_Transport -->|"1 import"| Rate_Limit
    REST_Transport -->|"1 import"| Transport_Base
    gRPC_Runtime -->|"1 import"| API_Config
    gRPC_Runtime -->|"1 import"| Error_Types
    gRPC_Runtime -->|"1 import"| REST_Runtime
    gRPC_Runtime -->|"1 import"| Rate_Limit
    gRPC_Transport -->|"1 import"| API_Config
    gRPC_Transport -->|"1 import"| Auth_Credentials
    gRPC_Transport -->|"1 import"| Error_Types
    gRPC_Transport -->|"1 import"| Rate_Limit
    gRPC_Transport -->|"1 import"| Transport_Base

    classDef blue fill:#e7f5ff,stroke:#1971c2,color:#1864ab
    classDef hub fill:#f8f9fa,stroke:#495057,color:#212529
    classDef orange fill:#fff4e6,stroke:#e8590c,color:#d9480f
    classDef violet fill:#f3f0ff,stroke:#7048e8,color:#5f3dc4
    classDef blue,hub,orange,violet stroke-width:2px,rx:10px
    style client fill:none,stroke:#868e96,stroke-width:2px
    style generated fill:none,stroke:#868e96,stroke-width:2px
    style transport fill:none,stroke:#868e96,stroke-width:2px
    style foundation fill:none,stroke:#868e96,stroke-width:2px
    linkStyle default stroke-width:2px,stroke-linecap:round,stroke-linejoin:round
```

| Group | Source | Role |
| --- | --- | --- |
| Client API | `client.py` | `KentikAPI`: reads the credentials and selects the transport. |
| Client Mixin | `client_mixin.py` | Mounts each service wrapper as `client.<service>`. |
| Generated Service Wrappers | `gen/{service}/services/{service}.py` | Send each call to the REST function or to the gRPC stub, for the transport in use. |
| Generated REST Services | `gen/{service}/services/` | One function per operation in the OpenAPI schema. Each function calls `request_json()`. |
| Generated Models | `gen/{service}/models/` | Pydantic request and response models. |
| Generated Error Classes | `gen/{service}/error/` | One error class per operation, picked by the response status. |
| Generated Proto Stubs | `gen/{service}/pb/` | The modules that protoc compiles. Wrappers call them on a gRPC transport. |
| API Config | `core/api_config.py` | `APIConfig`: base URL, credentials, TLS, timeouts, and the shared HTTP client. |
| REST Runtime | `core/rest_runtime.py` | `request_json()`: the one function that sends REST traffic. |
| gRPC Runtime | `core/grpc_runtime.py` | `call_grpc()`: the one function that sends gRPC traffic. |
| Error Types | `errors/` | The shared exception hierarchy under `KentikError`. |

## Services Without A Wrapper

The REST paths in the OpenAPI schema drive wrapper generation. If the schema
of a Service declares no paths, the generator writes its models and proto
stubs but no wrapper, and the client does not mount it. This is intentional.
REST operations are the contract of this SDK. Wrapper generation from protos
is out of scope.

6 Services are in that state today: `core`, `deviceconf`, `diagnostic`, `kptr`, `monitoring`, `net`.

Some of these Services declare gRPC RPCs upstream, but the RPCs have no
`google.api.http` annotation, so no path reaches the schema. That is a gap
in the upstream schema, not in the SDK. If upstream adds the annotation, the
next run generates the wrapper.

## REST-Only Services

These Services come from the local schema base, `schema/openapi/`. It holds
descriptions, maintained by hand, of endpoints that upstream does not publish.
Each client mounts these Services on a REST transport to their own host. A
client with `protocol="grpc"` also sends their calls over REST: `v5`.
