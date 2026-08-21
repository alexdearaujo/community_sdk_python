# HAND-WRITTEN: not modified by `make generate`. Edit directly.
"""Unit tests for parse_wrapper_method_signatures and render_endpoint_docs public interface."""

from pathlib import Path

from scripts.generation.endpoint_docs import parse_wrapper_method_signatures

# ---------------------------------------------------------------------------
# Fixture helpers
# ---------------------------------------------------------------------------

_REST_MODULE = """\
from typing import Optional
from kentik_api.core.api_config import APIConfig
from kentik_api.core.rest_runtime import request_json
from ..error import ListThingsError, GetThingError

def ListThings(
    api_config_override: Optional[APIConfig] = None,
) -> ListThingsResponse:
    body = request_json(
        method="get",
        path="/things/v1/thing",
        api_config_override=api_config_override,
        expected_status=200,
        operation_name="ListThings",
        error_cls=ListThingsError,
    )
    return ListThingsResponse(**body)


def GetThing(
    api_config_override: Optional[APIConfig] = None,
    *,
    thing_id: str,
) -> GetThingResponse:
    body = request_json(
        method="get",
        path=f"/things/v1/thing/{thing_id}",
        api_config_override=api_config_override,
        expected_status=200,
        operation_name="GetThing",
        error_cls=GetThingError,
    )
    return GetThingResponse(**body)
"""


def _make_wrapper(services_dir: Path, service: str, rest_stem: str) -> Path:
    """Writes a minimal ServiceWrapper file that mirrors the REST module fixture."""
    title = "".join(p.capitalize() for p in service.split("_"))
    wrapper = services_dir / f"{service}.py"
    wrapper.write_text(
        f"import kentik_api.gen.{service}.services.{rest_stem} as Rest{title}Module1\n"
        f"\n"
        f"class {title}ServiceWrapper:\n"
        f"    def __init__(self, transport):\n"
        f"        self._transport = transport\n"
        f"\n"
        f"    def list_things(self) -> ListThingsResponse:\n"
        f"        return Rest{title}Module1.ListThings()\n"
        f"\n"
        f"    def get_thing(self, *, thing_id: str) -> GetThingResponse:\n"
        f"        return Rest{title}Module1.GetThing(thing_id=thing_id)\n",
        encoding="utf-8",
    )
    return wrapper


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------


def test_parse_wrapper_method_signatures_maps_list_operation(tmp_path: Path) -> None:
    svc = tmp_path / "services"
    svc.mkdir()
    rest_file = svc / "ThingService.py"
    rest_file.write_text(_REST_MODULE, encoding="utf-8")
    wrapper = _make_wrapper(svc, "thing", "ThingService")

    result = parse_wrapper_method_signatures(wrapper)

    assert ("GET", "/things/v1/thing") in result
    method_name, params = result[("GET", "/things/v1/thing")]
    assert method_name == "list_things"
    assert params == []  # list_things takes no params besides self


def test_parse_wrapper_method_signatures_maps_get_with_path_param(
    tmp_path: Path,
) -> None:
    svc = tmp_path / "services"
    svc.mkdir()
    rest_file = svc / "ThingService.py"
    rest_file.write_text(_REST_MODULE, encoding="utf-8")
    wrapper = _make_wrapper(svc, "thing", "ThingService")

    result = parse_wrapper_method_signatures(wrapper)

    assert ("GET", "/things/v1/thing/{thing_id}") in result
    method_name, params = result[("GET", "/things/v1/thing/{thing_id}")]
    assert method_name == "get_thing"
    assert any(p[0] == "thing_id" for p in params)


def test_parse_wrapper_method_signatures_returns_empty_without_wrapper_class(
    tmp_path: Path,
) -> None:
    wrapper = tmp_path / "no_wrapper.py"
    wrapper.write_text("# no class here\n", encoding="utf-8")
    assert parse_wrapper_method_signatures(wrapper) == {}


def test_parse_wrapper_method_signatures_skips_init(tmp_path: Path) -> None:
    svc = tmp_path / "services"
    svc.mkdir()
    rest_file = svc / "ThingService.py"
    rest_file.write_text(_REST_MODULE, encoding="utf-8")
    wrapper = _make_wrapper(svc, "thing", "ThingService")

    result = parse_wrapper_method_signatures(wrapper)

    # __init__ should never appear as a key
    for _, (method_name, _) in result.items():
        assert method_name != "__init__"
