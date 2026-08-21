# Architecture Refactoring Spec

> **TEMPORARY — delete this file before merging to `kentik/community_sdk_python:main`.**

Three independent refactors, in implementation order. Each deepens a shallow
module by establishing a real seam. None depends on the others; they can be
implemented in separate commits.

---

## Refactor 1 — Extract `fixup` Phase Module

**Strength:** Strong  
**Files touched:** `scripts/generate_sdk.py`, `scripts/generation/fixup.py` (new),
`tests/generator/test_fixup.py` (new)

### Problem

`generate_modular_sdk()` in `scripts/generate_sdk.py` embeds ~250 lines of
generated-code post-processing inline — no seam, no name, no tests. Every time
a new service quirk surfaces (broken import alias, wrong docstring indent, duplicate
function name), the change lands inside a 500-line orchestration function. The
post-processing logic has no **locality**: it cannot be read, changed, or tested
apart from a full schema-download run.

The **deletion test** passes: removing the block from `generate_modular_sdk()` and
concentrating it in a new `fixup` phase module reduces the orchestrator and gives
the fixup logic a testable **interface**.

### What to build

Create `scripts/generation/fixup.py` with one public entrypoint:

```python
def fix_generated_service(service_dir: Path) -> None:
    """Applies all post-processing fixups to a freshly generated service directory."""
    _rebuild_models_init(service_dir)
    _fix_wildcard_exports(service_dir)
    _patch_service_files(service_dir)
```

Move the following logic out of `generate_modular_sdk()` and into `fixup.py`:

| Existing logic | New private function |
| --- | --- |
| Rebuild `models/__init__.py` from directory scan | `_rebuild_models_init(service_dir)` |
| Fix `from .module import *` in `__init__.py` files | `_fix_wildcard_exports(service_dir)` |
| All per-file content patches (import aliases, auth headers, path params, docstrings, typing imports, model imports, deduplication, error injection) | `_patch_service_files(service_dir)` |

The three standalone functions already in `generate_sdk.py` move into `fixup.py` as
module-level helpers (not public):

- `dedupe_top_level_function_names(content)`
- `normalize_triple_quoted_docstrings(content)`
- `patch_schema_for_clean_names(swagger_path, version)` — this one stays in
  `generate_sdk.py` because it runs *before* the schema availability window closes;
  the others run after.

Update `generate_modular_sdk()` orchestration loop:

```python
# Before (~250 lines):
for service_dir in SDK_OUTPUT_DIR.iterdir():
    if not service_dir.is_dir() or service_dir.name == "__pycache__":
        continue
    model_classes = discover_service_model_classes(service_dir)
    explicit_models_import = ...
    # ... 240 more lines ...

# After (3 lines):
from generation import fixup

for service_dir in SDK_OUTPUT_DIR.iterdir():
    if service_dir.is_dir() and service_dir.name != "__pycache__":
        fixup.fix_generated_service(service_dir)
```

Also expose in `scripts/generation/__init__.py`:

```python
from . import fixup
```

### Tests to write (`tests/generator/test_fixup.py`)

Each test creates a minimal scratch directory (`tmp_path`) with Python files that
look like generator output — no schema download required.

| Test | Input | Expected output |
| --- | --- | --- |
| `test_rebuild_models_init` | `models/` dir with two model files each defining a class | `models/__init__.py` exports both classes explicitly |
| `test_fix_wildcard_exports` | `__init__.py` with `from .foo import *` next to `foo.py` defining `class Bar` | `__init__.py` replaced with `from .foo import Bar as Bar` |
| `test_patch_auth_header` | Service file with `"Authorization": f"Bearer {token}"` | Replaced with Kentik auth headers |
| `test_patch_import_alias` | File with `from ..api_config import APIConfig, HTTPException` | Patched to correct import paths |
| `test_dedupe_function_names` | File with two `def List(...)` definitions | Second renamed to `List_2` |
| `test_normalize_docstrings` | File with inconsistently indented triple-quoted docstring | Normalized indentation |
| `test_model_wildcard_import` | Service file with `from ..models import *` | Replaced with explicit named imports |

### Documentation

| File | Change |
| --- | --- |
| `scripts/generation/README.md` | Add `fixup.py` row to the **Modules** table: owns "Generated-code post-processing (import patching, model init rebuild, docstring normalization)" with public interface `fix_generated_service()`. Update the call-order diagram to include `fixup` after the per-swagger loop and before wrapper/docs generation. |
| `CLAUDE.md` and `AGENTS.md` | In the "The generator's phase modules" section, add a `fixup.py` bullet describing `fix_generated_service()` and its three private helpers. Note that `generate_modular_sdk()` no longer contains inline post-processing. |
| `scripts/README.md` | Update any description of `generate_modular_sdk()` that mentions the inline post-processing loop to reference the `fixup` phase module instead. |
| `tests/generator/README.md` | Add `test_fixup.py` row to the files table describing what it covers. |

---

## Refactor 2 — Loud Failure in `inject_service_error_handling()`

**Strength:** Worth exploring  
**Files touched:** `scripts/generation/error_package.py`,
`tests/generator/test_error_package.py`

### Problem

`inject_service_error_handling(content: str) -> str` injects error class imports
by searching for the literal string:

```python
"from kentik_api.core.rest_runtime import request_json\n"
```

If that line is ever renamed or reformatted, the function returns the content
unchanged — no error raised, no indication of failure, nothing injected. The
bug surfaces later as a `NameError` at runtime when the error class name is used.
CLAUDE.md explicitly flags this as "a fragile coupling worth knowing about."

The **interface** (`str → str`) hides this precondition. The module is **shallow**
because the interesting invariant (the anchor must be present) lives outside the
interface.

### What to build

**Option A (minimal, recommended):** Return a sentinel and assert in tests.

```python
def inject_service_error_handling(content: str) -> str:
    ...
    if "from kentik_api.core.rest_runtime import request_json\n" not in content:
        # Loudly fail so the anchor string mismatch is caught at generation time,
        # not at runtime when an error class is used.
        if operation_ids:  # only required when there are operations to inject
            raise ValueError(
                "inject_service_error_handling: expected runtime import anchor "
                "'from kentik_api.core.rest_runtime import request_json' not found. "
                "If rest_runtime was moved or renamed, update this anchor."
            )
        return content
    ...
```

**Option B (deeper, if the anchor changes again later):** Accept parsed imports
instead of raw content — `inject_error_imports(imports: list[str], operations: list[str]) -> list[str]` —
so the seam sits at a structural boundary (import lines) instead of a positional
string match. Requires more refactoring in the callers.

Recommend Option A now; document Option B as the follow-up if the anchor breaks
again.

### Tests to write (add to `tests/generator/test_error_package.py`)

| Test | Input | Expected |
| --- | --- | --- |
| `test_inject_raises_when_anchor_missing` | File content with `operation_name="Foo"` but no runtime import line | `ValueError` raised |
| `test_inject_silent_when_no_operations` | File content with no `operation_name=` references and no anchor | Returns unchanged (no error) |
| `test_inject_succeeds_with_anchor_present` | File with correct runtime import line and one operation | Error class import injected correctly |

### Documentation

| File | Change |
| --- | --- |
| `CLAUDE.md` and `AGENTS.md` | Replace the "A fragile coupling worth knowing about" note with an updated note: the coupling is now **guarded** — `inject_service_error_handling()` raises `ValueError` if the anchor is absent and there are operations to inject. Keep the explanation of what the anchor is and why it must stay in sync with any rename of `request_json`. |
| `tests/generator/README.md` | Add `test_error_package.py` row update: note the three new tests covering the `ValueError` guard. |

---

## Refactor 3 — Testable Error Mapping in `call_grpc()`

**Strength:** Worth exploring  
**Files touched:** `src/kentik_api/core/grpc_runtime.py`,
`tests/runtime/test_grpc_runtime.py` (new)

### Problem

`call_grpc(stub_method, proto_request)` fuses the gRPC invocation with an 8-entry
`grpc.StatusCode → HTTP status` mapping table. There is no **seam** between them:
testing the mapping requires either a live gRPC channel or a complex stub mock.
A recent commit had to fix `exc.details() or ""` — a bug entirely in the mapping
path — but the mapping path was only reachable through a full gRPC call.

The module has low **depth**: the mapping table is the interesting behaviour, but
it's invisible through the interface. **Locality** is poor: a bug in the mapping
table is found by a test that also exercises the invocation.

### What to build

Extract a pure function for error mapping:

```python
def map_grpc_error(
    exc: grpc.RpcError,
    *,
    method: str = "gRPC",
    path: str = "unknown",
) -> HTTPException:
    """Maps a gRPC RpcError to the SDK exception hierarchy.

    Pure function — no I/O, no side effects. Testable without a gRPC channel.
    """
    code = exc.code()
    details = exc.details() or ""

    if code == grpc.StatusCode.UNAUTHENTICATED:
        return AuthenticationError(details)

    http_status = _GRPC_STATUS_TO_HTTP.get(code, 500)
    return HTTPException(
        status_code=http_status,
        message=details,
        method=method,
        path=path,
    )
```

Reduce `call_grpc()` to a thin caller:

```python
def call_grpc(stub_method, proto_request):
    """Calls one unary gRPC method and normalizes errors to the SDK exception hierarchy."""
    try:
        return stub_method(proto_request)
    except grpc.RpcError as exc:
        raise map_grpc_error(
            exc,
            method="gRPC",
            path=getattr(stub_method, "_method", b"unknown").decode("utf-8", errors="replace"),
        ) from exc
    except Exception as exc:
        raise TransportError(str(exc)) from exc
```

### Tests to write (`tests/runtime/test_grpc_runtime.py`)

Use a minimal `FakeRpcError` that satisfies `grpc.RpcError`:

```python
class FakeRpcError(grpc.RpcError):
    def __init__(self, code, details=None):
        self._code = code
        self._details = details
    def code(self): return self._code
    def details(self): return self._details
```

| Test | Status code | `details()` | Expected exception |
| --- | --- | --- | --- |
| `test_unauthenticated_raises_auth_error` | `UNAUTHENTICATED` | `"bad token"` | `AuthenticationError("bad token")` |
| `test_not_found_maps_to_404` | `NOT_FOUND` | `"missing"` | `HTTPException(404, "missing")` |
| `test_details_none_guard` | `NOT_FOUND` | `None` | `HTTPException(404, "")` — no `TypeError` |
| `test_unknown_status_maps_to_500` | `CANCELLED` (not in map) | `"cancelled"` | `HTTPException(500, "cancelled")` |
| `test_permission_denied_maps_to_403` | `PERMISSION_DENIED` | `"no"` | `HTTPException(403, "no")` |
| `test_resource_exhausted_maps_to_429` | `RESOURCE_EXHAUSTED` | `"rate"` | `HTTPException(429, "rate")` |

### Documentation

| File | Change |
| --- | --- |
| `src/kentik_api/core/README.md` | Add `map_grpc_error()` alongside `request_json()` in the shared-runtime description. Note it is a pure function: no I/O, no side effects, testable without a gRPC channel. |
| `CLAUDE.md` and `AGENTS.md` | In the shared-runtime section, add `map_grpc_error()` to the bullet describing `grpc_runtime.py`. Update the note that previously described the gRPC stub as untestable. |
| `docs/guides/grpc.md` | Add a brief note in the error-handling section explaining that status-code mapping is isolated in `map_grpc_error()` and can be tested independently. |
| `tests/runtime/README.md` | Add `test_grpc_runtime.py` row to the files table with a description of what it covers. |

---

## Implementation order

```text
Refactor 1 (fixup phase module)
    ↓  independent, no shared files
Refactor 2 (loud injection failure)
    ↓  independent, no shared files
Refactor 3 (gRPC error mapping)
```

All three are independent. Suggested commit messages:

```text
refactor: extract fixup phase module from generate_modular_sdk()
docs: add fixup.py to scripts/generation/README.md and CLAUDE.md

refactor: raise loudly when error injection anchor is missing
docs: update CLAUDE.md fragile-coupling note to reflect guarded anchor

refactor: extract map_grpc_error() pure function; add grpc_runtime tests
docs: document map_grpc_error() in core/README.md, CLAUDE.md, grpc.md
```
