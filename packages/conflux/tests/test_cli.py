from pathlib import Path

from conflux.cli import app
from typer.testing import CliRunner

runner = CliRunner()


def test_data_root_reports_configured_path(tmp_path: Path) -> None:
    result = runner.invoke(app, ["data-root"], env={"LAGUNE_DATA_DIR": str(tmp_path)})

    assert result.exit_code == 0
    assert result.output.strip() == str(tmp_path)


def test_data_root_fails_clearly_when_unconfigured() -> None:
    result = runner.invoke(app, ["data-root"], env={"LAGUNE_DATA_DIR": ""})

    assert result.exit_code == 2
    assert "LAGUNE_DATA_DIR is not set" in result.output
