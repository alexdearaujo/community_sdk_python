---
html_theme.sidebar_secondary.remove: true
---

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
%%{init: {"theme": "base", "fontFamily": "ui-monospace, SFMono-Regular, Menlo, monospace", "themeVariables": {"fontFamily": "ui-monospace, SFMono-Regular, Menlo, monospace", "primaryColor": "#f8f9fa", "primaryBorderColor": "#495057", "primaryTextColor": "#212529", "textColor": "#212529", "lineColor": "#77818c", "edgeLabelBackground": "#ffffff", "actorBkg": "#f8f9fa", "actorBorder": "#495057", "actorTextColor": "#212529", "actorLineColor": "#a9b3be", "signalColor": "#57616d", "signalTextColor": "#212529", "labelBoxBkgColor": "#f8f9fa", "labelBoxBorderColor": "#495057", "labelTextColor": "#212529", "loopTextColor": "#57616d", "noteBkgColor": "#fff9db", "noteBorderColor": "#f08c00", "noteTextColor": "#a35a00"}, "flowchart": {"curve": "step", "nodeSpacing": 30, "rankSpacing": 70, "wrappingWidth": 400}}}%%
sequenceDiagram
    participant C as Your code
    participant W as Service wrapper<br/>(37 services, 240 operations)
    box rgb(231,245,255) REST transport
    participant R as REST function<br/>gen/{service}/services/
    participant RJ as request_json()
    participant RA as Kentik REST API
    end
    box rgb(243,240,255) gRPC transport
    participant CG as call_grpc()
    participant GA as Kentik gRPC API
    end

    C->>W: client.{service}.{method}(arguments)
    alt REST transport
        W->>R: arguments
        R->>RJ: method, path, body, APIConfig
        RJ->>RA: HTTPS request with auth headers
        RA-->>RJ: JSON response
        RJ-->>R: JSON dict + quota
        R-->>W: Pydantic model
    else gRPC transport
        W->>CG: stub method + proto request
        CG->>GA: gRPC call over TLS
        GA-->>CG: proto response
        CG-->>W: proto response + quota
        W->>W: parse_grpc_response()
    end
    W-->>C: Pydantic model
    Note over C,GA: On a failure, request_json() or call_grpc() raises a KentikError subclass.
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

## Module Dependencies

The SDK splits into the parts below. Select one to see what it imports and what
imports it. The generator reads the imports from the source on every run.

```{raw} html
<div class="kx">
<div class="chips" role="group" aria-label="Show one path" data-paths-for="deps-svg"></div>
<figure>
<div class="diagram explorer"><svg id="deps-svg" viewBox="0 0 960 690" role="img" aria-label="Module dependencies: the shared foundation feeds the runtimes and the transports. They, the models and the proto stubs feed the service wrappers, which KentikAPI mounts." xmlns="http://www.w3.org/2000/svg"><defs><marker id="deps-ah" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" class="ah"/></marker><marker id="deps-ah-hi" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" class="ah-hi"/></marker></defs><g class="edge data" data-seg="base_rj" data-links="base>rj"><path d="M330,66 H140 V170" class="wire arrow" marker-end="url(#deps-ah)"/><text x="235" y="58" class="elabel" text-anchor="middle">APIConfig, auth</text></g><g class="edge data" data-seg="base_cg" data-links="base>cg"><path d="M430,102 V170" class="wire arrow" marker-end="url(#deps-ah)"/><text x="438" y="140" class="elabel" text-anchor="start">APIConfig</text></g><g class="edge data" data-seg="base_tr" data-links="base>tr"><path d="M530,66 H720 V170" class="wire arrow" marker-end="url(#deps-ah)"/><text x="625" y="58" class="elabel" text-anchor="middle">APIConfig, auth</text></g><g class="edge data" data-seg="rj_cg" data-links="rj>cg"><path d="M240,206 H330" class="wire arrow" marker-end="url(#deps-ah)"/><text x="276" y="198" class="elabel" text-anchor="middle">parsing</text></g><g class="edge data" data-seg="rj_rest" data-links="rj>rest"><path d="M140,242 V310" class="wire arrow" marker-end="url(#deps-ah)"/><text x="132" y="280" class="elabel" text-anchor="end">request_json()</text></g><g class="edge data" data-seg="cg_wrap" data-links="cg>wrap"><path d="M530,226 H575 V420 H490 V450" class="wire arrow" marker-end="url(#deps-ah)"/><text x="567" y="290" class="elabel" text-anchor="end">call_grpc()</text></g><g class="edge data" data-seg="models_rest" data-links="models>rest"><path d="M330,346 H240" class="wire arrow" marker-end="url(#deps-ah)"/><text x="294" y="338" class="elabel" text-anchor="middle">models</text></g><g class="edge data" data-seg="models_wrap" data-links="models>wrap"><path d="M430,382 V450" class="wire arrow" marker-end="url(#deps-ah)"/><text x="438" y="420" class="elabel" text-anchor="start">models</text></g><g class="edge data" data-seg="rest_wrap" data-links="rest>wrap"><path d="M140,382 V486 H330" class="wire arrow" marker-end="url(#deps-ah)"/><text x="148" y="440" class="elabel" text-anchor="start">operations</text></g><g class="edge data" data-seg="pb_wrap" data-links="pb>wrap"><path d="M720,382 V470 H530" class="wire arrow" marker-end="url(#deps-ah)"/><text x="728" y="430" class="elabel" text-anchor="start">proto stubs</text></g><g class="edge data" data-seg="tr_stem" data-links="tr>wrap,tr>client"><path d="M820,206 H860 V500" class="wire"/><text x="868" y="350" class="elabel" text-anchor="start">transport</text></g><g class="edge data" data-seg="tr_wrap" data-links="tr>wrap"><path d="M860,500 H530" class="wire arrow" marker-end="url(#deps-ah)"/></g><g class="edge data" data-seg="tr_client" data-links="tr>client"><path d="M860,500 V626 H530" class="wire arrow" marker-end="url(#deps-ah)"/></g><g class="edge data" data-seg="wrap_client" data-links="wrap>client"><path d="M430,522 V590" class="wire arrow" marker-end="url(#deps-ah)"/><text x="438" y="560" class="elabel" text-anchor="start">wrappers</text></g><g class="node fam-neutral hub " data-id="base" tabindex="0" role="button" aria-label="Select Shared foundation"><rect x="330" y="30" width="200" height="72" rx="14"/><text x="430.0" y="54.0" class="nm">Shared foundation</text><text x="430.0" y="71.0" class="ft">APIConfig, auth,</text><text x="430.0" y="88.0" class="ft">KentikError, RateLimit</text></g><g class="node fam-neutral hub " data-id="rj" tabindex="0" role="button" aria-label="Select request_json()"><rect x="40" y="170" width="200" height="72" rx="14"/><text x="140.0" y="194.0" class="nm">request_json()</text><text x="140.0" y="211.0" class="ft">core/rest_runtime.py</text><text x="140.0" y="228.0" class="ft">all REST traffic</text></g><g class="node fam-neutral hub " data-id="cg" tabindex="0" role="button" aria-label="Select call_grpc()"><rect x="330" y="170" width="200" height="72" rx="14"/><text x="430.0" y="194.0" class="nm">call_grpc()</text><text x="430.0" y="211.0" class="ft">core/grpc_runtime.py</text><text x="430.0" y="228.0" class="ft">all gRPC traffic</text></g><g class="node fam-violet proc " data-id="tr" tabindex="0" role="button" aria-label="Select Transports"><rect x="620" y="170" width="200" height="72" rx="14"/><text x="720.0" y="194.0" class="nm">Transports</text><text x="720.0" y="211.0" class="ft">transports/</text><text x="720.0" y="228.0" class="ft">REST and gRPC</text></g><g class="node fam-green proc " data-id="rest" tabindex="0" role="button" aria-label="Select REST functions and error classes"><rect x="40" y="310" width="200" height="72" rx="14"/><text x="140.0" y="334.0" class="nm">REST functions</text><text x="140.0" y="351.0" class="ft">gen/{service}/services/</text><text x="140.0" y="368.0" class="ft">+ error classes</text></g><g class="node fam-green src " data-id="models" tabindex="0" role="button" aria-label="Select Models"><rect x="330" y="310" width="200" height="72" rx="14"/><text x="430.0" y="334.0" class="nm">Models</text><text x="430.0" y="351.0" class="ft">gen/{service}/models/</text><text x="430.0" y="368.0" class="ft">Pydantic v2</text></g><g class="node fam-green src " data-id="pb" tabindex="0" role="button" aria-label="Select Proto stubs"><rect x="620" y="310" width="200" height="72" rx="14"/><text x="720.0" y="334.0" class="nm">Proto stubs</text><text x="720.0" y="351.0" class="ft">gen/{service}/pb/</text><text x="720.0" y="368.0" class="ft">protoc output</text></g><g class="node fam-green proc " data-id="wrap" tabindex="0" role="button" aria-label="Select Service wrappers"><rect x="330" y="450" width="200" height="72" rx="14"/><text x="430.0" y="474.0" class="nm">Service wrappers</text><text x="430.0" y="491.0" class="ft">client.{service}</text><text x="430.0" y="508.0" class="ft">one per service</text></g><g class="node fam-orange proc " data-id="client" tabindex="0" role="button" aria-label="Select KentikAPI client"><rect x="330" y="590" width="200" height="72" rx="14"/><text x="430.0" y="614.0" class="nm">KentikAPI</text><text x="430.0" y="631.0" class="ft">client.py</text><text x="430.0" y="648.0" class="ft">client_mixin.py</text></g></svg></div>
<figcaption>Select a part. Bold lines show what it needs. Moving lines show where it is used. Each arrow points from a module to a module that imports it. Every part also imports the shared foundation, but the diagram draws that only for the runtimes and the transports.</figcaption>
</figure>
<div class="legend" aria-hidden="true"><span><svg viewBox="0 0 34 10"><line x1="2" y1="5" x2="32" y2="5" stroke="var(--wire-hi)" stroke-linecap="round" stroke-width="3"/></svg>what the selected part needs</span><span><svg viewBox="0 0 34 10"><line x1="2" y1="5" x2="32" y2="5" stroke="var(--wire-hi)" stroke-linecap="round" stroke-width="3" stroke-dasharray="9 7"/></svg>where its data goes</span></div>
<div class="detail" data-detail-for="deps-svg" aria-live="polite"></div>
<script type="application/json" id="diagram-data">{"deps-svg": {"select": "wrap", "parts": {"base": {"title": "Shared foundation", "role": "APIConfig, the auth headers, the KentikError hierarchy and RateLimit. Every other part imports it.", "facts": ["Source: core/api_config.py, auth/, errors/, core/rate_limit.py", "Imported by call_grpc() (3), KentikAPI client (3), REST functions and error classes (97), request_json() (4), Transports (6), Service wrappers (37)"], "stops": "Expected: nothing in the SDK imports, so every call fails."}, "rj": {"title": "request_json()", "role": "The one function that sends REST traffic: auth headers, quota, and errors.", "facts": ["Source: core/rest_runtime.py", "Imports Shared foundation (4)", "Imported by call_grpc() (1), REST functions and error classes (54)"], "stops": "Expected: every REST call fails. gRPC calls fail too, because they parse responses with it."}, "cg": {"title": "call_grpc()", "role": "The one function that sends gRPC traffic: deadline, quota, and errors.", "facts": ["Source: core/grpc_runtime.py", "Imports Shared foundation (3), request_json() (1)", "Imported by Service wrappers (36)"], "stops": "Expected: every gRPC call fails. REST calls keep working."}, "tr": {"title": "Transports", "role": "RestTransport holds the APIConfig. GrpcTransport holds the TLS channel and the default deadline.", "facts": ["Source: transports/base.py, transports/rest_client.py, transports/grpc_client.py", "Imports Shared foundation (6)", "Imported by KentikAPI client (4), Service wrappers (74)"], "stops": "Expected: the client cannot be built, on either transport."}, "rest": {"title": "REST functions and error classes", "role": "One function per operation. Each one calls request_json() with its own error class.", "facts": ["Source: gen/{service}/services/, gen/{service}/error/", "Imports Shared foundation (97), Models (95), request_json() (54)", "Imported by KentikAPI client (37), Service wrappers (54)"], "stops": "Expected: REST calls fail for that service. gRPC calls through the same wrapper keep working."}, "models": {"title": "Models", "role": "The request and response models of every operation. They import nothing else in the SDK.", "facts": ["Source: gen/{service}/models/", "Imported by REST functions and error classes (95), Service wrappers (37)"], "stops": "Expected: the REST functions and the wrappers of that service do not import, so it does not mount."}, "pb": {"title": "Proto stubs", "role": "The modules that protoc compiles. Wrappers call them on a gRPC transport.", "facts": ["Source: gen/{service}/pb/", "Imported by Service wrappers (104)"], "stops": "Expected: gRPC calls for that service raise NotImplementedError. REST calls keep working."}, "wrap": {"title": "Service wrappers", "role": "Send each call to the REST function or to call_grpc(), for the transport in use.", "facts": ["Source: gen/{service}/services/{service}.py", "Imports Shared foundation (37), call_grpc() (36), Models (37), Proto stubs (104), REST functions and error classes (54), Transports (74)", "Imported by KentikAPI client (37)"], "stops": "Expected: the client does not mount that service, on either transport."}, "client": {"title": "KentikAPI client", "role": "Reads the credentials, picks the transport, and mounts every wrapper.", "facts": ["Source: client.py, client_mixin.py", "Imports Shared foundation (3), REST functions and error classes (37), Transports (4), Service wrappers (37)"], "stops": "Expected: nothing in the SDK can be called."}}, "links": {"base>cg": "3 import statements", "base>rj": "4 import statements", "base>tr": "6 import statements", "cg>wrap": "36 import statements", "models>rest": "95 import statements", "models>wrap": "37 import statements", "pb>wrap": "104 import statements", "rest>wrap": "54 import statements", "rj>cg": "1 import statements", "rj>rest": "54 import statements", "tr>client": "4 import statements", "tr>wrap": "74 import statements", "wrap>client": "37 import statements"}, "paths": {"rest": {"label": "REST call", "family": "blue", "title": "A call on a REST transport", "text": "The wrapper calls the REST function. It builds the request with the models and sends it with request_json().", "links": ["base>rj", "rj>rest", "models>rest", "rest>wrap", "wrap>client"]}, "grpc": {"label": "gRPC call", "family": "violet", "title": "A call on a gRPC transport", "text": "The wrapper builds the proto request with the stubs and sends it with call_grpc(), which parses the answer into the REST models.", "links": ["base>cg", "rj>cg", "cg>wrap", "pb>wrap", "models>wrap", "wrap>client"]}, "setup": {"label": "Client setup", "family": "orange", "title": "Building the client", "text": "KentikAPI builds one transport from the APIConfig and gives it to every wrapper that it mounts.", "links": ["base>tr", "tr>client", "tr>wrap", "wrap>client"]}}}}</script>
</div>
```

The table lists each module group, and the groups that it imports, with the
number of import statements.

| Group | Layer | Source | Imports from | Role |
| --- | --- | --- | --- | --- |
| Client API | Client Layer | `client.py` | API Config (1), Auth Credentials (1), Client Mixin (1), Error Types (1), REST Transport (1), gRPC Transport (1) | `KentikAPI`: reads the credentials and selects the transport. |
| Client Mixin | Client Layer | `client_mixin.py` | Generated REST Services (37), Generated Service Wrappers (37), REST Transport (1), gRPC Transport (1) | Mounts each service wrapper as `client.<service>`. |
| Auth Credentials | Shared Foundation | `auth/` | nothing in the SDK | Builds the Kentik auth headers for REST and for gRPC. |
| API Config | Shared Foundation | `core/api_config.py` | Error Types (1), Rate Limit (1) | `APIConfig`: base URL, credentials, TLS, timeouts, and the shared HTTP client. |
| REST Runtime | Shared Foundation | `core/rest_runtime.py` | API Config (1), Auth Credentials (1), Error Types (1), Rate Limit (1) | `request_json()`: the one function that sends REST traffic. |
| gRPC Runtime | Shared Foundation | `core/grpc_runtime.py` | API Config (1), Error Types (1), REST Runtime (1), Rate Limit (1) | `call_grpc()`: the one function that sends gRPC traffic. |
| Rate Limit | Shared Foundation | `core/rate_limit.py` | nothing in the SDK | `RateLimit`: the quota that each response reports. |
| Error Types | Shared Foundation | `errors/` | nothing in the SDK | The shared exception hierarchy under `KentikError`. |
| Transport Base | Transport Layer | `transports/base.py` | nothing in the SDK | The base class of both transports. |
| REST Transport | Transport Layer | `transports/rest_client.py` | API Config (1), Rate Limit (1), Transport Base (1) | `RestTransport`: holds the `APIConfig` for REST calls. |
| gRPC Transport | Transport Layer | `transports/grpc_client.py` | API Config (1), Auth Credentials (1), Error Types (1), Rate Limit (1), Transport Base (1) | `GrpcTransport`: the TLS channel, with auth and the default deadline. |
| Generated Service Wrappers | Generated Layer | `gen/{service}/services/{service}.py` | API Config (37), Generated Models (37), Generated Proto Stubs (104), Generated REST Services (54), REST Transport (37), gRPC Runtime (36), gRPC Transport (37) | Send each call to the REST function or to the gRPC stub, for the transport in use. |
| Generated REST Services | Generated Layer | `gen/{service}/services/` | API Config (54), Generated Error Classes (54), Generated Models (54), REST Runtime (54) | One function per operation in the OpenAPI schema. Each function calls `request_json()`. |
| Generated Models | Generated Layer | `gen/{service}/models/` | nothing in the SDK | Pydantic request and response models. |
| Generated Error Classes | Generated Layer | `gen/{service}/error/` | Error Types (43), Generated Models (41) | One error class per operation, picked by the response status. |
| Generated Proto Stubs | Generated Layer | `gen/{service}/pb/` | nothing in the SDK | The modules that protoc compiles. Wrappers call them on a gRPC transport. |

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
