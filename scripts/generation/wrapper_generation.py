"""Client mixin and dual-transport service wrapper generation."""

import re

from ._shared import (
    PROJECT_ROOT,
    SDK_OUTPUT_DIR,
    discover_service_model_classes,
    service_to_pascal_case,
)


def qualify_wrapper_annotation_types(text: str, model_classes: set[str]) -> str:
    """Qualifies model type names with rest_models in wrapper annotations."""
    if not model_classes:
        return text

    qualified = text
    for model_name in sorted(model_classes, key=len, reverse=True):
        qualified = re.sub(
            rf"(?<!\.)\b{re.escape(model_name)}\b",
            f"rest_models.{model_name}",
            qualified,
        )
    return qualified


def _generate_service_wrappers():
    """Auto-generates the dual-transport wrapper classes for every service."""
    print("Generating unified service wrappers...")

    def _to_snake_case(name: str) -> str:
        return re.sub(r"(?<!^)(?=[A-Z])", "_", name).lower()

    for service_dir in SDK_OUTPUT_DIR.iterdir():
        if not service_dir.is_dir() or service_dir.name in (
            "__pycache__",
            "docs",
            "core",
            "pb",
        ):
            continue

        service = service_dir.name
        title = service_to_pascal_case(service)
        model_classes = discover_service_model_classes(service_dir)

        # 1. Dynamically find the services directory
        services_folder = service_dir / "services"
        if not services_folder.exists():
            services_folder = service_dir / "service"
            if not services_folder.exists():
                continue

        # 2. Collect generated REST service modules (e.g. DeviceService.py, SyntheticsAdminService.py)
        rest_files = [
            f
            for f in sorted(services_folder.glob("*.py"))
            if f.name != "__init__.py"
            and f.name != f"{service}.py"
            and not f.name.startswith("async_")
            and f.stem.endswith("Service")
        ]

        if not rest_files:
            print(
                f"    ⚠️ Could not find REST functions for {service}, skipping wrapper."
            )
            continue

        required_typing_symbols = {"Union", "cast"}

        wrapper_code = [
            "from typing import Union, cast",
            f"from kentik_api.gen.{service} import models as rest_models",
            "from kentik_api.transports.grpc_client import GrpcTransport",
            "from kentik_api.transports.rest_client import RestTransport",
            "",
            f"class {title}ServiceWrapper:",
            '    """Unified Service routing to either gRPC or REST."""',
            "    def __init__(self, transport: Union[GrpcTransport, RestTransport]):",
            "        self._transport = transport",
            "        if isinstance(self._transport, GrpcTransport):",
            "            pass # TODO: Initialize gRPC stub here",
            "",
        ]

        emitted_method_names: set[str] = set()

        for idx, service_py in enumerate(rest_files, start=1):
            rest_module_name = service_py.stem  # e.g., 'DeviceService'
            module_alias = f"Rest{title}Module{idx}"
            wrapper_code.insert(
                2 + (idx - 1),
                f"import kentik_api.gen.{service}.{services_folder.name}.{rest_module_name} as {module_alias}",
            )

            content = service_py.read_text(encoding="utf-8")

            # Regex to find all generated functions
            func_pattern = re.compile(
                r"^def\s+([A-Z][a-zA-Z0-9_]*)\s*\((.*?)\)\s*->\s*([a-zA-Z0-9_\[\]\.]+):",
                re.MULTILINE | re.DOTALL,
            )

            for match in func_pattern.finditer(content):
                func_name_pascal = match.group(1)
                func_args_raw = match.group(2)
                return_type = match.group(3)

                # Convert PascalCase to snake_case (ListDevices -> list_devices)
                func_name_snake = _to_snake_case(func_name_pascal)

                # Keep wrapper method names unique across the full class.
                # If a collision occurs (e.g., many sub-services each define `List`),
                # prefix with module name and then add numeric suffixes if needed.
                unique_method_name = func_name_snake
                if unique_method_name in emitted_method_names:
                    module_prefix = _to_snake_case(
                        re.sub(r"Service$", "", rest_module_name)
                    )
                    unique_method_name = f"{module_prefix}_{func_name_snake}"
                    suffix = 2
                    while unique_method_name in emitted_method_names:
                        unique_method_name = (
                            f"{module_prefix}_{func_name_snake}_{suffix}"
                        )
                        suffix += 1

                emitted_method_names.add(func_name_snake)
                emitted_method_names.add(unique_method_name)

                # Clean up the signature for the wrapper (remove the api_config_override)
                sig_args = re.sub(
                    r"api_config_override:\s*Optional\[APIConfig\]\s*=\s*None,?\s*",
                    "",
                    func_args_raw,
                )
                sig_args = qualify_wrapper_annotation_types(sig_args, model_classes)
                return_type = qualify_wrapper_annotation_types(
                    return_type, model_classes
                )

                # Service modules may alias typing.List to TypingList to avoid
                # collisions with functions named `List`; wrappers should expose
                # standard List annotations.
                sig_args = re.sub(r"\bTypingList\b", "List", sig_args)
                return_type = re.sub(r"\bTypingList\b", "List", return_type)

                for typing_symbol in (
                    "Any",
                    "Optional",
                    "Dict",
                    "List",
                    "Tuple",
                    "Set",
                    "Literal",
                    "Callable",
                ):
                    if re.search(rf"\b{typing_symbol}\b", sig_args) or re.search(
                        rf"\b{typing_symbol}\b", return_type
                    ):
                        required_typing_symbols.add(typing_symbol)

                # Extract variable names to pass into the REST function call
                arg_names = re.findall(r"([a-zA-Z0-9_]+)\s*:", func_args_raw)
                call_args = [
                    f"{arg}={arg}" for arg in arg_names if arg != "api_config_override"
                ]

                call_args_str = ", ".join(call_args)
                if call_args_str:
                    call_args_str = ", " + call_args_str

                wrapper_code.extend(
                    [
                        f"    def {unique_method_name}(self, {sig_args}) -> {return_type}:",
                        "        if isinstance(self._transport, GrpcTransport):",
                        f'            raise NotImplementedError("gRPC translation for {func_name_pascal} is not yet implemented.")',
                        "        elif isinstance(self._transport, RestTransport):",
                        "            rest_transport = cast(RestTransport, self._transport)",
                        f"            return {module_alias}.{func_name_pascal}(",
                        f"                api_config_override=rest_transport.api_config{call_args_str}",
                        "            )",
                        "        else:",
                        '            raise TypeError(f"Unsupported transport type: {self._transport.__class__.__name__}")',
                        "",
                    ]
                )

        preferred_order = [
            "Union",
            "cast",
            "Any",
            "Optional",
            "Dict",
            "List",
            "Tuple",
            "Set",
            "Literal",
            "Callable",
        ]
        ordered_symbols = [
            symbol for symbol in preferred_order if symbol in required_typing_symbols
        ]
        wrapper_code[0] = f"from typing import {', '.join(ordered_symbols)}"

        # Write to gen/<service>/services/<service>.py
        wrapper_file = services_folder / f"{service}.py"
        wrapper_file.write_text("\n".join(wrapper_code), encoding="utf-8")


def _generate_client_mixin():
    """Generates an IDE-friendly Mixin class that mounts all service wrappers."""
    print("Generating IDE-Friendly Client Mixin...")

    imports = []
    type_hints = []
    mounts = []

    for service_dir in sorted(SDK_OUTPUT_DIR.iterdir()):
        if not service_dir.is_dir() or service_dir.name in (
            "__pycache__",
            "docs",
            "core",
            "pb",
        ):
            continue

        service = service_dir.name
        services_folder = service_dir / "services"
        if not services_folder.exists():
            services_folder = service_dir / "service"
            if not services_folder.exists():
                continue

        wrapper_file = services_folder / f"{service}.py"
        if not wrapper_file.exists():
            continue

        title = service_to_pascal_case(service)
        wrapper_class = f"{title}ServiceWrapper"

        # 1. Setup the import from the encapsulated gen directory
        imports.append(
            f"from kentik_api.gen.{service}.{services_folder.name}.{service} import {wrapper_class}"
        )

        # 2. Setup the IDE type hint
        type_hints.append(f"        {service}: '{wrapper_class}'")

        # 3. Setup the runtime mounting logic
        mounts.append(f"        self.{service} = {wrapper_class}(self._transport)")

    mixin_code = [
        "from typing import TYPE_CHECKING",
        "",
        *imports,
        "",
        "if TYPE_CHECKING:",
        "    from kentik_api.transports.grpc_client import GrpcTransport",
        "    from kentik_api.transports.rest_client import RestTransport",
        "",
        "class KentikClientMixin:",
        '    """Auto-generated Mixin to wire up all service wrappers to the main client."""',
        "",
        "    if TYPE_CHECKING:",
        "        _transport: 'GrpcTransport | RestTransport'",
        *type_hints,
        "",
        "    def _mount_generated_services(self) -> None:",
        '        """Mounts all generated service wrappers using the active transport."""',
        *mounts,
        "",
    ]

    mixin_file = PROJECT_ROOT / "src" / "kentik_api" / "client_mixin.py"
    mixin_file.write_text("\n".join(mixin_code), encoding="utf-8")


def generate() -> None:
    """Generates service wrappers, then the client mixin that mounts them."""
    _generate_service_wrappers()
    _generate_client_mixin()
