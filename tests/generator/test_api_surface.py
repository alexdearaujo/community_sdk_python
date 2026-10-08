# HAND-WRITTEN: not modified by `make generate`. Edit directly.
"""Tests for scripts/generation/api_surface.py.

Builds surface dicts directly rather than generating an SDK, so these stay offline
and fast. capture() itself is covered against a minimal fixture tree.
"""

from __future__ import annotations

from pathlib import Path

from scripts.generation import api_surface


def _surface(services: dict, **top) -> dict:
    return {
        "schema_version": 1,
        "requirements": top.get("requirements", {}),
        "gencode": top.get("gencode", {}),
        "services": services,
    }


def _service(operations=(), models=(), mounted=True) -> dict:
    return {
        "mounted": mounted,
        "operations": {
            op: {"operation": op.split()[-1], "status": 200} for op in operations
        },
        "models": list(models),
    }


def test_identical_surfaces_produce_no_delta():
    surface = _surface({"device": _service(["GET /device"], ["Device"])})

    delta = api_surface.diff(surface, surface)

    assert api_surface.is_empty(delta)
    assert "No public API surface changes" in api_surface.render_markdown(
        delta, since="v1.0.7"
    )


def test_added_service_is_reported_with_its_operations():
    before = _surface({})
    after = _surface({"kmeta": _service(["GET /kmeta/config"], ["ServiceNowConfig"])})

    markdown = api_surface.render_markdown(
        api_surface.diff(before, after), since="v1.0.7"
    )

    assert "### New services" in markdown
    assert "**kmeta** (`client.kmeta`)" in markdown
    assert "`GET /kmeta/config`" in markdown
    assert "Breaking changes" not in markdown


def test_unmounted_service_is_labelled_types_only():
    after = _surface({"kptr": _service([], ["PtrResult"], mounted=False)})

    markdown = api_surface.render_markdown(
        api_surface.diff(_surface({}), after), since="v1.0.7"
    )

    assert "types only, not mounted on the client" in markdown


def test_removed_operation_is_flagged_breaking():
    before = _surface({"device": _service(["GET /device", "POST /device"])})
    after = _surface({"device": _service(["GET /device"])})

    markdown = api_surface.render_markdown(
        api_surface.diff(before, after), since="v1.0.7"
    )

    assert markdown.startswith("### Breaking changes")
    assert "`device`: operation removed, `POST /device`" in markdown


def test_removed_service_is_flagged_breaking():
    before = _surface({"vault": _service(["GET /secrets"])})

    markdown = api_surface.render_markdown(
        api_surface.diff(before, _surface({})), since="v1.0.7"
    )

    assert "Services removed: `client.vault`" in markdown


def test_unmounting_a_service_is_flagged_breaking():
    before = _surface({"ktbgp": _service(["POST /routes/list"], mounted=True)})
    after = _surface({"ktbgp": _service(["POST /routes/list"], mounted=False)})

    markdown = api_surface.render_markdown(
        api_surface.diff(before, after), since="v1.0.7"
    )

    assert "`client.ktbgp` is no longer available" in markdown


def test_new_required_dependency_is_flagged_breaking():
    before = _surface({}, requirements={"grpcio": "grpcio>=1.78.0"})
    after = _surface(
        {}, requirements={"grpcio": "grpcio>=1.84.0", "protobuf": "protobuf>=7.35.1,<8"}
    )

    markdown = api_surface.render_markdown(
        api_surface.diff(before, after), since="v1.0.7"
    )

    assert "New required dependency, `protobuf>=7.35.1,<8`" in markdown
    assert "Dependency floor raised, `grpcio>=1.78.0` to `grpcio>=1.84.0`" in markdown


def test_gencode_bump_is_reported_but_not_breaking():
    before = _surface({}, gencode={"protobuf": "6.33.5"})
    after = _surface({}, gencode={"protobuf": "7.35.1"})

    markdown = api_surface.render_markdown(
        api_surface.diff(before, after), since="v1.0.7"
    )

    assert "`protobuf` gencode: `6.33.5` to `7.35.1`" in markdown
    assert "Breaking changes" not in markdown


def test_operations_are_keyed_by_method_and_path_not_operation_id():
    """Multi-file services reuse generic operation ids such as `List`."""
    before = _surface({"alerting": _service(["GET /alerts", "GET /mitigations"])})
    after = _surface({"alerting": _service(["GET /alerts"])})

    delta = api_surface.diff(before, after)

    assert delta["changed_services"]["alerting"]["removed_operations"] == [
        "GET /mitigations"
    ]


def test_capture_reads_a_generated_tree(tmp_path: Path):
    service = tmp_path / "demo"
    (service / "services").mkdir(parents=True)
    (service / "models").mkdir()
    (service / "models" / "Thing.py").write_text("class Thing(BaseModel):\n    pass\n")
    (service / "services" / "DemoService.py").write_text(
        "from kentik_api.core.rest_runtime import request_json\n"
        "def ListThings(*, cid: str) -> Thing:\n"
        "    return request_json(\n"
        '        method="get",\n'
        '        path=f"/demo/v1/{path_segment(cid)}/things",\n'
        "        expected_status=200,\n"
        "        error_cls=DemoError,\n"
        '        operation_name="ListThings",\n'
        "    )\n"
    )

    surface = api_surface.capture(tmp_path)

    assert surface["services"]["demo"]["models"] == ["Thing"]
    operations = surface["services"]["demo"]["operations"]
    assert "GET /demo/v1/{cid}/things" in operations
    assert operations["GET /demo/v1/{cid}/things"]["operation"] == "ListThings"
    assert operations["GET /demo/v1/{cid}/things"]["required_params"] == ["cid"]


def test_write_then_read_round_trips(tmp_path: Path):
    surface = _surface({"device": _service(["GET /device"])})
    path = tmp_path / "api_surface.json"

    api_surface.write(surface, path)

    assert api_surface.read(path) == surface


def test_summary_covers_mounted_and_types_only_services():
    """Rendered when no tagged release carries a surface record yet."""
    surface = _surface(
        {
            "device": _service(["GET /device", "POST /device"], ["Device"]),
            "kptr": _service([], ["PtrResult"], mounted=False),
            "plan": _service(["GET /plan"], []),
        },
        requirements={"protobuf": "protobuf>=7.35.1,<8"},
    )

    markdown = api_surface.render_summary(surface)

    assert "3 services (2 mounted on the client)" in markdown
    assert "3 REST operations" in markdown
    assert "**device**: `client.device`, 2 operations" in markdown
    assert "**plan**: `client.plan`, 1 operation" in markdown  # singular
    assert "**kptr**: types only, not mounted on the client" in markdown
    assert "`protobuf>=7.35.1,<8`" in markdown


def test_single_new_model_is_singular():
    before = _surface({"kptr": _service([], [])})
    after = _surface({"kptr": _service([], ["ListResolvedAddressesResponse"])})

    markdown = api_surface.render_markdown(
        api_surface.diff(before, after), since="v1.0.7"
    )

    assert "1 new model: `ListResolvedAddressesResponse`" in markdown
