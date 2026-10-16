# HAND-WRITTEN: not modified by `make generate`. Edit directly.
from __future__ import annotations

import json
from pathlib import Path

import pytest

from scripts.generation._shared import INTERNAL_GEN_DIRS, iter_service_dirs
from scripts.generation.parity import (
    select_latest_swagger_files_by_service,
    validate_generated_service_parity,
    validate_schema_files,
    validate_schema_files_or_raise,
)


def _write_swagger(base: Path, service: str, version: str, filename: str) -> Path:
    swagger_dir = base / service / version
    swagger_dir.mkdir(parents=True, exist_ok=True)
    swagger_path = swagger_dir / filename
    swagger_path.write_text("{}", encoding="utf-8")
    return swagger_path


def _valid_schema_file(tmp_path: Path, name: str) -> Path:
    path = tmp_path / name
    path.write_text(
        json.dumps({"swagger": "2.0", "info": {"title": "t"}, "paths": {}}),
        encoding="utf-8",
    )
    return path


def test_select_latest_swagger_files_by_service_picks_newest_version(tmp_path: Path):
    _write_swagger(tmp_path, "device", "v202211", "device.swagger.json")
    _write_swagger(tmp_path, "device", "v202309", "device.swagger.json")
    _write_swagger(tmp_path, "user", "v202211", "user.swagger.json")

    by_service, selected_count, ignored_count = select_latest_swagger_files_by_service(
        tmp_path
    )

    assert set(by_service) == {"device", "user"}
    assert len(by_service["device"]) == 1
    assert by_service["device"][0]["version"] == "v202309"
    assert selected_count == 2
    assert ignored_count == 1


def test_select_latest_swagger_files_by_service_groups_multiple_files_per_service(
    tmp_path: Path,
):
    _write_swagger(tmp_path, "alerting", "v1", "alerting.swagger.json")
    _write_swagger(tmp_path, "alerting", "v1", "alerting_message.swagger.json")

    by_service, selected_count, ignored_count = select_latest_swagger_files_by_service(
        tmp_path
    )

    assert len(by_service["alerting"]) == 2
    assert selected_count == 2
    assert ignored_count == 0


def test_validate_generated_service_parity_passes_when_sets_match(tmp_path: Path):
    (tmp_path / "device").mkdir()
    (tmp_path / "user").mkdir()

    validate_generated_service_parity({"device", "user"}, tmp_path)


def test_validate_generated_service_parity_raises_on_missing_service(tmp_path: Path):
    (tmp_path / "device").mkdir()

    with pytest.raises(RuntimeError, match="do not match"):
        validate_generated_service_parity({"device", "user"}, tmp_path)


def test_validate_generated_service_parity_raises_on_extra_directory(tmp_path: Path):
    (tmp_path / "device").mkdir()
    (tmp_path / "leftover").mkdir()

    with pytest.raises(RuntimeError, match="do not match"):
        validate_generated_service_parity({"device"}, tmp_path)


def test_validate_schema_files_passes_valid_files(tmp_path: Path):
    files = [
        _valid_schema_file(tmp_path, "device.swagger.json"),
        _valid_schema_file(tmp_path, "user.swagger.json"),
    ]

    assert validate_schema_files(files) == []


def test_validate_schema_files_rejects_empty_file(tmp_path: Path):
    empty = tmp_path / "empty.swagger.json"
    empty.write_text("", encoding="utf-8")

    failures = validate_schema_files([empty])

    assert len(failures) == 1
    assert failures[0]["path"] == empty
    assert "empty" in failures[0]["reason"]


def test_validate_schema_files_rejects_invalid_json(tmp_path: Path):
    broken = tmp_path / "broken.swagger.json"
    broken.write_text("{not json", encoding="utf-8")

    failures = validate_schema_files([broken])

    assert len(failures) == 1
    assert "invalid JSON" in failures[0]["reason"]


def test_validate_schema_files_rejects_missing_required_keys(tmp_path: Path):
    incomplete = tmp_path / "incomplete.swagger.json"
    incomplete.write_text(json.dumps({"info": {"title": "t"}}), encoding="utf-8")

    failures = validate_schema_files([incomplete])

    assert len(failures) == 1
    assert "paths" in failures[0]["reason"]
    assert "swagger/openapi" in failures[0]["reason"]


def test_validate_schema_files_reports_all_failures_before_raising(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
):
    empty = tmp_path / "empty.swagger.json"
    empty.write_text("", encoding="utf-8")
    broken = tmp_path / "broken.swagger.json"
    broken.write_text("{not json", encoding="utf-8")
    valid = _valid_schema_file(tmp_path, "device.swagger.json")

    failures = validate_schema_files([empty, broken, valid])
    assert {f["path"] for f in failures} == {empty, broken}

    with pytest.raises(RuntimeError, match="structural validation"):
        validate_schema_files_or_raise([empty, broken, valid])

    printed = capsys.readouterr().out
    assert str(empty) in printed
    assert str(broken) in printed
    assert str(valid) not in printed


def test_validate_schema_files_catches_truncated_file_like_2026_08_26_incident(
    tmp_path: Path,
):
    # Reproduces the real incident: device.swagger.json was locally truncated
    # from 1625 lines down to a single, non-JSON line.
    truncated = tmp_path / "device.swagger.json"
    truncated.write_text('  "swagger": "2.0",', encoding="utf-8")

    failures = validate_schema_files([truncated])

    assert len(failures) == 1
    assert "invalid JSON" in failures[0]["reason"]


# ---------------------------------------------------------------------------
# iter_service_dirs / INTERNAL_GEN_DIRS: the single Service-classification rule
# ---------------------------------------------------------------------------


def _make_gen_tree(root: Path, names: list[str]) -> None:
    """Builds a gen/-shaped tree: each name a directory holding models/."""
    for name in names:
        (root / name / "models").mkdir(parents=True, exist_ok=True)


def test_iter_service_dirs_excludes_every_internal_dir(tmp_path: Path):
    _make_gen_tree(tmp_path, ["device", "alerting", *INTERNAL_GEN_DIRS])

    names = [d.name for d in iter_service_dirs(tmp_path)]

    assert names == ["alerting", "device"], "sorted, internal dirs excluded"
    for internal in INTERNAL_GEN_DIRS:
        assert internal not in names


def test_iter_service_dirs_includes_operationless_service(tmp_path: Path):
    # A Service with models/ but no wrapper is still a Service: six exist today
    # (core, deviceconf, diagnostic, kptr, monitoring, net) and five are already
    # documented. Absence of a wrapper must not reclassify it as internal.
    _make_gen_tree(tmp_path, ["device"])
    (tmp_path / "operationless" / "models").mkdir(parents=True)
    (tmp_path / "operationless" / "services").mkdir()
    (tmp_path / "operationless" / "services" / "__init__.py").write_text("")

    names = [d.name for d in iter_service_dirs(tmp_path)]

    assert names == ["device", "operationless"]


def test_iter_service_dirs_skips_files_and_returns_sorted(tmp_path: Path):
    _make_gen_tree(tmp_path, ["zeta", "alpha"])
    (tmp_path / "README.md").write_text("not a service", encoding="utf-8")

    names = [d.name for d in iter_service_dirs(tmp_path)]

    assert names == ["alpha", "zeta"]


def test_iter_service_dirs_regression_pb_companions_excluded_core_included(
    tmp_path: Path,
):
    # Names the real defect: pb_companions (the proto descriptor registry,
    # created by _compile_proto_companions()) was documented as a Service,
    # while core -- a real generated Service -- was suppressed by a hardcoded
    # "core" literal. Their counts cancelled, so every count check passed.
    _make_gen_tree(tmp_path, ["core", "device", "pb_companions"])

    names = [d.name for d in iter_service_dirs(tmp_path)]

    assert "core" in names, "core is a real Service and must not be excluded"
    assert "pb_companions" not in names, "pb_companions is generator-internal"
    assert len(names) == 2
