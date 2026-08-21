# HAND-WRITTEN: not modified by `make generate`. Edit directly.
"""Generated-code post-processing: import patching, model init rebuild, file cleanup.

Called once per service directory by generate_modular_sdk() after all swagger
files for the service have been generated, outside the schema availability window.
"""

import re
import textwrap
from pathlib import Path

from ._shared import discover_service_model_classes
from .error_package import inject_service_error_handling


def fix_generated_service(service_dir: Path) -> None:
    """Applies all post-processing fixups to a freshly generated service directory."""
    model_classes = discover_service_model_classes(service_dir)
    _rebuild_models_init(service_dir)
    _fix_wildcard_exports(service_dir)
    _patch_service_files(service_dir, model_classes)


# ---------------------------------------------------------------------------
# Private helpers
# ---------------------------------------------------------------------------


def _rebuild_models_init(service_dir: Path) -> None:
    """Rebuilds models/__init__.py from a full directory scan.

    openapi-python-generator overwrites models/__init__.py on each invocation,
    keeping only the last-processed swagger file's models. Rebuilding from a
    full scan keeps every class explicitly bound regardless of how many swagger
    files contributed to the service.
    """
    models_dir = service_dir / "models"
    if not models_dir.exists():
        return
    init_lines = []
    for model_file in sorted(models_dir.glob("*.py")):
        if model_file.name == "__init__.py":
            continue
        classes = re.findall(
            r"^class\s+([A-Za-z0-9_]+)",
            model_file.read_text(encoding="utf-8"),
            re.MULTILINE,
        )
        if not classes:
            continue
        exports = ", ".join(f"{c} as {c}" for c in classes)
        init_lines.append(f"from .{model_file.stem} import {exports}")
    (models_dir / "__init__.py").write_text(
        "\n".join(init_lines) + ("\n" if init_lines else ""),
        encoding="utf-8",
    )


def _fix_wildcard_exports(service_dir: Path) -> None:
    """Replaces `from .module import *` with explicit named imports in __init__.py files."""
    for init_file in service_dir.rglob("__init__.py"):
        if "error" in init_file.parts:
            continue
        content = init_file.read_text(encoding="utf-8")
        new_lines = []
        for line in content.splitlines():
            match = re.match(r"^from \.([a-zA-Z0-9_]+) import \*$", line)
            if match:
                module_name = match.group(1)
                target_py = init_file.parent / f"{module_name}.py"
                if target_py.exists():
                    target_content = target_py.read_text(encoding="utf-8")
                    classes = re.findall(
                        r"^class\s+([A-Za-z0-9_]+)",
                        target_content,
                        flags=re.MULTILINE,
                    )
                    if classes:
                        explicit_imports = ", ".join([f"{c} as {c}" for c in classes])
                        new_lines.append(
                            f"from .{module_name} import {explicit_imports}"
                        )
                        continue
            new_lines.append(line)
        init_file.write_text("\n".join(new_lines) + "\n", encoding="utf-8")


def _patch_service_files(service_dir: Path, model_classes: set[str]) -> None:
    """Applies all content patches to generated .py files in a service directory."""
    explicit_models_import = (
        f"from ..models import {', '.join(sorted(model_classes))}"
        if model_classes
        else ""
    )
    explicit_models_local = (
        f"from .models import {', '.join(sorted(model_classes))}"
        if model_classes
        else ""
    )

    for py_file in service_dir.rglob("*.py"):
        # Skip pb/ (gRPC stubs must not be corrupted) and error/ (already generated correctly)
        if "pb" in py_file.parts or "error" in py_file.parts:
            continue

        if py_file.name.startswith("async_") or py_file.name == "api_config.py":
            py_file.unlink()
            continue

        # De-duplicate filenames (DeviceService_service.py -> DeviceService.py)
        if "Service_service" in py_file.name or "_service" in py_file.name.lower():
            clean_name = (
                py_file.name.replace("Service_service", "Service")
                .replace("_service_service", "Service")
                .replace("_service", "Service")
            )
            clean_name = clean_name[:1].upper() + clean_name[1:]
            new_path = py_file.with_name(clean_name)
            py_file.rename(new_path)
            py_file = new_path

        content = py_file.read_text(encoding="utf-8")

        content = re.sub(
            r"from \.*api_config import APIConfig, HTTPException",
            "from kentik_api.core.api_config import APIConfig\nfrom kentik_api.errors import HTTPException",
            content,
        )
        content = re.sub(
            r"from \.*api_config import APIConfig as APIConfig",
            "from kentik_api.core.api_config import APIConfig",
            content,
        )
        content = re.sub(
            r"from \.*api_config import HTTPException as HTTPException",
            "from kentik_api.errors import HTTPException",
            content,
        )
        content = re.sub(
            r"return ([A-Za-z0-9_]+)\(\*\*body\) if body.*? else \1\(\)",
            r"return \1(**body) if body is not None else \1.model_construct()",
            content,
        )
        # Path parameter sanitization: {device.id} -> {deviceid}
        content = re.sub(
            r"path\s*=\s*f[\"'].*?[\"']",
            lambda m: re.sub(
                r"\{([a-zA-Z0-9_]+)\.([a-zA-Z0-9_]+)\}", r"{\1\2}", m.group(0)
            ),
            content,
        )
        content = re.sub(
            r'["\']Authorization["\']:\s*f["\']Bearer\s*\{[^}]+\}["\'],?',
            r'"X-CH-Auth-Email": api_config.auth_email,\n        "X-CH-Auth-API-Token": api_config.auth_token,',
            content,
        )

        if py_file.name == "api_config.py":
            content = content.replace(
                "access_token: Optional[str] = None",
                "auth_email: Optional[str] = None\n    auth_token: Optional[str] = None",
            )
            content = content.replace("def get_access_token", "def get_auth_token")
            content = content.replace("self.access_token", "self.auth_token")

        functions = re.split(r"^(?=async def |def )", content, flags=re.MULTILINE)
        fixed_funcs = []
        for func in functions:
            if not func.strip():
                fixed_funcs.append(func)
                continue
            sig_part = func.split("->")[0] if "->" in func else func.split(":\n")[0]
            has_data_param = "data:" in sig_part or "data :" in sig_part
            has_json_kwarg = "json=" in func
            has_json_body_kwarg = "json_body=" in func

            if has_data_param and not (has_json_kwarg or has_json_body_kwarg):
                if "request_json(" in func:
                    func = re.sub(
                        r"(query_params=query_params)(,?)(\s*)",
                        r"\1,\n                json_body=data.model_dump()\3",
                        func,
                        count=1,
                    )
                else:
                    func = re.sub(
                        r"(params=query_params)(,?)(\s*\))",
                        r"\1, json=data.model_dump()\3",
                        func,
                    )
            func = re.sub(r"\bdata\.dict\(\)", "data.model_dump()", func)
            if not has_data_param and has_json_kwarg:
                func = re.sub(r",\s*json=data\.model_dump\(\)", "", func)
                func = re.sub(r"json=data\.model_dump\(\)", "", func)
            if not has_data_param and has_json_body_kwarg:
                func = re.sub(r",\s*json_body\s*=\s*data\.model_dump\(\)", "", func)
                func = re.sub(r"json_body\s*=\s*data\.model_dump\(\)\s*,?", "", func)
            fixed_funcs.append(func)

        content = "".join(fixed_funcs)

        if py_file.parent.name in ("services", "service") and py_file.name not in (
            "__init__.py",
        ):
            content = inject_service_error_handling(content)

        content = _normalize_triple_quoted_docstrings(content)

        if "from typing import *" in content:
            content = content.replace(
                "from typing import *",
                "from typing import Any, Callable, Dict, Generic, List, Optional, Set, Tuple, Type, TypeVar, Union",
            )
        # Some services expose an operation named `List`, clashing with typing.List (F811).
        if re.search(r"^def\s+List\s*\(", content, flags=re.MULTILINE):
            content = re.sub(
                r"from typing import ([^\n]*)\bList\b([^\n]*)",
                lambda m: f"from typing import {m.group(1)}List as TypingList{m.group(2)}",
                content,
                count=1,
            )
            content = re.sub(r"\bList\[", "TypingList[", content)

        if explicit_models_import:
            content = content.replace(
                "from ..models import *", explicit_models_import + "  # noqa: F401"
            )
            content = content.replace(
                "from .models import *", explicit_models_local + "  # noqa: F401"
            )

        content = _dedupe_top_level_function_names(content)
        py_file.write_text(content, encoding="utf-8")


def _dedupe_top_level_function_names(content: str) -> str:
    """Renames duplicate top-level def names to avoid F811 collisions."""
    func_name_pattern = re.compile(
        r"^def\s+([A-Za-z_][A-Za-z0-9_]*)\s*\(", re.MULTILINE
    )
    seen: dict[str, int] = {}
    out: list[str] = []
    cursor = 0
    for match in func_name_pattern.finditer(content):
        func_name = match.group(1)
        seen[func_name] = seen.get(func_name, 0) + 1
        if seen[func_name] == 1:
            continue
        new_name = f"{func_name}_{seen[func_name]}"
        out.append(content[cursor : match.start(1)])
        out.append(new_name)
        cursor = match.end(1)
    if not out:
        return content
    out.append(content[cursor:])
    return "".join(out)


def _normalize_triple_quoted_docstrings(content: str) -> str:
    """Normalizes indentation of triple-quoted docstrings for docutils/Sphinx."""
    pattern = re.compile(r"(^[ \t]*)(\"\"\"|''')([\s\S]*?)(\2)", re.MULTILINE)

    def _rewrite(match: re.Match[str]) -> str:
        indent = match.group(1)
        quote = match.group(2)
        body = match.group(3)
        if "\n" not in body:
            return match.group(0)
        dedented = textwrap.dedent(body).replace("\r\n", "\n").strip("\n")
        if not dedented:
            return f"{indent}{quote}{quote}"
        lines = dedented.split("\n")
        inner_indent = indent + ("    " if indent else "")
        formatted_lines = [
            (f"{inner_indent}{line.strip()}" if line.strip() else "") for line in lines
        ]
        return f"{indent}{quote}\n" + "\n".join(formatted_lines) + f"\n{indent}{quote}"

    return pattern.sub(_rewrite, content)
