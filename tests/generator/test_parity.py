from __future__ import annotations

from pathlib import Path

import pytest

from scripts.generation.parity import (
    select_latest_swagger_files_by_service,
    validate_generated_service_parity,
)


def _write_swagger(base: Path, service: str, version: str, filename: str) -> Path:
    swagger_dir = base / service / version
    swagger_dir.mkdir(parents=True, exist_ok=True)
    swagger_path = swagger_dir / filename
    swagger_path.write_text("{}", encoding="utf-8")
    return swagger_path


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
