"""Tests for docsnap CLI."""

import pytest
from click.testing import CliRunner
from docsnap.cli import main


def test_cli_help():
    """Test that CLI shows help."""
    runner = CliRunner()
    result = runner.invoke(main, ["--help"])
    assert result.exit_code == 0
    assert "Documentation snapshot tool" in result.output


def test_capture_command():
    """Test capture command with basic arguments."""
    runner = CliRunner()
    with runner.isolated_filesystem():
        # Create a dummy source directory
        import os
        os.makedirs("source")
        with open("source/test.txt", "w") as f:
            f.write("test content")

        result = runner.invoke(main, ["capture", "source"])
        assert result.exit_code == 0
        assert "Capturing documentation snapshots" in result.output