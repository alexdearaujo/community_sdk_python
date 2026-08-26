# HAND-WRITTEN: not modified by `make generate`. Edit directly.
from __future__ import annotations

import json
from pathlib import Path

import pytest

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
