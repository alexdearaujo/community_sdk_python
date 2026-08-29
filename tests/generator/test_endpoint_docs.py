# HAND-WRITTEN: not modified by `make generate`. Edit directly.
"""Unit tests for parse_wrapper_method_signatures, parse_wrapper_methods, and render_endpoint_docs."""

from pathlib import Path

import pytest

from scripts.generation._shared import parse_wrapper_methods
from scripts.generation.endpoint_docs import (
    EndpointDocsCollector,
    _provenance,
    parse_wrapper_method_signatures,
    render_endpoint_docs,
)

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


# ---------------------------------------------------------------------------
# parse_wrapper_methods (shared parser)
# ---------------------------------------------------------------------------

_WRAPPER_FIXTURE = """\
import kentik_api.gen.thing.services.ThingService as RestThingModule1

class ThingServiceWrapper:
    def __init__(self, transport):
        self._transport = transport

    def list_things(self) -> rest_models.ListThingsResponse:
        return RestThingModule1.ListThings()

    def create_thing(self, *, data: rest_models.CreateThingRequest) -> rest_models.CreateThingResponse:
        return RestThingModule1.CreateThing(data=data)

    def _private(self):
        pass
"""


def test_parse_wrapper_methods_returns_public_methods(tmp_path: Path) -> None:
    f = tmp_path / "thing.py"
    f.write_text(_WRAPPER_FIXTURE, encoding="utf-8")
    methods = parse_wrapper_methods(f)
    names = [m.name for m in methods]
    assert "list_things" in names
    assert "create_thing" in names
    assert "__init__" not in names
    assert "_private" not in names


def test_parse_wrapper_methods_detects_data_param(tmp_path: Path) -> None:
    f = tmp_path / "thing.py"
    f.write_text(_WRAPPER_FIXTURE, encoding="utf-8")
    methods = {m.name: m for m in parse_wrapper_methods(f)}
    assert not methods["list_things"].has_data_param
    assert methods["create_thing"].has_data_param


def test_parse_wrapper_methods_extracts_return_type(tmp_path: Path) -> None:
    f = tmp_path / "thing.py"
    f.write_text(_WRAPPER_FIXTURE, encoding="utf-8")
    methods = {m.name: m for m in parse_wrapper_methods(f)}
    assert "ListThingsResponse" in methods["list_things"].return_type


def test_parse_wrapper_methods_empty_without_class(tmp_path: Path) -> None:
    f = tmp_path / "empty.py"
    f.write_text("# nothing\n", encoding="utf-8")
    assert parse_wrapper_methods(f) == []


# ---------------------------------------------------------------------------
# _provenance: the AUTO-GENERATED header must name code that actually exists
# ---------------------------------------------------------------------------


def test_provenance_names_a_function_that_resolves():
    """Guards the defect where 42 pages named a function that did not exist.

    Asserts resolvability rather than a fixed string, so renaming the writer
    cannot leave the header stale without this failing.
    """
    header = _provenance(render_endpoint_docs)

    assert header.startswith("<!-- AUTO-GENERATED: ")
    inner = header.removeprefix("<!-- AUTO-GENERATED: ").removesuffix(" -->")
    module_rel, func_part = (part.strip() for part in inner.split(",", 1))
    func_name = func_part.removesuffix("()")

    project_root = Path(__file__).resolve().parents[2]
    module_file = project_root / module_rel
    assert module_file.exists(), f"provenance names a missing module: {module_rel}"

    source = module_file.read_text(encoding="utf-8")
    assert f"def {func_name}(" in source, (
        f"provenance names {func_name}(), which does not exist in {module_rel}"
    )


def test_provenance_tracks_a_rename():
    """A differently-named writer must produce a differently-named header."""

    def some_other_writer() -> None:  # pragma: no cover - name only
        pass

    assert "some_other_writer()" in _provenance(some_other_writer)


# ---------------------------------------------------------------------------
# EndpointDocsCollector.extract: failures must surface, not be swallowed
# ---------------------------------------------------------------------------


def test_extract_propagates_failure_instead_of_swallowing_it(tmp_path: Path):
    """A swallowed failure yields a silently empty page while the run succeeds.

    Same shape as the None-return that erased the gRPC runtime from the
    architecture diagram with no error anywhere.
    """
    unparseable = tmp_path / "broken.swagger.json"
    unparseable.write_text("{ this is not json", encoding="utf-8")

    collector = EndpointDocsCollector()

    with pytest.raises(Exception):
        collector.extract("broken_service", unparseable)
