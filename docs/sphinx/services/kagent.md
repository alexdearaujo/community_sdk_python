<!-- AUTO-GENERATED: scripts/generation/endpoint_docs.py, render_endpoint_docs() -->
<!-- Rebuilt on every `make generate`. Do not edit by hand. -->

# Kagent Service

## Overview

```mermaid
flowchart LR
    subgraph sdk["kentik_api"]
        KA["KentikAPI"]
        W["KagentServiceWrapper\nclient.kagent"]
        REST["REST functions\ngen/kagent/services/"]
        RJ["request_json()\ncore/rest_runtime"]
        M["Models\ngen/kagent/models/"]
        E["Error classes\ngen/kagent/error/"]
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

### AgentService

#### `GET` `/kagent/v202401/agents`

List agents.

Returns a list of agents in the account, optionally filtered by registration state, IDs or capabilities.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.kagent
    participant API as Kentik REST API

    C->>W: list_agents()
    W->>API: GET /kagent/v202401/agents
    alt success
        API-->>W: ListAgentsResponse (JSON)
        W-->>C: ListAgentsResponse
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
    participant W as client.kagent
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: list_agents()
    W->>R: build_grpc_request(ListAgentsRequest, arguments)
    R->>API: AgentService/ListAgents (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: parse_grpc_response(response)
        W-->>C: ListAgentsResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

##### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `unregistered` | query | `boolean` | No |
| `ids` | query | `string[]` | No |
| `capabilities` | query | `string[]` | No |
| `includeDesiredState` | query | `boolean` | No |

##### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `ListAgentsResponse` |
| default | An unexpected error response. | `rpcStatus` |

##### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.kagent.list_agents()
```

---

#### `POST` `/kagent/v202401/agents`

Create an agent.

Registers a new agent based on configuration in the request and returns it together with the commands for installing it on the target host.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.kagent
    participant API as Kentik REST API

    C->>W: create_agent(data=CreateAgentRequest(...))
    W->>API: POST /kagent/v202401/agents
    alt success
        API-->>W: CreateAgentResponse (JSON)
        W-->>C: CreateAgentResponse
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
    participant W as client.kagent
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: create_agent(data=CreateAgentRequest(...))
    W->>R: build_grpc_request(CreateAgentRequest, arguments)
    R->>API: AgentService/CreateAgent (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: parse_grpc_response(response)
        W-->>C: CreateAgentResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

##### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `data` | body | `CreateAgentRequest` | Yes |

##### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `CreateAgentResponse` |
| default | An unexpected error response. | `rpcStatus` |

##### Example

```python
from kentik_api.client import KentikAPI
from kentik_api.gen.kagent.models import CreateAgentRequest

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.kagent.create_agent(
    data=CreateAgentRequest(...),
)
```

---

#### `PUT` `/kagent/v202401/agents/authorize/{installId}`

Authorize an unregistered agent.

Approves the agent installed under the specified install ID and returns the ID assigned to it.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.kagent
    participant API as Kentik REST API

    C->>W: authorize(installId="installId-example")
    W->>API: PUT /kagent/v202401/agents/authorize/{installId}
    alt success
        API-->>W: AuthorizeResponse (JSON)
        W-->>C: AuthorizeResponse
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
    participant W as client.kagent
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: authorize(installId="installId-example")
    W->>R: build_grpc_request(AuthorizeRequest, arguments)
    R->>API: AgentService/Authorize (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: parse_grpc_response(response)
        W-->>C: AuthorizeResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

##### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `installId` | path | `string` | Yes |

##### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `AuthorizeResponse` |
| default | An unexpected error response. | `rpcStatus` |

##### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.kagent.authorize(
    installId="installId-example",
)
```

---

#### `POST` `/kagent/v202401/agents/install-commands`

Generate agent install commands.

Returns commands for deploying an agent. The commands embed a provisioning token and are ready to execute on the target host.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.kagent
    participant API as Kentik REST API

    C->>W: generate_install_commands(data=GenerateInstallCommandsRequest(...))
    W->>API: POST /kagent/v202401/agents/install-commands
    alt success
        API-->>W: GenerateInstallCommandsResponse (JSON)
        W-->>C: GenerateInstallCommandsResponse
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
    participant W as client.kagent
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: generate_install_commands(data=GenerateInstallCommandsRequest(...))
    W->>R: build_grpc_request(GenerateInstallCommandsRequest, arguments)
    R->>API: AgentService/GenerateInstallCommands (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: parse_grpc_response(response)
        W-->>C: GenerateInstallCommandsResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

##### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `data` | body | `GenerateInstallCommandsRequest` | Yes |

##### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `GenerateInstallCommandsResponse` |
| default | An unexpected error response. | `rpcStatus` |

##### Example

```python
from kentik_api.client import KentikAPI
from kentik_api.gen.kagent.models import GenerateInstallCommandsRequest

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.kagent.generate_install_commands(
    data=GenerateInstallCommandsRequest(...),
)
```

---

#### `GET` `/kagent/v202401/agents/{agent.id}`

Get agent configuration and state.

Returns configuration and state of the agent with the specified ID.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.kagent
    participant API as Kentik REST API

    C->>W: get_agent(agentid="agentid-example")
    W->>API: GET /kagent/v202401/agents/{agent.id}
    alt success
        API-->>W: GetAgentResponse (JSON)
        W-->>C: GetAgentResponse
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
    participant W as client.kagent
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: get_agent(agentid="agentid-example")
    W->>R: build_grpc_request(GetAgentRequest, arguments)
    R->>API: AgentService/GetAgent (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: parse_grpc_response(response)
        W-->>C: GetAgentResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

##### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `agentid` | path | `string` | Yes |
| `unregistered` | query | `boolean` | No |

##### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `GetAgentResponse` |
| default | An unexpected error response. | `rpcStatus` |

##### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.kagent.get_agent(
    agentid="agentid-example",
)
```

---

#### `PATCH` `/kagent/v202401/agents/{agent.id}`

Update configuration of an agent.

Updates the attributes of an agent selected by the field mask in the request.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.kagent
    participant API as Kentik REST API

    C->>W: update_agent(agentid="agentid-example", data=AgentServiceUpdateAgentBody(...))
    W->>API: PATCH /kagent/v202401/agents/{agent.id}
    alt success
        API-->>W: UpdateAgentResponse (JSON)
        W-->>C: UpdateAgentResponse
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
    participant W as client.kagent
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: update_agent(agentid="agentid-example", data=AgentServiceUpdateAgentBody(...))
    W->>R: build_grpc_request(UpdateAgentRequest, arguments)
    R->>API: AgentService/UpdateAgent (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: parse_grpc_response(response)
        W-->>C: UpdateAgentResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

##### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `agentid` | path | `string` | Yes |
| `mask` | query | `string` | No |
| `data` | body | `AgentServiceUpdateAgentBody` | Yes |

##### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `UpdateAgentResponse` |
| default | An unexpected error response. | `rpcStatus` |

##### Example

```python
from kentik_api.client import KentikAPI
from kentik_api.gen.kagent.models import AgentServiceUpdateAgentBody

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.kagent.update_agent(
    agentid="agentid-example",
    data=AgentServiceUpdateAgentBody(...),
)
```

---

#### `DELETE` `/kagent/v202401/agents/{agent.id}`

Delete an agent.

Deletes the agent with the specified ID.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.kagent
    participant API as Kentik REST API

    C->>W: delete_agent(agentid="agentid-example")
    W->>API: DELETE /kagent/v202401/agents/{agent.id}
    alt success
        API-->>W: DeleteAgentResponse (JSON)
        W-->>C: DeleteAgentResponse
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
    participant W as client.kagent
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: delete_agent(agentid="agentid-example")
    W->>R: build_grpc_request(DeleteAgentRequest, arguments)
    R->>API: AgentService/DeleteAgent (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: parse_grpc_response(response)
        W-->>C: DeleteAgentResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

##### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `agentid` | path | `string` | Yes |
| `unregistered` | query | `boolean` | No |

##### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `DeleteAgentResponse` |
| default | An unexpected error response. | `rpcStatus` |

##### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.kagent.delete_agent(
    agentid="agentid-example",
)
```

### AgentCapabilityService

#### `GET` `/kagent/v202401/agents/{agentId}/capabilities`

List agent capabilities.

Returns a list of all capabilities of the specified agent.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.kagent
    participant API as Kentik REST API

    C->>W: list_agent_capabilities(agentId="agentId-example")
    W->>API: GET /kagent/v202401/agents/{agentId}/capabilities
    alt success
        API-->>W: ListAgentCapabilitiesResponse (JSON)
        W-->>C: ListAgentCapabilitiesResponse
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
    participant W as client.kagent
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: list_agent_capabilities(agentId="agentId-example")
    W->>R: build_grpc_request(ListAgentCapabilitiesRequest, arguments)
    R->>API: AgentCapabilityService/ListAgentCapabilities (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: parse_grpc_response(response)
        W-->>C: ListAgentCapabilitiesResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

##### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `agentId` | path | `string` | Yes |

##### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `ListAgentCapabilitiesResponse` |
| default | An unexpected error response. | `rpcStatus` |

##### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.kagent.list_agent_capabilities(
    agentId="agentId-example",
)
```

---

#### `GET` `/kagent/v202401/agents/{agentId}/capabilities/{capability.name}`

Get an agent capability.

Returns configuration of the named capability of the specified agent.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.kagent
    participant API as Kentik REST API

    C->>W: get_agent_capability(agentId="agentId-example", capabilityname="capabilityname-example")
    W->>API: GET /kagent/v202401/agents/{agentId}/capabilities/{capability.name}
    alt success
        API-->>W: GetAgentCapabilityResponse (JSON)
        W-->>C: GetAgentCapabilityResponse
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
    participant W as client.kagent
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: get_agent_capability(agentId="agentId-example", capabilityname="capabilityname-example")
    W->>R: build_grpc_request(GetAgentCapabilityRequest, arguments)
    R->>API: AgentCapabilityService/GetAgentCapability (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: parse_grpc_response(response)
        W-->>C: GetAgentCapabilityResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

##### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `agentId` | path | `string` | Yes |
| `capabilityname` | path | `string` | Yes |

##### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `GetAgentCapabilityResponse` |
| default | An unexpected error response. | `rpcStatus` |

##### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.kagent.get_agent_capability(
    agentId="agentId-example",
    capabilityname="capabilityname-example",
)
```

---

#### `PATCH` `/kagent/v202401/agents/{agentId}/capabilities/{capability.name}`

Create or update an agent capability.

Adds the capability to the agent, or updates it if already present.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.kagent
    participant API as Kentik REST API

    C->>W: upsert_agent_capability(agentId="agentId-example", capabilityname="capabilityname-example", data=AgentCapabilityServiceUpsertAgentCapabilityBody(...))
    W->>API: PATCH /kagent/v202401/agents/{agentId}/capabilities/{capability.name}
    alt success
        API-->>W: UpsertAgentCapabilityResponse (JSON)
        W-->>C: UpsertAgentCapabilityResponse
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
    participant W as client.kagent
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: upsert_agent_capability(agentId="agentId-example", capabilityname="capabilityname-example", data=AgentCapabilityServiceUpsertAgentCapabilityBody(...))
    W->>R: build_grpc_request(UpsertAgentCapabilityRequest, arguments)
    R->>API: AgentCapabilityService/UpsertAgentCapability (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: parse_grpc_response(response)
        W-->>C: UpsertAgentCapabilityResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

##### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `agentId` | path | `string` | Yes |
| `capabilityname` | path | `string` | Yes |
| `mask` | query | `string` | No |
| `data` | body | `AgentCapabilityServiceUpsertAgentCapabilityBody` | Yes |

##### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `UpsertAgentCapabilityResponse` |
| default | An unexpected error response. | `rpcStatus` |

##### Example

```python
from kentik_api.client import KentikAPI
from kentik_api.gen.kagent.models import AgentCapabilityServiceUpsertAgentCapabilityBody

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.kagent.upsert_agent_capability(
    agentId="agentId-example",
    capabilityname="capabilityname-example",
    data=AgentCapabilityServiceUpsertAgentCapabilityBody(...),
)
```

---

#### `DELETE` `/kagent/v202401/agents/{agentId}/capabilities/{capability.name}`

Delete an agent capability.

Removes the named capability from the specified agent.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.kagent
    participant API as Kentik REST API

    C->>W: delete_agent_capability(agentId="agentId-example", capabilityname="capabilityname-example")
    W->>API: DELETE /kagent/v202401/agents/{agentId}/capabilities/{capability.name}
    alt success
        API-->>W: DeleteAgentCapabilityResponse (JSON)
        W-->>C: DeleteAgentCapabilityResponse
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
    participant W as client.kagent
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: delete_agent_capability(agentId="agentId-example", capabilityname="capabilityname-example")
    W->>R: build_grpc_request(DeleteAgentCapabilityRequest, arguments)
    R->>API: AgentCapabilityService/DeleteAgentCapability (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: parse_grpc_response(response)
        W-->>C: DeleteAgentCapabilityResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

##### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `agentId` | path | `string` | Yes |
| `capabilityname` | path | `string` | Yes |

##### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `DeleteAgentCapabilityResponse` |
| default | An unexpected error response. | `rpcStatus` |

##### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.kagent.delete_agent_capability(
    agentId="agentId-example",
    capabilityname="capabilityname-example",
)
```

### CapabilityAdminService

#### `GET` `/kagent/v202401/capabilities`

List all capabilities

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.kagent
    participant API as Kentik REST API

    C->>W: list_capabilities()
    W->>API: GET /kagent/v202401/capabilities
    alt success
        API-->>W: ListCapabilitiesResponse (JSON)
        W-->>C: ListCapabilitiesResponse
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
    participant W as client.kagent
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: list_capabilities()
    W->>R: build_grpc_request(ListCapabilitiesRequest, arguments)
    R->>API: CapabilityAdminService/ListCapabilities (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: parse_grpc_response(response)
        W-->>C: ListCapabilitiesResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

##### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `ListCapabilitiesResponse` |
| default | An unexpected error response. | `rpcStatus` |

##### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.kagent.list_capabilities()
```

---

#### `POST` `/kagent/v202401/capabilities`

Create a new capability

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.kagent
    participant API as Kentik REST API

    C->>W: create_capability(data=Capability(...))
    W->>API: POST /kagent/v202401/capabilities
    alt success
        API-->>W: CreateCapabilityResponse (JSON)
        W-->>C: CreateCapabilityResponse
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
    participant W as client.kagent
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: create_capability(data=Capability(...))
    W->>R: build_grpc_request(CreateCapabilityRequest, arguments)
    R->>API: CapabilityAdminService/CreateCapability (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: parse_grpc_response(response)
        W-->>C: CreateCapabilityResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

##### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `data` | body | `Capability` | Yes |

##### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `CreateCapabilityResponse` |
| default | An unexpected error response. | `rpcStatus` |

##### Example

```python
from kentik_api.client import KentikAPI
from kentik_api.gen.kagent.models import Capability

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.kagent.create_capability(
    data=Capability(...),
)
```

---

#### `GET` `/kagent/v202401/capabilities/{capability.name}`

Get a capabilities

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.kagent
    participant API as Kentik REST API

    C->>W: get_capability(capabilityname="capabilityname-example")
    W->>API: GET /kagent/v202401/capabilities/{capability.name}
    alt success
        API-->>W: GetCapabilityResponse (JSON)
        W-->>C: GetCapabilityResponse
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
    participant W as client.kagent
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: get_capability(capabilityname="capabilityname-example")
    W->>R: build_grpc_request(GetCapabilityRequest, arguments)
    R->>API: CapabilityAdminService/GetCapability (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: parse_grpc_response(response)
        W-->>C: GetCapabilityResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

##### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `capabilityname` | path | `string` | Yes |

##### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `GetCapabilityResponse` |
| default | An unexpected error response. | `rpcStatus` |

##### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.kagent.get_capability(
    capabilityname="capabilityname-example",
)
```

---

#### `PATCH` `/kagent/v202401/capabilities/{capability.name}`

Update an existing capability

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.kagent
    participant API as Kentik REST API

    C->>W: update_capability(capabilityname="capabilityname-example", data=CapabilityAdminServiceUpdateCapabilityBody(...))
    W->>API: PATCH /kagent/v202401/capabilities/{capability.name}
    alt success
        API-->>W: UpdateCapabilityResponse (JSON)
        W-->>C: UpdateCapabilityResponse
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
    participant W as client.kagent
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: update_capability(capabilityname="capabilityname-example", data=CapabilityAdminServiceUpdateCapabilityBody(...))
    W->>R: build_grpc_request(UpdateCapabilityRequest, arguments)
    R->>API: CapabilityAdminService/UpdateCapability (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: parse_grpc_response(response)
        W-->>C: UpdateCapabilityResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

##### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `capabilityname` | path | `string` | Yes |
| `data` | body | `CapabilityAdminServiceUpdateCapabilityBody` | Yes |

##### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `UpdateCapabilityResponse` |
| default | An unexpected error response. | `rpcStatus` |

##### Example

```python
from kentik_api.client import KentikAPI
from kentik_api.gen.kagent.models import CapabilityAdminServiceUpdateCapabilityBody

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.kagent.update_capability(
    capabilityname="capabilityname-example",
    data=CapabilityAdminServiceUpdateCapabilityBody(...),
)
```

---

#### `DELETE` `/kagent/v202401/capabilities/{capability.name}`

Delete a capability

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.kagent
    participant API as Kentik REST API

    C->>W: delete_capability(capabilityname="capabilityname-example")
    W->>API: DELETE /kagent/v202401/capabilities/{capability.name}
    alt success
        API-->>W: DeleteCapabilityResponse (JSON)
        W-->>C: DeleteCapabilityResponse
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
    participant W as client.kagent
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: delete_capability(capabilityname="capabilityname-example")
    W->>R: build_grpc_request(DeleteCapabilityRequest, arguments)
    R->>API: CapabilityAdminService/DeleteCapability (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: parse_grpc_response(response)
        W-->>C: DeleteCapabilityResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

##### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `capabilityname` | path | `string` | Yes |

##### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `DeleteCapabilityResponse` |
| default | An unexpected error response. | `rpcStatus` |

##### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.kagent.delete_capability(
    capabilityname="capabilityname-example",
)
```

### CapabilityReleaseService

#### `GET` `/kagent/v202401/releases`

GetCapabilityRelease can be used by install/upgrade modules to fetch a single release.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.kagent
    participant API as Kentik REST API

    C->>W: get_capability_release()
    W->>API: GET /kagent/v202401/releases
    alt success
        API-->>W: GetCapabilityReleaseResponse (JSON)
        W-->>C: GetCapabilityReleaseResponse
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
    participant W as client.kagent
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: get_capability_release()
    W->>R: build_grpc_request(GetCapabilityReleaseRequest, arguments)
    R->>API: CapabilityReleaseService/GetCapabilityRelease (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: parse_grpc_response(response)
        W-->>C: GetCapabilityReleaseResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

##### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `os` | query | `string` | No |
| `arch` | query | `string` | No |
| `channel` | query | `string` | No |
| `capability` | query | `string` | No |
| `semver` | query | `string` | No |
| `distro` | query | `string` | No |

##### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `GetCapabilityReleaseResponse` |
| default | An unexpected error response. | `rpcStatus` |

##### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.kagent.get_capability_release()
```

---

#### `GET` `/kagent/v202401/releases/latest`

GetCapabilityLatestReleases can be used by install/upgrade modules to fetch the latest available releases.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.kagent
    participant API as Kentik REST API

    C->>W: get_capability_latest_releases()
    W->>API: GET /kagent/v202401/releases/latest
    alt success
        API-->>W: GetCapabilityLatestReleasesResponse (JSON)
        W-->>C: GetCapabilityLatestReleasesResponse
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
    participant W as client.kagent
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: get_capability_latest_releases()
    W->>R: build_grpc_request(GetCapabilityLatestReleasesRequest, arguments)
    R->>API: CapabilityReleaseService/GetCapabilityLatestReleases (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: parse_grpc_response(response)
        W-->>C: GetCapabilityLatestReleasesResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

##### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `os` | query | `string` | No |
| `arch` | query | `string` | No |
| `channel` | query | `string` | No |
| `installId` | query | `string` | No |
| `capabilities` | query | `string[]` | No |
| `distro` | query | `string` | No |

##### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `GetCapabilityLatestReleasesResponse` |
| default | An unexpected error response. | `rpcStatus` |

##### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.kagent.get_capability_latest_releases()
```

---

#### `GET` `/kagent/v202401/releases/supported_distros`

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.kagent
    participant API as Kentik REST API

    C->>W: get_capability_supported_distros()
    W->>API: GET /kagent/v202401/releases/supported_distros
    alt success
        API-->>W: GetCapabilitySupportedDistrosResponse (JSON)
        W-->>C: GetCapabilitySupportedDistrosResponse
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
    participant W as client.kagent
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: get_capability_supported_distros()
    W->>R: build_grpc_request(GetCapabilitySupportedDistrosRequest, arguments)
    R->>API: CapabilityReleaseService/GetCapabilitySupportedDistros (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: parse_grpc_response(response)
        W-->>C: GetCapabilitySupportedDistrosResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

##### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `capabilities` | query | `string[]` | No |

##### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `GetCapabilitySupportedDistrosResponse` |
| default | An unexpected error response. | `rpcStatus` |

##### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.kagent.get_capability_supported_distros()
```

### ConfigService

#### `POST` `/kagent/v202401/config`

Create a config.

Creates a new config based on the request and returns it.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.kagent
    participant API as Kentik REST API

    C->>W: create_config(data=Config(...))
    W->>API: POST /kagent/v202401/config
    alt success
        API-->>W: CreateConfigResponse (JSON)
        W-->>C: CreateConfigResponse
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
    participant W as client.kagent
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: create_config(data=Config(...))
    W->>R: build_grpc_request(CreateConfigRequest, arguments)
    R->>API: ConfigService/CreateConfig (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: parse_grpc_response(response)
        W-->>C: CreateConfigResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

##### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `data` | body | `Config` | Yes |

##### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `CreateConfigResponse` |
| default | An unexpected error response. | `rpcStatus` |

##### Example

```python
from kentik_api.client import KentikAPI
from kentik_api.gen.kagent.models import Config

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.kagent.create_config(
    data=Config(...),
)
```

---

#### `GET` `/kagent/v202401/config/{config.name}`

Get a config.

Returns the config with the specified name.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.kagent
    participant API as Kentik REST API

    C->>W: get_config(configname="configname-example")
    W->>API: GET /kagent/v202401/config/{config.name}
    alt success
        API-->>W: GetConfigResponse (JSON)
        W-->>C: GetConfigResponse
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
    participant W as client.kagent
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: get_config(configname="configname-example")
    W->>R: build_grpc_request(GetConfigRequest, arguments)
    R->>API: ConfigService/GetConfig (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: parse_grpc_response(response)
        W-->>C: GetConfigResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

##### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `configname` | path | `string` | Yes |

##### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `GetConfigResponse` |
| default | An unexpected error response. | `rpcStatus` |

##### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.kagent.get_config(
    configname="configname-example",
)
```

---

#### `PATCH` `/kagent/v202401/config/{config.name}`

Update a config.

Updates the attributes of a config selected by the field mask in the request.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.kagent
    participant API as Kentik REST API

    C->>W: update_config(configname="configname-example", data=ConfigServiceUpdateConfigBody(...))
    W->>API: PATCH /kagent/v202401/config/{config.name}
    alt success
        API-->>W: UpdateConfigResponse (JSON)
        W-->>C: UpdateConfigResponse
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
    participant W as client.kagent
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: update_config(configname="configname-example", data=ConfigServiceUpdateConfigBody(...))
    W->>R: build_grpc_request(UpdateConfigRequest, arguments)
    R->>API: ConfigService/UpdateConfig (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: parse_grpc_response(response)
        W-->>C: UpdateConfigResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

##### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `configname` | path | `string` | Yes |
| `data` | body | `ConfigServiceUpdateConfigBody` | Yes |

##### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `UpdateConfigResponse` |
| default | An unexpected error response. | `rpcStatus` |

##### Example

```python
from kentik_api.client import KentikAPI
from kentik_api.gen.kagent.models import ConfigServiceUpdateConfigBody

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.kagent.update_config(
    configname="configname-example",
    data=ConfigServiceUpdateConfigBody(...),
)
```

---

#### `DELETE` `/kagent/v202401/config/{config.name}`

Delete a config.

Deletes the config with the specified name.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.kagent
    participant API as Kentik REST API

    C->>W: delete_config(configname="configname-example")
    W->>API: DELETE /kagent/v202401/config/{config.name}
    alt success
        API-->>W: DeleteConfigResponse (JSON)
        W-->>C: DeleteConfigResponse
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
    participant W as client.kagent
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: delete_config(configname="configname-example")
    W->>R: build_grpc_request(DeleteConfigRequest, arguments)
    R->>API: ConfigService/DeleteConfig (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: parse_grpc_response(response)
        W-->>C: DeleteConfigResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

##### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `configname` | path | `string` | Yes |

##### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `DeleteConfigResponse` |
| default | An unexpected error response. | `rpcStatus` |

##### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.kagent.delete_config(
    configname="configname-example",
)
```

### ProvisioningTokenService

#### `GET` `/kagent/v202401/provisioning-tokens`

List provisioning tokens.

Returns a list of all provisioning tokens in the account.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.kagent
    participant API as Kentik REST API

    C->>W: list_provisioning_tokens()
    W->>API: GET /kagent/v202401/provisioning-tokens
    alt success
        API-->>W: ListProvisioningTokensResponse (JSON)
        W-->>C: ListProvisioningTokensResponse
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
    participant W as client.kagent
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: list_provisioning_tokens()
    W->>R: build_grpc_request(ListProvisioningTokensRequest, arguments)
    R->>API: ProvisioningTokenService/ListProvisioningTokens (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: parse_grpc_response(response)
        W-->>C: ListProvisioningTokensResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

##### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `ListProvisioningTokensResponse` |
| default | An unexpected error response. | `rpcStatus` |

##### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.kagent.list_provisioning_tokens()
```

---

#### `POST` `/kagent/v202401/provisioning-tokens`

Create a provisioning token.

Creates a new provisioning token based on configuration in the request and returns it, including its secret value.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.kagent
    participant API as Kentik REST API

    C->>W: create_provisioning_token(data=ProvisioningToken(...))
    W->>API: POST /kagent/v202401/provisioning-tokens
    alt success
        API-->>W: CreateProvisioningTokenResponse (JSON)
        W-->>C: CreateProvisioningTokenResponse
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
    participant W as client.kagent
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: create_provisioning_token(data=ProvisioningToken(...))
    W->>R: build_grpc_request(CreateProvisioningTokenRequest, arguments)
    R->>API: ProvisioningTokenService/CreateProvisioningToken (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: parse_grpc_response(response)
        W-->>C: CreateProvisioningTokenResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

##### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `data` | body | `ProvisioningToken` | Yes |

##### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `CreateProvisioningTokenResponse` |
| default | An unexpected error response. | `rpcStatus` |

##### Example

```python
from kentik_api.client import KentikAPI
from kentik_api.gen.kagent.models import ProvisioningToken

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.kagent.create_provisioning_token(
    data=ProvisioningToken(...),
)
```

---

#### `GET` `/kagent/v202401/provisioning-tokens/{token}`

Get provisioning token configuration and status.

Returns configuration, usage and revocation status of the provisioning token with the specified value.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.kagent
    participant API as Kentik REST API

    C->>W: get_provisioning_token(token="token-example")
    W->>API: GET /kagent/v202401/provisioning-tokens/{token}
    alt success
        API-->>W: GetProvisioningTokenResponse (JSON)
        W-->>C: GetProvisioningTokenResponse
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
    participant W as client.kagent
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: get_provisioning_token(token="token-example")
    W->>R: build_grpc_request(GetProvisioningTokenRequest, arguments)
    R->>API: ProvisioningTokenService/GetProvisioningToken (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: parse_grpc_response(response)
        W-->>C: GetProvisioningTokenResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

##### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `token` | path | `string` | Yes |

##### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `GetProvisioningTokenResponse` |
| default | An unexpected error response. | `rpcStatus` |

##### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.kagent.get_provisioning_token(
    token="token-example",
)
```

---

#### `GET` `/kagent/v202401/provisioning-tokens/{token}/agents`

List agents registered with a provisioning token.

Returns the IDs of all agents that have registered with the provisioning token with the specified value.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.kagent
    participant API as Kentik REST API

    C->>W: list_agents_by_provisioning_token(token="token-example")
    W->>API: GET /kagent/v202401/provisioning-tokens/{token}/agents
    alt success
        API-->>W: ListAgentsByProvisioningTokenResponse (JSON)
        W-->>C: ListAgentsByProvisioningTokenResponse
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
    participant W as client.kagent
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: list_agents_by_provisioning_token(token="token-example")
    W->>R: build_grpc_request(ListAgentsByProvisioningTokenRequest, arguments)
    R->>API: ProvisioningTokenService/ListAgentsByProvisioningToken (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: parse_grpc_response(response)
        W-->>C: ListAgentsByProvisioningTokenResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

##### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `token` | path | `string` | Yes |

##### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `ListAgentsByProvisioningTokenResponse` |
| default | An unexpected error response. | `rpcStatus` |

##### Example

```python
from kentik_api.client import KentikAPI

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.kagent.list_agents_by_provisioning_token(
    token="token-example",
)
```

---

#### `POST` `/kagent/v202401/provisioning-tokens/{token}/revoke`

Revoke a provisioning token.

Revokes the provisioning token with the specified value. Agents already registered with the token are not affected, but the token can no longer be used for new registrations.

**REST transport**

```mermaid
sequenceDiagram
    participant C as Caller
    participant W as client.kagent
    participant API as Kentik REST API

    C->>W: revoke_provisioning_token(token="token-example", data=ProvisioningTokenServiceRevokeProvisioningTokenBody(...))
    W->>API: POST /kagent/v202401/provisioning-tokens/{token}/revoke
    alt success
        API-->>W: RevokeProvisioningTokenResponse (JSON)
        W-->>C: RevokeProvisioningTokenResponse
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
    participant W as client.kagent
    participant R as grpc_runtime
    participant API as Kentik gRPC API

    C->>W: revoke_provisioning_token(token="token-example", data=ProvisioningTokenServiceRevokeProvisioningTokenBody(...))
    W->>R: build_grpc_request(RevokeProvisioningTokenRequest, arguments)
    R->>API: ProvisioningTokenService/RevokeProvisioningToken (gRPC/TLS)
    alt success
        API-->>R: response message
        R-->>W: parse_grpc_response(response)
        W-->>C: RevokeProvisioningTokenResponse
    else gRPC error, deadline, or unreachable
        R-->>W: map_grpc_error()
        W-->>C: raise AuthenticationError, HTTPException, or TransportError
    end
```

##### Parameters

| Name | In | Type | Required |
| --- | --- | --- | --- |
| `token` | path | `string` | Yes |
| `data` | body | `ProvisioningTokenServiceRevokeProvisioningTokenBody` | Yes |

##### Responses

| Status | Description | Model |
| --- | --- | --- |
| 200 | A successful response. | `RevokeProvisioningTokenResponse` |
| default | An unexpected error response. | `rpcStatus` |

##### Example

```python
from kentik_api.client import KentikAPI
from kentik_api.gen.kagent.models import ProvisioningTokenServiceRevokeProvisioningTokenBody

# Both transports work: protocol="rest" (default) or protocol="grpc".
client = KentikAPI(protocol="rest")  # loads KENTIK_EMAIL/KENTIK_API_TOKEN from .env
response = client.kagent.revoke_provisioning_token(
    token="token-example",
    data=ProvisioningTokenServiceRevokeProvisioningTokenBody(...),
)
```

## Data Models

<details>
<summary>Model relationships (30 of 60 models)</summary>

```mermaid
classDiagram
    class Agent
    class AgentCapability
    class AgentCapabilityServiceUpsertAgentCapabilityBody
    class AgentConfig
    class AgentRegistration
    class AgentServiceUpdateAgentBody
    class AuthorizeResponse
    class BootstrapInfo
    class Capability
    class CapabilityAdminServiceUpdateCapabilityBody
    class CapabilityRelease
    class CapabilitySupportedDistro
    class Config
    class ConfigLayer
    class ConfigServiceUpdateConfigBody
    class CreateAgentRequest
    class CreateAgentResponse
    class CreateCapabilityResponse
    class CreateConfigResponse
    class CreateProvisioningTokenResponse
    class DeleteAgentCapabilityResponse
    class DeleteAgentResponse
    class DeleteCapabilityResponse
    class DeleteConfigResponse
    class GenerateInstallCommandsRequest
    class GenerateInstallCommandsResponse
    class GetAgentCapabilityResponse
    class GetAgentResponse
    class GetCapabilityLatestReleasesResponse
    class GetCapabilityReleaseResponse
    Agent --> AgentConfig
    AgentServiceUpdateAgentBody --> AgentConfig
    Config --> ConfigLayer
    CreateAgentRequest --> AgentRegistration
    CreateAgentResponse --> Agent
    CreateAgentResponse --> BootstrapInfo
    CreateCapabilityResponse --> Capability
    CreateConfigResponse --> Config
    GenerateInstallCommandsResponse --> BootstrapInfo
    GetAgentCapabilityResponse --> AgentCapability
    GetAgentResponse --> Agent
    GetCapabilityLatestReleasesResponse --> CapabilityRelease
    GetCapabilityReleaseResponse --> CapabilityRelease
```

</details>

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.kagent.models.Agent
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.kagent.models.AgentCapability
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.kagent.models.AgentCapabilityServiceUpsertAgentCapabilityBody
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.kagent.models.AgentConfig
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.kagent.models.AgentRegistration
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.kagent.models.AgentServiceUpdateAgentBody
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.kagent.models.AuthorizeResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.kagent.models.BootstrapInfo
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.kagent.models.Capability
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.kagent.models.CapabilityAdminServiceUpdateCapabilityBody
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.kagent.models.CapabilityDistro
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.kagent.models.CapabilityRelease
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.kagent.models.CapabilitySupportedDistro
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.kagent.models.CompatibilityInfo
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.kagent.models.Config
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.kagent.models.ConfigLayer
```

```{eval-rst}
.. autoclass:: kentik_api.gen.kagent.models.ConfigLayerLayerType
   :members:
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.kagent.models.ConfigServiceUpdateConfigBody
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.kagent.models.CreateAgentRequest
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.kagent.models.CreateAgentResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.kagent.models.CreateCapabilityResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.kagent.models.CreateConfigResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.kagent.models.CreateProvisioningTokenResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.kagent.models.DeleteAgentCapabilityResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.kagent.models.DeleteAgentResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.kagent.models.DeleteCapabilityResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.kagent.models.DeleteConfigResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.kagent.models.GenerateInstallCommandsRequest
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.kagent.models.GenerateInstallCommandsResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.kagent.models.GetAgentCapabilityResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.kagent.models.GetAgentResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.kagent.models.GetCapabilityLatestReleasesResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.kagent.models.GetCapabilityReleaseResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.kagent.models.GetCapabilityResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.kagent.models.GetCapabilitySupportedDistrosResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.kagent.models.GetConfigResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.kagent.models.GetProvisioningTokenResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.kagent.models.HostMetadata
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.kagent.models.InstallConfig
```

```{eval-rst}
.. autoclass:: kentik_api.gen.kagent.models.InstallerType
   :members:
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.kagent.models.ListAgentCapabilitiesResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.kagent.models.ListAgentsByProvisioningTokenResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.kagent.models.ListAgentsResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.kagent.models.ListCapabilitiesResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.kagent.models.ListProvisioningTokensResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.kagent.models.ProvisioningToken
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.kagent.models.ProvisioningTokenAgentConfig
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.kagent.models.ProvisioningTokenServiceRevokeProvisioningTokenBody
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.kagent.models.RegistrationConfig
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.kagent.models.RevokeProvisioningTokenResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.kagent.models.RuntimeConfig
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.kagent.models.RuntimeConfigEnvVar
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.kagent.models.TelemetryConfig
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.kagent.models.TokenRevoked
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.kagent.models.UpdateAgentResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.kagent.models.UpdateCapabilityResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.kagent.models.UpdateConfigResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.kagent.models.UpsertAgentCapabilityResponse
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.kagent.models.protobufAny
```

```{eval-rst}
.. autopydantic_model:: kentik_api.gen.kagent.models.rpcStatus
```
