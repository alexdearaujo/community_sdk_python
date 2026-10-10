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


def _service(operations=(), models=(), mounted=True, fields=None, enums=None) -> dict:
    return {
        "mounted": mounted,
        "operations": {
            op: {"operation": op.split()[-1], "status": 200} for op in operations
        },
        "models": list(models),
        "fields": fields or {},
        "enums": enums or {},
    }


def _field(type_="Optional[str]", required=False) -> dict:
    return {"type": type_, "required": required}


def _render(before: dict, after: dict) -> str:
    return api_surface.render_markdown(api_surface.diff(before, after), since="v1.0.7")


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

    assert "Service removed: `client.vault`" in markdown


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
    (service / "models" / "Thing.py").write_text(
        "class Thing(BaseModel):\n"
        '    model_config = {"populate_by_name": True}\n'
        '    name: str = Field(validation_alias="name")\n'
        '    note: Optional[str] = Field(validation_alias="note", default=None)\n'
    )
    (service / "models" / "Color.py").write_text(
        'class Color(str, Enum):\n    RED = "RED"\n    BLUE = "BLUE"\n'
    )
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

    demo = surface["services"]["demo"]
    assert demo["models"] == ["Color", "Thing"]
    assert demo["fields"] == {
        "Thing": {
            "name": {"type": "str", "required": True},
            "note": {"type": "Optional[str]", "required": False},
        }
    }
    assert demo["enums"] == {"Color": ["RED", "BLUE"]}
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


def test_renamed_field_is_flagged_breaking():
    """kmeta renamed ServiceNowConfig.credentialVaultId to credentialVaultName."""
    before = _surface({"kmeta": _service(fields={"Config": {"vaultId": _field()}})})
    after = _surface({"kmeta": _service(fields={"Config": {"vaultName": _field()}})})

    markdown = _render(before, after)

    assert markdown.startswith("### Breaking changes")
    assert "`kmeta`: field removed, `Config.vaultId`" in markdown
    assert "field added, `Config.vaultName` (`Optional[str]`)" in markdown


def test_new_optional_field_is_not_breaking_but_a_required_one_is():
    before = _surface({"demo": _service(fields={"Thing": {}})})
    optional = _surface({"demo": _service(fields={"Thing": {"note": _field()}})})
    required = _surface(
        {"demo": _service(fields={"Thing": {"name": _field("str", required=True)}})}
    )

    assert "Breaking changes" not in _render(before, optional)
    assert "new required field `Thing.name`" in _render(before, required)


def test_retyped_or_newly_required_field_is_breaking_but_relaxing_is_not():
    def surface(field: dict) -> dict:
        return _surface({"demo": _service(fields={"Thing": {"count": field}})})

    optional_str = surface(_field())
    assert "changed from" in _render(optional_str, surface(_field("Optional[int]")))
    assert "changed from" in _render(optional_str, surface(_field(required=True)))
    relaxed = _render(surface(_field(required=True)), optional_str)
    assert "Breaking changes" not in relaxed
    assert "`Thing.count`: `Optional[str]`, required to `Optional[str]`" in relaxed


def test_removed_enum_value_is_breaking_and_an_added_one_is_not():
    before = _surface({"demo": _service(enums={"Color": ["RED", "BLUE"]})})
    after = _surface({"demo": _service(enums={"Color": ["RED", "GREEN"]})})

    markdown = _render(before, after)

    assert "`demo`: enum value removed, `Color.BLUE`" in markdown
    assert "enum value added, `Color.GREEN`" in markdown
    names = [
        n for _, n in api_surface.breaking_changes(api_surface.diff(before, after))
    ]
    assert names == ["Color.BLUE"]


def test_operation_status_and_required_params_changes_are_reported():
    before = _surface({"demo": _service(["GET /thing"])})
    after = _surface({"demo": _service(["GET /thing"])})
    after["services"]["demo"]["operations"]["GET /thing"].update(
        status=201, required_params=["id"]
    )

    markdown = _render(before, after)

    assert "`GET /thing` succeeds with 201, not 200" in markdown
    assert "`demo`: `GET /thing` now requires `id`" in markdown


def test_a_record_without_fields_compares_as_unchanged():
    """Records written before schema_version 2 carry no fields or enums."""
    before = _surface({"demo": _service(models=["Thing"])})
    del before["services"]["demo"]["fields"], before["services"]["demo"]["enums"]
    after = _surface(
        {"demo": _service(models=["Thing"], fields={"Thing": {"note": _field()}})}
    )

    assert api_surface.is_empty(api_surface.diff(before, after))


def test_breaking_changes_name_what_a_changelog_entry_must_mention():
    before = _surface(
        {"demo": _service(["GET /thing"], ["Old"], fields={"T": {"a": _field()}})}
    )
    after = _surface({"demo": _service([], [], fields={"T": {}})})

    names = [
        name
        for _, name in api_surface.breaking_changes(api_surface.diff(before, after))
    ]

    assert names == ["/thing", "Old", "T.a"]


def test_regeneration_alert_lists_changes_and_next_steps():
    before = _surface({"kmeta": _service(fields={"Config": {"vaultId": _field()}})})
    after = _surface({"kmeta": _service(fields={"Config": {"vaultName": _field()}})})

    alert = api_surface.render_regeneration_alert(before, after)

    assert "API SURFACE CHANGED since HEAD: 1 BREAKING change" in alert
    assert "`kmeta`: field removed, `Config.vaultId`" in alert
    assert "make check-changelog SINCE=HEAD" in alert
    assert "make release-notes SINCE=HEAD" in alert


def test_regeneration_alert_is_quiet_when_nothing_changed():
    surface = _surface({"demo": _service(["GET /thing"])})

    alert = api_surface.render_regeneration_alert(surface, surface)

    assert "unchanged since HEAD" in alert
    assert "CHANGED" not in alert


def test_regeneration_alert_says_when_there_is_no_committed_record():
    alert = api_surface.render_regeneration_alert(None, _surface({}))

    assert "No api_surface.json is committed at HEAD" in alert
