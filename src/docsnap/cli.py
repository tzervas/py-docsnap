"""Command-line interface for docsnap."""

import click
from pathlib import Path


@click.group()
@click.version_option()
def main():
    """Documentation snapshot tool for capturing and managing documentation states."""
    pass


@main.command()
@click.argument("source", type=click.Path(exists=True))
@click.option("--output", "-o", type=click.Path(), help="Output directory for snapshots")
@click.option("--format", "-f", type=click.Choice(["png", "jpg", "pdf"]), default="png")
def capture(source, output, format):
    """Capture documentation snapshots from source directory."""
    source_path = Path(source)
    output_path = Path(output) if output else Path.cwd() / "docsnap_output"

    click.echo(f"📸 Capturing documentation snapshots from {source_path}")
    click.echo(f"📁 Output directory: {output_path}")
    click.echo(f"🎨 Format: {format}")

    # TODO: Implement actual snapshot capture logic
    click.echo("✅ Snapshot capture completed (placeholder)")


@main.command()
@click.argument("snapshot_dir", type=click.Path(exists=True))
def compare(snapshot_dir):
    """Compare documentation snapshots for changes."""
    click.echo(f"🔍 Comparing snapshots in {snapshot_dir}")
    # TODO: Implement comparison logic
    click.echo("✅ Comparison completed (placeholder)")


if __name__ == "__main__":
    main()