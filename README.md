# py-docsnap

Python documentation snapshot tool for capturing and managing documentation states.

## Installation

```bash
pip install py-docsnap
```

## Usage

Capture documentation snapshots:

```bash
docsnap capture /path/to/docs --output ./snapshots --format png
```

Compare snapshots:

```bash
docsnap compare ./snapshots
```

## Development

This project uses [uv](https://github.com/astral-sh/uv) for dependency management.

```bash
# Install dependencies
uv sync

# Run tests
uv run pytest

# Format code
uv run black src/
uv run isort src/
```

## License

MIT License - see [LICENSE](LICENSE) for details.