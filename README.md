# py-docsnap

<!-- FLEET-BADGES:BEGIN -->
[![CI](https://github.com/tzervas/py-docsnap/actions/workflows/fleet-ci.yml/badge.svg?branch=main)](https://github.com/tzervas/py-docsnap/actions/workflows/fleet-ci.yml?query=branch%3Amain)
[![Security](https://github.com/tzervas/py-docsnap/actions/workflows/fleet-security.yml/badge.svg?branch=main)](https://github.com/tzervas/py-docsnap/actions/workflows/fleet-security.yml?query=branch%3Amain)
<!-- FLEET-BADGES:END -->

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